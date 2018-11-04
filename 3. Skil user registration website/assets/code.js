var email_ ,btc_, ltc_, eth_, doge_


$(document).ready(function(){
  email_ =document.getElementById("email")
  btc_ =document.getElementById("btc")
  ltc_ =document.getElementById("ltc")
  eth_ =document.getElementById("eth")
  doge_ =document.getElementById("doge")
})

$(document).on('click','.button',function(){
  if(email_.value.length == 0){
    alert("Email can't be empty")
  }
  else{
    var email = email_.value;
    var btc = btc_.value;
    var ltc = ltc_.value;
    var eth = eth_.value;
    var doge = doge_.value;
    var requestURL = "https://alexaskill.pythonanywhere.com/?action=register&id="+email+"&btc="+btc+"&eth="+eth+"&ltc="+ltc+"&doge="+doge;
    console.log(requestURL)
    $.getJSON(requestURL, function( data ) {
      console.log(data)
    });
    $('.jumbotron').html("<h3><span class=\"highlight\">"+email+" </span>has been successfully registered with us!");
  }
});



// test0@test.com
// 13tQQiLKaVZJvqmGdmv14UgXJt2RTDphrK
// http://alexaskill.pythonanywhere.com/?action=fetch&id=test0@test.com&crypto=all


//
// $(document).ready(function () {
//   $("#hidethisyo").hide();
//   document.getElementById("inp").value="Enter roll number (Ex. 2016/B2/345)";
//   $("#inp").focus(function(){
//     if(document.getElementById("inp").value==="Enter roll number (Ex. 2016/B2/345)"){
//       document.getElementById("inp").value="";
//     }
//   });
//   $(".my_btn").click(function(){
//     stro = grecaptcha.getResponse()
//     if(stro){
//       $("#hidethisyo").show();
//     }
//     else{
//       //alert("Fill the captcha correctly!");
//       // do nothing onii-chan [@_@]
//     }
//       var roll = document.getElementById("inp").value;
//       roll=roll.toLowerCase();
//       if(roll[1]=='k')
//         roll = roll.replace("k","0");
//       roll = roll.replace("/","-");
//       roll = roll.replace("/","-");
//       roll = roll.replace("/","-");
//       year = parseInt(roll.slice(1,4));
//       console.log(year);
//       if(stro){
//           requestURL='https://timetraveller.pythonanywhere.com/?reg_id='+roll+"&g-recaptcha-response="+stro;
//           console.log(requestURL);
//       }
//       else{
//         //lets fill some null value in the requestURL to return some error response
//         requestURL='https://timetraveller.pythonanywhere.com/?reg_id=2k16-b2-3333'
//       }
//       //requestURL="data.json";Ì¥
//       $.getJSON(requestURL, function(data) {
//         console.log(data);
//         if(data['name']===undefined) {
//             alert("Captcha not filled or data unavailable. If the problem persists visit 'reform query' page to submit us your data related problem so we can fix it.");
//             grecaptcha.reset();
//             console.log("Gomenasai! no data present for you desu >///< ");
//         }
//         else{
//           console.log("we're here");
//           $(".main_data").css("display", "block");
//           $('html,body').animate({
//             scrollTop: $("#start").offset().top},
//             1000);
//           grecaptcha.reset();
//
//           // $(".main_data").css("opacity", "1");
//           var gpa=document.getElementById("gpa");
//           var dr_rank=document.getElementById("dr_rank");
//           var rank=document.getElementById("rank");
//           var name=document.getElementById("name");
//           var branch=document.getElementById("branch");
//           var roll=document.getElementById("roll_no");
//           var gpa_text=document.getElementById("gpa_text");
//           var dr_text=document.getElementById("dr_text");
//           var rank_text=document.getElementById("rank_text");
//           gpa.innerHTML=data['gpa']['agg'];
//           dr_rank.innerHTML=data['meta']['dep_rank']['agg'];
//           rank.innerHTML=data['meta']['uni_rank']['agg'];
//           branch.innerHTML=data['branch'];
//           roll.innerHTML=data['roll'];
//           name.innerHTML=data['name'];
