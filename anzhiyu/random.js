var posts=["2025/01/22/Kuwait City/","2025/01/23/Kuwait/","2025/01/22/test/","2025/01/22/mdhelp/","2025/01/21/hello-world/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };