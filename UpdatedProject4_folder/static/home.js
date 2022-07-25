const headerImg = document.querySelector('.head')

const UPDATE_TIME_INTERVAL = 4000

//  Enter URLs of your own custom images
const imagesArray = [
  "../static/images/burgers-and-fries.jpg",
  "../static/images/ground-beef-pizza.jpg",
  "../static/images/hotwings.jpeg",
  "../static/images/meatloverspizza.jpg",
  "../static/images/chipotle-lentil-tacos.jpg",
  "../static/images/frozenyogurt.jpg",
  "../static/images/cupcakes.jpg",
  "../static/images/Chocolate-Lava-Cakes.jpg",
  "../static/images/vegan-brownies.jpg",
  "../static/images/vegan-nice-cream.jpg",
  "../static/images/veggie-mushroom-and-olives.jpg",
  "../static/images/BBQ-Chicken-Pizza.jpg"
]

let i = 0

setInterval(()=>{
  if(i == 11){
    i = 0
  }
  else {i = i + 1};
  console.log('i was run',i)
  console.log(headerImg);
  headerImg.src = imagesArray[i]
},UPDATE_TIME_INTERVAL)


const popularitemsclass = [...document.querySelectorAll('.popularitemsclass')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

popularitemsclass.forEach((item, i) => {
    let containerDimenstions = item.getBoundingClientRect();
    let containerWidth = containerDimenstions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})

const veganandglutenfreeclass = [...document.querySelectorAll('.veganandglutenfreeclass')];

veganandglutenfreeclass.forEach((item, i) => {
    let containerDimenstions = item.getBoundingClientRect();
    let containerWidth = containerDimenstions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})


const sweettreatsclass = [...document.querySelectorAll('.sweettreatsclass')];

sweettreatsclass.forEach((item, i) => {
    let containerDimenstions = item.getBoundingClientRect();
    let containerWidth = containerDimenstions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})


const pizzasclass = [...document.querySelectorAll('.pizzasclass')];

pizzasclass.forEach((item, i) => {
    let containerDimenstions = item.getBoundingClientRect();
    let containerWidth = containerDimenstions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})
