ha3_75tan = 0.065543;
ha7_5tan = 0.131652;
ha11_25tan = 0.198912;
ha15tan = 0.267949; // tan of 15 degrees, 360/24 = 15
ha18_75tan = 0.339454;
ha22_5tan = 0.414214;
ha26_25tan = 0.493145;
ha30tan = 0.57735;
ha33_75tan = 0.668179;
ha37_5tan = 0.767327;
ha41_25tan = 0.876976;
ha45tan = 1;
ha48_75tan = 1.140281;
ha52_5tan = 1.303225;
ha56_25tan = 1.496606;
ha60tan = 1.7320508;
ha63_75tan = 2.027799;
ha67_5tan = 2.414214;
ha71_25tan = 2.945905;
ha75tan = 3.7320508;
ha78_75tan = 5.027339;
ha82_5tan = 7.595754;
ha86_25tan = 15.257052;
ha90tan = 5729578;

//**********
function main(){
	badnum=0
	checkban()// checks if input is a number ref 
	checkval()// checks if input is in the range 0 to 90
	if(badnum==0)// skips cal() if input error
		cal()
}

//**********
function checknumber(){
	var x=document.trigform.latin.value
	var anum=/(^\d+$)|(^\d+\.\d+$)/
	if (anum.test(x))
		testresult=true
	else
	{
		alert("The value entered was not recognised !");
		badnum=1;
		testresult=false
	}
	return (testresult)
}

//**********
function checkban(){
	if (document.layers||document.all)
		return checknumber()
	else
		return true
}

//**********
function checkval(){
	var x=document.trigform.latin.value
	if ( x <0 || x >90)
	{
		alert("The value must be in the range 0 to 90");
		badnum=1
	}
}

//**********
// start of calculation

function cal(){
	degLat = eval(document.trigform.latin.value);
	degtopi = eval(degLat * 3.1415927 / 180); // convert lat degrees to pi radians
	sinLat = Math.sin(degtopi);
	document.trigform._0.value = " 0 degrees";
	docalc(ha3_75tan);
	document.trigform._3_75.value = " "+ shadAng + " deg";
	docalc(ha7_5tan);
	document.trigform._7_5.value = " "+ shadAng + " deg";
	docalc(ha11_25tan);
	document.trigform._11_25.value = " "+ shadAng + " deg";
	docalc(ha15tan);
	document.trigform._15.value =  " "+ shadAng + " deg";
	docalc(ha18_75tan);
	document.trigform._18_75.value = " "+ shadAng + " deg";
	docalc(ha22_5tan);
	document.trigform._22_5.value = " "+ shadAng + " deg";
	docalc(ha26_25tan);
	document.trigform._26_25.value = " "+ shadAng + " deg";
	docalc(ha30tan);
	document.trigform._30.value = " "+ shadAng + " deg";
	docalc(ha33_75tan);
	document.trigform._33_75.value = " "+ shadAng + " deg";
	docalc(ha37_5tan);
	document.trigform._37_5.value = " "+ shadAng + " deg";
	docalc(ha41_25tan);
	document.trigform._41_25.value = " "+ shadAng + " deg";
	docalc(ha45tan);
	document.trigform._45.value = " "+ shadAng + " deg";
	docalc(ha48_75tan);
	document.trigform._48_75.value = " "+ shadAng + " deg";
	docalc(ha52_5tan);
	document.trigform._52_5.value = " "+ shadAng + " deg"
	docalc(ha56_25tan);
	document.trigform._56_25.value = " "+ shadAng + " deg";
	docalc(ha60tan);
	document.trigform._60.value = " "+ shadAng + " deg";
	docalc(ha63_75tan);
	document.trigform._63_75.value = " "+ shadAng + " deg";
	docalc(ha67_5tan);
	document.trigform._67_5.value = " "+ shadAng + " deg";
	docalc(ha71_25tan);
	document.trigform._71_25.value = " "+ shadAng + " deg";
	docalc(ha75tan);
	document.trigform._75.value = " "+ shadAng + " deg";
	docalc(ha78_75tan);
	document.trigform._78_75.value = " "+ shadAng + " deg";
	docalc(ha82_5tan);
	document.trigform._82_5.value = " "+ shadAng + " deg";
	docalc(ha86_25tan);
	document.trigform._86_25.value = " "+ shadAng + " deg";
	docalc(ha90tan);
	document.trigform._90.value = " "+ shadAng + " deg";
} //EoF_cal

function docalc(x){
	multrig = eval(x * sinLat);
	radShadAng = Math.atan(multrig);
	angle = eval(radShadAng * 180 /  3.1415927); // convert rads to degrees
	shadAng = Math.round(angle * 100)/100; // round to 2 decimal places
} //EoF_docalc