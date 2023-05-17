<?php
$messages = json_decode(file_get_contents("messages.json"), true);
$reversedMessages = array_reverse($messages);

foreach ($reversedMessages as $message) {
    $user = $message[0];
    $messageContent = $message[1];
    echo "<tr>";
    echo "<td class='text-left'>$user</td>";
    echo "<td class='text-left'>$messageContent</td>";
    echo "</tr>";
}
?>
