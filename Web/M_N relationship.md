# M:N Relationship



### 중개모델

- 두 개의 모델을 연결하는 브릿지 역할을 하는 모델

- 예시

  ```python
  # 의사 데이터
  class Doctor(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  # 환자 데이터
  class Patient(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'    
  ```

  - 위 두개 모델을 연결해줄 중개모델 생성

  ```python
  # 중개모델
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
     
  	def __str__(self):
          return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

  - 데이터 삽입

  ```shell
  doctor1 = Doctor.objects.create(name='justin')
  patient1 = Patient.objects.create(name='tony')
  Reservation.objects.create(doctor=doctor1, patient=patient1)
  
  #추가 생성
  patient2 = Patient.objects.create(name='harry')
  Reservation.objects.create(doctor=doctor1, patient=patient2)
  ```

  - 데이터 조회

  ```shell
  # 의사의 예약 환자 조회
  doctor1.reservation_et.all()
  # 환자의 담당 의사 조회
  patient1.reservation_set.all()
  ```

  

  



### ManyToManyFields

> 다대다 관계 설정 시 사용하는 모델 필드

- 하나의 필수 위치인자(다대다 관계로 설정할 모델 클래스)가 필요

- add,remove 같은 RelatedManager를 사용하여 관련 개체를 추가 제거 또는 만들 수 있음

- 필드는 어떤 모델에도 작성 가능

  - 단, ManyToManyField를 어디에 두냐에 따라 역참조와 참조의 관계가 달라짐
  - ManyToManyField를 두는 클래스가 참조, 없는 객체가 역참조

- 예시

  ```python
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
      
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor) # Doctor 모델에 작성할 수도 있음
      name = models.TextField()
      
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  - 데이터 생성

  ```shell
  doctor1 = Doctor.objects.create(name='justin')
  patient1 = Patient.objects.create(name='tony')
  patient2 = Patient.objects.create(name='harry')
  
  #관계 데이터 생성
  patient1.doctors.add(doctor1)
  ```

  - 데이터 조회

  ```shell
  patient1.doctors.all()
  # <QuerySet [<Doctor: 1번 의사 justin]>
  
  doctor1.patient_set.all()
  # <QuerySet [<Patient: 1번 환자 tony]>
  ```

  - 역참조를 통한 데이터 생성

  ```shell
  doctor1.patient_set.add(patient2)
  ```

  - 데이터 조회

  ```shell
  doctor1.patient_set.all()
  # <QuerySet [<Patient: 1번 환자 tony>, <Patient: 2번 환자 harry>]>
  patient2.doctors.all()
  # <QuerySet [<Doctor: 1번 의사 justin]>
  patient1.doctors.all()
  # <QuerySet [<Doctor: 1번 의사 justin]>
  ```

  - 데이터 삭제

  ```shell
  # 참조에서 삭제
  patient2.doctors.remove(doctor1)
  # 역참조에서 삭제
  doctor1.patient_set.remove(patient1)
  ```

  





#### Arguments

##### related_name

- target model (관계 필드를 가지지 않은 모델)이 source model(관계 필드를 가진 모델)을 참조할 때 사용할 manager의 이름을 설정

- 즉, 역참조 때 사용하는 manager 이름을 설정

- 설정하면 과거의 manager 이름(=targetmodel_set)은 사용할 수 없게 됨

- 예시

  ```python
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, related_name='this_is_related_name')
      name = models.TextField()
  ```

  - 데이터 조회시

  ```shell
  doctor1 = Doctor.objects.get(pk=1)
  # related_name 사용
  doctor1.this_is_related_name.all()
  # 이전 이름 사용 불가
  doctor1.patient_set.all() # AttributeError 발생(AttributeError :'Doctor' object has no attribute 'patient_set')
  ```

  



##### through

- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 주로 사용됨 



##### symmetrical

- ManyToManyField 가 동일한 모델(on self)를 가리키는 정의에서만 사용

- `symmetrical = True`(= 기본값) 일 경우 django는 person_set 매니저를 추가하지 않음

- source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함

  - follow 기능을 예시로 들 수 있음
    - 내가 당신과 친구라면 당신도 나와 친구이다!
  - 대칭을 원하지 않으면 False로 설정

- 예시

  ```python
  from django.db import models
  
  class Person(models.Model) :
      friends = models.ManyToManyField('self', symmetrical=False)
  
  ```

  

#### Related Manager

> 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저

- 같은 이름의 메서드여도 각 관계(1:N,M:N)에 따라 다르게 사용 및 동작
  - 1:N에서는 target 모델 인스턴스만 사용 가능
  - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능



##### add

- 지정된 객체를 관련 객체 집합에 추가

- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음

- 모델 인스턴스, 필드 값(PK)을 인자로 받음

- 예시

  ```shell
  doctor1 = Doctor.objects.create(name='junstin')
  patient1 = Patient.objects.create(name='tony')
  
  doctor1.patient_set.add(patient1)
  patioent1.doctors.add(doctor1)
  ```

  

##### remove

- 관련 객체 집합에서 지정된 모델 객체를 제거

- 내부적으로 QuerySet.delete()를 사용하여 관게가 삭제됨

- 모델 인스턴스, 필드 값(=PK)을 인자로 허용

- 예시

  ```shell
  doctor1 = Doctor.objects.get(pk=1)
  patient1 = Patient.objects.get(pk=1)
  
  doctor1.patient_set.remove(patient1)
  patient1.doctors.remove(doctor1l)
  ```

  



