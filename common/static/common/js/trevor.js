$(document).ready(function() {
    
    
    var bgNormal = {"background-image": $('body').css("background-image"), 
        "background-repeat": $('body').css("background-repeat"), 
        "background-position": $('body').css("background-position")}
    
    var bgPlatonicSolid = {"background-image": bgNormal["background-image"],
        "background-repeat": "no-repeat, " + bgNormal["background-repeat"],
        "background-position": "50% 120px, " + bgNormal["background-position"]}
    
    $('nav li').hover(function(){
        
        if ($(this).index() < 4) {
            if ($(this).index() == 0) {
                bgPlatonicSolid["background-image"] = "url(/static/common/images/tetrahedron.png), " + bgNormal["background-image"];
            } else if ($(this).index() == 1) {
                bgPlatonicSolid["background-image"] = "url(/static/common/images/star-tetrahedron.png), " + bgNormal["background-image"];
            } else if ($(this).index() == 2) { 
                bgPlatonicSolid["background-image"] = "url(/static/common/images/cube.png), " + bgNormal["background-image"];
            } else if ($(this).index() == 3) { 
                bgPlatonicSolid["background-image"] = "url(/static/common/images/octahedron.png), " + bgNormal["background-image"];
            }
            
            $('body').css(bgPlatonicSolid);
        } else {
            return;
        }
    }, function() {
        $('body').css(bgNormal);
    });
    
})