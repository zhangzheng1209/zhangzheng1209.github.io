var posts=["2025/01/21/hello-world/","2025/01/22/test/","2025/01/22/mdhelp/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };