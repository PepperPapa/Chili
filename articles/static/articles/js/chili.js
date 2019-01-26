$(document).ready(function() {
    
    // articles/5/edit
    // 文章edit页面首先获取服务器传会来的内容，然后写入到trix-editor tag元素中
    // 之所以这么做是因为trix框架会自动清理其中的内容，所以服务器将文章内容
    // 事先放入到一个隐藏tag中
    var ele_article=document.getElementById("article__content");
    if (ele_article) {
        var element = document.querySelector("trix-editor");
        element.editor.insertHTML(ele_article.innerHTML);
        ele_article.remove();
    }
});
