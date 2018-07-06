$("document").ready(function() {

    //Not used current as datepicker
    //var today = new Date(2000, new Date().getMonth(), new Date().getDate());
    //$('#startDate').datepicker({
    //    uiLibrary: 'bootstrap4',
    //    iconsLibrary: 'fontawesome',
    //    minDate: today,
    //    maxDate: function () {
    //        return $('#endDate').val();
    //    }
    //});
    //  $('#endDate').datepicker({
    //      uiLibrary: 'bootstrap4',
    //      iconsLibrary: 'fontawesome',
    //      minDate: function () {
    //          return $('#startDate').val();
    //      }
    //  });

    $(function() {
        $('input[name="daterange"]').daterangepicker({
            timePicker: true,
            timePickerIncrement: 30,
            locale: {
                format: 'MM/DD/YYYY'
                //format: 'MM/DD/YYYY h:mm A'
            }
        });
    });

    var viewportWidth = $(window).width();
    var viewportHeight = $(window).height();
    
    console.log("Viewport Width: "+viewportWidth+", Viewport Height: "+viewportHeight);
    
    $( "#name1" ).autocomplete({
      source: [ "Joshua", "Gene", "Larry", "Mo", "Cameron", "Mitch", "Robert", "Larry", "Brad", "Jerry", "Jeff", "Curly", "Glenn", "Matt" ]
    });

    /*$( function() {//Test JQuery-UI functioning
        $( "#draggable" ).draggable();
    } );*/
    
    $(".flashed-message").delay(5000).slideToggle();
 
    $(".super_secure_dropdown_text").on("click", (function(){//For future secure paths
        $("#denied").delay( 200 ).animate({
                opacity: 1,
                bottom: "+=320"
             }, 75, function() {
                    $("#denied").delay( 2000 ).animate({
                    opacity: 0,
                    bottom: "0"
                 }, 300, function() {}
                    );
        });
    }));
    
    $("#login-welcome").delay( 1000 ).animate({// Good working example of multiple effects
        opacity: 0,
        right: "+=1000",//Note the element cannot be moved if static
        height: "toggle"
      }, 1500, function() {
            $("#login-second").animate({
            opacity: 1
         }, 750, function() {
             $("#login-second-btn-clk").animate({
             opacity: 1
             }, 300, function() {
                
                });
          });
      });
                
    $("button").on("click", (function(){
        val = $(this).attr("value");
        var custSel1Arr = [];
        if (val == "Login") {
            $(".form1").toggleClass("invisible");
            $("#name1").focus();
            console.log("Value: "+val);            
        } else if (val == "Register") {
            $(".form2")/*.slideToggle("fast")*/.toggleClass("invisible");
            $("#name2").focus();
            console.log("Value: "+val);
        } else if (val == "Begin") {
            //populate form plz--------------------------------------------------------------------------
            if ($("li.cust-sel1").size() < 3) {
                $( this ).click(function( event ) {
                  event.preventDefault();
                });
            } else {
                
                $("div#new-query-cycle").find("li.cust-sel1").each(function(){
                    if(($.trim($(this).val()).length>0)){
                     custSel1Arr.push($(this).text());
                    }
                    
                });
                
                /*console.log("Text item: " + custSel1Arr[0] + ", " + custSel1Arr[1] + ", " + custSel1Arr[2] + ", " + custSel1Arr[3] + ", "  );
                var i;
                for (i = 0; i < 8; i++) { 
                    if (custSel1Arr[i] == undefined) {
                        console.log("In");
                    }
                }*/
            }
        }  else if (val == "Reset") {
            $("li.sel1").removeClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel1" );
            $("#render-form-button").addClass("disabled");
            $("#render-icon").removeClass("fa-check");
            console.log("Value: "+val);
        } else if (val == "New") {
            $("#new-or-archive").animate({// Good working example of multiple effects
                opacity: 0,
                bottom: "+=500",//Note the element cannot be moved if static
                //width: [ "toggle", "swing" ],
                height: [ "toggle", "swing" ]
              }, 750, function() {
                    $("#new-query-cycle").removeClass("invisible")
                    $("#new-query-cycle").animate({
                    opacity: 1
                 }, 500
                     );
              });
        } else if (val == "Archives") {
            $("#new-or-archive").animate({// Good working example of multiple effects
                opacity: 0,
                bottom: "+=200",//Note the element cannot be moved if static
                //width: [ "toggle", "swing" ],
                height: [ "toggle", "swing" ]
            }, 750, function() {
                    $("#archived-query-request").animate({
                        opacity: 1
                    }, 500, function() { 
                     $("#archived-query-request").delay(3000).animate({
                         opacity: 0
                     }, 500, function() { 
                         $("#new-or-archive").delay(1000).animate({
                            opacity: 1,
                            top: "+=200",//Note the element cannot be moved if static
                            //width: [ "toggle", "swing" ],
                            height: [ "toggle", "swing" ]
                         }, 750
                         );
                            });
                 });
            });
        } else {
            console.log("Button value undefined");
        }
        //console.log(typeof val);
        //$(".append").append(" "+step1 +"<br><b>Selection Criterea:</b> ");
    }));
    
    $("li.sel1").on("click", (function(){
        val = $(this).attr("value");
        //console.log("About to change class: "+$("li.cust-sel1").size());
        //console.log("Value: "+val);
        
        if (val == "all") {//Dynamically changes list visuals to indicate selection
            $("li.sel1").addClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
            console.log("About to change class: "+typeof $("li.cust-sel1").size());
        } else {//Dynamically changes list visuals to indicate selection
            $(this).toggleClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
            console.log("About to change classes: " + $("li.cust-sel1").length);
        } 
        
        if ($("li.cust-sel1").size() >= 3) {//Dynamically changes Render Form buttin according to specification
            $("#render-form-button").removeClass("disabled");
            $("#render-icon").addClass("fa-check");
        } else {//Dynamically changes Render Form buttin according to specification
            $("#render-form-button").addClass("disabled");
            $("#render-icon").removeClass("fa-check");
        }
        //console.log(typeof val);
        //$(".append").append(" "+step1 +"<br><b>Selection Criterea:</b> ");
    }));
    
});//$("document").ready(function() {

  /*$( function() {//Good example of going back and forth between animations
    var state = true;
    $( "#button" ).on( "click", function() {
      if ( state ) {
        $( "#effect" ).animate({
          backgroundColor: "#aa0000",
          color: "#fff",
          width: 500
        }, 1000 );
      } else {
        $( "#effect" ).animate({
          backgroundColor: "#fff",
          color: "#000",
          width: 240
        }, 1000 );
      }
      state = !state;
    });
  } );*/