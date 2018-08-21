# data and feature handling

## Data preprocessing
* 대부분의 데이터는 우리가 원하는 대로 되어있지 않음
* 미리보기(pandas): head(), tail()
* 형태 요약(pandas); info(), descirbe()
* 수치형/카테고리형 데이터 인지 구분!

## Missing Data Handle (Drop, impulating)
* 결측치의 원인: 수집 X, 서버 오류, 수집 시점, Human error
* Missingno: 결측치 데이터의 시각화
* 결측치 종류: MCAR, MAR, NI
* 결측치 처리 방법: 완전제거법(=Drop)(비효율적), 단일대체방법(평균, 중앙값, 최빈값 등으로 ==> 편향의 위험), 다중대체방법

### 제거하기 VS 대체하기
* 제거하기
* 대체하기: 평균값, 중앙값, 최빈값, 확률분포, 내외부 데이터(다른 컬럼의 데이터 포함), 머신러닝을 이용한 예측(predictive imputor)

## Feature Engineering
* One-hot: 텍스트, 범주형 ==> 수치형 데이터 (scikit-learn LabelEncoder)
* binning(bucketing): 수치형 => 텍스트, 범주형

## 텍스트 데이터 다루기
* BOW (back of word): 출현횟수로만 고려 ==> 순서가 완전히 무시됨, 
* n-gram: 단어를 n개씩 묶어 처리 (1-gram, 2-gram, 3-gram)
* 2가지를 조합해 사용

## Feature Extract
* Raw 데이터에서 Feature 추출
* TF: 단어빈도, IDF: 역문서빈도 ==> TF-IDF 기법: 단어별로 가중치를 부여

## Error 데이터 다루기
* 참고할수 있는 데이터가 있다면 보정 (ex: 소득 - 보험료)

## 이상치(Outlier Data) 다루기
* 데이터, 샘플에서 동떨어진 값 => 이상치
* 이상치 - 정상치를 나누는 기준의 모호함이 문제
* 기법: 보정, 제거, 대체

## Feature Selection
* 적절한 Selection만으로도 좋은 성능
* pandas, scikit-learn을 이용해 가능
* 정규분포 형태의 데이터가 성능이 좋음 ==> log 함수

## Feature Scaling
* minMax: 0 ~ 1 사이로 배치

## 차원의 저주
* 일정 수중 이상의 자원 수의 증가 ==> 성능 하락(outfitting)
* 차원 축소 기법(scikit-learn의 PCA)
* t-SNE: N차원 --> 2차원

## Underfitting, Overfitting
* 시각화를 통해 최적점을 찾아주어야 함

## 기타
* 시각화: plotnine(python에서 R의 ggplot 문법 사용 가능)
* 정해진 최적화 기법은 없음 ==> 데이터마다 적절한 방법이 다름