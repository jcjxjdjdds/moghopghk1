$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$Msg = $message->text;
$re1 = $update->callback_query->message->message_id;
$re2 = $message->chat->id;
$re3 = $update->callback_query->data;
$alI = $update->callback_query->message->chat->id;
$re = rand(5,100);
if($Msg == "روايات" or $Msg == "روايه" ){
bot('sendDocument',[
'chat_id'=>$re2,
'document'=>"https://t.me/reaylop/$re",
'caption'=>". تم اختيار هذه الروايه لك .", 
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'روايات اخرى','callback_data'=>'lool']],]
     ])
  ]);
}

if($re3 == "lool"){
bot('editmessagemedia',[
'chat_id'=>$alI,
'message_id'=>$re1,
'media'=>json_encode([
'type'=>'document',
'media'=>"https://t.me/reaylop/$re",
'caption'=>". تم اختيار هذه الروايه لك .", 
'parse_mode'=>"MarkDown",
]),
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'روايات اخرى','callback_data'=>'lool']],]
     ])
  ]);
}

