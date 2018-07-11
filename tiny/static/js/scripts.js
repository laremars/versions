$("document").ready(function() {
    
    
    //if ($(window).height() < 768) {
    //}
    $(function() {
        /*$('input[name="daterange"]').daterangepicker({
            timePicker: true,
            timePickerIncrement: 30,
            locale: {
                format: 'MM/DD/YYYY'
                //format: 'MM/DD/YYYY h:mm A'
            }
        });*/
        $('input[name="daterange"]').daterangepicker({
            ranges: {
                'Today': [moment(), moment()],
                'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                'Last 7 Days': [moment().subtract(6, 'days'), moment()],
                'Last 30 Days': [moment().subtract(29, 'days'), moment()],
                'This Month': [moment().startOf('month'), moment().endOf('month')],
                'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')],
                'Last Year': [moment().subtract(1, 'year'), moment()]
            },
            "startDate": "07/04/2018",
            "endDate": "07/10/2018"
        }, function(start, end, label) {
          console.log('New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')');
        });
    });

    $('li.sel1').css('cursor', 'pointer');
    $('li.sel-mult').css('cursor', 'pointer');
    
    console.log("Viewport Width: "+$(window).width()+", Viewport Height: "+$(window).height());
    
    $( "#name1" ).autocomplete({
      source: [ "Joshua", "Gene", "Larry", "Mo", "Cameron", "Mitch", "Robert", "Larry", "Brad", "Jerry", "Jeff", "Curly", "Glenn", "Matt" ]
    });
    
    $( "#name1" ).val("Larry");
    
    $( "#rep-type" ).click( function() {
        $( "#report_type" ).val("histogram");
        console.log( $( "#report_type" ).val() );
    });
    

    /*$( function() {//Test JQuery-UI functioning
        $( "#draggable" ).draggable();
    } );*/
    
    $(".flashed-message").delay(5000).slideToggle();
 
    $(".super_secure_dropdown_text").on("click", (function(){// For future secure paths
        $("#denied").delay( 50 ).animate({// Good working example of multiple effects
                opacity: 1,
                bottom: "+=320"//Note the element cannot be moved if static
             }, 75, function() {// Effect lasts 75ms, then the next function kicks off afer a 2s delay
                    $("#denied").delay( 1000 ).animate({// delay two seconds
                    opacity: 0,
                    bottom: "0"
                 }, 300, function() {}
                    );
        });
    }));
    
    $("#login-welcome").delay( 50 ).animate({
        opacity: 0,
        right: "+=1000",
        height: "toggle"
      }, 300, function() {
            $("#login-second").animate({
            opacity: 1
         }, 300, function() {
             $("#login-second-btn-clk").animate({
             opacity: 1
             }, 300, function() {
                
                });
          });
      });
                
    $("button").on("click", (function(){
        val = $(this).attr("value");
        var sel_mult = [];
        var sel1 = [];
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
                
                /*if ($("li.cust-sel1").size() < 3) {
                    $( this ).click(function( event ) {
                      event.preventDefault();
                    });
                  
                } else {
                    
                    $("div#new-query-cycle").find("li.cust-sel1").each(function(){
                        if(($.trim($(this).val()).length>0)){
                         custSel1Arr.push($(this).text());
                         console.log($(this).parent().html());
                        }
                        
                    });
                    */
                    /*console.log("Text item: " + custSel1Arr[0] + ", " + custSel1Arr[1] + ", " + custSel1Arr[2] + ", " + custSel1Arr[3] + ", "  );
                    var i;
                    for (i = 0; i < 8; i++) { 
                        if (custSel1Arr[i] == undefined) {
                            console.log("In");
                        }
                    }
                    }*/
                    
                console.log("Begin");
                var tester = [];
                $("div#collapse-tester").find("li.cust-sel-mult").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       tester.push( $( this ).text() );
                    }
                });
                $( "#tester" ).val( tester );
                //console.log( $( "#tester" ).val() );
                
                var line;
                $("div#collapse-line").find("li.cust-sel1").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       line = $( this ).text();
                    }
                });
                $( "#line" ).val( line );
                //console.log( $( "#line" ).val() );
                
                var process_type;
                $("div#collapse-process_type").find("li.cust-sel1").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       process_type = $( this ).text();
                    }
                });
                $( "#process_type" ).val( process_type );
                //console.log( $( "#process_type" ).val() );
                
                var output;
                $("div#collapse-output").find("li.cust-sel1").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       output = $( this ).text();//This may actually be an array coming back
                    }
                });
                $( "#output" ).val( output );
                //console.log( $( "#output" ).val() );
                
                var product;
                $("div#collapse-product").find("li.cust-sel1").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       product = $( this ).text();
                    }
                });
                $( "#product" ).val( product );
                //console.log( $( "#product" ).val() );
                
                var report_type;
                $("div#collapse-report_type").find("li.cust-sel1").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       report_type = $( this ).text();
                    }
                });
                $( "#report_type" ).val( report_type );
                //console.log( $( "#report_type" ).val() );
                
                
            
        }  else if (val == "Reset") {
            $("li.sel1").removeClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel1" );
            $("li.sel-mult").removeClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel-mult" );
            $("#render-form-button").addClass("disabled");
            $("#render-icon").removeClass("fa-check");
            console.log("Value: "+val);
        } else if (val == "New") {
            $("#new-or-archive").animate({// Good working example of multiple effects
                opacity: 0,
                bottom: "+=500",//Note the element cannot be moved if static
                //width: [ "toggle", "swing" ],//weird effect when both width and height swing are on
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
            }, 200, function() {
                    $("#archived-query-request").animate({
                        opacity: 1
                    }, 200, function() { 
                     $("#archived-query-request").delay(200).animate({
                         opacity: 0
                     }, 200, function() { 
                         $("#new-or-archive").delay(200).animate({
                            opacity: 1,
                            top: "+=200",//Note the element cannot be moved if static
                            //width: [ "toggle", "swing" ],
                            height: [ "toggle", "swing" ]
                         }, 200
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
    
    $( "li.sel1, .sel-mult" ).hover(
      function() {
        $( this ).append( $( '<span class="text-success"> <<<</span>' ) );
        $( this ).addClass("bg-light");
      }, function() {
        $( this ).find( "span:last" ).remove();
        $( this ).removeClass("bg-light");
      }
    );
    
    $("li.sel-mult").on("click", (function(){//Multiple Select Field Logic
        val = $(this).attr("value");
        //console.log("About to change class: "+$("li.cust-sel1").size());
        //console.log("Value: "+val);
        
        if (val == "all") {//Dynamically changes list visuals to indicate selection
            $( this ).addClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel-mult " );//Adds selected class to "all" field
            $( this ).siblings().addClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel-mult " );//Only targets immediate siblings for selection
            console.log("About to change class: "+typeof $("li.cust-sel-mult").size());
        } else {//Dynamically changes list visuals to indicate selection
            var sibs = $( this ).siblings( "li[value!='all']" ).add( this );//this returns all elements in clocked list with exception of item with value = "all"
            var custClassCount = 0;
            $( this ).toggleClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel-mult " );//if the value isn't all, only add the classes to this item
            
            $( sibs ).each(function( index ) {
              if ( $( this ).hasClass( "cust-sel-mult" ) ) {
                  custClassCount ++;
              }
            });
            
            if ( custClassCount >= sibs.size() ) {
                $( this ).siblings( "li[value='all']" ).addClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel-mult " );// all items have been chosen, so highlight all
            } else {
                $( this ).siblings( "li[value='all']" ).removeClass("list-group-item-primary font-weight-bold text-success shadow-lg cust-sel-mult " );// a sibling to the above item was clicked, meaning all shouldn't be selected unless all items are now highlighted
            }
            
        }
        

            $("#render-form-button").removeClass("disabled");
            $("#render-icon").addClass("fa-check");

        //console.log(typeof val);
        //$(".append").append(" "+step1 +"<br><b>Selection Criterea:</b> ");
    }));

    $("li.sel1").on("click", (function(){//Single Select Field Logic
        val = $(this).attr("value");
        $( this ).toggleClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1 " );//if the value isn't all, only add the classes to this item
        $( this ).siblings().removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
        $("#render-form-button").removeClass("disabled");
        $("#render-icon").addClass("fa-check");
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