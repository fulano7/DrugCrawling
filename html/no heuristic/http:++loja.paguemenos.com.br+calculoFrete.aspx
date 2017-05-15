

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head id="Head1"><title>
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
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTkwODQzNzQyN2RkbEiSgE4HLYsoBcHz+2rjFN/QDPoZgGUG9Fiq2KUSqGc=" />


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
