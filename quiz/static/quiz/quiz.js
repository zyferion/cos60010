const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')

// present quiz questions and answers 
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

// get quiz results
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
            // console.log(response)
            const results = response.results
            //console.log(results)
            quizForm.style.display="none" // hide the form when it is submitted
            
            const cls = ['container', 'p-3', 'text-bold', 'h5']
            scoreBox.classList.add(...cls)
            scoreBox.innerHTML += `Total score: You got <b>${response.score} out of ${response.num_questions}</b> questions correct.`
            scoreBox.innerHTML += `<br>`
            scoreBox.innerHTML += `Percentage score: ${response.score_}%`

            // display each question and response
            results.forEach(res=>{
                const resDiv = document.createElement("dev")
                for (const [question, resp] of Object.entries(res)){
                    //console.log(question)
                    //console.log(resp)
                    //console.log('===========')

                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    if(resp=='not answered'){
                        resDiv.innerHTML += '- not answered'
                        resDiv.classList.add('bg-danger')
                    } 
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']
                        
                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` | answered: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | correct answer: ${correct}`
                            resDiv.innerHTML += ` | answered:  ${answer}`
                        }
                    }
                }

                //const body = document.getElementsByTagName('BODY')[0]
                resultBox.append(resDiv)

                var hr_elem = document.createElement("p")
                resultBox.append(hr_elem)

                var br_elem = document.createElement("br")
                resultBox.append(br_elem)
            })


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

