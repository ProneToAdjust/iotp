<?php echo "Fan Control"?>

<!-- form to control on/off of led -->

<FORM action="<?=$_SERVER['PHP_SELF']?>" method = "post">

<input type="submit" name="submitted" value="ON"/>
<input type="submit" name="submitted" value="OFF"/>

</FORM>

<?php echo "Brightness Control"?>

<!-- form to control brightness of led -->

<FORM action="<?=$_SERVER['PHP_SELF']?>" method = "post">

<input type="submit" name="submitted" value="LOW"/>
<input type="submit" name="submitted" value="MED"/>
<input type="submit" name="submitted" value="HIGH"/>

</FORM>

<!-- switch case to control the on/off and brightness of led -->

<?php

	switch($_POST['submitted'])
	{
		case "ON":
		$OFFpython = "sudo python /var/www/html/setTextFile.py 1";
		$cmd = exec($OFFpython);
		echo "ON";
		break;
		
		case "LOW":
		$OFFpython = "sudo python /var/www/html/setTextFile.py 2";
		$cmd = exec($OFFpython);
		echo "LOW";
		break;
		
		case "MED":
		$OFFpython = "sudo python /var/www/html/setTextFile.py 3";
		$cmd = exec($OFFpython);
		echo "MED";
		break;
		
		case "HIGH":
		$OFFpython = "sudo python /var/www/html/setTextFile.py 4";
		$cmd = exec($OFFpython);
		echo "HIGH";
		break;
		
		case "OFF":
		$OFFpython = "sudo python /var/www/html/setTextFile.py 0";
		$cmd = exec($OFFpython);
		echo "OFF";
		break;
		
				}

?>
