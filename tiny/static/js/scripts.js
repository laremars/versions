$("document").ready(function() {

    /*$( function() {//Test JQuery-UI functioning
        $( "#draggable" ).draggable();
    } );*/
    $(".form1").slideToggle();
    $(".form2").slideToggle();
    
    $("button").click(function(){
        val = $(this).attr("value");
        if (val == "Login") {
            $(".form1").removeClass("invisible").slideToggle("fast");
            $("#name1").focus();
            
        } else if (val == "Register") {
            $(".form2").slideToggle("fast").removeClass("invisible");
            $("#name2").focus();
        } else {
            console.log("Button value undefined");
        }
        //console.log(typeof val);
        //$(".append").append(" "+step1 +"<br><b>Selection Criterea:</b> ");
    });
    
    

    
});//$("document").ready(function() {