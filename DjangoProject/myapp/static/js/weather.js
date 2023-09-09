let url="https://api.openweathermap.org/data/2.5/weather?appid=6fa99e1f96f024f79970c5a3532b2ac6&units=metric&q=vadakara"
// fetch(url).then(res=>res.json()).then(data=>console.log(data))

function fetchWeather(){
    let city=id_city.value
    fetch(`https://api.openweathermap.org/data/2.5/weather?appid=6fa99e1f96f024f79970c5a3532b2ac6&units=metric&q=${city}`).then(res=>res.json()).then(data=>displayWeather(data))
}

function displayWeather(data){
    let name=data.name
    let icon=data.weather[0].icon
    let type=data.weather[0].main
    let description=data.weather[0].description
    let temp=data.main.temp
    let date= new Date().toLocaleDateString()
    // console.log(name,icon,type,description,temp);
    let htmldata=`
    <article class="widget mt-5">
    <div class="weatherIcon"><i class="wi wi-day-cloudy"></i></div>
    <div class="weatherInfo">
      <div class="temperature"><span>${temp}&deg;</span></div>
      <div class="description">    
        <div class="weatherCondition">${type}</div>    
        <div class="place">${name}</div>
      </div>
    </div>
    <div class="date">${date}</div>
  </article>
    `
document.querySelector("#id_result").innerHTML=htmldata
}

function getCurrentweather(){
    navigator.geolocation.getCurrentPosition((p)=>{
        let lat=p.coords.latitude
        let lon=p.coords.longitude
        fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=6fa99e1f96f024f79970c5a3532b2ac6&units=metric`).then(res=>res.json()).then(data=>displayWeather(data))
    })

    
}