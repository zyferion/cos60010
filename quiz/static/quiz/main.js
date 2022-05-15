const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const subject = modalBtn.getAttribute('data-subject')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you ready to attempt "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>Subject: <b>${subject}</b></li>
                <li>Total number of questions: <b>${numQuestions}</b></li>
                <li>You only have <b>one</b> attempt. </li>
                <li> All questions are of <b>equal</b> value. </li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))