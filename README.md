# Aile_Soy_Agaci
 

<h3>Programın Ana Ekranı</h3>
<ul type="square">
<li>Ekleme,Silme ve veritabanı işlemleri yapılır</li>
<li>Hiçbir Alan boş geçilemez, yoksa excepte uğrar</li>
<li>Eğer eklenilecek kişinin annesi, babası ya da çocukları yoksa ilgili alana "-1" yazılır. (Aksi halde algoritma patlar)</li>
</ul>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/117829171-2d8f0000-b27b-11eb-8193-7b60eb1763fa.PNG" width="800" title="hover text">
</p>

<hr>

<h3>Eklenen Sülalenin Şeması</h3>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/117830096-fcfb9600-b27b-11eb-95b8-653502e03c9f.png" width="800" title="hover text">
</p>

<hr>

<h3>Veritabanı Yapısı</h3>
<ul type="square">
<li>Eklenen kişilerin adı, soyadı ve cinsiyeti "kisi" tablosuna,</li>
<li>AnneID, BabaID ve CocuklarID gibi search yapmamıza yarayacak bağıntılar "bagintilar" tablosuna kaydedilir(ID's are Auto Increment)</li>

</ul>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/117830441-51067a80-b27c-11eb-8b1f-f5446570390b.png" title="hover text">
</p>



<hr>

<h3>VT Yapısı - 2</h3>


<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/117830691-8c08ae00-b27c-11eb-870b-c858a274794e.PNG" width="800" title="hover text">
</p>



<hr>

<h3>Algoritmanın Gerçekleşmesi</h3>
<ul type="square">
<li>Algoritma Stringsel Olarak "Anne -> Baba -> Oğul"  gibi yollar döndürür ve bu stringsel işlemden akrabaları ayıklarız</li>
<li>Örneğin: dayi1 = "Anne -> Baba -> Oğul" veya dayi2 = "Anne -> Anne -> Oğul" gibi.</li>
<li>Algoritma İşlem Önceliğinden kuzenleri tespit edememektedir. "Kuzen" yerine "Teyze -> Oğlu" gibi ifadeler verir</li>
<li>Gerisinde "Anne, Baba, Oğul, Kız, Amca, Dayı, Teyze, Hala, Dede, Nine" gibi akrabalık bağlantılarını tespit edebilir</li>

</ul>

<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/117831291-17823f00-b27d-11eb-89f8-254288af9040.PNG" width="800" title="hover text">
</p>




