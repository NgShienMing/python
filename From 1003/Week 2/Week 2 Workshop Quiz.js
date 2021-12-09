// Q1
let data = [
  {
    year: 2021,
    sem: 1,
    units: [
      {
        code: "eng0001",
        grade: "HD",
        mark: 92
      },
      {
        code: "eng0002",
        grade: "HD",
        mark: 80
      },
      {
        code: "eng0011",
        grade: "C",
        mark: 62
      },
      {
        code: "eng0012",
        grade: "P",
        mark: 52
      },
    ]
  }
];
console.log(`Mark: ${data[0].units[1].mark}`);

// Q2
mark = 50;
if (mark >= 0 && mark <= 100)
{
    console.log("valid result")
}

// Q3
let spiders = 1;

while (spiders < 10)
{
    console.log("Argh! spiders!");
    spiders = spiders + 1;
}

for (let spiders = 1; spiders < 10; spiders++)
{
    console.log("Argh! spiders!")
}

// Q4
let data = [
  506, false, "164", 514, 135, 547, "18", 743, 838, 313, 885, 
  652, false, false, "949", 353, 855, "963", 368, false, 
  "179", 706, "189", 573, "744", 149, "266", true, true, 
  "781", false, 224, "643", 176, false, "845", 465, 235, 968, 
  302, "238", "755", 959, "540", 249, 622, "547", "193", 158, 
  true, "177", true, "582", "427", false, "849", 418, "545", 
  true, "990", "497", "724", false, 544, 141, false, "102", 
  183, 633, "847", 992, 271, 835, 551, "972", 574, false, 
  271, false, 810, 54, true, true, 513, 13, false, 268, 
  "418", 77, 707, "936", false, false, 628, 932, false, 319, 
  148, "207", false
];
let sortedData = {
    string: [],
    boolean: [],
    number:[]
};
for (let i = 0; i < data.length; i++)
{
  if (typeof(data[i]) == "string")
  {
    sortedData.string.push(data[i]);
  }
  else if (typeof(data[i]) == "boolean")
  {
    sortedData.boolean.push(data[i]);
  }
  else if (typeof(data[i]) == "number")
  {
    sortedData.number.push(data[i]);
  }
}
console.log(sortedData);

// Q5
let data = [7976, 5580, 4832, 2520, 3089, 6275, 9894, 3850, 2760, 1078, 2691, 8934, 1152, 4335, 7212, 7524, 4797, 5016, 3996, 8310];
let largestNumber = data[0], smallestNumber = data[0];
for (let i = 1; i < data.length - 1; i++)
{
  if (data[i] > largestNumber)
  {
    largestNumber = data[i];
  }
  else if (data[i] < smallestNumber)
  {
    smallestNumber = data[i];
  }
}
console.log(`Largest number: ${largestNumber}\nSmallest number: ${smallestNumber}`);
// max = Math.max(...data);
// min = Math.min(...data);
// console.log(max + "\n" + min)



/*
let data4 = [
    -151, 497, 920, -849, -473, -213, 365, -338, -23, -712, 
    161, 595, -914, 157, -768, 64, 749, 781, 539, -201, -377, 
    -85, 267, 230, -197, 616, -605, 669, -133, -36, -65, -794, 
    -146, -440, -79, 867, 533, 341, -982, 181, 975, -958, -562, 
    -707, 130, 730, -86, 769, 47, 658, -68, -470, 619, -797, 
    259, -572, -455, 454, -780, 145, 668, 489, -840, 380, 974, 
    25, 89, -573, -539, 892, 457, 295, 936, -847, -282, 905, 
    973, -918, -684, -942, -129, 26, -15, -678, 158, 421, -229, 
    -32, 426, -836, 923, -442, 736, -984, -547, 582, 797, 209, 
    -784, -842
];
let odd = [];
let even = [];

  for (let i = 0; i < data4.length; i++) 
  {
    if (data4[i] % 2 === 0) 
    {
      even.push(data4[i]);
    } 
    else 
    {
      odd.push(data4[i]);
    }
  }
console.log(even);
console.log(odd);

const LIMIT = 50;
let dat = [];
while (dat.length < LIMIT)
{
    let number = Math.random()*100;
    dat.push(number);
}
console.log(dat)
*/