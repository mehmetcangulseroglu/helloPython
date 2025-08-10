#####################################################Day15######################################################
#15.güne özel bir kütüphane örneği oluşturmayı bir doküman okumayı araştırmak ??
#mesela ses kaydedici , gif oluşturucu ,geri sayan sayaç
#yapay zeka halleder fakat google'a voice recorder python diye yazınca ordan bul hazır kütüphane kodlarını
#veya voice recorder pypi diye yazınca ordan bulabilirsin söylemiştik pypi'ı


#####################################################Day16######################################################
#Git nedir ? Terminal komutları nelerdir ? araştırınız ?
#Git nedir Github nedir ? nasıl kullanılır ? araştırınız ?

#terminal komutları-> pwd,ls,cd,cd ..,clear,tab kullanımı,touch,rm,rm -rf,mkdir
#git status,git init,git config --global user.name "name",git config --global user.email "email" ????


#####################################################Day17######################################################
#git init,ls -la,git add .,ls -la yapınca .git varsa git init yapılmıştır
#git commit -m "ilk commit"
#git log,git restore

#Branch nedir ? -> Branch, bir projenin farklı versiyonlarını yönetmek için kullanılan bir özelliktir.dallanma diyebiliriz sonra istersem dallanmaları merge edebilirim oraya geleceğiz
#git branch -> şu anki branch'i gösterir
#git branch branch_ismi -> yeni bir branch oluşturur
#git checkout branch_ismi -> branch'e geçiş yapar ve git switch branch_ismi ile aynı işlemi yapar
#yuvarlak görsel çok faydalı onun üstünden göster

#Merge işlemleri ?
#Merge, iki veya daha fazla branch'i birleştirmek için kullanılır. Bu işlem, genellikle bir feature branch'in ana branch'e (master veya main) entegre edilmesi için yapılır.

#önce ana branch'e geçiş yapıyoruz sonra #git merge birleştirilecekbranchismi# yaparsın
#bunun ismi fast forwarding -> ana branchte commit atmadan birleştirme yapılması yani
#eğer ana branchte commit varsa ve merge yaparsan fast forward olmuyor


#####################################################Day18######################################################
#sublime text indirin ve git default editor olarak ayarlayın ?? gitte hangi komutla olur ??
#conflict nedir ? nasıl çözülür ? çakışma durumu
#conflict, iki branch'in aynı dosyada farklı değişiklikler yapması durumunda ortaya çıkar. Bu durumda, Git hangi değişikliğin kullanılacağını bilemez ve bir çakışma durumu oluşur.
#yani ilk branchte bir dosyada değişiklik yapıp commit ettikten sonra ikinci branchte aynı dosyada farklı değişiklik yapıp iki branchi merge edersen olur
#conflict çözümü için, çakışan dosyayı açıp hangi değişikliğin kullanılacağını manuel olarak seçmeniz gerekir dosya içinde. Daha sonra, dosyayı kaydedip tekrar commit etmeniz gerekir.

#commitler arasında gezmek ??
#git checkout commit_hash -> commit'e geçiş yapar - head değişir


#git reset --hard dönmek istediğin commitin_hash -> commit'e geri döner ve diğerlerini siler - head değişir ve çalışma dizini de değişir
#git revert commit_hash -> resetten daha çok kullanılır commit'i geri alır ve yeni bir commit oluşturur - head değişmez
#farkı şu ki reset hard ile geri döndüğünde commitler silinir revert ile geri döndüğünde commitler silinmez yeni bir commit oluşturulur

#git stash nedir ? nasıl kullanılır ?
#Stash, geçici olarak değişikliklerinizi saklamak için kullanılır. Örneğin, bir branch'te çalışırken başka bir branch'e geçmeniz gerektiğinde, değişikliklerinizi stash yaparak saklayabilirsiniz.illa ki commit yapmana gerek yok
#git stash pop -> en son stash'i geri alır ve çalışma dizinine uygular
#tag nedir ? nasıl kullanılır ?
#Tag, belirli bir commit'i işaretlemek için kullanılır. Örneğin, bir sürüm numarası veya önemli bir değişiklik için tag oluşturabilirsiniz.


#########################################################Day19-20######################################################
#github nedir ? nasıl kullanılır ?
#git push , pull request ,git pull fetch
#git clone nedir ? nasıl kullanılır ? git clone proje_linki(githubcode) -> projeyi klonlar pcye
#mesela bir projeyi githubdan klonlamak için git clone sonra proje linkini yazarsın sonra yeni branch oluşturursun push edersin pull request yaparsın
#git pull -> remote branch'teki değişiklikleri yerel branch'e alır ve merge eder
#yani git pull aslında git fetch + git merge işlemini yapar
#git fetch -> remote branch'teki değişiklikleri yerel branch'e alır ama merge etmez

#git ignore nedir ? nasıl kullanılır ?
#Git ignore, belirli dosyaların veya dizinlerin Git tarafından izlenmemesini sağlar. Örneğin, geçici dosyalar veya yapılandırma dosyaları gibi izlenmesini istemediğiniz dosyaları .gitignore dosyasına ekleyebilirsiniz.o dosyanın adını yazarsın .gitignore dosyasına