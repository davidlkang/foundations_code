<html><body><?php

$p = $_POST['password'];
$Inputfilename = $_POST['inputfilename'];
$Outputfilename = $_POST['outputfilename'];
$p = strtoupper($p);
$p = bin2hex($p);
$p = str_pad($p, 20, '20', STR_PAD_RIGHT);
$Y0 = 0;
LoopAD39:
$i = file_get_contents($Inputfilename, NULL, NULL, $Y0, 44345);
$CX = strlen($i);
$CX = ($CX + 1) / 2;
settype($CX, "integer");

if($CX == 22173){
	$J = 1;
	$Y0 = $Y0 + 44346;}
else{
	$J = 0;}

$i = bin2hex($i);
$i = chunk_split($i, 4, "~");
$i = explode("~", $i);
$p_Split = chunk_split($p, 2, "~");
$p_teile = explode("~", $p_Split);


for([$C0=0, $C1=1, $Z=0, $C2=0]; ;[$CX--, $Z++]){
	$BX = 16;
	if($CX > 0){
		$AX = strrev(hex2bin($i[$Z]));
		$AX = bin2hex($AX);
		for( ; ;[$BX--, $C0++, $C1++, $C2++]){
			if($BX >= 0){
				if($C0 < 9){
					$BP =  $p_teile[$C1].$p_teile[$C0];
					$BP = str_pad($BP, 4 ,"0", STR_PAD_LEFT);
					$BP = hexdec($BP);

					if($CX > $BP){
						$BP = $BP - $CX;
						$BP = dechex($BP);
						$BP = substr($BP, 4, 4);}
					else{
						$BP = $BP - $CX;
						$BP = dechex($BP);}

					$BP = str_pad($BP, 4 ,"0", STR_PAD_LEFT);
					$BP0 = chunk_split($BP, 2, "~");
					$BP0 = explode("~", $BP0);
					$BP1 = $BP0[1];
					$V[$C2] = $BP1;}

				else {
					if($C2 == 9){
						$C2 = 0;}
					if(empty($V[$C2 + 1])){
						$V[$C2 + 1] = '20';}
					$BP = $V[$C2 + 1] . $V[$C2];
					$BP = str_pad($BP, 4 ,"0", STR_PAD_LEFT);
					$BP = hexdec($BP);

					if($CX > $BP){
						$BP = $BP - $CX;
						$BP = dechex($BP);
						$BP = substr($BP, 4, 4);}
					else{
						$BP = $BP-$CX;
						$BP= dechex($BP);}

					$BP = str_pad($BP, 4 ,"0", STR_PAD_LEFT);
					$BP0 = chunk_split($BP, 2, "~");
					$BP0 = explode("~", $BP0);
					$BP1 = $BP0[1];
					$V[$C2] = $BP1;}
				$AX = str_pad($AX, 4, "0", STR_PAD_LEFT);
				$AX = hexdec($AX);
				$BP = hexdec($BP);
				$AX = $AX ^ $BP;
				$AX = $AX ^ $CX;
				$AX = dechex($AX);
				$AX = str_pad($AX, 4 ,"0", STR_PAD_LEFT);}

			else {
				$AX = hex2bin($AX);
				$AX = strrev($AX);

				if(empty($F)){
					$F = $AX;}
				else {
					$F .= $AX;}
				break;}}}
	else {
		break;}}

if($J == 1){
	goto LoopAD39;}

file_put_contents("$Outputfilename", $F);

?></body></html>
