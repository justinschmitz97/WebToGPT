<<<<< https://vuejs.org/guide/ >>>>>

# Community Guide | Vue.js

URL: https://vuejs.org/about/community-guide

# Community Guide [​](#community-guide)

Vue's community is growing incredibly fast and if you're reading this, there's a good chance you're ready to join it. So... welcome!

Now we'll answer both what the community can do for you and what you can do for the community.

## Resources [​](#resources)

### Code of Conduct [​](#code-of-conduct)

Our [Code of Conduct](/about/coc) is a guide to make it easier to enrich all of us and the technical communities in which we participate.

### Stay in the Know [​](#stay-in-the-know)

* Follow our [official Twitter account](https://twitter.com/vuejs).
* Follow our [team members](/about/team) on Twitter or GitHub.
* Follow the [RFC discussions](https://github.com/vuejs/rfcs).
* Subscribe to the [official blog](https://blog.vuejs.org/).

### Get Support [​](#get-support)

* [Discord Chat](https://discord.com/invite/vue): A place for Vue devs to meet and chat in real time.
* [Forum](https://forum.vuejs.org/): The best place to ask questions and get answers about Vue and its ecosystem.
* [DEV Community](https://dev.to/t/vue): Share and discuss Vue related topics on Dev.to.
* [Meetups](https://events.vuejs.org/meetups): Want to find local Vue enthusiasts like yourself? Interested in becoming a community leader? We have the help and support you need right here!
* [GitHub](https://github.com/vuejs): If you have a bug to report or feature to request, that's what the GitHub issues are for. Please respect the rules specified in each repository's issue template.
* [Twitter Community (unofficial)](https://twitter.com/i/communities/1516368750634840064): A Twitter community, where you can meet other Vue enthusiasts, get help, or just chat about Vue.

### Explore the Ecosystem [​](#explore-the-ecosystem)

* [The Awesome Vue Page](https://github.com/vuejs/awesome-vue): See what other awesome resources have been published by other awesome people.
* [Vue Telescope Explorer](https://vuetelescope.com/explore): Explore websites made with Vue, with insights on what framework / libraries they use.
* [Made with Vue.js](https://madewithvuejs.com/): showcases of projects and libraries made with Vue.
* [The "Show and Tell" Subforum](https://github.com/vuejs/core/discussions/categories/show-and-tell): Another great place to check out what others have built with and for the growing Vue ecosystem.

## What You Can Do [​](#what-you-can-do)

### Help Fellow Users [​](#help-fellow-users)

Code contribution is not the only form of contribution to the Vue community. Answering a question for a fellow Vue user on Discord or the forum is also considered a valuable contribution.

### Help Triage Issues [​](#help-triage-issues)

Triaging an issue means gathering missing information, running the reproduction, verifying the issue's validity, and investigating the cause of the issue.

We receive many issues in [our repositories on GitHub](https://github.com/vuejs) every single day. Our bandwidth is limited compared to the amount of users we have, so issue triaging alone can take an enormous amount of effort from the team. By helping us triage the issues, you are helping us become more efficient, allowing us to spend time on higher priority work.

You don't have to triage an issue with the goal of fixing it (although that would be nice too). Sharing the result of your investigation, for example the commit that led to the bug, can already save us a ton of time.

### Contribute Code [​](#contribute-code)

Contributing bug fixes or new features is the most direct form of contribution you can make.

The Vue core repository provides a [contributing guide](https://github.com/vuejs/core/blob/main/.github/contributing.md), which contains pull request guidelines and information regarding build setup and high-level architecture. Other sub-project repositories may also contain its own contribution guide - please make sure to read them before submitting pull requests.

Bug fixes are welcome at any time. For new features, it is best to discuss the use case and implementation details first in the [RFC repo](https://github.com/vuejs/rfcs/discussions).

### Share (and Build) Your Experience [​](#share-and-build-your-experience)

Apart from answering questions and sharing resources in the forum and chat, there are a few other less obvious ways to share and expand what you know:

* **Develop learning materials.** It's often said that the best way to learn is to teach. If there's something interesting you're doing with Vue, strengthen your expertise by writing a blog post, developing a workshop, or even publishing a gist that you share on social media.
* **Watch a repo you care about.** This will send you notifications whenever there's activity in that repository, giving you insider knowledge about ongoing discussions and upcoming features. It's a fantastic way to build expertise so that you're eventually able to help address issues and pull requests.

### Translate Docs [​](#translate-docs)

I hope that right now, you're reading this sentence in your preferred language. If not, would you like to help us get there?

See the [Translations guide](/translations/) for more details on how you can get involved.

### Become a Community Leader [​](#become-a-community-leader)

There's a lot you can do to help Vue grow in your community:

* **Present at your local meetup.** Whether it's giving a talk or running a workshop, you can bring a lot of value to your community by helping both new and experienced Vue developers continue to grow.
* **Start your own meetup.** If there's not already a Vue meetup in your area, you can start your own! Use the [resources at events.vuejs.org](https://events.vuejs.org/resources/#getting-started) to help you succeed!
* **Help meetup organizers.** There can never be too much help when it comes to running an event, so offer a hand to help out local organizers to help make every event a success.

If you have any questions on how you can get more involved with your local Vue community, reach out on Twitter at [@vuejs\_events](https://www.twitter.com/vuejs_events)!

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/about/community-guide.md)

---


<<<<< https://vuejs.org/guide/ >>>>>

# API Reference | Vue.js

URL: https://vuejs.org/api/

# API Reference

Filter
## Global API

### Application

* [createApp()](/api/application#createapp)
* [createSSRApp()](/api/application#createssrapp)
* [app.mount()](/api/application#app-mount)
* [app.unmount()](/api/application#app-unmount)
* [app.onUnmount()](/api/application#app-onunmount)
* [app.component()](/api/application#app-component)
* [app.directive()](/api/application#app-directive)
* [app.use()](/api/application#app-use)
* [app.mixin()](/api/application#app-mixin)
* [app.provide()](/api/application#app-provide)
* [app.runWithContext()](/api/application#app-runwithcontext)
* [app.version](/api/application#app-version)
* [app.config](/api/application#app-config)
* [app.config.errorHandler](/api/application#app-config-errorhandler)
* [app.config.warnHandler](/api/application#app-config-warnhandler)
* [app.config.performance](/api/application#app-config-performance)
* [app.config.compilerOptions](/api/application#app-config-compileroptions)
* [app.config.globalProperties](/api/application#app-config-globalproperties)
* [app.config.optionMergeStrategies](/api/application#app-config-optionmergestrategies)
* [app.config.idPrefix](/api/application#app-config-idprefix)
* [app.config.throwUnhandledErrorInProduction](/api/application#app-config-throwunhandlederrorinproduction)
### General

* [version](/api/general#version)
* [nextTick()](/api/general#nexttick)
* [defineComponent()](/api/general#definecomponent)
* [defineAsyncComponent()](/api/general#defineasynccomponent)
## Composition API

### setup()

* [Basic Usage](/api/composition-api-setup#basic-usage)
* [Accessing Props](/api/composition-api-setup#accessing-props)
* [Setup Context](/api/composition-api-setup#setup-context)
* [Usage with Render Functions](/api/composition-api-setup#usage-with-render-functions)
### Reactivity: Core

* [ref()](/api/reactivity-core#ref)
* [computed()](/api/reactivity-core#computed)
* [reactive()](/api/reactivity-core#reactive)
* [readonly()](/api/reactivity-core#readonly)
* [watchEffect()](/api/reactivity-core#watcheffect)
* [watchPostEffect()](/api/reactivity-core#watchposteffect)
* [watchSyncEffect()](/api/reactivity-core#watchsynceffect)
* [watch()](/api/reactivity-core#watch)
* [onWatcherCleanup()](/api/reactivity-core#onwatchercleanup)
### Reactivity: Utilities

* [isRef()](/api/reactivity-utilities#isref)
* [unref()](/api/reactivity-utilities#unref)
* [toRef()](/api/reactivity-utilities#toref)
* [toValue()](/api/reactivity-utilities#tovalue)
* [toRefs()](/api/reactivity-utilities#torefs)
* [isProxy()](/api/reactivity-utilities#isproxy)
* [isReactive()](/api/reactivity-utilities#isreactive)
* [isReadonly()](/api/reactivity-utilities#isreadonly)
### Reactivity: Advanced

* [shallowRef()](/api/reactivity-advanced#shallowref)
* [triggerRef()](/api/reactivity-advanced#triggerref)
* [customRef()](/api/reactivity-advanced#customref)
* [shallowReactive()](/api/reactivity-advanced#shallowreactive)
* [shallowReadonly()](/api/reactivity-advanced#shallowreadonly)
* [toRaw()](/api/reactivity-advanced#toraw)
* [markRaw()](/api/reactivity-advanced#markraw)
* [effectScope()](/api/reactivity-advanced#effectscope)
* [getCurrentScope()](/api/reactivity-advanced#getcurrentscope)
* [onScopeDispose()](/api/reactivity-advanced#onscopedispose)
### Lifecycle Hooks

* [onMounted()](/api/composition-api-lifecycle#onmounted)
* [onUpdated()](/api/composition-api-lifecycle#onupdated)
* [onUnmounted()](/api/composition-api-lifecycle#onunmounted)
* [onBeforeMount()](/api/composition-api-lifecycle#onbeforemount)
* [onBeforeUpdate()](/api/composition-api-lifecycle#onbeforeupdate)
* [onBeforeUnmount()](/api/composition-api-lifecycle#onbeforeunmount)
* [onErrorCaptured()](/api/composition-api-lifecycle#onerrorcaptured)
* [onRenderTracked()](/api/composition-api-lifecycle#onrendertracked)
* [onRenderTriggered()](/api/composition-api-lifecycle#onrendertriggered)
* [onActivated()](/api/composition-api-lifecycle#onactivated)
* [onDeactivated()](/api/composition-api-lifecycle#ondeactivated)
* [onServerPrefetch()](/api/composition-api-lifecycle#onserverprefetch)
### Dependency Injection

* [provide()](/api/composition-api-dependency-injection#provide)
* [inject()](/api/composition-api-dependency-injection#inject)
* [hasInjectionContext()](/api/composition-api-dependency-injection#has-injection-context)
### Helpers

* [useAttrs()](/api/composition-api-helpers#useattrs)
* [useSlots()](/api/composition-api-helpers#useslots)
* [useModel()](/api/composition-api-helpers#usemodel)
* [useTemplateRef()](/api/composition-api-helpers#usetemplateref)
* [useId()](/api/composition-api-helpers#useid)
## Options API

### Options: State

* [data](/api/options-state#data)
* [props](/api/options-state#props)
* [computed](/api/options-state#computed)
* [methods](/api/options-state#methods)
* [watch](/api/options-state#watch)
* [emits](/api/options-state#emits)
* [expose](/api/options-state#expose)
### Options: Rendering

* [template](/api/options-rendering#template)
* [render](/api/options-rendering#render)
* [compilerOptions](/api/options-rendering#compileroptions)
* [slots](/api/options-rendering#slots)
### Options: Lifecycle

* [beforeCreate](/api/options-lifecycle#beforecreate)
* [created](/api/options-lifecycle#created)
* [beforeMount](/api/options-lifecycle#beforemount)
* [mounted](/api/options-lifecycle#mounted)
* [beforeUpdate](/api/options-lifecycle#beforeupdate)
* [updated](/api/options-lifecycle#updated)
* [beforeUnmount](/api/options-lifecycle#beforeunmount)
* [unmounted](/api/options-lifecycle#unmounted)
* [errorCaptured](/api/options-lifecycle#errorcaptured)
* [renderTracked](/api/options-lifecycle#rendertracked)
* [renderTriggered](/api/options-lifecycle#rendertriggered)
* [activated](/api/options-lifecycle#activated)
* [deactivated](/api/options-lifecycle#deactivated)
* [serverPrefetch](/api/options-lifecycle#serverprefetch)
### Options: Composition

* [provide](/api/options-composition#provide)
* [inject](/api/options-composition#inject)
* [mixins](/api/options-composition#mixins)
* [extends](/api/options-composition#extends)
### Options: Misc

* [name](/api/options-misc#name)
* [inheritAttrs](/api/options-misc#inheritattrs)
* [components](/api/options-misc#components)
* [directives](/api/options-misc#directives)
### Component Instance

* [$data](/api/component-instance#data)
* [$props](/api/component-instance#props)
* [$el](/api/component-instance#el)
* [$options](/api/component-instance#options)
* [$parent](/api/component-instance#parent)
* [$root](/api/component-instance#root)
* [$slots](/api/component-instance#slots)
* [$refs](/api/component-instance#refs)
* [$attrs](/api/component-instance#attrs)
* [$watch()](/api/component-instance#watch)
* [$emit()](/api/component-instance#emit)
* [$forceUpdate()](/api/component-instance#forceupdate)
* [$nextTick()](/api/component-instance#nexttick)
## Built-ins

### Directives

* [v-text](/api/built-in-directives#v-text)
* [v-html](/api/built-in-directives#v-html)
* [v-show](/api/built-in-directives#v-show)
* [v-if](/api/built-in-directives#v-if)
* [v-else](/api/built-in-directives#v-else)
* [v-else-if](/api/built-in-directives#v-else-if)
* [v-for](/api/built-in-directives#v-for)
* [v-on](/api/built-in-directives#v-on)
* [v-bind](/api/built-in-directives#v-bind)
* [v-model](/api/built-in-directives#v-model)
* [v-slot](/api/built-in-directives#v-slot)
* [v-pre](/api/built-in-directives#v-pre)
* [v-once](/api/built-in-directives#v-once)
* [v-memo](/api/built-in-directives#v-memo)
* [v-cloak](/api/built-in-directives#v-cloak)
### Components

* [<Transition>](/api/built-in-components#transition)
* [<TransitionGroup>](/api/built-in-components#transitiongroup)
* [<KeepAlive>](/api/built-in-components#keepalive)
* [<Teleport>](/api/built-in-components#teleport)
* [<Suspense>](/api/built-in-components#suspense)
### Special Elements

* [<component>](/api/built-in-special-elements#component)
* [<slot>](/api/built-in-special-elements#slot)
* [<template>](/api/built-in-special-elements#template)
### Special Attributes

* [key](/api/built-in-special-attributes#key)
* [ref](/api/built-in-special-attributes#ref)
* [is](/api/built-in-special-attributes#is)
## Single-File Component

### Syntax Specification

* [Overview](/api/sfc-spec#overview)
* [Language Blocks](/api/sfc-spec#language-blocks)
* [Automatic Name Inference](/api/sfc-spec#automatic-name-inference)
* [Pre-Processors](/api/sfc-spec#pre-processors)
* [src Imports](/api/sfc-spec#src-imports)
* [Comments](/api/sfc-spec#comments)
### <script setup>

* [Basic Syntax](/api/sfc-script-setup#basic-syntax)
* [Reactivity](/api/sfc-script-setup#reactivity)
* [Using Components](/api/sfc-script-setup#using-components)
* [Using Custom Directives](/api/sfc-script-setup#using-custom-directives)
* [defineProps() & defineEmits()](/api/sfc-script-setup#defineprops-defineemits)
* [defineModel()](/api/sfc-script-setup#definemodel)
* [defineExpose()](/api/sfc-script-setup#defineexpose)
* [defineOptions()](/api/sfc-script-setup#defineoptions)
* [defineSlots()](/api/sfc-script-setup#defineslots)
* [useSlots() & useAttrs()](/api/sfc-script-setup#useslots-useattrs)
* [Usage alongside normal <script>](/api/sfc-script-setup#usage-alongside-normal-script)
* [Top-level await](/api/sfc-script-setup#top-level-await)
* [Import Statements](/api/sfc-script-setup#imports-statements)
* [Generics](/api/sfc-script-setup#generics)
* [Restrictions](/api/sfc-script-setup#restrictions)
### CSS Features

* [Scoped CSS](/api/sfc-css-features#scoped-css)
* [CSS Modules](/api/sfc-css-features#css-modules)
* [v-bind() in CSS](/api/sfc-css-features#v-bind-in-css)
## Advanced APIs

### Custom Elements

* [defineCustomElement()](/api/custom-elements#definecustomelement)
* [useHost()](/api/custom-elements#usehost)
* [useShadowRoot()](/api/custom-elements#useshadowroot)
* [this.$host](/api/custom-elements#this-host)
### Render Function

* [h()](/api/render-function#h)
* [mergeProps()](/api/render-function#mergeprops)
* [cloneVNode()](/api/render-function#clonevnode)
* [isVNode()](/api/render-function#isvnode)
* [resolveComponent()](/api/render-function#resolvecomponent)
* [resolveDirective()](/api/render-function#resolvedirective)
* [withDirectives()](/api/render-function#withdirectives)
* [withModifiers()](/api/render-function#withmodifiers)
### Server-Side Rendering

* [renderToString()](/api/ssr#rendertostring)
* [renderToNodeStream()](/api/ssr#rendertonodestream)
* [pipeToNodeWritable()](/api/ssr#pipetonodewritable)
* [renderToWebStream()](/api/ssr#rendertowebstream)
* [pipeToWebWritable()](/api/ssr#pipetowebwritable)
* [renderToSimpleStream()](/api/ssr#rendertosimplestream)
* [useSSRContext()](/api/ssr#usessrcontext)
* [data-allow-mismatch](/api/ssr#data-allow-mismatch)
### TypeScript Utility Types

* [PropType<T>](/api/utility-types#proptype-t)
* [MaybeRef<T>](/api/utility-types#mayberef)
* [MaybeRefOrGetter<T>](/api/utility-types#maybereforgetter)
* [ExtractPropTypes<T>](/api/utility-types#extractproptypes)
* [ExtractPublicPropTypes<T>](/api/utility-types#extractpublicproptypes)
* [ComponentCustomProperties](/api/utility-types#componentcustomproperties)
* [ComponentCustomOptions](/api/utility-types#componentcustomoptions)
* [ComponentCustomProps](/api/utility-types#componentcustomprops)
* [CSSProperties](/api/utility-types#cssproperties)
### Custom Renderer

* [createRenderer()](/api/custom-renderer#createrenderer)
### Compile-Time Flags

* [\_\_VUE\_OPTIONS\_API\_\_](/api/compile-time-flags#VUE_OPTIONS_API)
* [\_\_VUE\_PROD\_DEVTOOLS\_\_](/api/compile-time-flags#VUE_PROD_DEVTOOLS)
* [\_\_VUE\_PROD\_HYDRATION\_MISMATCH\_DETAILS\_\_](/api/compile-time-flags#VUE_PROD_HYDRATION_MISMATCH_DETAILS)
* [Configuration Guides](/api/compile-time-flags#configuration-guides)

---


<<<<< https://vuejs.org/guide/ >>>>>

# Application API | Vue.js

URL: https://vuejs.org/api/application

[Skip to content](#VPContent)On this page Application API has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Built-in Components | Vue.js

URL: https://vuejs.org/api/built-in-components

[Skip to content](#VPContent)On this page Built-in Components has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Built-in Directives | Vue.js

URL: https://vuejs.org/api/built-in-directives

[Skip to content](#VPContent)On this page Built-in Directives has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Built-in Special Attributes | Vue.js

URL: https://vuejs.org/api/built-in-special-attributes

[Skip to content](#VPContent)On this page Built-in Special Attributes has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Built-in Special Elements | Vue.js

URL: https://vuejs.org/api/built-in-special-elements

[Skip to content](#VPContent)On this page Built-in Special Elements has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Compile-Time Flags | Vue.js

URL: https://vuejs.org/api/compile-time-flags

[Skip to content](#VPContent)On this page Compile-Time Flags has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Component Instance | Vue.js

URL: https://vuejs.org/api/component-instance

[Skip to content](#VPContent)On this page Component Instance has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Composition API: Dependency Injection | Vue.js

URL: https://vuejs.org/api/composition-api-dependency-injection

[Skip to content](#VPContent)On this page Composition API: Dependency Injection has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Composition API: Helpers | Vue.js

URL: https://vuejs.org/api/composition-api-helpers

[Skip to content](#VPContent)On this page Composition API: Helpers has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Composition API: Lifecycle Hooks | Vue.js

URL: https://vuejs.org/api/composition-api-lifecycle

[Skip to content](#VPContent)On this page Composition API: Lifecycle Hooks has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Composition API: setup() | Vue.js

URL: https://vuejs.org/api/composition-api-setup

[Skip to content](#VPContent)On this page Composition API: setup() has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Custom Elements API | Vue.js

URL: https://vuejs.org/api/custom-elements

[Skip to content](#VPContent)On this page Custom Elements API has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Custom Renderer API | Vue.js

URL: https://vuejs.org/api/custom-renderer

[Skip to content](#VPContent)On this page Custom Renderer API has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Global API: General | Vue.js

URL: https://vuejs.org/api/general

[Skip to content](#VPContent)On this page Global API: General has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Options: Composition | Vue.js

URL: https://vuejs.org/api/options-composition

[Skip to content](#VPContent)On this page Options: Composition has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Options: Lifecycle | Vue.js

URL: https://vuejs.org/api/options-lifecycle

[Skip to content](#VPContent)On this page Options: Lifecycle has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Options: Misc | Vue.js

URL: https://vuejs.org/api/options-misc

[Skip to content](#VPContent)On this page Options: Misc has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Options: Rendering | Vue.js

URL: https://vuejs.org/api/options-rendering

[Skip to content](#VPContent)On this page Options: Rendering has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Options: State | Vue.js

URL: https://vuejs.org/api/options-state

[Skip to content](#VPContent)On this page Options: State has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Reactivity API: Advanced | Vue.js

URL: https://vuejs.org/api/reactivity-advanced

[Skip to content](#VPContent)On this page Reactivity API: Advanced has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Reactivity API: Core | Vue.js

URL: https://vuejs.org/api/reactivity-core

[Skip to content](#VPContent)On this page Reactivity API: Core has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Reactivity API: Utilities | Vue.js

URL: https://vuejs.org/api/reactivity-utilities

[Skip to content](#VPContent)On this page Reactivity API: Utilities has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Render Function APIs | Vue.js

URL: https://vuejs.org/api/render-function

[Skip to content](#VPContent)On this page Render Function APIs has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# SFC CSS Features | Vue.js

URL: https://vuejs.org/api/sfc-css-features

[Skip to content](#VPContent)On this page SFC CSS Features has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# <script setup> | Vue.js

URL: https://vuejs.org/api/sfc-script-setup

[Skip to content](#VPContent)On this page <script setup> has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# SFC Syntax Specification | Vue.js

URL: https://vuejs.org/api/sfc-spec

[Skip to content](#VPContent)On this page SFC Syntax Specification has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Server-Side Rendering API | Vue.js

URL: https://vuejs.org/api/ssr

[Skip to content](#VPContent)On this page Server-Side Rendering API has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Utility Types | Vue.js

URL: https://vuejs.org/api/utility-types

[Skip to content](#VPContent)On this page Utility Types has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Introduction | Vue.js

URL: https://vuejs.org/guide/

[Skip to content](#VPContent)On this page Introduction has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Accessibility | Vue.js

URL: https://vuejs.org/guide/best-practices/accessibility

[Skip to content](#VPContent)On this page Accessibility has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Performance | Vue.js

URL: https://vuejs.org/guide/best-practices/performance

[Skip to content](#VPContent)On this page Performance has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Production Deployment | Vue.js

URL: https://vuejs.org/guide/best-practices/production-deployment

[Skip to content](#VPContent)On this page Production Deployment has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Security | Vue.js

URL: https://vuejs.org/guide/best-practices/security

[Skip to content](#VPContent)On this page Security has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# KeepAlive | Vue.js

URL: https://vuejs.org/guide/built-ins/keep-alive

[Skip to content](#VPContent)On this page KeepAlive has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Suspense | Vue.js

URL: https://vuejs.org/guide/built-ins/suspense

[Skip to content](#VPContent)On this page Suspense has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Teleport | Vue.js

URL: https://vuejs.org/guide/built-ins/teleport

[Skip to content](#VPContent)On this page Teleport has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Transition | Vue.js

URL: https://vuejs.org/guide/built-ins/transition

[Skip to content](#VPContent)On this page Transition has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# TransitionGroup | Vue.js

URL: https://vuejs.org/guide/built-ins/transition-group

[Skip to content](#VPContent)On this page TransitionGroup has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Async Components | Vue.js

URL: https://vuejs.org/guide/components/async

[Skip to content](#VPContent)On this page Async Components has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Fallthrough Attributes | Vue.js

URL: https://vuejs.org/guide/components/attrs

[Skip to content](#VPContent)On this page Fallthrough Attributes has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Component Events | Vue.js

URL: https://vuejs.org/guide/components/events

[Skip to content](#VPContent)On this page Component Events has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Props | Vue.js

URL: https://vuejs.org/guide/components/props

[Skip to content](#VPContent)On this page Props has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Provide / Inject | Vue.js

URL: https://vuejs.org/guide/components/provide-inject

[Skip to content](#VPContent)On this page Provide / Inject has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Component Registration | Vue.js

URL: https://vuejs.org/guide/components/registration

[Skip to content](#VPContent)On this page Component Registration has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Slots | Vue.js

URL: https://vuejs.org/guide/components/slots

[Skip to content](#VPContent)On this page Slots has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Component v-model | Vue.js

URL: https://vuejs.org/guide/components/v-model

[Skip to content](#VPContent)On this page Component v-model has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Creating a Vue Application | Vue.js

URL: https://vuejs.org/guide/essentials/application

[Skip to content](#VPContent)On this page Creating a Vue Application has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Class and Style Bindings | Vue.js

URL: https://vuejs.org/guide/essentials/class-and-style

[Skip to content](#VPContent)On this page Class and Style Bindings has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Components Basics | Vue.js

URL: https://vuejs.org/guide/essentials/component-basics

[Skip to content](#VPContent)On this page Components Basics has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Computed Properties | Vue.js

URL: https://vuejs.org/guide/essentials/computed

[Skip to content](#VPContent)On this page Computed Properties has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Conditional Rendering | Vue.js

URL: https://vuejs.org/guide/essentials/conditional

[Skip to content](#VPContent)On this page Conditional Rendering has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Event Handling | Vue.js

URL: https://vuejs.org/guide/essentials/event-handling

[Skip to content](#VPContent)On this page Event Handling has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Form Input Bindings | Vue.js

URL: https://vuejs.org/guide/essentials/forms

[Skip to content](#VPContent)On this page Form Input Bindings has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Lifecycle Hooks | Vue.js

URL: https://vuejs.org/guide/essentials/lifecycle

[Skip to content](#VPContent)On this page Lifecycle Hooks has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# List Rendering | Vue.js

URL: https://vuejs.org/guide/essentials/list

[Skip to content](#VPContent)On this page List Rendering has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Reactivity Fundamentals | Vue.js

URL: https://vuejs.org/guide/essentials/reactivity-fundamentals

[Skip to content](#VPContent)On this page Reactivity Fundamentals has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Template Refs | Vue.js

URL: https://vuejs.org/guide/essentials/template-refs

[Skip to content](#VPContent)On this page Template Refs has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Template Syntax | Vue.js

URL: https://vuejs.org/guide/essentials/template-syntax

[Skip to content](#VPContent)On this page Template Syntax has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Watchers | Vue.js

URL: https://vuejs.org/guide/essentials/watchers

[Skip to content](#VPContent)On this page Watchers has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Animation Techniques | Vue.js

URL: https://vuejs.org/guide/extras/animation

[Skip to content](#VPContent)On this page Animation Techniques has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Composition API FAQ | Vue.js

URL: https://vuejs.org/guide/extras/composition-api-faq

[Skip to content](#VPContent)On this page Composition API FAQ has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Reactivity in Depth | Vue.js

URL: https://vuejs.org/guide/extras/reactivity-in-depth

[Skip to content](#VPContent)On this page Reactivity in Depth has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Reactivity Transform | Vue.js

URL: https://vuejs.org/guide/extras/reactivity-transform

[Skip to content](#VPContent)On this page Reactivity Transform has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Render Functions & JSX | Vue.js

URL: https://vuejs.org/guide/extras/render-function

[Skip to content](#VPContent)On this page Render Functions & JSX has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Rendering Mechanism | Vue.js

URL: https://vuejs.org/guide/extras/rendering-mechanism

[Skip to content](#VPContent)On this page Rendering Mechanism has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Ways of Using Vue | Vue.js

URL: https://vuejs.org/guide/extras/ways-of-using-vue

[Skip to content](#VPContent)On this page Ways of Using Vue has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Vue and Web Components | Vue.js

URL: https://vuejs.org/guide/extras/web-components

[Skip to content](#VPContent)On this page Vue and Web Components has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Introduction | Vue.js

URL: https://vuejs.org/guide/introduction

[Skip to content](#VPContent)On this page Introduction has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Quick Start | Vue.js

URL: https://vuejs.org/guide/quick-start

[Skip to content](#VPContent)On this page Quick Start has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Composables | Vue.js

URL: https://vuejs.org/guide/reusability/composables

[Skip to content](#VPContent)On this page Composables has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Custom Directives | Vue.js

URL: https://vuejs.org/guide/reusability/custom-directives

[Skip to content](#VPContent)On this page Custom Directives has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Plugins | Vue.js

URL: https://vuejs.org/guide/reusability/plugins

[Skip to content](#VPContent)On this page Plugins has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Routing | Vue.js

URL: https://vuejs.org/guide/scaling-up/routing

[Skip to content](#VPContent)On this page Routing has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Single-File Components | Vue.js

URL: https://vuejs.org/guide/scaling-up/sfc

[Skip to content](#VPContent)On this page Single-File Components has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Server-Side Rendering (SSR) | Vue.js

URL: https://vuejs.org/guide/scaling-up/ssr

[Skip to content](#VPContent)On this page Server-Side Rendering (SSR) has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# State Management | Vue.js

URL: https://vuejs.org/guide/scaling-up/state-management

[Skip to content](#VPContent)On this page State Management has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Testing | Vue.js

URL: https://vuejs.org/guide/scaling-up/testing

[Skip to content](#VPContent)On this page Testing has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Tooling | Vue.js

URL: https://vuejs.org/guide/scaling-up/tooling

[Skip to content](#VPContent)On this page Tooling has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# TypeScript with Composition API | Vue.js

URL: https://vuejs.org/guide/typescript/composition-api

[Skip to content](#VPContent)On this page TypeScript with Composition API has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# TypeScript with Options API | Vue.js

URL: https://vuejs.org/guide/typescript/options-api

[Skip to content](#VPContent)On this page TypeScript with Options API has loaded

---


<<<<< https://vuejs.org/guide/ >>>>>

# Using Vue with TypeScript | Vue.js

URL: https://vuejs.org/guide/typescript/overview

[Skip to content](#VPContent)On this page Using Vue with TypeScript has loaded

---

