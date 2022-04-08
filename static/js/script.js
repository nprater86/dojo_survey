submitBtn = document.getElementById('submitBtn');
username = document.getElementById('name');

submitBtn.onclick = () => {
    if (!username.value){
        event.preventDefault();
        alert('Please enter your name!');
    }
}