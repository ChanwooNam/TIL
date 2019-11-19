// for loop 활용
var students = [
  { name: '아이유1', type: 'female' },
  { name: '아이유2', type: 'male' },
  { name: '아이유3', type: 'female' },
  { name: '아이유4', type: 'male' },
]

var strongStudents = []
// students라는 배열의 객체들 중 type이 female인 요소들만 뽑기!
// students 원본 배열 자체를 바꾸고 싶은게 아니라,
// 원하는 조건에 맞는 데이터들만 골라서 새로운 배열 만들기 

for (var i = 0; i < students.length; i++){
  if (students[i].type == 'female') {
    strongStudents.push(students[i])
  }
}
console.log(strongStudents)     // 원본 유지
console.log(students)           // 새로운 배열
console.log(students[i].name)   // 객체 내 속성 접근하기 


// filter Helper 활용
const STRONG_STUDENTS = STUDENTS.filter(student => student.type == 'female')
console.log(STRONG_STUDENTS)    // 새로운 배열
console.log(STUDENTS)           // 원본 유지 


// Filter Helper를 사용해서 numbers 배열 중 50보다 큰 값만 필터링해서 새로운 배열에 저장하기 

const numbers = [15, 35, 13, 36, 69, 3, 61, 55, 99, 5]
const newNumbers = numbers.filter(function(number) {
  return number > 50
})

console.log(numbers)
console.log(newNumbers)

