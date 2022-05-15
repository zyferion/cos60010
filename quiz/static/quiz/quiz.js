const url = window.location.href
const quizBox = document.getElementById('quiz-box')


$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        //console.log(response)
        const data = response.data
        //console.log(data)

        data.forEach(i =>{
            for (const [question,answers] of Object.entries(i)){
                quizBox.innerHTML += `
                    <br>
                    <div class ="mb-2">
                        <b>${question}</b>
                    </div>
                    <hr>
                 `
                 answers.forEach(answer=>{
                     quizBox.innerHTML += `
                     <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for = "${question}">${answer}</label>
                     </div>
                `
                 })
            }
        });

    },
    error: function(error) {
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    
    //initialise empty dictionary
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value

    // check if question has been attempted
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    // send data to /save
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            console.log(response)
        },
        error: function(error) {
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=> {
    e.preventDefault()

    sendData()
})

