// upload image
document.querySelector('#uploadForm').addEventListener('submit', function(e){
    e.preventDefault()

    const fileInput = document.querySelector('#imageInput')
    const message = document.querySelector('#message')

    if(!fileInput.files.length){
        message.textContent = "Please select an image!"
        message.style.color = 'red'
        return ;
    }
})