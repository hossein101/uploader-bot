<?php
ob_start();
define('API_KEY','187882019:AAG0iIZXUOCtjz_1-hHPDW3UXh83NvhKdG4');
$admin = "262171688";
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
@bot.message_handler(content_types=['video','photo','sticker','document','audio','voice'])
def all(m):
  try:
            if m.photo :
                fileid = m.photo[1].file_id
            elif m.video :
                fileid = m.video.file_id
            elif m.sticker :
                fileid = m.sticker.file_id
            elif m.document :
                fileid = m.document.file_id
            elif m.audio :
                fileid = m.audio.file_id
            elif m.voice :
                fileid = m.voice.file_id
            e = m.from_user.username
            text = m
            redis.sadd('files',fileid)
            link = urllib2.Request("https://api.pwrtelegram.xyz/bot{}/getFile?file_id={}".format(token,fileid))
            open = urllib2.build_opener()
            f = open.open(link)
            link1 = f.read()
            jdat = json.loads(link1)
            patch = jdat['result']['file_path']
            send = 'https://storage.pwrtelegram.xyz/{}'.format(patch)
            link = urllib2.Request("http://api.gpmod.ir/shorten/?url={}&username={}".format(opizo_email,send))
            opeen = urllib2.build_opener()
            j = opeen.open(link)
            lin1 = j.read()
            bot.send_message(m.chat.id,'در حال آپلود فایل....')
            bot.send_message(m.chat.id,'<b>تبریک فایل آپلود شد!</b>\n\n<b>لینک فایل شما:</b>\n{}\n\n<b>ساخته شده توسط:</b> \nMuteTeam | @MuteTeam'.format(lin1),parse_mode='HTML')
  except:
   bot.send_message(m.chat.id,link1)
  $file_o = __DIR__.'/users/'.$eid.'.json';
  file_put_contents($file_o,json_encode($update->edited_message->text));
  //$up = file_get_contents(__DIR__.'/users/'.$eid.'.json');
  //str_replace("edited_message","message",$up);
}elseif(preg_match('/^\/([Ss]tart)/',$text1)){
  $text = "من همه پیامارو میبینم😋\nاگه کسی پیامشو ادیت کنه من میفهمم و میگم😛\nاینجوری هم میتونی مچ بگیری هم با دوستات شوخی کنی\n با سازنده من آشنا شو و منو به گروهات دعوت کن\n👇👇👇👇";
  bot('sendmessage',[
    'chat_id'=>$chat_id,
    'text'=>$text,
    'parse_mode'=>'html',
    'reply_markup'=>json_encode([
      'inline_keyboard'=>[
        [
          ['text'=>'😸 Channel 😸','url'=>'https://telegram.me/Red_Ch']
        ],
        [
          ['text'=>'🔰سازنده بات🔰','url'=>'https://telegram.me/SiCk_KoN_BaW']
        ],
	[
          ['text'=>'👥 Add To Group ➕','url'=>'https://telegram.me/donteditt_bot?startgroup=new']
        ]
      ]
    ])
  ]);
}elseif( $fadmin == $admin |  $fadmin == $admin2 and $update->message->text == '/stats'){
    $txtt = file_get_contents('member.txt');
    $member_id = explode("\n",$txtt);
    $mmemcount = count($member_id) -1;
  bot('sendMessage',[
      'chat_id'=>$chat_id,
      'text'=>"کاربران : $mmemcount 👤 "
    ]);

}elseif(isset($update->message-> new_chat_member )){
bot('sendMessage',[
      'chat_id'=>$chat_id,
      'text'=>"نبینم کسی ادیت کنه ها😐😂
سازنده بات: @SiCk_KoN_BaW "
      ]);
}
  
  
  
  
  
  
  
$txxt = file_get_contents('member.txt');
    $pmembersid= explode("\n",$txxt);
    if (!in_array($chat_id,$pmembersid)){
      $aaddd = file_get_contents('member.txt');
      $aaddd .= $chat_id."\n";
      file_put_contents('member.txt',$aaddd);
    }
