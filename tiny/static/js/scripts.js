$("document").ready(function() {

    $(function() {
        /*$('input[name="daterange"]').daterangepicker({
            timePicker: true,
            timePickerIncrement: 30,
            locale: {
                format: 'MM/DD/YYYY'
                //format: 'MM/DD/YYYY h:mm A'
            }
        });*/
        /*
        An excellent resource for different methods of controlling the
            daterangepicker exists on its site:
            http://www.daterangepicker.com/
        */
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
            "startDate": moment().subtract(30, 'days'),
            "endDate": moment()
        }, function(start, end, label) {
          console.log('New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')');
        });
    });

    $('li.sel1').css('cursor', 'pointer');
    $('li.sel-mult').css('cursor', 'pointer');
    
    console.log("Viewport Width: "+$(window).width()+", Viewport Height: "+$(window).height());
    
    /*
        .autocomplete is a JQuery method which allows a text input field to predict predetermined field names
        this has two potential purposes:
            the first purpose is largely convenience
            the second purpose is ensuring proper input formatting, so that the value matched predetermined constraints
    */
    
    $( "#name1" ).autocomplete({
      source: [ "Joshua", "Gene", "Larry", "Mo", "Cameron", "Mitch", "Robert", "Larry", "Brad", "Jerry", "Jeff", "Curly", "Glenn", "Matt", "Pete" ]
    });
    
    $( "#step_name" ).autocomplete({
      source: [ "OK", "CFR", "IOPE", "WDAT0", "X-AXIS", "PWR" ]
    });
    
    $( "#name1" ).val("Larry");
    
    /*$( function() {//Test JQuery-UI functioning
        $( "#draggable" ).draggable();
    } );*/
    
    //$(".flashed-message").delay(5000).slideToggle();
    
    var secureCounter = 0;
    $(".super_secure_dropdown_text").on("click", (function(){// For future secure paths
        secureCounter++;
        if ( secureCounter <= 17 ) {
            $( "#score" ).append( "<p><strong>Current Score:</strong> "+secureCounter+"</p><p><strong>High Score:</strong> 17</p>" );
        } else {
            $( "#score" ).append( "<p>Wow, did you... </p><p><strong>New High Score:</strong> "+secureCounter+"</p>" );
        }
        
        $("#denied").delay( 50 ).animate({// Good working example of multiple effects
                opacity: 1,
                bottom: "+=330"//Note the element cannot be moved if static
             }, 75, function() {// Effect lasts 75ms, then the next function kicks off afer a 2s delay
                    $("#denied").delay( 1000*secureCounter ).animate({// delay one second times the number of times the user was warned
                    opacity: 0,
                    bottom: "0"
                 }, 300*secureCounter, function() {
                             $( "#score" ).empty();
                         });
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
        } else if (val == "Begin-Default") {
            $( "#step_name" ).val( "OK" ); //Set defaults
            $( "#part_number" ).val( "all" ); //Set defaults
            $( "#tester" ).val( "all" ); //Set defaults
            
            $("#new-query-cycle").animate({// Good working example of multiple effects
                opacity: 0,
                bottom: "+=500",//Note the element cannot be moved if static
                //width: [ "toggle", "swing" ],//weird effect when both width and height swing are on
                height: [ "toggle", "swing" ]
              }, 750, function() {
                    $("#query-form").animate({
                        opacity: 1
                 }, 500
                     );
              });
              
            autoScroll("#interface-description");
            
            $( ".page-header" ).append( ' <p class="lead ml-5 pl-5 text-primary text-monospace col-9">Press <code class="text-dark">Cancel</code> to return to the selection menu. </p>' );
            
        } else if (val == "Begin") {
            //populate form plz--------------------------------------------------------------------------
                
            autoScroll("#interface-description");
            
            $("div#collapse-date").find("li.cust-sel1").each(function() {
                if( ( $.trim( $( this ).val() ).length>0) ){
                   //console.log( $( this ).val() );
                    switch( $( this ).text()) {
                        case "Last Year":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(1, 'years'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Last 6 Months":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(6, 'months'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Last 90 Days":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(3, 'months'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Last 60 Days":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(2, 'months'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Last 30 Days":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(30, 'days'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Last 15 Days":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(15, 'days'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Last 7 Days":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(7, 'days'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        case "Yesterday":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment().subtract(1, 'days'));
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment().subtract(1, 'days'));
                            break;
                        case "Today":
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment());
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            break;
                        default:
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment());
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                            console.log("list item not defined")
                    }
                } else {
                            $('input[name="daterange"]').data('daterangepicker').setStartDate(moment());
                            $('input[name="daterange"]').data('daterangepicker').setEndDate(moment());
                }
            });
            

            var tester = [];
            $("div#collapse-tester").find("li.cust-sel-mult").each(function() {
                if( ( $.trim( $( this ).val() ).length>0) ){
                   tester.push( $( this ).text() );
                }
            });
            if (tester.length > 0) {
                $( "#tester" ).val( tester );
            } else {
                $( "#tester" ).val( "all" ); //Set defaults
            }
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
            if (process_type) {
                $( "#process_type" ).val( process_type );
            } else {
                $( "#process_type" ).val( "all" ); //Set defaults
            }
            //console.log( $( "#process_type" ).val() );
            
            
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
            
            var output;
            $("div#collapse-output").find("li.cust-sel1").first().each(function() {
                if( ( $.trim( $( this ).val() ).length>0) ){
                   output = $( this ).text();//This may actually be an array coming back
                }
            });
            if ( report_type == "histogram" || report_type == "time_series" ) {//They want a plot, as indicated above
                $( "#output" ).val( "plot" );
            } else {
                $( "#output" ).val( output );
            }
            //console.log( $( "#output" ).val() );
            
            $( "#step_name" ).val( "OK" ); //Set defaults
            $( "#part_number" ).val( "all" ); //Set defaults
            
            $("#new-query-cycle").animate({// Good working example of multiple effects
                opacity: 0,
                bottom: "+=500",//Note the element cannot be moved if static
                //width: [ "toggle", "swing" ],//weird effect when both width and height swing are on
                height: [ "toggle", "swing" ]
              }, 750, function() {
                    $("#query-form").animate({
                        opacity: 1
                 }, 500
                     );
              });

            
        } else if (val == "Reset") {
            $("li.sel1").removeClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel1" );
            $("li.sel-mult").removeClass( "list-group-item-primary text-right font-weight-bold text-success shadow-lg cust-sel-mult" );
            $("#render-form-button").addClass("disabled");
            $("#render-icon").removeClass("fa-check");
            console.log("Value: "+val);
            $("div#accordion").find("li.dependent").each(function() {
                $( this ).attr("style", "display:none;");
            });
            
        } else if (val == "Cancel") {
            $("#query-form").animate({// Good working example of multiple effects
                opacity: 0
              }, 300, function() {
                    $("#new-query-cycle").delay(250).animate({
                opacity: 1,
                bottom: "-=500",//Note the element cannot be moved if static
                height: [ "toggle", "swing" ]
                 }, 500
                     );
              });
        } else if (val == "New") {
            $("#interface-description").text("Click on any item to prepopulate form fields.").delay(5000).animate({
                opacity: 0
            }, 200
            );
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
              
        } else if (val == "Archives") {//will be removed once archived queries have been implemented
            $("#new-or-archive").animate({// Good working example of multiple effects: moves current div out...
                opacity: 0,
                bottom: "+=200",//Note the element cannot be moved if static
                height: [ "toggle", "swing" ]
            }, 200, function() {
                    $("#archived-query-request").animate({//reveals warning message...
                        opacity: 1
                    }, 200, function() { 
                            $("#archived-query-request").delay(500).animate({//hides warning message
                                opacity: 0
                         }, 200, function() { 
                                 $("#new-or-archive").delay(200).animate({//moves div back in for valid selection
                                    opacity: 1,
                                    bottom: "0",
                                    height: [ "toggle", "swing" ]}, 200, function(){
                                        //additional effects can continue if desired
                                    });
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
    
    $("li.sel-mult").on("click", (function(){//Custom Multiple Select Field Logic
    
        val = $(this).attr("value");
        
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

    $("li.sel1").on("click", (function(){//Custom Single Select Field Logic
    
        val = $(this).attr("value");
        /*
        if ( val == "TX") {
            console.log(typeof val+" : "+val);
        }
        */

        
        
        if ( $( this ).hasClass("nested-sib") ) { //Ensures siblings can't be selected at the same time -- Depends strongly on DOM structure for traversal
            $( this ).parentsUntil(".nested").find(".nested-sib").not( $( this ) ).removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
            console.log( val )
        }
        
        $( this ).toggleClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1 " ); //if the value isn't all, only add the classes to this item
        $( this ).siblings().removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" ); //Ensures siblings can't be selected at the same time
        
        if ( val == "CSV" && $( this ).hasClass("cust-sel1") ) {//csv and plot options shouldn't be selected at the same time
            $( this ).parentsUntil(".nested").find("li[value='None']").addClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" ); // Selects None
        }
        
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        checkDependentDisplay(val, $( this ).hasClass("cust-sel1"), $( this ).hasClass("dependent"), $( this ).prop("classList") );

        
        $("#render-form-button").removeClass("disabled");
        $("#render-icon").addClass("fa-check");
        
    }));
    
    $( "#report_type" ).change( function() {
        if ( $( this ).val() != "none" ) {
            $( "#output" ).val("plot");
        } else {
             $( "#output" ).val("csv");
        }
    });
    /*
    $("#heading-tester").on("click", (function(){
        $('html, body').delay(10).animate({
            scrollTop: $('#heading-tester').offset().top - 60
        }, 350);
    }));
*/

    autoScroll("#heading-tester","#heading-tester", 0, 20, 300);
    autoScroll("#heading-line");
    autoScroll("#heading-date","#heading-date", 0, 20, 500);
    autoScroll("#heading-step");
    autoScroll("#heading-process_type");
    autoScroll("#heading-product");
    autoScroll("#heading-output");
    autoScroll("#render-default-form-button", "#interface-title");
    autoScroll("#login", "#mee");
    autoScroll("#register", "#mee");
    autoScroll("#reset-button", "#heading-date", -90);

    
    /*
        Only requires one argument: identifier. 
        Defaults to scroll to the top of the element specified by the passed in identifier on click, which should be a string value representing the class or id
        If there is a second optional target passed in, the autoScroll function will instead jump to the top of this element after the passed in identifier is clicked. Target can be equal to identifier
        The third optional parameter represents additonal distance from the top of the screen, raltive to the identifier: should be a positive or negative integer
        The fourth optional parameter represents the delay between the click event and the beginning of the scroll animation. No supplied delay will default to near instant event triggering
        The fifth optional parameter represents the duration of the scroll animation. no supplied duration will default animation to 300ms
    */
    function autoScroll(identifier, target, dist, delay, animation) {
        target = typeof target=='undefined' ? identifier : target;//target becomes identifier if not supplied in the function call
        dist = typeof dist=='undefined' ? 0 : dist;//dist becomes 0px if not supplied in the function call
        delay = typeof delay=='undefined' ? 20 : delay;//delay becomes 1ms if not supplied in the function call
        animation = typeof animation=='undefined' ? 300 : animation;//animation becomes 300ms if not supplied in the function call
        $(identifier).on("click", (function(){
            $('html, body').delay(delay).animate({//optional delay before animation begins
                scrollTop: $(target).offset().top + dist - 60
            }, animation);//optional animation period
        }));
    }
    
    function checkDependentDisplay(value, isSelected, isDependent, arr) {
        //console.log(arr.toString())

        if (value == "all") {//sets "all" to unique value before switch statement
            var thisList = "";
            $.each( arr, function( i, list ){
              switch(list){
                  case "product":
                      value = "allProduct"
                      console.log(value);
                      break;
                  case "process":
                      value = "allProcess"
                      console.log(value);
                      break;
                  case "line":
                      value = "allLine"
                      console.log(value);
                      break;
                  case "step":
                      value = "allStep"
                      console.log(value);
                      break;
                  case "tester":
                      value = "allTester"
                      console.log(value);
                      break;
                  default:
                      break;
              }
            });
        }

        switch( value ) {
            case "allProduct":
            case "TX":
            case "RX":
                if (isSelected) {
                    $("div#collapse-process_type").find("li.dependent").each(function() {
                        $( this ).removeAttr("style").removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
                        //console.log("remove attr from "+ $(this).text())
                    });
                    $("div#collapse-line").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;").removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
                    });
                    $("div#collapse-tester").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;").removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
                    });
                } else {
                    $("div#accordion").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;").removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
                    });
                }
                break;
                
            case "allProcess":
            case "ICC":
            case "ECU":
                
                
            
                if (isSelected) {
                
                    $("div#collapse-product").find("li.cust-sel1").each(function() {
                        if ( $( this ).text() == "TX" ) {
                            $("div#collapse-line").find("li.dependent").each(function() {
                                if ( $( this ).text().indexOf("TX") !== -1) {
                                    $( this ).removeAttr("style");
                                } else {
                                    $( this ).attr("style", "display:none;");
                                }
                            });
                        } else if ( $( this ).text() == "RX" ) {
                            $("div#collapse-line").find("li.dependent").each(function() {
                                if ( $( this ).text().indexOf("RX") !== -1) {
                                    $( this ).removeAttr("style");
                                } else {
                                    $( this ).attr("style", "display:none;");
                                }
                            });
                        } else if ( $( this ).text() == "all" ) {
                            $("div#collapse-line").find("li.dependent").each(function() {
                                $( this ).removeAttr("style");
                            });
                        } else {
                            $("div#collapse-line").find("li.dependent").each(function() {
                                $( this ).attr("style", "display:none;");
                            });
                        }
                    });
                    
                    $("div#collapse-tester").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;");
                    });
                    
                    $("div#collapse-line").find("li.cust-sel1").each(function() {
                        $( this ).removeClass( "list-group-item-primary font-weight-bold text-success shadow-lg cust-sel1" );
                    });
                    
                } else {
                
                    $("div#collapse-line").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;");
                    });
                    $("div#collapse-tester").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;");
                    });
                    
                }
                
                break;
                
            case "allLine":
                $( "li.tester" ).each(function() {
                    $( this ).removeAttr("style");
                });
                break;
            case "TX1":
            case "TX2":
            case "TX3":
            case "TX4":
            case "RX1":
            case "RX2":
            case "RX3":
            case "RX4":
            
                var dep = [];
                $("div#collapse-tester").find("li.dependent").each(function() {
                    if( ( $.trim( $( this ).val() ).length>0) ){
                       dep.push( $( this ).text() );
                    }
                });
                
                var product="";
                var process="";
                var line="";
                
                if (isSelected) {
                
                    $("div#collapse-product").find("li.cust-sel1").each(function() {
                        product = $( this ).text();
                    });
                    $("div#collapse-process_type").find("li.cust-sel1").each(function() {
                        process = $( this ).text();
                    });
                    $("div#collapse-line").find("li.cust-sel1").each(function() {
                        line = $( this ).text();
                    });
                    $.each(dep, function(index, value){
                        if ( ((value.charAt(0) == line.charAt(0) && value.charAt(1) == line.charAt(2)) || line == "all") && (value.includes(process) || process == "all") ) {
                            $( "li.tester[value='"+value+"']" ).removeAttr("style");
                        } else {
                                $( "li.tester[value='"+value+"']" ).attr("style", "display:none;");
                        }
                    });
                    
                    /*if (process != "allProcess"){
                        $.each(dep, function(index, value){
                            if ( value.charAt(0) == product.charAt(0) && value.charAt(1) == line.charAt(2) && value.includes(process) ) {
                                $( "li[value='"+value+"']" ).removeAttr("style");
                            } else {
                                if ( value != "allLine" ) {//don't want to get rid of items matching this value
                                    $( "li[value='"+value+"']" ).attr("style", "display:none;");
                                }
                            }
                        });
                    } else {
                        $.each(dep, function(index, value){
                            if ( value.charAt(0) == product.charAt(0) && value.charAt(1) == line.charAt(2) ) {
                                $( "li[value='"+value+"']" ).removeAttr("style");
                            } else {
                                if ( value != "all" ) {//don't want to get rid of items matching this value
                                    $( "li[value='"+value+"']" ).attr("style", "display:none;");
                                }
                            }
                        });
                    }*/

                    
                } else {
                    $("div#collapse-tester").find("li.dependent").each(function() {
                        $( this ).attr("style", "display:none;");
                    });
                }
                break;
                
            default:
                console.log("list item not defined inside the checkDependentDisplay function")
        }
    }
    
    
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