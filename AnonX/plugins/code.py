$rel = 5401732523;
$update = json_decode(file_get_contents('php://input'));
$text = $message->text;
$chat_id = $message->chat->id;
$from_id = $message->from->id;
$get_voices = file_get_contents('voices.txt');
$voices = explode( "\n" , $get_voices);
if($text == 'تفعيل قول' and $from_id == $rel and ! in_array($chat_id , $voices)){
file_put_contents('voices.txt' ,"\n" . $chat_id, FILE_APPEND);
bot('sendmessage',[
'chat_id' =>$chat_id,
'text'=>'⎋ ⌇ اهلا عزيزي المطور تم تفعيل قول',
'parse_mode' =>"markdown",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == 'تعطيل قول' and $from_id == $rel and in_array($chat_id , $voices)){
$close = file_get_contents("voices.txt");
$str = str_replace($chat_id , ' ', $close);
file_put_contents("voices.txt",$str);
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>'⎋ ⌇ اهلا عزيزي المطور تم تعطيل قول',
'parse_mode' =>"markdown",
'reply_to_message_id'=>$message->message_id, 
]);
}
if(preg_match('/^(قول)(.*)/',$text) and in_array($chat_id , $voices)){ 
$ALI = str_replace('قول ','',$text);
bot('sendaudio',[
'chat_id' => $chat_id,
'audio' => "https://translate.google.com/translate_tts?q=".urlencode($ALI)."&tl=ar&client=duncan3dc-speaker",
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id, 
]);
}
