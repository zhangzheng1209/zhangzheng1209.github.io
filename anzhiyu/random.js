var posts=["2025/01/21/hello-world/","2025/01/22/Rabat_2024/","2025/01/22/mdhelp/","2025/02/09/nizwa_2024/","2025/02/08/Kuwait City/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };