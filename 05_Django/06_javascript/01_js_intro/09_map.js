// 숫자가 담긴 배열의 요소에 각각 2를 곱하여 새로운 배열 만들기

// ES5
var numbers = [1, 2, 3]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i] *2)
}
console.log(doubleNumbers)
console.log(numbers)        // 원본 유지

// ES6+
const NUMBERS = [1, 2, 3]
const DOUBLE_NUMBERS = NUMBERS.map(function(numbers) {
  // return이 없으면 undefined (까먹지 말자...)
  return numbers * 2
})
console.log(DOUBLE_NUMBERS)
console.log(NUMBERS)    // 원본 유지

// 화살표 함수 사용하여 한 줄로 줄이기!
const DOUBLE_NUMBERS2 = NUMBERS.map( numbers => numbers * 2 )


// map 핼퍼를 사용해서 images 배열 안의 객체들의 height들만 저장되어 있는 height 배열을 만들어보자.
const images = [
  { height: '34px', width: '59px' }, 
  { height: '11px', width: '135px' }, 
  { height: '681px', width: '592px' }, 
]

const heights = images.map( image => image.height)

console.log(heights)
console.log(images)

// map 핼퍼를 사용해서 "distance / time => 속도"를 저장하는 새로운 배열 speeds를 만드시오.
const trips = [
  { distance: 34, time:10 },
  { distance: 90, time:20 },
  { distance: 111, time:28 },
]

const speeds = trips.map( trip => trip.distance / trip.time )
console.log(speeds)








