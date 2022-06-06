// Toggle Click - Button
// Fade In Button
// Fade Out Button
$(document).ready(function() {
    console.log("hello!");
    $("button").html ("Iʻll show the date and time..")
    $(".btn1").html ("Click once to make it disappear!")
    $(".btn2").html ("To show it again, click here.")
    $("button").on("click", function(event) {
        $("#date").toggleClass('warning');
        console.log(" the times clicked on any buttons");    
    });
      $(".btn1").click(function(){
      $(".hate").fadeOut(1000);
    });
    $(".btn2").click(function(){
        $(".hate").fadeIn(1000);
  })
});
