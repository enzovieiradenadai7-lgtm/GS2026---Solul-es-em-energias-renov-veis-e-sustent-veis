<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Citizen Assist AI – Energia do chuveiro</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#EDF3F5; --sur:#FFFFFF; --tx:#10252E; --mut:#55707C; --line:#D3E0E5;
  --panel:#10252E; --panel-tx:#E6EFF2; --panel-mut:#8FA9B4; --panel-line:#27424E;
  --atual:#5E7A87; --a:#2F7FA6; --sun:#E9A820; --sun-ink:#7A5300;
  --disp:"Bricolage Grotesque","Avenir Next","Segoe UI",system-ui,sans-serif;
  --body:"Figtree","Segoe UI",system-ui,-apple-system,sans-serif;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#0A171D; --sur:#11252E; --tx:#E6EFF2; --mut:#91A9B3; --line:#223B46;
    --panel:#0F303D; --panel-line:#2A4F5E;
    --atual:#7E99A5; --a:#4FA3CC; --sun:#F2B93B; --sun-ink:#F2B93B;
    color-scheme:dark;
  }
}
*{box-sizing:border-box}
html{scroll-padding-top:16px}
body{margin:0;background:var(--bg);color:var(--tx);font-family:var(--body);font-size:1rem;line-height:1.6}
:focus-visible{outline:3px solid var(--sun);outline-offset:2px}

.layout{display:grid;grid-template-columns:340px 1fr;min-height:100vh}
.panel{background:var(--panel);color:var(--panel-tx);padding:36px 28px;position:sticky;top:0;align-self:start;height:100vh;overflow:auto}
.brand{font-family:var(--disp);font-weight:700;font-size:1.15rem;margin:0 0 4px}
.brand-sub{color:var(--panel-mut);font-size:.92rem;margin:0 0 36px}
.field{margin-bottom:28px}
.field-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px}
.field label{font-weight:500}
.val{font-family:var(--disp);font-size:1.5rem;font-weight:700}
.val small{font-family:var(--body);font-size:.85rem;font-weight:400;color:var(--panel-mut);margin-left:4px}
input[type=range]{width:100%;accent-color:var(--sun);height:28px}
.tarifa-row{display:flex;align-items:center;gap:10px}
.tarifa-row span{color:var(--panel-mut)}
input[type=number]{width:100%;padding:10px 12px;font:inherit;font-size:1.05rem;color:var(--panel-tx);background:transparent;border:1px solid var(--panel-line);border-radius:8px}
.help{color:var(--panel-mut);font-size:.85rem;margin:8px 0 0}
.err{color:#FFB4A2;font-size:.88rem;margin:8px 0 0;min-height:1.3em}

main{padding:48px clamp(20px,5vw,64px) 56px;max-width:860px}
.hero{padding-bottom:36px;border-bottom:1px solid var(--line);margin-bottom:36px}
.hero p{margin:0}
.hero .lead{font-size:1.1rem;color:var(--mut)}
.hero .big{font-family:var(--disp);font-weight:700;font-size:clamp(3rem,9vw,5.2rem);line-height:1.05;letter-spacing:-.02em;margin:6px 0 2px}
.hero .big span{font-size:.38em;font-weight:500;color:var(--mut);letter-spacing:0;margin-left:8px}
.hero .detail{max-width:60ch}

h2{font-family:var(--disp);font-weight:700;font-size:1.5rem;letter-spacing:-.01em;margin:0 0 6px}
.intro{color:var(--mut);margin:0 0 22px;max-width:62ch}
section{margin-bottom:44px}

.bars{display:grid;gap:14px;margin-bottom:26px}
.bar-row{display:grid;grid-template-columns:150px 1fr 120px;align-items:center;gap:14px}
.bar-name{font-weight:500;font-size:.95rem}
.track{height:22px;background:var(--line);border-radius:11px;overflow:hidden}
.fill{height:100%;border-radius:11px;transition:width .5s cubic-bezier(.2,.7,.2,1)}
.bar-val{text-align:right;font-variant-numeric:tabular-nums;font-size:.92rem}
.bar-val b{display:block;font-family:var(--disp);font-size:1.05rem}

.alts{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.alt{background:var(--sur);border:1px solid var(--line);border-top:5px solid var(--a);border-radius:6px 6px 14px 14px;padding:20px}
.alt.solar{border-top-color:var(--sun)}
.alt h3{font-family:var(--disp);font-size:1.15rem;margin:0 0 2px}
.alt .tag{color:var(--mut);font-size:.88rem;margin:0 0 14px}
.alt .save{font-family:var(--disp);font-weight:700;font-size:1.8rem;line-height:1.1;margin:0 0 14px}
.alt .save small{font-family:var(--body);font-weight:400;font-size:.88rem;color:var(--mut)}
dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:6px 12px;font-size:.93rem}
dt{color:var(--mut)}
dd{margin:0;text-align:right;font-variant-numeric:tabular-nums}

.rec p{max-width:62ch;margin:0 0 12px}
.rec .first{font-size:1.1rem}

details{border:1px solid var(--line);border-radius:12px;background:var(--sur);padding:4px 18px}
summary{cursor:pointer;font-weight:600;padding:12px 0}
details p,details li{color:var(--mut);font-size:.93rem;max-width:64ch}
details ul{padding-left:18px;margin:0 0 12px}
.aviso{border-left:4px solid var(--sun);padding:8px 14px;margin:6px 0 14px;color:var(--tx);font-size:.93rem}

@media (max-width:860px){
  .layout{grid-template-columns:1fr}
  .panel{position:static;height:auto;padding:24px 20px}
  .brand-sub{margin-bottom:22px}
  .field{margin-bottom:20px}
  main{padding-top:32px}
}
@media (max-width:640px){
  .alts{grid-template-columns:1fr}
  .bar-row{grid-template-columns:1fr auto;row-gap:6px}
  .track{grid-column:1 / -1;order:3}
}
@media (prefers-reduced-motion:reduce){.fill{transition:none}}
</style>
</head>
<body>
<div class="layout">

  <aside class="panel">
    <h1 class="brand">Citizen Assist AI</h1>
    <p class="brand-sub">Energia: quanto o chuveiro elétrico pesa na sua conta de luz.</p>

    <div class="field">
      <div class="field-top"><label for="pessoas">Pessoas na casa</label><span class="val" id="v-pessoas"></span></div>
      <input id="pessoas" type="range" min="1" max="10" step="1" value="4">
    </div>

    <div class="field">
      <div class="field-top"><label for="minutos">Duração de cada banho</label><span class="val" id="v-minutos"></span></div>
      <input id="minutos" type="range" min="1" max="30" step="1" value="10">
    </div>

    <div class="field">
      <div class="field-top"><label for="tarifa">Tarifa da conta de luz</label></div>
      <div class="tarifa-row"><span>R$</span><input id="tarifa" type="number" min="0.01" step="0.01" value="1.00" inputmode="decimal"><span>/kWh</span></div>
      <p class="help">Está na sua conta de luz. Sem ela, use R$ 1,00 como estimativa.</p>
      <p class="err" id="err" role="alert"></p>
    </div>
  </aside>

  <main>
    <div class="hero" aria-live="polite">
      <p class="lead">Seu chuveiro gasta cerca de</p>
      <p class="big"><b id="h-rs"></b><span>por mês</span></p>
      <p class="detail" id="h-detail"></p>
    </div>

    <section>
      <h2>Quanto cada opção consome</h2>
      <p class="intro">Consumo em kWh por mês, no mesmo período de 30 dias. Quanto menor a barra, menor a conta.</p>
      <div class="bars" id="bars"></div>
    </section>

    <section>
      <h2>Duas formas de gastar menos</h2>
      <p class="intro">A primeira não custa nada. A segunda usa uma fonte renovável, o sol, e exige investimento.</p>
      <div class="alts">
        <article class="alt">
          <h3>Banhos mais curtos</h3>
          <p class="tag" id="a-tag"></p>
          <p class="save"><span id="a-eco"></span> <small>por mês</small></p>
          <dl>
            <dt>CO₂ evitado</dt><dd id="a-co2"></dd>
            <dt>Investimento</dt><dd>R$ 0,00</dd>
            <dt>Retorno</dt><dd>imediato</dd>
          </dl>
        </article>
        <article class="alt solar">
          <h3>Aquecedor solar de água</h3>
          <p class="tag">Fonte renovável, cobre cerca de 70% do aquecimento</p>
          <p class="save"><span id="b-eco"></span> <small>por mês</small></p>
          <dl>
            <dt>CO₂ evitado</dt><dd id="b-co2"></dd>
            <dt>Investimento</dt><dd id="b-inv"></dd>
            <dt>Retorno</dt><dd id="b-pay"></dd>
          </dl>
        </article>
      </div>
    </section>

    <section class="rec">
      <h2>O que recomendamos</h2>
      <p class="intro">Com base nos números da sua casa.</p>
      <div id="rec"></div>
    </section>

    <section>
      <details>
        <summary>De onde vêm os números e quais são os limites</summary>
        <p class="aviso">Tudo aqui é estimativa. Não é resultado garantido.</p>
        <p>Fontes: ANEEL (tarifas), Procel/Inmetro (potência dos equipamentos), CRESESB (radiação solar) e MCTI (emissão da rede elétrica).</p>
        <ul>
          <li>Chuveiro elétrico de 5.500 W, usado 30 dias por mês.</li>
          <li>Aquecedor solar instalado por R$ 4.000, cobrindo 70% da energia do banho.</li>
          <li>Emissão de 0,06 kg de CO₂ por kWh de energia elétrica.</li>
          <li>Os valores reais mudam com a distribuidora, o clima, o modelo do chuveiro, o preço da instalação e o espaço no telhado.</li>
          <li>Como a rede elétrica brasileira já é em grande parte renovável, o ganho em CO₂ é pequeno. O principal benefício é financeiro.</li>
        </ul>
      </details>
    </section>
  </main>
</div>

<script>

var POT = 5500, DIAS = 30, FATOR = 0.06, REDUCAO = 3, FRACAO = 0.70, CUSTO_SOLAR = 4000;

var el = function (id) { return document.getElementById(id); };
var n1 = function (v) { return v.toLocaleString("pt-BR", { minimumFractionDigits: 1, maximumFractionDigits: 1 }); };
var rs = function (v) { return v.toLocaleString("pt-BR", { style: "currency", currency: "BRL" }); };

function barra(nome, cor, kwh, custo, max) {
  var pct = max > 0 ? Math.max(kwh / max * 100, 2) : 0;
  return '<div class="bar-row"><span class="bar-name">' + nome + '</span>' +
    '<div class="track"><div class="fill" style="width:' + pct.toFixed(1) + '%;background:' + cor + '"></div></div>' +
    '<span class="bar-val"><b>' + n1(kwh) + ' kWh</b>' + rs(custo) + '</span></div>';
}

function calcular() {
  var pessoas = Number(el("pessoas").value);
  var minutos = Number(el("minutos").value);
  var tarifa = Number(el("tarifa").value);

  el("v-pessoas").innerHTML = pessoas + "<small>" + (pessoas === 1 ? "pessoa" : "pessoas") + "</small>";
  el("v-minutos").innerHTML = minutos + "<small>min</small>";

  if (!(tarifa > 0)) {
    el("err").textContent = "Informe uma tarifa maior que zero, por exemplo 0,95.";
    return;
  }
  el("err").textContent = "";


  var kwh = (POT / 1000) * (pessoas * minutos / 60) * DIAS;
  var custo = kwh * tarifa;
  var co2 = kwh * FATOR;

  
  var minNovo = Math.max(minutos - REDUCAO, 1);
  var kwhA = (POT / 1000) * (pessoas * minNovo / 60) * DIAS;
  var ecoA = (kwh - kwhA) * tarifa;
  var co2A = (kwh - kwhA) * FATOR;

  var kwhB = kwh * (1 - FRACAO);
  var ecoB = (kwh - kwhB) * tarifa;
  var co2B = (kwh - kwhB) * FATOR;
  var payback = ecoB > 0 ? CUSTO_SOLAR / ecoB : 0;

 
  el("h-rs").textContent = rs(custo);
  el("h-detail").textContent = "São " + n1(kwh) + " kWh e " + n1(co2) + " kg de CO₂ por mês, com " +
    pessoas + (pessoas === 1 ? " pessoa" : " pessoas") + " e banhos de " + minutos + " minutos.";

  
  el("bars").innerHTML =
    barra("Hoje", "var(--atual)", kwh, custo, kwh) +
    barra("Banhos mais curtos", "var(--a)", kwhA, kwhA * tarifa, kwh) +
    barra("Aquecedor solar", "var(--sun)", kwhB, kwhB * tarifa, kwh);

  
  el("a-tag").textContent = "De " + minutos + " para " + minNovo + " minutos por banho";
  el("a-eco").textContent = rs(ecoA);
  el("a-co2").textContent = n1(co2A) + " kg/mês";
  el("b-eco").textContent = rs(ecoB);
  el("b-co2").textContent = n1(co2B) + " kg/mês";
  el("b-inv").textContent = rs(CUSTO_SOLAR);
  el("b-pay").textContent = payback > 0 ? n1(payback / 12) + " anos" : "–";

  
  var rec = '<p class="first">Comece pelos banhos mais curtos. Não custa nada e já reduz a conta em cerca de ' + rs(ecoA) + ' por mês.</p>';
  if (payback > 0 && payback <= 72) {
    rec += "<p>O aquecedor solar se paga em cerca de " + n1(payback / 12) + " anos. Se você tem telhado com sol, vale pedir orçamentos.</p>";
  } else {
    rec += "<p>Nesta situação o aquecedor solar demora para se pagar. Compare orçamentos com cuidado antes de decidir.</p>";
  }
  rec += "<p>Esses valores são estimativas. O resultado real depende da sua distribuidora, do clima e do equipamento.</p>";
  el("rec").innerHTML = rec;
}

["pessoas", "minutos", "tarifa"].forEach(function (id) { el(id).addEventListener("input", calcular); });
calcular();
</script>
</body>
</html>