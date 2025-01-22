var posts=["2025/01/22/1/","2025/01/21/hello-world/","2025/01/22/mdhelp/","2025/01/22/mdhelp1/","2025/01/22/mdhelp2/","2025/01/22/test/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };