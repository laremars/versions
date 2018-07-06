$("document").ready(function() {

    var viewportWidth = $(window).width();
    var viewportHeight = $(window).height();
    
    console.log("Viewport Width: "+viewportWidth+", Viewport Height: "+viewportHeight);
    
    $( "#name1" ).autocomplete({
      source: [ "Joshua", "Gene", "Larry", "Mo", "Cameron", "Mitch", "Robert", "Larry", "Brad", "Jerry", "Jeff", "Curly", "Glenn", "Matt" ]
    });

    /*$( function() {//Test JQuery-UI functioning
        $( "#draggable" ).draggable();
    } );*/
    $(".form1").slideToggle();
    
    $(".form2").slideToggle();

    $(".flashed-message").delay(5000).slideToggle();
    
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
        if (val == "Login") {
            $(".form1").removeClass("invisible").slideToggle("fast");
            $("#name1").focus();
            console.log("Value: "+val);            
        } else if (val == "Register") {
            $(".form2").slideToggle("fast").removeClass("invisible");
            $("#name2").focus();
            console.log("Value: "+val);
        } else if (val == "Begin") {
            //populate form plz--------------------------------------------------------------------------
            if ($("li.cust-sel1").size() < 3) {
                $( this ).click(function( event ) {
                  event.preventDefault();
                });
            } else {
                console.log("Value: "+val);
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
        console.log("About to change class: "+$("li.cust-sel1").size());
        console.log("Value: "+val);
        
        if (val == "all") {
            $("li.sel1").addClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel1" );
            console.log("About to change class: "+typeof $("li.cust-sel1").size());
        } else {
            $(this).toggleClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel1" );
            console.log("About to change classes: " + $("li.cust-sel1").length);
        } 
        
        if ($("li.cust-sel1").size() >= 3) {
            $("#render-form-button").removeClass("disabled");
            $("#render-icon").addClass("fa-check");
        } else {
            $("#render-form-button").addClass("disabled");
            $("#render-icon").removeClass("fa-check");
        }
        //console.log(typeof val);
        //$(".append").append(" "+step1 +"<br><b>Selection Criterea:</b> ");
    }));
    
});//$("document").ready(function() {

/*$("#login-welcome").animate({// Good working example of multiple effects
    opacity: 0,
    left: "+=150",//Note the element cannot be moved if static
    height: "toggle"
  }, 2000, function() {
        $("#login-welcome").animate({
        opacity: 0.25,
        left: "+=50",
        height: "toggle"
      }, 1000, function() {
        // Animation complete.
      });
  });
  $("#login-welcome").animate({// Good working example of multiple effects
        opacity: 0,
        left: "+=150",//Note the element cannot be moved if static
        height: "toggle"
      }, 2000, function() {
            $(this).animate({
            opacity: 0.25,
            left: "+=50",
            height: "toggle"
          }, 1000, function() {
            $( this ).after( "<div>Animation complete.</div>" );
          });
      });
  $( function() {//Good example of going back and forth between animations
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