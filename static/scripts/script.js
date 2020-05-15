console.log("HI")


function validateForm() {
        let title = document.forms["form"]["programme_title"].value;
        let date = document.forms["form"]["programme_date"].value;
        let time = document.forms["form"]["programme_time"].value;
        let description = document.forms["form"]["programme_description"].value;
        
        if (title === ""){
            alert("name must be filled")
            return false;
        }
        if (date === ""){
            alert("date must be filled")
            return false;
        }
        if (time === ""){
            alert("time must be filled")
            return false;
        }
        if (description === ""){
            alert("Description must be filled")
            return false;
        }


}
