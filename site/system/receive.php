<?php
$validKey = ""; # YOUR KEY HERE

$key = $_GET["key"];
$user = $_GET["user"];
$message = $_GET["message"];

if ($key === $validKey) {
    $messages = json_decode(file_get_contents("messages.json"), true);
    $messages[] = array($user, $message);
    file_put_contents("messages.json", json_encode($messages));
} else {
    http_response_code(403);
}
?>
