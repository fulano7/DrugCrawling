

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head id="Head1"><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info = {"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"a4d057be66","applicationID":"23426771","transactionName":"MgBQZhEHWUpXWxIMWQtKc2EzSVRYWlsTCVkDF1dGBkhWSkZA","queueTime":0,"applicationTime":61,"agent":"","atts":""}</script><script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(2),u=e(3),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}finally{f.emit("fn-end",[c.now()],t)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now()])}},{}],2:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],3:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],4:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=m(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){v[e]=m(e).concat(n)}function m(e){return v[e]||[]}function w(e){return p[e]=p[e]||o(t)}function g(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var v={},y={},b={on:l,emit:t,get:w,listeners:m,context:n,buffer:g,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(2),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!x++){var e=h.info=NREUM.info,n=d.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+h.offset],null,"api");var t=d.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===d.readyState&&i()}function i(){f("mark",["domContent",a()+h.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-h.offset}var u=(new Date).getTime(),f=e("handle"),c=e(2),s=e("ee"),p=window,d=p.document,l="addEventListener",m="attachEvent",w=p.XMLHttpRequest,g=w&&w.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:w,REQ:p.Request,EV:p.Event,PR:p.Promise,MO:p.MutationObserver};var v=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1026.min.js"},b=w&&g&&g[l]&&!/CriOS/.test(navigator.userAgent),h=n.exports={offset:u,now:a,origin:v,features:{},xhrWrappable:b};e(1),d[l]?(d[l]("DOMContentLoaded",i,!1),p[l]("load",r,!1)):(d[m]("onreadystatechange",o),p[m]("onload",r)),f("mark",["firstbyte",u],null,"api");var x=0,E=e(4)},{}]},{},["loader"]);</script><title>
	Calcule o Frete
</title><link href="//fonts.googleapis.com/css?family=Ropa+Sans:400,400italic" rel="stylesheet" type="text/css" />
     <link rel="stylesheet" type="text/css" href="/includes/minify.aspx?reset.css|fonts.css|main.css|navegacao.css|tipTip.css|button.css" media="screen" />
     <link rel="stylesheet" href="/includes/minify.aspx?c-mobile.css,custom" media="screen" />   
     <script type="text/javascript" src="http://loja.paguemenos.com.br/js/dateTimePicker/jquery-1.6.2.min.js"></script>  
     <script type="text/javascript" src="http://loja.paguemenos.com.br/js/jquerymeiomask.js"></script>  
     <script type="text/javascript" src="http://loja.paguemenos.com.br/js/funcoes.js"></script>  
</head>
<body class="modal-cep">
    <form name="form1" method="post" action="./calculoFrete.aspx" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTkwODQzNzQyN2Rkv4OGiagUGrY72A37YZmRx+Pdk9izIt8iRjnGlO/fxPY=" />


<script type="text/javascript" src="/ajaxpro/prototype.ashx"></script>
<script type="text/javascript" src="/ajaxpro/core.ashx"></script>
<script type="text/javascript" src="/ajaxpro/converter.ashx"></script>
<script type="text/javascript" src="/ajaxpro/IKCLojaMaster.CalculoFrete,PagueMenos2016.ashx"></script>

<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="D52CC7FB" />
    <div class="box-cep">
        <div class="imagem"><img src="http://loja.paguemenos.com.br/Imagens/produtos/bannercep.png" border="0" /></div>
        <h1 class="cep-title">
            <span>Seja Bem-vindo :)</span>  
        </h1>  
        <p class="cep-subtitle">
           Clique no seu estado e garanta <br />
            descontos exclusivos
        </p>
        <div class="cep-form dn">
            <h2>Informe seu CEP</h2>
            <div class="cep-field cep-numero">
                <span>CEP</span>
                <input type="text" id="zipCodeInput" class="cep msk" title="cep"/>
            </div>           
            <div class="cep-field cep-button" id="entrar">
                <a href="javascript:;" class="btn-entrar">Entrar na loja</a>
            </div>
        </div>
            <div class="cep-buttons uf-buttons">
                <ul class="bts-container">
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('69900001');">ACRE</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('57000001');">ALAGOAS</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('69000001');">AMAZONAS</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('68900001');">AMAPÁ</a></li>                    
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('40000001');">BAHIA</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('70000001');">BRASÍLIA - DF</a></li>
                    <li class="uf-item"><a class="uf-link" id="bt-ceara" href="#">CEARÁ</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('29000001');">ESPIRITO SANTO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('74001970');">GOIÁS</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('65000001');">MARANHÃO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('78000001');">MATO GROSSO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('79000001');">MATO GROSSO DO SUL</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('32000001');">MINAS GERAIS</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('66000001');">PARÁ</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('58010150');">PARAÍBA</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('01000001');">PARANÁ</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('50000001');">PERNAMBUCO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('64000001');">PIAUÍ</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('20000001 ');">RIO DE JANEIRO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('59000001');">RIO GRANDE DO NORTE</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('90000001');">RIO GRANDE DO SUL</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('76800001');">RONDÔNIA</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('69300001');">RORAIMA</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('88000001');">SANTA CATARINA</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('01000001');">SÃO PAULO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('49000001');">SERGIPE</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('77000001');">TOCANTINS</a></li> 
                </ul>
            </div>
            <div class="cep-buttons ceara-buttons dn">
                <ul class="bts-container">
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('61940001');">FORTALEZA</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('63000001');">JUAZEIRO</a></li>
                    <li class="uf-item"><a class="uf-link" href="javascript:ValidarCep('61940001');">DEMAIS CIDADES</a></li>
                    <li class="uf-item"><a class="uf-link" id="bt-voltar" href="#">Voltar</a></li>
                </ul>
            </div>
        <ul class="cep-info">
            <li><a href="#" onclick="Redirect('http://www.buscacep.correios.com.br/')">D&uacute;vidas sobre seu CEP?</a></li>
            <li><a href="#" onclick="Redirect('/institucionais/faleconosco.aspx')" >D&uacute;vidas no acesso desta loja? </a></li>
            <li><a href="#" onclick="Redirect('http://portal.paguemenos.com.br/portal/')">Institucional</a></li>
            <li><a href="#" onclick="Redirect('http://paguemenos.riweb.com.br/')">Informa&ccedil;&otilde;es financeiras</a></li>
            <li><a href="#" onclick="Redirect('/institucionais/faleconosco.aspx')">Fale Conosco</a></li>
            <li><a href="#" onclick="Redirect('/institucionais/AntesCompra/ComoComprar.aspx')">Como Comprar</a></li>
        </ul>
    </div>
    </form>
    <script type="text/javascript" src="/includes/minify.aspx?jquerymeiomask.js"></script>      
    <script type="text/javascript">
        jQuery('#entrar a.btn-entrar').click(function () {
            var zip = jQuery('#zipCodeInput').val();

            if (zip != "" || ddd != "") {
                CalculoFrete.ValidateZipCode(zip, ValidateZipCode_callback);
            }
            else {
                alert("Por favor, informe seu CEP.");
            }
        });

        jQuery('.closemodal').click(function () {
            parent.jQuery.fancybox.close();
        });

        jQuery('.msk').setMask();

        function ValidarCep(zip) {
            CalculoFrete.ValidateZipCode(zip, ValidateZipCode_callback);
        }

        function ValidateZipCode_callback(res) {
            if (res.value) {
                if (res.value[0] == "") {
                    parent.jQuery.fancybox.close();
                    window.parent.location = res.value[1];
                } else if (res.value[0] == "1") {
                    parent.location.reload();
                    window.parent.location = res.value[1];
                } else {
                    if (confirm(res.value + "\n Deseja navegar na loja mesmo assim? ")) {
                        parent.jQuery.fancybox.close();
                        window.parent.location = res.value[1];
                    }
                }
            }
        }

        function Redirect(url) {
            window.parent.jQuery.fancybox.close();
            window.parent.location = url;
        }

        jQuery('#bt-ceara').click(function (event) {
            jQuery('.uf-buttons').toggleClass('dn');
            jQuery('.ceara-buttons').toggleClass('dn');
        });
        jQuery('#bt-voltar').click(function (event) {
            jQuery('.uf-buttons').toggleClass('dn');
            jQuery('.ceara-buttons').toggleClass('dn');
        });
    </script>
</body>
</html>
