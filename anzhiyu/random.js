var posts=["2025/02/08/Kuwait City/","2025/01/21/hello-world/","2025/01/23/Kuwait/","2025/01/22/Rabat_2024/","2025/01/22/test/","2025/01/22/mdhelp/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };