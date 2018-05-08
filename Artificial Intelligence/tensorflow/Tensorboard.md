## Tensorboard
=============================
* 수치, TF 그래프의 시각화

### 사용법
#### 1. 기록할 텐서(Tensor) 지정
```python
w2_hist = tf.summary.histogram('weights2', W2)
cost_sum = tf.summary.scalar('cost', cost)
```

#### 2. Merge
* 한번에 사용하기 위해 1에서 생성한 객체를 merge
```python
summary = tf.summary.merge_all()
```

#### 3. Writer, Graph 추가
* 파일의 저장 위치 지정

```python
writer = tf.summary.FileWriter('./logs')
writer.add_graph(sess.graph) # 그래프 추가
```

* 그래프의 가독성을 위해 여러개의 노드(뉴런)을 묶을 수 있음
```python
with tf.name_scope('layer1') as scope:
    # 내용
```

#### 4. Summary 실행
* summary도 일종의 Tensor => 실행해야 할 필요 있음
```python
global_step = 0
...
s, _ = sess.run([summary, optimizer], feed_dict=feed_dict)
writer.add_summary(s, global_step=global_step)
global_step += 1
```

#### 5. Tensorboard 실행
`tensorboard --logdir ./logs`

### 응용
#### 한번에 여러 개의 그래프(수치)를 기록하고 싶을때
* ex: learning_late가 0.01일때와 0.00001 일때의 비교
1. 로그를 저장할 디렉토리의 하위에 각각의 실행기록을 저장
2. `tensorboard --logdir ./logs` 처럼 상위 디렉토리로 Tensorboard 실행