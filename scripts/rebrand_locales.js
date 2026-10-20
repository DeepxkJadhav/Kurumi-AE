const fs = require('fs');
const path = require('path');

const localesDir = path.join(__dirname, '..', 'static', 'locales');

function sanitizeObjectStrings(obj, replacers) {
  for (const key in obj) {
    if (typeof obj[key] === 'string') {
      let str = obj[key];
      for (const [pattern, replacement] of replacers) {
        str = str.replace(pattern, replacement);
      }
      obj[key] = str;
    } else if (typeof obj[key] === 'object' && obj[key] !== null) {
      sanitizeObjectStrings(obj[key], replacers);
    }
  }
}

// Rebrand EN
function updateEn() {
  const filePath = path.join(localesDir, 'en.json');
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  // Specific overrides first
  data.buttons.social = 'Shadow Domain';
  data.buttons.socialCharging = 'Shadow Domain charging — come back in {{days}} days.';
  data.buttons.agentTools = 'Zafkiel Tools';

  if (data.clickGuide && data.clickGuide.floatingOverview) {
    data.clickGuide.floatingOverview.body = 'The buttons beside your character open voice, Agent, Shadow Domain, settings, and rest.';
  }
  if (data.clickGuide && data.clickGuide.social) {
    data.clickGuide.social.body = 'Shadow Domain unlocks after three calendar days for new users. Open the community here once it is available.';
  }
  if (data.clickGuide && data.clickGuide.socialClose) {
    data.clickGuide.socialClose.title = 'Return from Shadow Domain';
    data.clickGuide.socialClose.body = 'Shadow Domain is now open. Click × to close this page and return to Kurumi to explore other buttons.';
  }

  if (data.instanceAccess) data.instanceAccess.title = 'Connect to Kurumi-AE';
  if (data.chat) {
    data.chat.cropTabHideNeko = 'Hide Companion';
    data.chat.reactWindowAriaLabel = 'Gothic Chat Window';
  }

  // Deep sanitize
  sanitizeObjectStrings(data, [
    [/cat girl/gi, 'spirit'],
    [/catgirl/gi, 'spirit'],
    [/nekoverse/gi, 'Shadow Domain'],
    [/Neko Universe/gi, 'Shadow Domain'],
    [/NekoClaw/g, 'Zafkiel Tools'],
    [/N\.E\.K\.O\./g, 'Kurumi-AE'],
    [/N\.E\.K\.O/g, 'Kurumi-AE'],
    [/\bNEKO\b/g, 'Kurumi-AE'],
    [/\bNeko's\b/g, "Kurumi's"],
    [/\bNeko\b/g, 'Kurumi'],
    [/\bneko\b/g, 'spirit']
  ]);

  fs.writeFileSync(filePath, JSON.stringify(data, null, 4), 'utf8');
  console.log('en.json deeply sanitized and updated successfully.');
}

// Rebrand ZH-CN
function updateZhCN() {
  const filePath = path.join(localesDir, 'zh-CN.json');
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  data.buttons.social = '暗影领域';
  data.buttons.socialCharging = '暗影领域充能中 {{days}}天后再回来看看吧';
  data.buttons.agentTools = '时之工坊';

  if (data.settings && data.settings.toggles) {
    data.settings.toggles.proactiveCommunityChat = '暗影领域社区';
    data.settings.toggles.proactiveCommunityChatTooltip = '使用暗影领域探索页的公开卡牌进行搭话';
  }

  if (data.clickGuide) {
    if (data.clickGuide.floatingOverview) data.clickGuide.floatingOverview.body = '角色旁的按钮分别通向语音、时之工坊、暗影领域、设置和休憩。';
    if (data.clickGuide.social) {
      data.clickGuide.social.title = '暗影领域';
      data.clickGuide.social.body = '暗影领域在新用户使用满三个自然日后解锁，届时可以从这里进入社区。';
    }
    if (data.clickGuide.socialBack) {
      data.clickGuide.socialBack.title = '从暗影领域回来';
      data.clickGuide.socialBack.body = '暗影领域已经打开了。点 × 关闭这个页面，就能回到角色旁边，继续认识快捷按钮。';
    }
    if (data.clickGuide.socialClose) {
      data.clickGuide.socialClose.title = '从暗影领域回来';
      data.clickGuide.socialClose.body = '暗影领域已经打开了。点 × 关闭这个页面，就能回到角色旁边，继续认识快捷按钮。';
    }
  }

  if (data.tutorial && data.tutorial.step8) {
    data.tutorial.step8.title = '🔨 时之工坊';
    data.tutorial.step8.desc = '打开时之工坊面板，使用键盘鼠标控制、浏览器控制、用户插件等功能。让狂三帮你操控电脑、协助工作、陪你玩耍~';
  }

  // Deep sanitize
  sanitizeObjectStrings(data, [
    [/猫娘/g, '精灵'],
    [/喵宇宙/g, '暗影领域'],
    [/猫爪/g, '时之工坊'],
    [/N\.E\.K\.O\./g, 'Kurumi-AE'],
    [/N\.E\.K\.O/g, 'Kurumi-AE'],
    [/\bNEKO\b/g, 'Kurumi-AE']
  ]);

  fs.writeFileSync(filePath, JSON.stringify(data, null, 4), 'utf8');
  console.log('zh-CN.json deeply sanitized and updated successfully.');
}

// Rebrand ZH-TW
function updateZhTW() {
  const filePath = path.join(localesDir, 'zh-TW.json');
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  data.buttons.social = '暗影領域';
  data.buttons.socialCharging = '暗影領域充能中 {{days}}天後再回來看看吧';
  data.buttons.agentTools = '時之工坊';

  if (data.settings && data.settings.toggles) {
    data.settings.toggles.proactiveCommunityChat = '暗影領域社群';
    data.settings.toggles.proactiveCommunityChatTooltip = '使用暗影領域探索頁的公開卡牌進行搭話';
  }

  if (data.clickGuide) {
    if (data.clickGuide.floatingOverview) data.clickGuide.floatingOverview.body = '角色旁的按鈕分別通往語音、時之工坊、暗影領域、設定和休憩。';
    if (data.clickGuide.social) {
      data.clickGuide.social.title = '暗影領域';
      data.clickGuide.social.body = '暗影領域在新使用者使用滿三個自然日後解鎖，屆時可以從這裡進入社群。';
    }
    if (data.clickGuide.socialBack) {
      data.clickGuide.socialBack.title = '從暗影領域回來';
      data.clickGuide.socialBack.body = '暗影領域已經打開了。點 × 關閉這個頁面，就能回到角色旁邊，繼續認識快捷按鈕。';
    }
    if (data.clickGuide.socialClose) {
      data.clickGuide.socialClose.title = '從暗影領域回來';
      data.clickGuide.socialClose.body = '暗影領域已經打開了。點 × 關閉這個頁面，就能回到角色旁邊，繼續認識快捷按鈕。';
    }
  }

  if (data.tutorial && data.tutorial.step8) {
    data.tutorial.step8.title = '🔨 時之工坊';
    data.tutorial.step8.desc = '打開時之工坊面板，使用鍵盤滑鼠控制、瀏覽器控制、使用者外掛程式等功能。讓狂三幫你操控電腦、協助工作、陪你玩耍~';
  }

  // Deep sanitize
  sanitizeObjectStrings(data, [
    [/貓娘/g, '精靈'],
    [/喵宇宙/g, '暗影領域'],
    [/貓爪/g, '時之工坊'],
    [/N\.E\.K\.O\./g, 'Kurumi-AE'],
    [/N\.E\.K\.O/g, 'Kurumi-AE'],
    [/\bNEKO\b/g, 'Kurumi-AE']
  ]);

  fs.writeFileSync(filePath, JSON.stringify(data, null, 4), 'utf8');
  console.log('zh-TW.json deeply sanitized and updated successfully.');
}

// Rebrand other languages
function updateOtherLanguages() {
  const langs = [
    { file: 'es.json', social: 'Dominio de Sombras', tools: 'Herramientas Zafkiel' },
    { file: 'ja.json', social: '影の領域', tools: 'ザフキエルツール' },
    { file: 'ko.json', social: '그림자 영역', tools: '자프키엘 도구' },
    { file: 'pt.json', social: 'Domínio das Sombras', tools: 'Ferramentas Zafkiel' },
    { file: 'ru.json', social: 'Теневое Царство', tools: 'Инструменты Зафкиэль' }
  ];

  langs.forEach(({ file, social, tools }) => {
    const filePath = path.join(localesDir, file);
    if (!fs.existsSync(filePath)) return;
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    sanitizeObjectStrings(data, [
      [/Neko Universe/gi, social],
      [/NekoClaw/gi, tools],
      [/nekoverse/gi, social],
      [/N\.E\.K\.O\./g, 'Kurumi-AE'],
      [/N\.E\.K\.O/g, 'Kurumi-AE'],
      [/\bNEKO\b/g, 'Kurumi-AE']
    ]);

    fs.writeFileSync(filePath, JSON.stringify(data, null, 4), 'utf8');
    console.log(`${file} deeply sanitized and updated successfully.`);
  });
}

updateEn();
updateZhCN();
updateZhTW();
updateOtherLanguages();
console.log('All locales thoroughly purged of Neko/nekoverse!');
