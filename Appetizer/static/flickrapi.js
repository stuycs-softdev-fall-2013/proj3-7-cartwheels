console.log("yo");

var TAGS;
var APIKey = "fd256a5b01cbb9f16e88a7c9523d65e0";

if ({{typeOfDish}} != 'A cheeseburger'){
    var FORMAT;
    var SAUCE;

    if ({{typeOfFormat}} === ' in a salad '){	
	FORMAT = 'salad';
    }
    else if ({{typeOfFormat}} === ' in a pita '){
	FORMAT = 'pita';
    }
    else{
	FORMAT = 'rice';
    }
    
    if ({{typeOfSauce}} === ' with white sauce, hot sauce, and BBQ sauce'){
	SAUCE = '%2C+white sauce%2C+hot sauce%2C+BBQ sauce';
    }
    else if ({{typeOfSauce}} === " with white sauce"){
	SAUCE = "%2C+white sauce";
    }
    else if ({{typeOfSauce}} === " with white sauce and BBQ sauce"){
	SAUCE = "%2C+white sauce%2C+BBQ sauce";
    }
    else{
	SAUCE = "";
    }

    TAGS = "halal%2C+" + {{typeOfDish}} + "%2C+" + FORMAT + SAUCE;
}

else{
    TAGS = "halal%2C+cheeseburger";
}

 
var JSONcall = "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=" + APIKEY + "&tags=" + TAGS + "&tag_mode=all&format=rest&auth_token=AUTHTOKENHERE"; 
    //    $.getJSON('http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' +

var main = function(){
    console.log(JSONcall);
}()