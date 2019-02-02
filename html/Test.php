<FORM action="<?=$_SERVER['PHP_SELF']?>" method = "post">
<input type="submit" name="submitted" value="ON"/>
<input type="submit" name="submitted" value="OFF"/>

</FORM>

<?php

	switch($_POST['submitted'])
	{
		case "ON":
		
		$servername = "localhost";
		$username = "phpmyadmin";
		$password = "root";
		$dbname = "mydb";
		$conn = new mysqli($servername, $username, $password, $dbname);
		
		if($conn->connect_error){die("Connection Failed: ".$conn->connect_error);}
		
		$sql = "UPDATE LED SET value = 1 where ID = 1";
		
		if($conn->query($sql) === TRUE){
			echo "Successfully Turn On";
			}
			else{
				echo "Error updating record: ".$conn->error;
				}
		$conn->close();
		break;
		
		case "OFF":
		
		$servername = "localhost";
		$username = "phpmyadmin";
		$password = "root";
		$dbname = "mydb";
		$conn = new mysqli($servername, $username, $password, $dbname);
		
		if($conn->connect_error){die("Connection Failed: ".$conn->connect_error);}
		
		$sql = "UPDATE LED SET value = 0 where ID = 1";
		
		if($conn->query($sql) === TRUE){
			echo "Successfully Turn Off";
			}
			else{
				echo "Error updating record: ".$conn->error;
				}
		$conn->close();
		break;
		
				}

?>
