<!DOCTYPE html>
<html lang="en">
<head>
  <meta id="bb-bootstrap" data-current-user="{&quot;isKbdShortcutsEnabled&quot;: true, &quot;isSshEnabled&quot;: false, &quot;isAuthenticated&quot;: false}"
 />
  
  
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>404 &mdash; Bitbucket</title>
  <script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(2),u=e(3),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}finally{f.emit("fn-end",[c.now()],t)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now()])}},{}],2:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],3:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],4:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=m(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){v[e]=m(e).concat(n)}function m(e){return v[e]||[]}function w(e){return p[e]=p[e]||o(t)}function g(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var v={},y={},b={on:l,emit:t,get:w,listeners:m,context:n,buffer:g,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(2),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!x++){var e=h.info=NREUM.info,n=d.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+h.offset],null,"api");var t=d.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===d.readyState&&i()}function i(){f("mark",["domContent",a()+h.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-h.offset}var u=(new Date).getTime(),f=e("handle"),c=e(2),s=e("ee"),p=window,d=p.document,l="addEventListener",m="attachEvent",w=p.XMLHttpRequest,g=w&&w.prototype;NREUM.o={ST:setTimeout,SI:p.setImmediate,CT:clearTimeout,XHR:w,REQ:p.Request,EV:p.Event,PR:p.Promise,MO:p.MutationObserver};var v=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1059.min.js"},b=w&&g&&g[l]&&!/CriOS/.test(navigator.userAgent),h=n.exports={offset:u,now:a,origin:v,features:{},xhrWrappable:b};e(1),d[l]?(d[l]("DOMContentLoaded",i,!1),p[l]("load",r,!1)):(d[m]("onreadystatechange",o),p[m]("onload",r)),f("mark",["firstbyte",u],null,"api");var x=0,E=e(4)},{}]},{},["loader"]);</script>
  



<meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">
<meta name="bb-api-canon-url" content="https://api.bitbucket.org">


<meta name="bb-commit-hash" content="b25eee5d4e77">
<meta name="bb-app-node" content="app-172">
<meta name="bb-view-name" content="bitbucket.apps.repo2.views.filebrowse_raw">
<meta name="ignore-whitespace" content="False">
<meta name="tab-size" content="None">
<meta name="locale" content="en">

<meta name="application-name" content="Bitbucket">
<meta name="apple-mobile-web-app-title" content="Bitbucket">


  
  <meta name="theme-color" content="#0049B0">
  <meta name="msapplication-TileColor" content="#0052CC">
  <meta name="msapplication-TileImage" content="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/img/logos/bitbucket/mstile-150x150.png">
  <link rel="apple-touch-icon" sizes="180x180" type="image/png" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/img/logos/bitbucket/apple-touch-icon.png">
  <link rel="icon" sizes="192x192" type="image/png" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/img/logos/bitbucket/android-chrome-192x192.png">
  <link rel="icon" sizes="16x16 24x24 32x32 64x64" type="image/x-icon" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/img/logos/bitbucket/favicon_2017.ico">
  <link rel="mask-icon" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/img/logos/bitbucket/safari-pinned-tab.svg" color="#0052CC">



<link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket">

  <meta name="description" content="">
  
  
    
  



  <link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/css/entry/vendor.css" />
<link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/css/entry/app.css" />




  <link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/css/entry/adg3.css">

  
  <script nonce="B0ZQbvAx7LMqukan">
  window.__sentry__ = {"dsn": "https://ea49358f525d4019945839a3d7a8292a@sentry.io/159509", "release": "b25eee5d4e77 (production)", "tags": {"project": "bitbucket-core"}, "environment": "production"};
</script>
<script src="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/dist/webpack/sentry.js"></script>
  <script src="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/dist/webpack/early.js"></script>
  
</head>
<body class="production adg3 "
    data-static-url="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/"
data-base-url="https://bitbucket.org"
data-no-avatar-image="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/img/default_avatar/user_blue.svg"
data-current-user="{&quot;isKbdShortcutsEnabled&quot;: true, &quot;isSshEnabled&quot;: false, &quot;isAuthenticated&quot;: false}"
data-atlassian-id="{&quot;loginStatusUrl&quot;: &quot;https://id.atlassian.com/profile/rest/profile&quot;}"
data-settings="{&quot;MENTIONS_MIN_QUERY_LENGTH&quot;: 3}"

data-current-repo="{&quot;scm&quot;: &quot;hg&quot;, &quot;readOnly&quot;: false, &quot;mainbranch&quot;: {&quot;name&quot;: &quot;default&quot;}, &quot;language&quot;: &quot;python&quot;, &quot;owner&quot;: {&quot;username&quot;: &quot;pypa&quot;, &quot;uuid&quot;: &quot;eeed5f62-f24a-4bdd-9190-1966bfb7cf0e&quot;, &quot;isTeam&quot;: true}, &quot;fullslug&quot;: &quot;pypa/setuptools&quot;, &quot;slug&quot;: &quot;setuptools&quot;, &quot;id&quot;: 2716149, &quot;pygmentsLanguage&quot;: &quot;python&quot;}"






data-browser-monitoring="true"
data-switch-create-pullrequest-commit-status="true"

data-track-js-errors="true"


>
<div id="page">
  
    
      <div id="adg3-navigation"
   data-is-closed
  
   data-is-focused-task>
  <nav class="skeleton-nav">
    <div class="skeleton-nav--left">
      <div class="skeleton-nav--left-top">
        <ul class="skeleton-nav--items">
          <li></li>
          <li></li>
          <li></li>
          <li class="skeleton--icon"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
        </ul>
      </div>
      <div class="skeleton-nav--left-bottom">
        <div class="skeleton-nav--left-bottom-wrapper">
          <div class="skeleton-nav--item-help"></div>
          <div class="skeleton-nav--item-profile"></div>
        </div>
      </div>
    </div>
    <div class="skeleton-nav--right">
      <ul class="skeleton-nav--items-wide">
        <li class="skeleton--icon-logo-container">
          <div class="skeleton--icon-container"></div>
          <div class="skeleton--icon-description"></div>
          <div class="skeleton--icon-logo"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
      </ul>
    </div>
  </nav>
</div>


    
    <div id="wrapper">
      
  
  


      

      
  
    <div id="nps-survey-container"></div>
  


      
  

<div id="account-warning" data-module="header/account-warning"
  data-unconfirmed-addresses="false"
  data-no-addresses="false"
  
></div>



      
  
<header id="aui-message-bar">
  
</header>


    <div id="content" role="main">
      
        
          <header class="app-header">
            <div class="app-header--primary">
              
                <div class="app-header--context">
                  <div class="app-header--breadcrumbs">
                    
                  </div>
                  <h1 class="app-header--heading">
                    
                  </h1>
                </div>
                
              </div>
              <div class="app-header--secondary">
                
                  
                
              </div>
            </header>
          
        
        
        
  <div class="aui-page-panel aui-page-panel-no-header">
    <div class="aui-page-panel-inner">
      <div id="error" class="404 aui-page-panel-content">
        <span class="icon icon-404"></span>
        <h1>
          That link has no power here
        </h1>
        <p>
          
            Return to the <a href="javascript:window.history.back()">previous page</a> or
            go back to your <a href="/dashboard/overview">dashboard</a>.
          
        </p>
      </div>
    </div>
  </div>

      </div>
    </div>
  

  
</div>

  <div id="adg3-dialog"></div>



  

<div data-module="components/mentions/index">
  
    
    
  
  
    
    
  
  
    
    
  
</div>
<div data-module="components/typeahead/emoji/index">
  
    
    
  
</div>

<div data-module="components/repo-typeahead/index">
  
    
    
  
</div>

    
    
  

    
    
  

    
    
  

    
    
  


  <aui-inline-dialog
    id="help-menu-dialog"
    data-aui-alignment="bottom right"

    
    data-aui-alignment-static="true"
    data-module="header/help-menu"
    responds-to="toggle"
    aria-hidden="true">

  <div id="help-menu-section">
    <h1 class="help-menu-heading">Help</h1>

    <form id="help-menu-search-form" class="aui" target="_blank" method="get"
        action="https://support.atlassian.com/customer/search">
      <span id="help-menu-search-icon" class="aui-icon aui-icon-large aui-iconfont-search"></span>
      <input id="help-menu-search-form-input" name="q" class="text" type="text" placeholder="Ask a question">
    </form>

    <ul id="help-menu-links">
      <li>
        <a class="support-ga" data-support-gaq-page="DocumentationHome"
            href="https://confluence.atlassian.com/x/bgozDQ" target="_blank">
          Online help
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="GitTutorials"
            href="https://www.atlassian.com/git?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=help_dropdown&amp;utm_content=learn_git"
            target="_blank">
          Learn Git
        </a>
      </li>
      <li>
        <a id="keyboard-shortcuts-link"
           href="#">Keyboard shortcuts</a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="DocumentationTutorials"
            href="https://confluence.atlassian.com/x/Q4sFLQ" target="_blank">
          Bitbucket tutorials
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="SiteStatus"
            href="https://status.bitbucket.org/" target="_blank">
          Site status
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="Home"
            href="https://support.atlassian.com/bitbucket-cloud/" target="_blank">
          Support
        </a>
      </li>
    </ul>
  </div>
</aui-inline-dialog>
  





  

  <div class="_mustache-templates">
    
      <script id="mention-result" type="text/html">
        
<span class="mention-result">
  <span class="aui-avatar aui-avatar-small mention-result--avatar">
    <span class="aui-avatar-inner">
      <img src="[[avatar_url]]">
    </span>
  </span>
  [[#display_name]]
    <span class="display-name mention-result--display-name">[[&display_name]]</span> <small class="username mention-result--username">[[&username]]</small>
  [[/display_name]]
  [[^display_name]]
    <span class="username mention-result--username">[[&username]]</span>
  [[/display_name]]
  [[#is_teammate]][[^is_team]]
    <span class="aui-lozenge aui-lozenge-complete aui-lozenge-subtle mention-result--lozenge">teammate</span>
  [[/is_team]][[/is_teammate]]
</span>
      </script>
    
      <script id="mention-call-to-action" type="text/html">
        
[[^query]]
<li class="bb-typeahead-item">Begin typing to search for a user</li>
[[/query]]
[[#query]]
<li class="bb-typeahead-item">Continue typing to search for a user</li>
[[/query]]

      </script>
    
      <script id="mention-no-results" type="text/html">
        
[[^searching]]
<li class="bb-typeahead-item">Found no matching users for <em>[[query]]</em>.</li>
[[/searching]]
[[#searching]]
<li class="bb-typeahead-item bb-typeahead-searching">Searching for <em>[[query]]</em>.</li>
[[/searching]]

      </script>
    
      <script id="emoji-result" type="text/html">
        
<span class="emoji-result">
  <span class="emoji-result--avatar">
    <img class="emoji" src="[[src]]">
  </span>
  <span class="name emoji-result--name">[[&name]]</span>
</span>

      </script>
    
      <script id="repo-typeahead-result" type="text/html">
        <span class="aui-avatar aui-avatar-project aui-avatar-xsmall">
  <span class="aui-avatar-inner">
    <img src="[[avatar]]">
  </span>
</span>
<span class="owner">[[&owner]]</span>/<span class="slug">[[&slug]]</span>

      </script>
    
      <script id="share-form-template" type="text/html">
        

<div class="error aui-message hidden">
  <span class="aui-icon icon-error"></span>
  <div class="message"></div>
</div>
<form class="aui">
  <table class="widget bb-list aui">
    <thead>
    <tr class="assistive">
      <th class="user">User</th>
      <th class="role">Role</th>
      <th class="actions">Actions</th>
    </tr>
    </thead>
    <tbody>
      <tr class="form">
        <td colspan="2">
          <input type="text" class="text bb-user-typeahead user-or-email"
                 placeholder="Username or email address"
                 autocomplete="off"
                 data-bb-typeahead-focus="false"
                 [[#disabled]]disabled[[/disabled]]>
        </td>
        <td class="actions">
          <button type="submit" class="aui-button aui-button-light" disabled>Add</button>
        </td>
      </tr>
    </tbody>
  </table>
</form>

      </script>
    
      <script id="share-detail-template" type="text/html">
        

[[#username]]
<td class="user
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[displayName]]">
    <a href="/[[username]]/" class="user">
      <span class="aui-avatar aui-avatar-xsmall">
        <span class="aui-avatar-inner">
          <img src="[[avatar]]">
        </span>
      </span>
      <span>[[displayName]]</span>
    </a>
  </div>
</td>
[[/username]]
[[^username]]
<td class="email
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[email]]">
    <span class="aui-icon aui-icon-small aui-iconfont-email"></span>
    [[email]]
  </div>
</td>
[[/username]]
<td class="role
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    [[#group]]
      [[#hasCustomGroups]]
        <select class="group [[#noGroupChoices]]hidden[[/noGroupChoices]]">
          [[#groups]]
            <option value="[[slug]]"
                [[#isSelected]]selected[[/isSelected]]>
              [[name]]
            </option>
          [[/groups]]
        </select>
      [[/hasCustomGroups]]
      [[^hasCustomGroups]]
      <label>
        <input type="checkbox" class="admin"
            [[#isAdmin]]checked[[/isAdmin]]>
        Administrator
      </label>
      [[/hasCustomGroups]]
    [[/group]]
    [[^group]]
      <ul>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^read]]aui-lozenge-subtle[[/read]]"
            data-permission="read">
          read
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^write]]aui-lozenge-subtle[[/write]]"
            data-permission="write">
          write
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^admin]]aui-lozenge-subtle[[/admin]]"
            data-permission="admin">
          admin
        </li>
      </ul>
    [[/group]]
  </div>
</td>
<td class="actions
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    <a href="#" class="delete">
      <span class="aui-icon aui-icon-small aui-iconfont-remove">Delete</span>
    </a>
  </div>
</td>

      </script>
    
      <script id="share-team-template" type="text/html">
        

<div class="clearfix">
  <span class="team-avatar-container">
    <span class="aui-avatar aui-avatar-medium">
      <span class="aui-avatar-inner">
        <img src="[[avatar]]">
      </span>
    </span>
  </span>
  <span class="team-name-container">
    [[display_name]]
  </span>
</div>
<p class="helptext">
  
    Existing users are granted access to this team immediately.
    New users will be sent an invitation.
  
</p>
<div class="share-form"></div>

      </script>
    
      <script id="scope-list-template" type="text/html">
        <ul class="scope-list">
  [[#scopes]]
    <li class="scope-list--item">
      <span class="scope-list--icon aui-icon aui-icon-small [[icon]]"></span>
      <span class="scope-list--description">[[description]]</span>
    </li>
  [[/scopes]]
</ul>

      </script>
    
  </div>




  
  


<script nonce="B0ZQbvAx7LMqukan">
  window.__initial_state__ = {"global": {"targetFeatures": {"pr-merge-sign-off": true, "clone-mirrors": true, "require-issue-key": true, "adg3": true, "revert-pull-request": true, "pr-checkout-command": true, "new-signup-flow": true, "fe_word_diff": true, "clonebundles": true, "use-moneybucket": true, "search-results-adg3-page": true, "2017-logos": true, "diff-renames-public": true, "app-passwords": true, "guidance-message": true, "ignore-whitespace-button": true, "trello-boards": true, "atlassian-editor": false, "code-search-cta": true, "evolution": false, "diff-renames-internal": true, "search-syntax-highlighting": true, "code-search-cta-launch": true, "source_webitem": true, "lfs_post_beta": true}, "targetUser": {"username": "pypa", "website": null, "display_name": "PyPA", "uuid": "{eeed5f62-f24a-4bdd-9190-1966bfb7cf0e}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/pypa"}, "html": {"href": "https://bitbucket.org/pypa/"}, "avatar": {"href": "https://bitbucket.org/account/pypa/avatar/32/"}}, "extra": {"has_atlassian_account": false}, "created_on": "2011-04-12T09:20:29.664631+00:00", "location": null, "type": "team"}, "features": {"pr-merge-sign-off": true, "ignore-whitespace-button": true, "require-issue-key": true, "adg3": true, "revert-pull-request": true, "pr-checkout-command": true, "new-signup-flow": true, "fe_word_diff": true, "source_webitem": true, "2017-logos": true, "diff-renames-public": true, "app-passwords": true, "guidance-message": true, "use-moneybucket": true, "clone-mirrors": true, "trello-boards": true, "code-search-cta": true, "diff-renames-internal": true, "search-syntax-highlighting": true, "code-search-cta-launch": true, "search-results-adg3-page": true, "lfs_post_beta": true}, "isNavigationOpen": true, "locale": "en", "path": "/pypa/setuptools/raw/bootstrap/ez_setup.py", "geoip_country": null, "focusedTaskBackButtonUrl": null, "isFocusedTask": true}, "repository": {"section": {"connectActions": [], "cloneProtocol": "https", "currentRepository": {"scm": "hg", "name": "setuptools", "links": {"clone": [{"href": "https://bitbucket.org/pypa/setuptools", "name": "https"}, {"href": "ssh://hg@bitbucket.org/pypa/setuptools", "name": "ssh"}], "self": {"href": "https://bitbucket.org/!api/2.0/repositories/pypa/setuptools"}, "html": {"href": "https://bitbucket.org/pypa/setuptools"}, "avatar": {"href": "https://bitbucket.org/pypa/setuptools/avatar/32/"}}, "full_name": "pypa/setuptools", "owner": {"username": "pypa", "website": null, "display_name": "PyPA", "uuid": "{eeed5f62-f24a-4bdd-9190-1966bfb7cf0e}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/pypa"}, "html": {"href": "https://bitbucket.org/pypa/"}, "avatar": {"href": "https://bitbucket.org/account/pypa/avatar/32/"}}, "created_on": "2011-04-12T09:20:29.664631+00:00", "location": null, "type": "team"}, "type": "repository", "slug": "setuptools", "is_private": false, "uuid": "{687a3757-d959-4866-babd-40ad4dd7939b}"}, "menuItems": [{"analytics_label": "repository.overview", "icon_class": "icon-overview", "badge_label": null, "weight": 100, "url": "/pypa/setuptools/overview", "tab_name": "overview", "can_display": true, "label": "Overview", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-overview-link", "icon": "icon-overview"}, {"analytics_label": "repository.source", "icon_class": "icon-source", "badge_label": null, "weight": 200, "url": "/pypa/setuptools/src", "tab_name": "source", "can_display": true, "label": "Source", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-source-link", "icon": "icon-source"}, {"analytics_label": "repository.commits", "icon_class": "icon-commits", "badge_label": null, "weight": 300, "url": "/pypa/setuptools/commits/", "tab_name": "commits", "can_display": true, "label": "Commits", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-commits-link", "icon": "icon-commits"}, {"analytics_label": "repository.branches", "icon_class": "icon-branches", "badge_label": null, "weight": 400, "url": "/pypa/setuptools/branches/", "tab_name": "branches", "can_display": true, "label": "Branches", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-branches-link", "icon": "icon-branches"}, {"analytics_label": "repository.pullrequests", "icon_class": "icon-pull-requests", "badge_label": "0 open pull requests", "weight": 500, "url": "/pypa/setuptools/pull-requests/", "tab_name": "pullrequests", "can_display": true, "label": "Pull requests", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-pullrequests-link", "icon": "icon-pull-requests"}, {"analytics_label": "user.addon", "icon_class": "aui-iconfont-build", "badge_label": null, "weight": 550, "url": "/pypa/setuptools/addon/pipelines/home", "tab_name": "repopage-nprEbg-add-on-link", "can_display": true, "label": "Pipelines", "anchor": true, "analytics_payload": {}, "icon_url": null, "type": "connect_menu_item", "id": "repopage-nprEbg-add-on-link", "target": "_self"}, {"analytics_label": "repository.downloads", "icon_class": "icon-downloads", "badge_label": null, "weight": 800, "url": "/pypa/setuptools/downloads/", "tab_name": "downloads", "can_display": true, "label": "Downloads", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-downloads-link", "icon": "icon-downloads"}], "bitbucketActions": [{"analytics_label": "repository.clone", "icon_class": "icon-clone", "badge_label": null, "weight": 100, "url": "#clone", "tab_name": "clone", "can_display": true, "label": "<strong>Clone<\/strong> this repository", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-clone-button", "icon": "icon-clone"}, {"analytics_label": "repository.compare", "icon_class": "aui-icon-small aui-iconfont-devtools-compare", "badge_label": null, "weight": 400, "url": "/pypa/setuptools/branches/compare", "tab_name": "compare", "can_display": true, "label": "<strong>Compare<\/strong> branches or tags", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-compare-link", "icon": "aui-icon-small aui-iconfont-devtools-compare"}, {"analytics_label": "repository.fork", "icon_class": "icon-fork", "badge_label": null, "weight": 500, "url": "/pypa/setuptools/fork", "tab_name": "fork", "can_display": true, "label": "<strong>Fork<\/strong> this repository", "anchor": true, "analytics_payload": {}, "target": "_self", "type": "menu_item", "id": "repo-fork-link", "icon": "icon-fork"}], "activeMenuItem": "source"}}};
  window.__settings__ = {"SOCIAL_AUTH_ATLASSIANID_LOGOUT_URL": "https://id.atlassian.com/logout", "CANON_URL": "https://bitbucket.org", "API_CANON_URL": "https://api.bitbucket.org"};
</script>

<script src="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/jsi18n/en/djangojs.js"></script>

  <script src="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/dist/webpack/locales/en.js"></script>

<script src="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/dist/webpack/vendor.js"></script>
<script src="https://d301sr5gafysq2.cloudfront.net/b25eee5d4e77/dist/webpack/app.js"></script>


<script async src="https://www.google-analytics.com/analytics.js"></script>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","queueTime":0,"licenseKey":"a2cef8c3d3","agent":"","transactionName":"Z11RZxdWW0cEVkYLDV4XdUYLVEFdClsdAAtEWkZQDlJBGgRFQhFMQl1DXFcZQ10AQkFYBFlUVlEXWEJHAGpAAxU=","applicationID":"1841284","errorBeacon":"bam.nr-data.net","applicationTime":173}</script>
</body>
</html>