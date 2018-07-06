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





$( function() {
    var selectedEffect = "slide";
    
    // run the currently selected effect
    function runEffect() {
      // get effect type from
      
 
      // Most effect types need no options passed by default
      var options = {};
      // some effects have required parameters, i.e.: scale and size
 
      // Run the effect
      $( ".effectThis" ).toggle( selectedEffect, options, 0 );
    };
 
    // Set effect from select menu value
    $( "#clickHere" ).on( "click", function() {
      runEffect();
    });
    
});

$("document").ready(function() {
  $( function() {
    $( "#draggable" ).draggable();
 
    $( "#droppable, #droppable-inner" ).droppable({
      classes: {
        "ui-droppable-active": "ui-state-active",
        "ui-droppable-hover": "ui-state-hover"
      },
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "> p" )
            .html( "Dropped!" );
        return false;
      }
    });
 
    $( "#droppable2, #droppable2-inner" ).droppable({
      greedy: true,
      classes: {
        "ui-droppable-active": "ui-state-active",
        "ui-droppable-hover": "ui-state-hover"
      },
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "> p" )
            .html( "Dropped!" );
      }
    });
  } );
  
      $(".theDiv").draggable();

//            $("#theDiv").draggable({
//                axis: "x",
//                handle: "h2",
//                revert: true,
//            });

    $(".theDrop").droppable({
        accept: ".theDiv",  // A fucntion can be used in place of the class returning true or false
        hoverClass: "highlight",
        tolerance: "fit",
        
        activate: function (evt, ui) {
            $(this).find("h2").css("background-color", "cornsilk");
        },
        activate: function (evt, ui) {
            $( ".change" ).text("color", "red");
        },
        deactivate: function (evt, ui) {
            $(this).find("h2").css("background-color", "");
        },
        drop: function(evt, ui) {
            $(this).find("h2").text("Dropped");
            ui.draggable.find("h2").text("Dropped");
        }
    });
    /*
    $( ".theDrop" ).on( "dropover", function( evt, ui ) {
        $( ".change" ).css("color", "red");
    } );
  */
    $(function () {
        $("#catalog").accordion();
        $("#catalog li").draggable({
            appendTo: "body",
            helper: "clone",
            connectToSortable: "#cart ol"
        });
        $("#cart ol").sortable({
            items: "li:not(.placeholder)",
            connectWith: "li",
            sort: function () {
    
                $(this).removeClass("ui-state-default");
            },
            over: function () {
                //hides the placeholder when the item is over the sortable
                $(".placeholder").hide(); 
    
            },
            out: function () {
                if ($(this).children(":not(.placeholder)").length == 0) {
                    //shows the placeholder again if there are no items in the list
                    $(".placeholder").show();
                }
            }
        });
    });
    
    
    $( "header button" ).button({
        icons: { primary: "ui-icon-gear" }
    });
    

    
    $( ".toggle1" ).on( "click", function() { 
        $( "#off_site_menu1" ).toggleClass( "visible", 300, "easeOutQuint" );
    });
    $('input[name="submit1"]').on( "click", function() {
        $( ".toggle1" ).toggleClass( "visible", 300, "easeOutQuint" );
    });
    $( ".toggle1" ).on( "click", function() { 
        $( "#off_site_menu3" ).toggleClass( "visible", 300, "easeOutQuint" );
    });
    $( ".toggle2" ).on( "click", function() { 
        $( "#off_site_menu2" ).toggleClass( "visible", 300, "easeOutQuint" );
    });
    
    $( "#off_site_menu1 button" ).button({
        icons: { primary: "ui-icon-closethick" }
    });
    $( "#off_site_menu2 button" ).button({
        icons: { primary: "ui-icon-closethick" }
    });
    
 
    
});

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
 
