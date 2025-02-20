let array = [2, 3, 4];
array.unshift(1);  // 1 დამატებულია დასაწყისში
console.log(array);  // [1, 2, 3, 4]

let array = [1, 2, 3, 4];
let removedElement = array.shift();  // 1 წაიშლება
console.log(array);  // [2, 3, 4]
console.log(removedElement);  // 1

let array = [1, 2, 3, 4];
array.splice(2, 1, 5, 6);  // 2-ზე ვხსნებით ერთი ელემენტი და ვამატებთ 5 და 6
console.log(array);  // [1, 2, 5, 6, 4]

let array = [1, 2, 3, 4, 5];
let newArray = array.slice(1, 4);  // ინდექსები 1-დან 3-მდე
console.log(newArray);  // [2, 3, 4]

let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let newArray = array1.concat(array2);  // აერთიანებს ორივე მასივს
console.log(newArray);  // [1, 2, 3, 4, 5, 6]
