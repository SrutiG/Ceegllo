
$(document).ready(function() {
    $("#cancelBT").click(function() {
        parent.history.back();
        return false;
    });
    $(".dropdown-toggle").dropdown();

    $(".semester-future").on('click', '.add-class', function() {
            var newDiv = $(".class-future")[0].outerHTML;
            $(this).before(newDiv);
            $(this).prev().children(".class-name").removeAttr("value");
            $(this).prev().children(".cred").removeAttr("value");
            $(this).prev().children(".class-name").attr("placeholder", "Class");
            $(this).prev().children(".cred").attr("placeholder", "Credits");
    });
    $(".semester").on('click', '.add-class', function() {
                var newDiv = $(".class-prev")[0].outerHTML;
                $(this).before(newDiv);
                $(this).prev().children(".class-name").removeAttr("value");
                $(this).prev().children(".cred").removeAttr("value");
                $(this).prev().children(".grade").removeAttr("value");
                $(this).prev().children(".class-name").attr("placeholder", "Class");
                $(this).prev().children(".cred").attr("placeholder", "Credits");
                $(this).prev().children(".grade").attr("placeholder", "Grade");
    });
    $("#addSemester").click(function() {
        var newDiv = $(".semester-template")[0].outerHTML;
        $(this).before(newDiv);
        $(".semester-template:last").removeAttr("style");
    })
    $("#addFutureSemester").click(function() {
        var newDiv = $(".semester-future-template")[0].outerHTML;
        $(this).before(newDiv);
        $(".semester-future-template:last").removeAttr("style");
    })

});

function editCollege(){
        window.location="../editcollege";
    }

function goBack() {
    window.history.back();
}

