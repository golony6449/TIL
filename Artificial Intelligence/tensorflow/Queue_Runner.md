## Queue Runners
=========================
* 데이터셋이 큰 경우는 OOM(Out Of Memory) 오류 발생

### 실행 단계
1. 파일 이름을 리스트로 만듦
2. 셔플 (선택)
3. Filename Queue 생성
4. Reader 정의 (파일을 읽어오는 역할)
5. 데이터 decode (Datatype, Default 값 등 지정)
6. batch 생성
7. Coordinator, thread 생성 `tf.train.Coordinator()`, `tf.train.start_queue_runners(sess=sess, coord=coord)`
8. `sess.run()` 실행
9. `coord.request_stop()`, `coord.join(thread)` 실행

### 코드
* 원문: 모두를 위한 딥러닝 Season1 Lab 04-2
```python
import tensorflow as tf
filename_queue = tf.train.string_input_producer([
    'data-01-test-score.csv'], shuffle=False, name='filename_queue')

# Reader 정의
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Decode
record_defaults = [[0.], [0.], [0.], [0.]]
xy = tf.decode_csv(value, record_defaults)

train_x_batch, train_y_batch = tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)

# 변수 및 placeholder 생성
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00001)
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(2001):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_batch, Y: y_batch})

    if step % 10 == 0:
        print(step, 'cost: ', cost_val, '\n predict: ', hy_val)

coord.request_stop()
coord.join(threads)
```

### shuffle_batch
```python
min_after_dequeue = 10000
capacity = min_after_dequeue + 3 * batch_size
example_batch, label_batch = tf.train.shuffle_batch([example, label],                                           batch_size=batch_size,                                     capacity=capacity, min_after_dequeue=min_after_dequeue)
```

### 참고자료
* https://www.tensorflow.org/programmers_guide/reading_data