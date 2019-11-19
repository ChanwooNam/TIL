// ES5 for loop
var iot1 = ['도현', '혁진', '은애']
for (var i = 0; i < iot1.length; i++) {
  console.log(iot1[i])
}

// ES6+
const IOT1 = ['수연', '승찬', '한석', '경희', '영선']
IOT1.forEach(function(student) {
  console.log(student)
})

// 한 줄로 리팩토링 가능!
IOT1.forEach( student => console.log(student) )


// forEach는 기본으로 들어오는 return 값은 없다. 
const result = IOT1.forEach( 
  student => console.log(student) 
)
console.log(result)   // undefined



// [ 실습 ] for를 forEach로 바꾸기!
function handleStudent() {
  const students = [
    { id: 1, name: '홍길동', status: '응애?'},
    { id: 15, name: '이순신', status: 'ddddddd'},
    { id: 28, name: '유관순', status: 'easy...'},
  ]

  // for 
  for (let i = 0; i < students.length; i++) {
    console.log(students[i])
    console.log(students[i].name)
    console.log(students[i].status)
  }

  // forEach
  students.forEach(function(students) {
    console.log(students)
    console.log(students.name)
    console.log(students.status)
  })
}
handleStudent()


// [실습] iamges 배열 안에 있는 정보를 곱해 넓이를 구하여 areas 배열에 저장하세요.
const iamges = [
  { height: 30, width: 55},
  { height: 50, width: 178},
  { height: 81, width: 35},
]

const areas = []

// 정답 코드 ( forEach 활용 )
iamges.forEach(function(images) {
  areas.push(images.height * images.width)
})

console.log(areas)
