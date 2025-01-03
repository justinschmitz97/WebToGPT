# https://vuejs.org/guide/

## Community Guide | Vue.js

[Read the full article](https://vuejs.org/about/community-guide)

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

The Vue core repository provides a [contributing guide](https://github.com/vuejs/core/blob/main/.github/contributing.md), which contains pull request guidelines and information regarding build setup and high\-level architecture. Other sub\-project repositories may also contain its own contribution guide \- please make sure to read them before submitting pull requests.

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



## Plugins | Vue.js

[Read the full article](https://vuejs.org/guide/reusability/plugins)

# Plugins [​](#plugins)

## Introduction [​](#introduction)

Plugins are self\-contained code that usually add app\-level functionality to Vue. This is how we install a plugin:

js\`\`\`
import { createApp } from 'vue'

const app = createApp({})

app.use(myPlugin, {
 /\* optional options \*/
})
\`\`\`A plugin is defined as either an object that exposes an `install()` method, or simply a function that acts as the install function itself. The install function receives the [app instance](/api/application) along with additional options passed to `app.use()`, if any:

js\`\`\`
const myPlugin = {
 install(app, options) {
 // configure the app
 }
}
\`\`\`There is no strictly defined scope for a plugin, but common scenarios where plugins are useful include:

1. Register one or more global components or custom directives with [`app.component()`](/api/application#app-component) and [`app.directive()`](/api/application#app-directive).
2. Make a resource [injectable](/guide/components/provide-inject) throughout the app by calling [`app.provide()`](/api/application#app-provide).
3. Add some global instance properties or methods by attaching them to [`app.config.globalProperties`](/api/application#app-config-globalproperties).
4. A library that needs to perform some combination of the above (e.g. [vue\-router](https://github.com/vuejs/vue-router-next)).

## Writing a Plugin [​](#writing-a-plugin)

In order to better understand how to create your own Vue.js plugins, we will create a very simplified version of a plugin that displays `i18n` (short for [Internationalization](https://en.wikipedia.org/wiki/Internationalization_and_localization)) strings.

Let's begin by setting up the plugin object. It is recommended to create it in a separate file and export it, as shown below to keep the logic contained and separate.

js\`\`\`
// plugins/i18n.js
export default {
 install: (app, options) =\> {
 // Plugin code goes here
 }
}
\`\`\`We want to create a translation function. This function will receive a dot\-delimited `key` string, which we will use to look up the translated string in the user\-provided options. This is the intended usage in templates:

template\`\`\`
\{{ $translate('greetings.hello') }}\
\`\`\`Since this function should be globally available in all templates, we will make it so by attaching it to `app.config.globalProperties` in our plugin:

js\`\`\`
// plugins/i18n.js
export default {
 install: (app, options) =\> {
 // inject a globally available $translate() method
 app.config.globalProperties.$translate = (key) =\> {
 // retrieve a nested property in \`options\`
 // using \`key\` as the path
 return key.split('.').reduce((o, i) =\> {
 if (o) return o\[i]
 }, options)
 }
 }
}
\`\`\`Our `$translate` function will take a string such as `greetings.hello`, look inside the user provided configuration and return the translated value.

The object containing the translated keys should be passed to the plugin during installation via additional parameters to `app.use()`:

js\`\`\`
import i18nPlugin from './plugins/i18n'

app.use(i18nPlugin, {
 greetings: {
 hello: 'Bonjour!'
 }
})
\`\`\`Now, our initial expression `$translate('greetings.hello')` will be replaced by `Bonjour!` at runtime.

See also: [Augmenting Global Properties](/guide/typescript/options-api#augmenting-global-properties) 

TIP

Use global properties scarcely, since it can quickly become confusing if too many global properties injected by different plugins are used throughout an app.

### Provide / Inject with Plugins [​](#provide-inject-with-plugins)

Plugins also allow us to use `inject` to provide a function or attribute to the plugin's users. For example, we can allow the application to have access to the `options` parameter to be able to use the translations object.

js\`\`\`
// plugins/i18n.js
export default {
 install: (app, options) =\> {
 app.provide('i18n', options)
 }
}
\`\`\`Plugin users will now be able to inject the plugin options into their components using the `i18n` key:

vue\`\`\`
\
import { inject } from 'vue'

const i18n = inject('i18n')

console.log(i18n.greetings.hello)
\
\`\`\`js\`\`\`
export default {
 inject: \['i18n'],
 created() {
 console.log(this.i18n.greetings.hello)
 }
}
\`\`\`### Bundle for NPM [​](#bundle-for-npm)

If you further want to build and publish your plugin for others to use, see [Vite's section on Library Mode](https://vitejs.dev/guide/build.html#library-mode).

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/reusability/plugins.md)



## Production Deployment | Vue.js

[Read the full article](https://vuejs.org/guide/best-practices/production-deployment)

# Production Deployment [​](#production-deployment)

## Development vs. Production [​](#development-vs-production)

During development, Vue provides a number of features to improve the development experience:

* Warning for common errors and pitfalls
* Props / events validation
* [Reactivity debugging hooks](/guide/extras/reactivity-in-depth#reactivity-debugging)
* Devtools integration

However, these features become useless in production. Some of the warning checks can also incur a small amount of performance overhead. When deploying to production, we should drop all the unused, development\-only code branches for smaller payload size and better performance.

## Without Build Tools [​](#without-build-tools)

If you are using Vue without a build tool by loading it from a CDN or self\-hosted script, make sure to use the production build (dist files that end in `.prod.js`) when deploying to production. Production builds are pre\-minified with all development\-only code branches removed.

* If using global build (accessing via the `Vue` global): use `vue.global.prod.js`.
* If using ESM build (accessing via native ESM imports): use `vue.esm-browser.prod.js`.

Consult the [dist file guide](https://github.com/vuejs/core/tree/main/packages/vue#which-dist-file-to-use) for more details.

## With Build Tools [​](#with-build-tools)

Projects scaffolded via `create-vue` (based on Vite) or Vue CLI (based on webpack) are pre\-configured for production builds.

If using a custom setup, make sure that:

1. `vue` resolves to `vue.runtime.esm-bundler.js`.
2. The [compile time feature flags](/api/compile-time-flags) are properly configured.
3. `process.env.NODE_ENV` is replaced with `"production"` during build.

Additional references:

* [Vite production build guide](https://vitejs.dev/guide/build.html)
* [Vite deployment guide](https://vitejs.dev/guide/static-deploy.html)
* [Vue CLI deployment guide](https://cli.vuejs.org/guide/deployment.html)

## Tracking Runtime Errors [​](#tracking-runtime-errors)

The [app\-level error handler](/api/application#app-config-errorhandler) can be used to report errors to tracking services:

js\`\`\`
import { createApp } from 'vue'

const app = createApp(...)

app.config.errorHandler = (err, instance, info) =\> {
 // report error to tracking services
}
\`\`\`Services such as [Sentry](https://docs.sentry.io/platforms/javascript/guides/vue/) and [Bugsnag](https://docs.bugsnag.com/platforms/javascript/vue/) also provide official integrations for Vue.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/best-practices/production-deployment.md)



## Reactivity API: Advanced | Vue.js

[Read the full article](https://vuejs.org/api/reactivity-advanced)

# Reactivity API: Advanced [​](#reactivity-api-advanced)

## shallowRef() [​](#shallowref)

Shallow version of [`ref()`](/api/reactivity-core#ref).

* **Type**

ts\`\`\`
function shallowRef\(value: T): ShallowRef\

interface ShallowRef\ {
 value: T
}
\`\`\`
* **Details**

Unlike `ref()`, the inner value of a shallow ref is stored and exposed as\-is, and will not be made deeply reactive. Only the `.value` access is reactive.

`shallowRef()` is typically used for performance optimizations of large data structures, or integration with external state management systems.
* **Example**

js\`\`\`
const state = shallowRef({ count: 1 })

// does NOT trigger change
state.value.count = 2

// does trigger change
state.value = { count: 2 }
\`\`\`
* **See also**

	+ [Guide \- Reduce Reactivity Overhead for Large Immutable Structures](/guide/best-practices/performance#reduce-reactivity-overhead-for-large-immutable-structures)
	+ [Guide \- Integration with External State Systems](/guide/extras/reactivity-in-depth#integration-with-external-state-systems)

## triggerRef() [​](#triggerref)

Force trigger effects that depends on a [shallow ref](#shallowref). This is typically used after making deep mutations to the inner value of a shallow ref.

* **Type**

ts\`\`\`
function triggerRef(ref: ShallowRef): void
\`\`\`
* **Example**

js\`\`\`
const shallow = shallowRef({
 greet: 'Hello, world'
})

// Logs "Hello, world" once for the first run\-through
watchEffect(() =\> {
 console.log(shallow.value.greet)
})

// This won't trigger the effect because the ref is shallow
shallow.value.greet = 'Hello, universe'

// Logs "Hello, universe"
triggerRef(shallow)
\`\`\`

## customRef() [​](#customref)

Creates a customized ref with explicit control over its dependency tracking and updates triggering.

* **Type**

ts\`\`\`
function customRef\(factory: CustomRefFactory\): Ref\

type CustomRefFactory\ = (
 track: () =\> void,
 trigger: () =\> void
) =\> {
 get: () =\> T
 set: (value: T) =\> void
}
\`\`\`
* **Details**

`customRef()` expects a factory function, which receives `track` and `trigger` functions as arguments and should return an object with `get` and `set` methods.

In general, `track()` should be called inside `get()`, and `trigger()` should be called inside `set()`. However, you have full control over when they should be called, or whether they should be called at all.
* **Example**

Creating a debounced ref that only updates the value after a certain timeout after the latest set call:

js\`\`\`
import { customRef } from 'vue'

export function useDebouncedRef(value, delay = 200\) {
 let timeout
 return customRef((track, trigger) =\> {
 return {
 get() {
 track()
 return value
 },
 set(newValue) {
 clearTimeout(timeout)
 timeout = setTimeout(() =\> {
 value = newValue
 trigger()
 }, delay)
 }
 }
 })
}
\`\`\`Usage in component:

vue\`\`\`
\
import { useDebouncedRef } from './debouncedRef'
const text = useDebouncedRef('hello')
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNplUkFugzAQ/MqKC1SiIekxIpEq9QVV1BMXCguhBdsyaxqE/PcuGAhNfYGd3Z0ZDwzeq1K7zqB39OI205UiaJGMOieiapTUBAOYFt/wUxqRYf6OBVgotGzA30X5Bt59tX4iMilaAsIbwelxMfCvWNfSD+Gw3++fEhFHTpLFuCBsVJ0ScgUQjw6Az+VatY5PiroHo3IeaeHANlkrh7Qg1NBL43cILUmlMAfqVSXK40QUOSYmHAZHZO0KVkIZgu65kTnWp8Qb+4kHEXfjaDXkhd7DTTmuNZ7MsGyzDYbz5CgSgbdppOBFqqT4l0eX1gZDYOm057heOBQYRl81coZVg9LQWGr+IlrchYKAdJp9h0C6KkvUT3A6u8V1dq4ASqRgZnVnWg04/QWYNyYzC2rD5Y3/hkDgz8fY/cOT1ZjqizMZzGY3rDPC12KGZYyd3J26M8ny1KKx7c3X25q1c1wrZN3L9LCMWs/+AmeG6xI=)

Use with caution

When using customRef, we should be cautious about the return value of its getter, particularly when generating new object datatypes each time the getter is run. This affects the relationship between parent and child components, where such a customRef has been passed as a prop.

The parent component's render function could be triggered by changes to a different reactive state. During rerender, the value of our customRef is reevaluated, returning a new object datatype as a prop to a child component. This prop is compared with its last value in the child component, and since they are different, the reactive dependencies of the customRef are triggered in the child component. Meanwhile, the reactive dependencies in the parent component do not run because the customRef's setter was not called, and its dependencies were not triggered as a result.

[See it in the Playground](https://play.vuejs.org/#eNqFVEtP3DAQ/itTS9Vm1ZCt1J6WBZUiDvTQIsoNcwiOkzU4tmU7+9Aq/71jO1mCWuhlN/PyfPP45kAujCk2HSdLsnLMCuPBcd+Zc6pEa7T1cADWOa/bW17nYMPPtvRsDT3UVrcww+DZ0flStybpKSkWQQqPU0IVVUwr58FYvdvDWXgpu6ek1pqSHL0fS0vJw/z0xbN1jUPHY/Ys87Zkzzl4K5qG2zmcnUN2oAqg4T6bQ/wENKNXNk+CxWKsSlmLTSk7XlhedYxnWclYDiK+MkQCoK4wnVtnIiBJuuEJNA2qPof7hzkEoc8DXgg9yzYTBBFgNr4xyY4FbaK2p6qfI0iqFgtgulOe27HyQRy69Dk1JXY9C03JIeQ6wg4xWvJCqFpnlNytOcyC2wzYulQNr0Ao+Mhw0KnTTEttl/CIaIJiMz8NGBHFtYetVrPwa58/IL48Zag4N0ssquNYLYBoW16J0vOkC3VQtVqk7cG9QcHz1kj0QAlgVYkNMFk6d0bJ1pbGYKUkmtD42HmvFfi94WhOEiXwjUnBnlEz9OLTJwy5qCo44D4O7en71SIFjI/F9VuG4jEy/GHQKq5hQrJAKOc4uNVighBF5/cygS0GgOMoK+HQb7+EWvLdMM7weVIJy5kXWi0Rj+xaNRhLKRp1IvB9hxYegA6WJ1xkUe9PcF4e9a+suA3YwYiC5MQ79KlFUzw5rZCZEUtoRWuE5PaXCXmxtuWIkpJSSr39EXXHQcWYNWfP/9A/uV3QUXJjueN2E1ZhtPnSIqGS+er3T77D76Ox1VUn0fsd4y3HfewCxuT2vVMVwp74RbTX8WQI1dy5qx12xI1Fpa1K5AreeEHCCN8q/QXul+LrSC3s4nh93jltkVPDIYt5KJkcIKStCReo4rVQ/CZI6dyEzToCCJu7hAtry/1QH/qXncQB400KJwqPxZHxEyona0xS/E3rt1m9Ld1rZl+uhaxecRtP3EjtgddCyimtXyj9H/Ii3eId7uOGTkyk/wOEbQ9h)

## shallowReactive() [​](#shallowreactive)

Shallow version of [`reactive()`](/api/reactivity-core#reactive).

* **Type**

ts\`\`\`
function shallowReactive\(target: T): T
\`\`\`
* **Details**

Unlike `reactive()`, there is no deep conversion: only root\-level properties are reactive for a shallow reactive object. Property values are stored and exposed as\-is \- this also means properties with ref values will **not** be automatically unwrapped.

Use with Caution

Shallow data structures should only be used for root level state in a component. Avoid nesting it inside a deep reactive object as it creates a tree with inconsistent reactivity behavior which can be difficult to understand and debug.
* **Example**

js\`\`\`
const state = shallowReactive({
 foo: 1,
 nested: {
 bar: 2
 }
})

// mutating state's own properties is reactive
state.foo\+\+

// ...but does not convert nested objects
isReactive(state.nested) // false

// NOT reactive
state.nested.bar\+\+
\`\`\`

## shallowReadonly() [​](#shallowreadonly)

Shallow version of [`readonly()`](/api/reactivity-core#readonly).

* **Type**

ts\`\`\`
function shallowReadonly\(target: T): Readonly\
\`\`\`
* **Details**

Unlike `readonly()`, there is no deep conversion: only root\-level properties are made readonly. Property values are stored and exposed as\-is \- this also means properties with ref values will **not** be automatically unwrapped.

Use with Caution

Shallow data structures should only be used for root level state in a component. Avoid nesting it inside a deep reactive object as it creates a tree with inconsistent reactivity behavior which can be difficult to understand and debug.
* **Example**

js\`\`\`
const state = shallowReadonly({
 foo: 1,
 nested: {
 bar: 2
 }
})

// mutating state's own properties will fail
state.foo\+\+

// ...but works on nested objects
isReadonly(state.nested) // false

// works
state.nested.bar\+\+
\`\`\`

## toRaw() [​](#toraw)

Returns the raw, original object of a Vue\-created proxy.

* **Type**

ts\`\`\`
function toRaw\(proxy: T): T
\`\`\`
* **Details**

`toRaw()` can return the original object from proxies created by [`reactive()`](/api/reactivity-core#reactive), [`readonly()`](/api/reactivity-core#readonly), [`shallowReactive()`](#shallowreactive) or [`shallowReadonly()`](#shallowreadonly).

This is an escape hatch that can be used to temporarily read without incurring proxy access / tracking overhead or write without triggering changes. It is **not** recommended to hold a persistent reference to the original object. Use with caution.
* **Example**

js\`\`\`
const foo = {}
const reactiveFoo = reactive(foo)

console.log(toRaw(reactiveFoo) === foo) // true
\`\`\`

## markRaw() [​](#markraw)

Marks an object so that it will never be converted to a proxy. Returns the object itself.

* **Type**

ts\`\`\`
function markRaw\(value: T): T
\`\`\`
* **Example**

js\`\`\`
const foo = markRaw({})
console.log(isReactive(reactive(foo))) // false

// also works when nested inside other reactive objects
const bar = reactive({ foo })
console.log(isReactive(bar.foo)) // false
\`\`\`Use with Caution

`markRaw()` and shallow APIs such as `shallowReactive()` allow you to selectively opt\-out of the default deep reactive/readonly conversion and embed raw, non\-proxied objects in your state graph. They can be used for various reasons:

	+ Some values simply should not be made reactive, for example a complex 3rd party class instance, or a Vue component object.
	+ Skipping proxy conversion can provide performance improvements when rendering large lists with immutable data sources.They are considered advanced because the raw opt\-out is only at the root level, so if you set a nested, non\-marked raw object into a reactive object and then access it again, you get the proxied version back. This can lead to **identity hazards** \- i.e. performing an operation that relies on object identity but using both the raw and the proxied version of the same object:

js\`\`\`
const foo = markRaw({
 nested: {}
})

const bar = reactive({
 // although \`foo\` is marked as raw, foo.nested is not.
 nested: foo.nested
})

console.log(foo.nested === bar.nested) // false
\`\`\`Identity hazards are in general rare. However, to properly utilize these APIs while safely avoiding identity hazards requires a solid understanding of how the reactivity system works.

## effectScope() [​](#effectscope)

Creates an effect scope object which can capture the reactive effects (i.e. computed and watchers) created within it so that these effects can be disposed together. For detailed use cases of this API, please consult its corresponding [RFC](https://github.com/vuejs/rfcs/blob/master/active-rfcs/0041-reactivity-effect-scope.md).

* **Type**

ts\`\`\`
function effectScope(detached?: boolean): EffectScope

interface EffectScope {
 run\(fn: () =\> T): T \| undefined // undefined if scope is inactive
 stop(): void
}
\`\`\`
* **Example**

js\`\`\`
const scope = effectScope()

scope.run(() =\> {
 const doubled = computed(() =\> counter.value \* 2\)

 watch(doubled, () =\> console.log(doubled.value))

 watchEffect(() =\> console.log('Count: ', doubled.value))
})

// to dispose all effects in the scope
scope.stop()
\`\`\`

## getCurrentScope() [​](#getcurrentscope)

Returns the current active [effect scope](#effectscope) if there is one.

* **Type**

ts\`\`\`
function getCurrentScope(): EffectScope \| undefined
\`\`\`

## onScopeDispose() [​](#onscopedispose)

Registers a dispose callback on the current active [effect scope](#effectscope). The callback will be invoked when the associated effect scope is stopped.

This method can be used as a non\-component\-coupled replacement of `onUnmounted` in reusable composition functions, since each Vue component's `setup()` function is also invoked in an effect scope.

A warning will be thrown if this function is called without an active effect scope. In 3\.5\+, this warning can be suppressed by passing `true` as the second argument.

* **Type**

ts\`\`\`
function onScopeDispose(fn: () =\> void, failSilently?: boolean): void
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/reactivity-advanced.md)



## Routing | Vue.js

[Read the full article](https://vuejs.org/guide/scaling-up/routing)

# Routing [​](#routing)

## Client\-Side vs. Server\-Side Routing [​](#client-side-vs-server-side-routing)

Routing on the server side means the server is sending a response based on the URL path that the user is visiting. When we click on a link in a traditional server\-rendered web app, the browser receives an HTML response from the server and reloads the entire page with the new HTML.

In a [Single\-Page Application](https://developer.mozilla.org/en-US/docs/Glossary/SPA) (SPA), however, the client\-side JavaScript can intercept the navigation, dynamically fetch new data, and update the current page without full page reloads. This typically results in a more snappy user experience, especially for use cases that are more like actual "applications", where the user is expected to perform many interactions over a long period of time.

In such SPAs, the "routing" is done on the client side, in the browser. A client\-side router is responsible for managing the application's rendered view using browser APIs such as [History API](https://developer.mozilla.org/en-US/docs/Web/API/History) or the [`hashchange` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/hashchange_event).

## Official Router [​](#official-router)

 [Watch a Free Video Course on Vue School](https://vueschool.io/courses/vue-router-4-for-everyone?friend=vuejs "Free Vue Router Course") Vue is well\-suited for building SPAs. For most SPAs, it's recommended to use the officially\-supported [Vue Router library](https://github.com/vuejs/router). For more details, see Vue Router's [documentation](https://router.vuejs.org/).

## Simple Routing from Scratch [​](#simple-routing-from-scratch)

If you only need very simple routing and do not wish to involve a full\-featured router library, you can do so with [Dynamic Components](/guide/essentials/component-basics#dynamic-components) and update the current component state by listening to browser [`hashchange` events](https://developer.mozilla.org/en-US/docs/Web/API/Window/hashchange_event) or using the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History).

Here's a bare\-bone example:

vue\`\`\`
\
import { ref, computed } from 'vue'
import Home from './Home.vue'
import About from './About.vue'
import NotFound from './NotFound.vue'

const routes = {
 '/': Home,
 '/about': About
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () =\> {
 currentPath.value = window.location.hash
})

const currentView = computed(() =\> {
 return routes\[currentPath.value.slice(1\) \|\| '/'] \|\| NotFound
})
\

\
 \Home\ \|
 \About\ \|
 \Broken Link\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNptUk1vgkAQ/SsTegAThZp4MmhikzY9mKanXkoPWxjLRpgly6JN1P/eWb5Eywlm572ZN2/m5GyKwj9U6CydsIy1LAyUaKpiHZHMC6UNnEDjbgqxyovKYAIX2GmVg8sktwe9qhzbdz+wga15TW++VWX6fB3dAt6UeVEVJT2me2hhEcWKSgOamVjCCk4RAbiBu6xbT5tI2ML8VDeI6HLlxZXWSOZdmJTJPJB3lJSoo5+pWBipyE9FmU4soU2IJHk+MGUrS4OE2nMtIk4F/aA7BW8Cq3WjYlDbP4isQu4wVp0F1Q1uFH1IPDK+c9cb1NW8B03tyJ//uvhlJmP05hM4n60TX/bb2db0CoNmpbxMDgzmRSYMcgQQCkjZhlXkPASRs7YmhoFYw/k+WXvKiNrTcQgpmuFv7ZOZFSyQ4U9a7ZFgK2lvSTXFDqmIQbCUJTMHFkQOBAwKg16kM3W6O7K3eSs+nbeK+eee1V/XKK0dY4Q3vLhR6uJxMUK8/AFKaB6k)

vue\`\`\`
\
import Home from './Home.vue'
import About from './About.vue'
import NotFound from './NotFound.vue'

const routes = {
 '/': Home,
 '/about': About
}

export default {
 data() {
 return {
 currentPath: window.location.hash
 }
 },
 computed: {
 currentView() {
 return routes\[this.currentPath.slice(1\) \|\| '/'] \|\| NotFound
 }
 },
 mounted() {
 window.addEventListener('hashchange', () =\> {
 this.currentPath = window.location.hash
 })
 }
}
\

\
 \Home\ \|
 \About\ \|
 \Broken Link\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNptUstO6zAQ/ZVR7iKtVJKLxCpKK3Gli1ggxIoNZmGSKbFoxpEzoUi0/87YeVBKNonHPmfOmcdndN00yXuHURblbeFMwxtFpm6sY7i1NcLW2RriJPWBB8bT8/WL7Xh6D9FPwL3lG9tROWHGiwGmqLDUMjhhYgtr+FQEEKdxFqRXfaR9YrkKAoqOnocfQaDEre523PNKzXqx7M8ADrlzNEYAReccEj9orjLYGyrtPtnZQrOxlFS6rXqgZJdPUC5s3YivMhuTDCkeDe6/dSalvognrkybnIgl7c4UuLhcwuHgS3v2/7EPvzRruRXJ7/SDU12W/98l451pGQndIvaWi0rTK8YrEPx64ymKFQOce5DOzlfs4cdlkA+NzdNpBSRgrJudZpQIINdQOdyuVfQnVdHGzydP9QYO549hXIII45qHkKUL/Ail8EUjBgX+z9k3JLgz9OZJgeInYElAkJlWmCcDUBGkAsrTyWS0isYV9bv803x1OTiWwzlrWtxZ2lDGDO90mWepV3+vZojHL3QQKQE=)

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/scaling-up/routing.md)



## Options: Lifecycle | Vue.js

[Read the full article](https://vuejs.org/api/options-lifecycle)

# Options: Lifecycle [​](#options-lifecycle)

See also

For shared usage of lifecycle hooks, see [Guide \- Lifecycle Hooks](/guide/essentials/lifecycle)

## beforeCreate [​](#beforecreate)

Called when the instance is initialized.

* **Type**

ts\`\`\`
interface ComponentOptions {
 beforeCreate?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

Called immediately when the instance is initialized and props are resolved.

Then the props will be defined as reactive properties and the state such as `data()` or `computed` will be set up.

Note that the `setup()` hook of Composition API is called before any Options API hooks, even `beforeCreate()`.

## created [​](#created)

Called after the instance has finished processing all state\-related options.

* **Type**

ts\`\`\`
interface ComponentOptions {
 created?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

When this hook is called, the following have been set up: reactive data, computed properties, methods, and watchers. However, the mounting phase has not been started, and the `$el` property will not be available yet.

## beforeMount [​](#beforemount)

Called right before the component is to be mounted.

* **Type**

ts\`\`\`
interface ComponentOptions {
 beforeMount?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

When this hook is called, the component has finished setting up its reactive state, but no DOM nodes have been created yet. It is about to execute its DOM render effect for the first time.

**This hook is not called during server\-side rendering.**

## mounted [​](#mounted)

Called after the component has been mounted.

* **Type**

ts\`\`\`
interface ComponentOptions {
 mounted?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

A component is considered mounted after:

	+ All of its synchronous child components have been mounted (does not include async components or components inside `` trees).
	+ Its own DOM tree has been created and inserted into the parent container. Note it only guarantees that the component's DOM tree is in\-document if the application's root container is also in\-document.This hook is typically used for performing side effects that need access to the component's rendered DOM, or for limiting DOM\-related code to the client in a [server\-rendered application](/guide/scaling-up/ssr).

**This hook is not called during server\-side rendering.**

## beforeUpdate [​](#beforeupdate)

Called right before the component is about to update its DOM tree due to a reactive state change.

* **Type**

ts\`\`\`
interface ComponentOptions {
 beforeUpdate?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

This hook can be used to access the DOM state before Vue updates the DOM. It is also safe to modify component state inside this hook.

**This hook is not called during server\-side rendering.**

## updated [​](#updated)

Called after the component has updated its DOM tree due to a reactive state change.

* **Type**

ts\`\`\`
interface ComponentOptions {
 updated?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

A parent component's updated hook is called after that of its child components.

This hook is called after any DOM update of the component, which can be caused by different state changes. If you need to access the updated DOM after a specific state change, use [nextTick()](/api/general#nexttick) instead.

**This hook is not called during server\-side rendering.**

WARNING

Do not mutate component state in the updated hook \- this will likely lead to an infinite update loop!

## beforeUnmount [​](#beforeunmount)

Called right before a component instance is to be unmounted.

* **Type**

ts\`\`\`
interface ComponentOptions {
 beforeUnmount?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

When this hook is called, the component instance is still fully functional.

**This hook is not called during server\-side rendering.**

## unmounted [​](#unmounted)

Called after the component has been unmounted.

* **Type**

ts\`\`\`
interface ComponentOptions {
 unmounted?(this: ComponentPublicInstance): void
}
\`\`\`
* **Details**

A component is considered unmounted after:

	+ All of its child components have been unmounted.
	+ All of its associated reactive effects (render effect and computed / watchers created during `setup()`) have been stopped.Use this hook to clean up manually created side effects such as timers, DOM event listeners or server connections.

**This hook is not called during server\-side rendering.**

## errorCaptured [​](#errorcaptured)

Called when an error propagating from a descendant component has been captured.

* **Type**

ts\`\`\`
interface ComponentOptions {
 errorCaptured?(
 this: ComponentPublicInstance,
 err: unknown,
 instance: ComponentPublicInstance \| null,
 info: string
 ): boolean \| void
}
\`\`\`
* **Details**

Errors can be captured from the following sources:

	+ Component renders
	+ Event handlers
	+ Lifecycle hooks
	+ `setup()` function
	+ Watchers
	+ Custom directive hooks
	+ Transition hooksThe hook receives three arguments: the error, the component instance that triggered the error, and an information string specifying the error source type.

TIP

In production, the 3rd argument (`info`) will be a shortened code instead of the full information string. You can find the code to string mapping in the [Production Error Code Reference](/error-reference/#runtime-errors).

You can modify component state in `errorCaptured()` to display an error state to the user. However, it is important that the error state should not render the original content that caused the error; otherwise the component will be thrown into an infinite render loop.

The hook can return `false` to stop the error from propagating further. See error propagation details below.

**Error Propagation Rules**

	+ By default, all errors are still sent to the application\-level [`app.config.errorHandler`](/api/application#app-config-errorhandler) if it is defined, so that these errors can still be reported to an analytics service in a single place.
	+ If multiple `errorCaptured` hooks exist on a component's inheritance chain or parent chain, all of them will be invoked on the same error, in the order of bottom to top. This is similar to the bubbling mechanism of native DOM events.
	+ If the `errorCaptured` hook itself throws an error, both this error and the original captured error are sent to `app.config.errorHandler`.
	+ An `errorCaptured` hook can return `false` to prevent the error from propagating further. This is essentially saying "this error has been handled and should be ignored." It will prevent any additional `errorCaptured` hooks or `app.config.errorHandler` from being invoked for this error.

## renderTracked  [​](#rendertracked)

Called when a reactive dependency has been tracked by the component's render effect.

**This hook is development\-mode\-only and not called during server\-side rendering.**

* **Type**

ts\`\`\`
interface ComponentOptions {
 renderTracked?(this: ComponentPublicInstance, e: DebuggerEvent): void
}

type DebuggerEvent = {
 effect: ReactiveEffect
 target: object
 type: TrackOpTypes /\* 'get' \| 'has' \| 'iterate' \*/
 key: any
}
\`\`\`
* **See also** [Reactivity in Depth](/guide/extras/reactivity-in-depth)

## renderTriggered  [​](#rendertriggered)

Called when a reactive dependency triggers the component's render effect to be re\-run.

**This hook is development\-mode\-only and not called during server\-side rendering.**

* **Type**

ts\`\`\`
interface ComponentOptions {
 renderTriggered?(this: ComponentPublicInstance, e: DebuggerEvent): void
}

type DebuggerEvent = {
 effect: ReactiveEffect
 target: object
 type: TriggerOpTypes /\* 'set' \| 'add' \| 'delete' \| 'clear' \*/
 key: any
 newValue?: any
 oldValue?: any
 oldTarget?: Map\ \| Set\
}
\`\`\`
* **See also** [Reactivity in Depth](/guide/extras/reactivity-in-depth)

## activated [​](#activated)

Called after the component instance is inserted into the DOM as part of a tree cached by [``](/api/built-in-components#keepalive).

**This hook is not called during server\-side rendering.**

* **Type**

ts\`\`\`
interface ComponentOptions {
 activated?(this: ComponentPublicInstance): void
}
\`\`\`
* **See also** [Guide \- Lifecycle of Cached Instance](/guide/built-ins/keep-alive#lifecycle-of-cached-instance)

## deactivated [​](#deactivated)

Called after the component instance is removed from the DOM as part of a tree cached by [``](/api/built-in-components#keepalive).

**This hook is not called during server\-side rendering.**

* **Type**

ts\`\`\`
interface ComponentOptions {
 deactivated?(this: ComponentPublicInstance): void
}
\`\`\`
* **See also** [Guide \- Lifecycle of Cached Instance](/guide/built-ins/keep-alive#lifecycle-of-cached-instance)

## serverPrefetch  [​](#serverprefetch)

Async function to be resolved before the component instance is to be rendered on the server.

* **Type**

ts\`\`\`
interface ComponentOptions {
 serverPrefetch?(this: ComponentPublicInstance): Promise\
}
\`\`\`
* **Details**

If the hook returns a Promise, the server renderer will wait until the Promise is resolved before rendering the component.

This hook is only called during server\-side rendering can be used to perform server\-only data fetching.
* **Example**

js\`\`\`
export default {
 data() {
 return {
 data: null
 }
 },
 async serverPrefetch() {
 // component is rendered as part of the initial request
 // pre\-fetch data on server as it is faster than on the client
 this.data = await fetchOnServer(/\* ... \*/)
 },
 async mounted() {
 if (!this.data) {
 // if data is null on mount, it means the component
 // is dynamically rendered on the client. Perform a
 // client\-side fetch instead.
 this.data = await fetchOnClient(/\* ... \*/)
 }
 }
}
\`\`\`
* **See also** [Server\-Side Rendering](/guide/scaling-up/ssr)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/options-lifecycle.md)



## Props | Vue.js

[Read the full article](https://vuejs.org/guide/components/props)

# Props [​](#props)

> This page assumes you've already read the [Components Basics](/guide/essentials/component-basics). Read that first if you are new to components.

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-3-reusable-components-with-props?friend=vuejs "Free Vue.js Props Lesson")## Props Declaration [​](#props-declaration)

Vue components require explicit props declaration so that Vue knows what external props passed to the component should be treated as fallthrough attributes (which will be discussed in [its dedicated section](/guide/components/attrs)).

In SFCs using ``, props can be declared using the `defineProps()` macro:

vue\`\`\`
\
const props = defineProps(\['foo'])

console.log(props.foo)
\
\`\`\`In non\-`` components, props are declared using the [`props`](/api/options-state#props) option:

js\`\`\`
export default {
 props: \['foo'],
 setup(props) {
 // setup() receives props as the first argument.
 console.log(props.foo)
 }
}
\`\`\`Notice the argument passed to `defineProps()` is the same as the value provided to the `props` options: the same props options API is shared between the two declaration styles.

Props are declared using the [`props`](/api/options-state#props) option:

js\`\`\`
export default {
 props: \['foo'],
 created() {
 // props are exposed on \`this\`
 console.log(this.foo)
 }
}
\`\`\`In addition to declaring props using an array of strings, we can also use the object syntax:

js\`\`\`
export default {
 props: {
 title: String,
 likes: Number
 }
}
\`\`\`js\`\`\`
// in \
defineProps({
 title: String,
 likes: Number
})
\`\`\`js\`\`\`
// in non\-\
export default {
 props: {
 title: String,
 likes: Number
 }
}
\`\`\`For each property in the object declaration syntax, the key is the name of the prop, while the value should be the constructor function of the expected type.

This not only documents your component, but will also warn other developers using your component in the browser console if they pass the wrong type. We will discuss more details about [prop validation](#prop-validation) further down this page.

See also: [Typing Component Props](/guide/typescript/options-api#typing-component-props) 

If you are using TypeScript with ``, it's also possible to declare props using pure type annotations:

vue\`\`\`
\
defineProps\()
\
\`\`\`More details: [Typing Component Props](/guide/typescript/composition-api#typing-component-props) 

## Reactive Props Destructure  [​](#reactive-props-destructure)

Vue's reactivity system tracks state usage based on property access. E.g. when you access `props.foo` in a computed getter or a watcher, the `foo` prop gets tracked as a dependency.

So, given the following code:

js\`\`\`
const { foo } = defineProps(\['foo'])

watchEffect(() =\> {
 // runs only once before 3\.5
 // re\-runs when the "foo" prop changes in 3\.5\+
 console.log(foo)
})
\`\`\`In version 3\.4 and below, `foo` is an actual constant and will never change. In version 3\.5 and above, Vue's compiler automatically prepends `props.` when code in the same `` block accesses variables destructured from `defineProps`. Therefore the code above becomes equivalent to the following:

js\`\`\`
const props = defineProps(\['foo'])

watchEffect(() =\> {
 // \`foo\` transformed to \`props.foo\` by the compiler
 console.log(props.foo)
})
\`\`\`In addition, you can use JavaScript's native default value syntax to declare default values for the props. This is particularly useful when using the type\-based props declaration:

ts\`\`\`
const { foo = 'hello' } = defineProps\()
\`\`\`If you prefer to have more visual distinction between destructured props and normal variables in your IDE, Vue's VSCode extension provides a setting to enable inlay\-hints for destructured props.

### Passing Destructured Props into Functions [​](#passing-destructured-props-into-functions)

When we pass a destructured prop into a function, e.g.:

js\`\`\`
const { foo } = defineProps(\['foo'])

watch(foo, /\* ... \*/)
\`\`\`This will not work as expected because it is equivalent to `watch(props.foo, ...)` \- we are passing a value instead of a reactive data source to `watch`. In fact, Vue's compiler will catch such cases and throw a warning.

Similar to how we can watch a normal prop with `watch(() => props.foo, ...)`, we can watch a destructured prop also by wrapping it in a getter:

js\`\`\`
watch(() =\> foo, /\* ... \*/)
\`\`\`In addition, this is the recommended approach when we need to pass a destructured prop into an external function while retaining reactivity:

js\`\`\`
useComposable(() =\> foo)
\`\`\`The external function can call the getter (or normalize it with [toValue](/api/reactivity-utilities#tovalue)) when it needs to track changes of the provided prop, e.g. in a computed or watcher getter.

## Prop Passing Details [​](#prop-passing-details)

### Prop Name Casing [​](#prop-name-casing)

We declare long prop names using camelCase because this avoids having to use quotes when using them as property keys, and allows us to reference them directly in template expressions because they are valid JavaScript identifiers:

js\`\`\`
defineProps({
 greetingMessage: String
})
\`\`\`js\`\`\`
export default {
 props: {
 greetingMessage: String
 }
}
\`\`\`template\`\`\`
\{{ greetingMessage }}\
\`\`\`Technically, you can also use camelCase when passing props to a child component (except in [in\-DOM templates](/guide/essentials/component-basics#in-dom-template-parsing-caveats)). However, the convention is using kebab\-case in all cases to align with HTML attributes:

template\`\`\`
\
\`\`\`We use [PascalCase for component tags](/guide/components/registration#component-name-casing) when possible because it improves template readability by differentiating Vue components from native elements. However, there isn't as much practical benefit in using camelCase when passing props, so we choose to follow each language's conventions.

### Static vs. Dynamic Props [​](#static-vs-dynamic-props)

So far, you've seen props passed as static values, like in:

template\`\`\`
\
\`\`\`You've also seen props assigned dynamically with `v-bind` or its `:` shortcut, such as in:

template\`\`\`
\
\

\
\
\`\`\`### Passing Different Value Types [​](#passing-different-value-types)

In the two examples above, we happen to pass string values, but *any* type of value can be passed to a prop.

#### Number [​](#number)

template\`\`\`
\
\
\

\
\
\`\`\`#### Boolean [​](#boolean)

template\`\`\`
\
\

\
\
\

\
\
\`\`\`#### Array [​](#array)

template\`\`\`
\
\
\

\
\
\`\`\`#### Object [​](#object)

template\`\`\`
\
\
\

\
\
\`\`\`### Binding Multiple Properties Using an Object [​](#binding-multiple-properties-using-an-object)

If you want to pass all the properties of an object as props, you can use [`v-bind` without an argument](/guide/essentials/template-syntax#dynamically-binding-multiple-attributes) (`v-bind` instead of `:prop-name`). For example, given a `post` object:

js\`\`\`
export default {
 data() {
 return {
 post: {
 id: 1,
 title: 'My Journey with Vue'
 }
 }
 }
}
\`\`\`js\`\`\`
const post = {
 id: 1,
 title: 'My Journey with Vue'
}
\`\`\`The following template:

template\`\`\`
\
\`\`\`Will be equivalent to:

template\`\`\`
\
\`\`\`## One\-Way Data Flow [​](#one-way-data-flow)

All props form a **one\-way\-down binding** between the child property and the parent one: when the parent property updates, it will flow down to the child, but not the other way around. This prevents child components from accidentally mutating the parent's state, which can make your app's data flow harder to understand.

In addition, every time the parent component is updated, all props in the child component will be refreshed with the latest value. This means you should **not** attempt to mutate a prop inside a child component. If you do, Vue will warn you in the console:

js\`\`\`
const props = defineProps(\['foo'])

// ❌ warning, props are readonly!
props.foo = 'bar'
\`\`\`js\`\`\`
export default {
 props: \['foo'],
 created() {
 // ❌ warning, props are readonly!
 this.foo = 'bar'
 }
}
\`\`\`There are usually two cases where it's tempting to mutate a prop:

1. **The prop is used to pass in an initial value; the child component wants to use it as a local data property afterwards.** In this case, it's best to define a local data property that uses the prop as its initial value:

js\`\`\`
const props = defineProps(\['initialCounter'])

// counter only uses props.initialCounter as the initial value;
// it is disconnected from future prop updates.
const counter = ref(props.initialCounter)
\`\`\`js\`\`\`
export default {
 props: \['initialCounter'],
 data() {
 return {
 // counter only uses this.initialCounter as the initial value;
 // it is disconnected from future prop updates.
 counter: this.initialCounter
 }
 }
}
\`\`\`
2. **The prop is passed in as a raw value that needs to be transformed.** In this case, it's best to define a computed property using the prop's value:

js\`\`\`
const props = defineProps(\['size'])

// computed property that auto\-updates when the prop changes
const normalizedSize = computed(() =\> props.size.trim().toLowerCase())
\`\`\`js\`\`\`
export default {
 props: \['size'],
 computed: {
 // computed property that auto\-updates when the prop changes
 normalizedSize() {
 return this.size.trim().toLowerCase()
 }
 }
}
\`\`\`

### Mutating Object / Array Props [​](#mutating-object-array-props)

When objects and arrays are passed as props, while the child component cannot mutate the prop binding, it **will** be able to mutate the object or array's nested properties. This is because in JavaScript objects and arrays are passed by reference, and it is unreasonably expensive for Vue to prevent such mutations.

The main drawback of such mutations is that it allows the child component to affect parent state in a way that isn't obvious to the parent component, potentially making it more difficult to reason about the data flow in the future. As a best practice, you should avoid such mutations unless the parent and child are tightly coupled by design. In most cases, the child should [emit an event](/guide/components/events) to let the parent perform the mutation.

## Prop Validation [​](#prop-validation)

Components can specify requirements for their props, such as the types you've already seen. If a requirement is not met, Vue will warn you in the browser's JavaScript console. This is especially useful when developing a component that is intended to be used by others.

To specify prop validations, you can provide an object with validation requirements to the `defineProps()` macro`props` option, instead of an array of strings. For example:

js\`\`\`
defineProps({
 // Basic type check
 // (\`null\` and \`undefined\` values will allow any type)
 propA: Number,
 // Multiple possible types
 propB: \[String, Number],
 // Required string
 propC: {
 type: String,
 required: true
 },
 // Required but nullable string
 propD: {
 type: \[String, null],
 required: true
 },
 // Number with a default value
 propE: {
 type: Number,
 default: 100
 },
 // Object with a default value
 propF: {
 type: Object,
 // Object or array defaults must be returned from
 // a factory function. The function receives the raw
 // props received by the component as the argument.
 default(rawProps) {
 return { message: 'hello' }
 }
 },
 // Custom validator function
 // full props passed as 2nd argument in 3\.4\+
 propG: {
 validator(value, props) {
 // The value must match one of these strings
 return \['success', 'warning', 'danger'].includes(value)
 }
 },
 // Function with a default value
 propH: {
 type: Function,
 // Unlike object or array default, this is not a factory
 // function \- this is a function to serve as a default value
 default() {
 return 'Default function'
 }
 }
})
\`\`\`TIP

Code inside the `defineProps()` argument **cannot access other variables declared in ``**, because the entire expression is moved to an outer function scope when compiled.

js\`\`\`
export default {
 props: {
 // Basic type check
 // (\`null\` and \`undefined\` values will allow any type)
 propA: Number,
 // Multiple possible types
 propB: \[String, Number],
 // Required string
 propC: {
 type: String,
 required: true
 },
 // Required but nullable string
 propD: {
 type: \[String, null],
 required: true
 },
 // Number with a default value
 propE: {
 type: Number,
 default: 100
 },
 // Object with a default value
 propF: {
 type: Object,
 // Object or array defaults must be returned from
 // a factory function. The function receives the raw
 // props received by the component as the argument.
 default(rawProps) {
 return { message: 'hello' }
 }
 },
 // Custom validator function
 // full props passed as 2nd argument in 3\.4\+
 propG: {
 validator(value, props) {
 // The value must match one of these strings
 return \['success', 'warning', 'danger'].includes(value)
 }
 },
 // Function with a default value
 propH: {
 type: Function,
 // Unlike object or array default, this is not a factory
 // function \- this is a function to serve as a default value
 default() {
 return 'Default function'
 }
 }
 }
}
\`\`\`Additional details:

* All props are optional by default, unless `required: true` is specified.
* An absent optional prop other than `Boolean` will have `undefined` value.
* The `Boolean` absent props will be cast to `false`. You can change this by setting a `default` for it — i.e.: `default: undefined` to behave as a non\-Boolean prop.
* If a `default` value is specified, it will be used if the resolved prop value is `undefined` \- this includes both when the prop is absent, or an explicit `undefined` value is passed.

When prop validation fails, Vue will produce a console warning (if using the development build).

If using [Type\-based props declarations](/api/sfc-script-setup#type-only-props-emit-declarations) , Vue will try its best to compile the type annotations into equivalent runtime prop declarations. For example, `defineProps` will be compiled into `{ msg: { type: String, required: true }}`.

Note

Note that props are validated **before** a component instance is created, so instance properties (e.g. `data`, `computed`, etc.) will not be available inside `default` or `validator` functions.

### Runtime Type Checks [​](#runtime-type-checks)

The `type` can be one of the following native constructors:

* `String`
* `Number`
* `Boolean`
* `Array`
* `Object`
* `Date`
* `Function`
* `Symbol`
* `Error`

In addition, `type` can also be a custom class or constructor function and the assertion will be made with an `instanceof` check. For example, given the following class:

js\`\`\`
class Person {
 constructor(firstName, lastName) {
 this.firstName = firstName
 this.lastName = lastName
 }
}
\`\`\`You could use it as a prop's type:

js\`\`\`
defineProps({
 author: Person
})
\`\`\`js\`\`\`
export default {
 props: {
 author: Person
 }
}
\`\`\`Vue will use `instanceof Person` to validate whether the value of the `author` prop is indeed an instance of the `Person` class.

### Nullable Type [​](#nullable-type)

If the type is required but nullable, you can use the array syntax that includes `null`:

js\`\`\`
defineProps({
 id: {
 type: \[String, null],
 required: true
 }
})
\`\`\`js\`\`\`
export default {
 props: {
 id: {
 type: \[String, null],
 required: true
 }
 }
}
\`\`\`Note that if `type` is just `null` without using the array syntax, it will allow any type.

## Boolean Casting [​](#boolean-casting)

Props with `Boolean` type have special casting rules to mimic the behavior of native boolean attributes. Given a `` with the following declaration:

js\`\`\`
defineProps({
 disabled: Boolean
})
\`\`\`js\`\`\`
export default {
 props: {
 disabled: Boolean
 }
}
\`\`\`The component can be used like this:

template\`\`\`
\
\

\
\
\`\`\`When a prop is declared to allow multiple types, the casting rules for `Boolean` will also be applied. However, there is an edge when both `String` and `Boolean` are allowed \- the Boolean casting rule only applies if Boolean appears before String:

js\`\`\`
// disabled will be casted to true
defineProps({
 disabled: \[Boolean, Number]
})

// disabled will be casted to true
defineProps({
 disabled: \[Boolean, String]
})

// disabled will be casted to true
defineProps({
 disabled: \[Number, Boolean]
})

// disabled will be parsed as an empty string (disabled="")
defineProps({
 disabled: \[String, Boolean]
})
\`\`\`js\`\`\`
// disabled will be casted to true
export default {
 props: {
 disabled: \[Boolean, Number]
 }
}

// disabled will be casted to true
export default {
 props: {
 disabled: \[Boolean, String]
 }
}

// disabled will be casted to true
export default {
 props: {
 disabled: \[Number, Boolean]
 }
}

// disabled will be parsed as an empty string (disabled="")
export default {
 props: {
 disabled: \[String, Boolean]
 }
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/props.md)



## Built-in Special Attributes | Vue.js

[Read the full article](https://vuejs.org/api/built-in-special-attributes)

# Built\-in Special Attributes [​](#built-in-special-attributes)

## key [​](#key)

The `key` special attribute is primarily used as a hint for Vue's virtual DOM algorithm to identify vnodes when diffing the new list of nodes against the old list.

* **Expects:** `number | string | symbol`
* **Details**

Without keys, Vue uses an algorithm that minimizes element movement and tries to patch/reuse elements of the same type in\-place as much as possible. With keys, it will reorder elements based on the order change of keys, and elements with keys that are no longer present will always be removed / destroyed.

Children of the same common parent must have **unique keys**. Duplicate keys will cause render errors.

The most common use case is combined with `v-for`:

template\`\`\`
\
 \...\
\
\`\`\`It can also be used to force replacement of an element/component instead of reusing it. This can be useful when you want to:

	+ Properly trigger lifecycle hooks of a component
	+ Trigger transitionsFor example:

template\`\`\`
\
 \{{ text }}\
\
\`\`\`When `text` changes, the `` will always be replaced instead of patched, so a transition will be triggered.
* **See also** [Guide \- List Rendering \- Maintaining State with `key`](/guide/essentials/list#maintaining-state-with-key)

## ref [​](#ref)

Denotes a [template ref](/guide/essentials/template-refs).

* **Expects:** `string | Function`
* **Details**

`ref` is used to register a reference to an element or a child component.

In Options API, the reference will be registered under the component's `this.$refs` object:

template\`\`\`
\
\hello\
\`\`\`In Composition API, the reference will be stored in a ref with matching name:

vue\`\`\`
\
import { useTemplateRef } from 'vue'

const pRef = useTemplateRef('p')
\

\
 \hello\
\
\`\`\`If used on a plain DOM element, the reference will be that element; if used on a child component, the reference will be the child component instance.

Alternatively `ref` can accept a function value which provides full control over where to store the reference:

template\`\`\`
\ child = el" /\>
\`\`\`An important note about the ref registration timing: because the refs themselves are created as a result of the render function, you must wait until the component is mounted before accessing them.

`this.$refs` is also non\-reactive, therefore you should not attempt to use it in templates for data\-binding.
* **See also**

	+ [Guide \- Template Refs](/guide/essentials/template-refs)
	+ [Guide \- Typing Template Refs](/guide/typescript/composition-api#typing-template-refs)
	+ [Guide \- Typing Component Template Refs](/guide/typescript/composition-api#typing-component-template-refs)

## is [​](#is)

Used for binding [dynamic components](/guide/essentials/component-basics#dynamic-components).

* **Expects:** `string | Component`
* **Usage on native elements**

	+ Only supported in 3\.1\+When the `is` attribute is used on a native HTML element, it will be interpreted as a [Customized built\-in element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-customized-builtin-example), which is a native web platform feature.

There is, however, a use case where you may need Vue to replace a native element with a Vue component, as explained in [in\-DOM Template Parsing Caveats](/guide/essentials/component-basics#in-dom-template-parsing-caveats). You can prefix the value of the `is` attribute with `vue:` so that Vue will render the element as a Vue component instead:

template\`\`\`
\
 \\
\
\`\`\`
* **See also**

	+ [Built\-in Special Element \- ``](/api/built-in-special-elements#component)
	+ [Dynamic Components](/guide/essentials/component-basics#dynamic-components)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/built-in-special-attributes.md)



## Composition API: Helpers | Vue.js

[Read the full article](https://vuejs.org/api/composition-api-helpers)

# Composition API: Helpers [​](#composition-api-helpers)

## useAttrs() [​](#useattrs)

Returns the `attrs` object from the [Setup Context](/api/composition-api-setup#setup-context), which includes the [fallthrough attributes](/guide/components/attrs#fallthrough-attributes) of the current component. This is intended to be used in `` where the setup context object is not available.

* **Type**

ts\`\`\`
function useAttrs(): Record\
\`\`\`

## useSlots() [​](#useslots)

Returns the `slots` object from the [Setup Context](/api/composition-api-setup#setup-context), which includes parent passed slots as callable functions that return Virtual DOM nodes. This is intended to be used in `` where the setup context object is not available.

If using TypeScript, [`defineSlots()`](/api/sfc-script-setup#defineslots) should be preferred instead.

* **Type**

ts\`\`\`
function useSlots(): Record\ VNode\[]\>
\`\`\`

## useModel() [​](#usemodel)

This is the underlying helper that powers [`defineModel()`](/api/sfc-script-setup#definemodel). If using ``, `defineModel()` should be preferred instead.

* Only available in 3\.4\+
* **Type**

ts\`\`\`
function useModel(
 props: Record\,
 key: string,
 options?: DefineModelOptions
): ModelRef

type DefineModelOptions\ = {
 get?: (v: T) =\> any
 set?: (v: T) =\> any
}

type ModelRef\ = Ref\ \& \[
 ModelRef\,
 Record\
]
\`\`\`
* **Example**

js\`\`\`
export default {
 props: \['count'],
 emits: \['update:count'],
 setup(props) {
 const msg = useModel(props, 'count')
 msg.value = 1
 }
}
\`\`\`
* **Details**

`useModel()` can be used in non\-SFC components, e.g. when using raw `setup()` function. It expects the `props` object as the first argument, and the model name as the second argument. The optional third argument can be used to declare custom getter and setter for the resulting model ref. Note that unlike `defineModel()`, you are responsible for declaring the props and emits yourself.

## useTemplateRef()  [​](#usetemplateref)

Returns a shallow ref whose value will be synced with the template element or component with a matching ref attribute.

* **Type**

ts\`\`\`
function useTemplateRef\(key: string): Readonly\\>
\`\`\`
* **Example**

vue\`\`\`
\
import { useTemplateRef, onMounted } from 'vue'

const inputRef = useTemplateRef('input')

onMounted(() =\> {
 inputRef.value.focus()
})
\

\
 \
\
\`\`\`
* **See also**

	+ [Guide \- Template Refs](/guide/essentials/template-refs)
	+ [Guide \- Typing Template Refs](/guide/typescript/composition-api#typing-template-refs)
	+ [Guide \- Typing Component Template Refs](/guide/typescript/composition-api#typing-component-template-refs)

## useId()  [​](#useid)

Used to generate unique\-per\-application IDs for accessibility attributes or form elements.

* **Type**

ts\`\`\`
function useId(): string
\`\`\`
* **Example**

vue\`\`\`
\
import { useId } from 'vue'

const id = useId()
\

\
 \
 \Name:\
 \
 \
\
\`\`\`
* **Details**

IDs generated by `useId()` are unique\-per\-application. It can be used to generate IDs for form elements and accessibility attributes. Multiple calls in the same component will generate different IDs; multiple instances of the same component calling `useId()` will also have different IDs.

IDs generated by `useId()` are also guaranteed to be stable across the server and client renders, so they can be used in SSR applications without leading to hydration mismatches.

If you have more than one Vue application instance of the same page, you can avoid ID conflicts by giving each app an ID prefix via [`app.config.idPrefix`](/api/application#app-config-idprefix).
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/composition-api-helpers.md)



## Ways of Using Vue | Vue.js

[Read the full article](https://vuejs.org/guide/extras/ways-of-using-vue)

# Ways of Using Vue [​](#ways-of-using-vue)

We believe there is no "one size fits all" story for the web. This is why Vue is designed to be flexible and incrementally adoptable. Depending on your use case, Vue can be used in different ways to strike the optimal balance between stack complexity, developer experience and end performance.

## Standalone Script [​](#standalone-script)

Vue can be used as a standalone script file \- no build step required! If you have a backend framework already rendering most of the HTML, or your frontend logic isn't complex enough to justify a build step, this is the easiest way to integrate Vue into your stack. You can think of Vue as a more declarative replacement of jQuery in such cases.

Vue also provides an alternative distribution called [petite\-vue](https://github.com/vuejs/petite-vue) that is specifically optimized for progressively enhancing existing HTML. It has a smaller feature set, but is extremely lightweight and uses an implementation that is more efficient in no\-build\-step scenarios.

## Embedded Web Components [​](#embedded-web-components)

You can use Vue to [build standard Web Components](/guide/extras/web-components) that can be embedded in any HTML page, regardless of how they are rendered. This option allows you to leverage Vue in a completely consumer\-agnostic fashion: the resulting web components can be embedded in legacy applications, static HTML, or even applications built with other frameworks.

## Single\-Page Application (SPA) [​](#single-page-application-spa)

Some applications require rich interactivity, deep session depth, and non\-trivial stateful logic on the frontend. The best way to build such applications is to use an architecture where Vue not only controls the entire page, but also handles data updates and navigation without having to reload the page. This type of application is typically referred to as a Single\-Page Application (SPA).

Vue provides core libraries and [comprehensive tooling support](/guide/scaling-up/tooling) with amazing developer experience for building modern SPAs, including:

* Client\-side router
* Blazing fast build tool chain
* IDE support
* Browser devtools
* TypeScript integrations
* Testing utilities

SPAs typically require the backend to expose API endpoints \- but you can also pair Vue with solutions like [Inertia.js](https://inertiajs.com) to get the SPA benefits while retaining a server\-centric development model.

## Fullstack / SSR [​](#fullstack-ssr)

Pure client\-side SPAs are problematic when the app is sensitive to SEO and time\-to\-content. This is because the browser will receive a largely empty HTML page, and has to wait until the JavaScript is loaded before rendering anything.

Vue provides first\-class APIs to "render" a Vue app into HTML strings on the server. This allows the server to send back already\-rendered HTML, allowing end users to see the content immediately while the JavaScript is being downloaded. Vue will then "hydrate" the application on the client side to make it interactive. This is called [Server\-Side Rendering (SSR)](/guide/scaling-up/ssr) and it greatly improves Core Web Vital metrics such as [Largest Contentful Paint (LCP)](https://web.dev/lcp/).

There are higher\-level Vue\-based frameworks built on top of this paradigm, such as [Nuxt](https://nuxt.com/), which allow you to develop a fullstack application using Vue and JavaScript.

## JAMStack / SSG [​](#jamstack-ssg)

Server\-side rendering can be done ahead of time if the required data is static. This means we can pre\-render an entire application into HTML and serve them as static files. This improves site performance and makes deployment a lot simpler since we no longer need to dynamically render pages on each request. Vue can still hydrate such applications to provide rich interactivity on the client. This technique is commonly referred to as Static\-Site Generation (SSG), also known as [JAMStack](https://jamstack.org/what-is-jamstack/).

There are two flavors of SSG: single\-page and multi\-page. Both flavors pre\-render the site into static HTML, the difference is that:

* After the initial page load, a single\-page SSG "hydrates" the page into an SPA. This requires more upfront JS payload and hydration cost, but subsequent navigations will be faster, since it only needs to partially update the page content instead of reloading the entire page.
* A multi\-page SSG loads a new page on every navigation. The upside is that it can ship minimal JS \- or no JS at all if the page requires no interaction! Some multi\-page SSG frameworks such as [Astro](https://astro.build/) also support "partial hydration" \- which allows you to use Vue components to create interactive "islands" inside static HTML.

Single\-page SSGs are better suited if you expect non\-trivial interactivity, deep session lengths, or persisted elements / state across navigations. Otherwise, multi\-page SSG would be the better choice.

The Vue team also maintains a static\-site generator called [VitePress](https://vitepress.dev/), which powers this website you are reading right now! VitePress supports both flavors of SSG. [Nuxt](https://nuxt.com/) also supports SSG. You can even mix SSR and SSG for different routes in the same Nuxt app.

## Beyond the Web [​](#beyond-the-web)

Although Vue is primarily designed for building web applications, it is by no means limited to just the browser. You can:

* Build desktop apps with [Electron](https://www.electronjs.org/)
* Build mobile apps with [Ionic Vue](https://ionicframework.com/docs/vue/overview)
* Build desktop and mobile apps from the same codebase with [Quasar](https://quasar.dev/) or [Tauri](https://tauri.app)
* Build 3D WebGL experiences with [TresJS](https://tresjs.org/)
* Use Vue's [Custom Renderer API](/api/custom-renderer) to build custom renderers, like those for [the terminal](https://github.com/vue-terminal/vue-termui)!
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/ways-of-using-vue.md)



## SFC Syntax Specification | Vue.js

[Read the full article](https://vuejs.org/api/sfc-spec)

# SFC Syntax Specification [​](#sfc-syntax-specification)

## Overview [​](#overview)

A Vue Single\-File Component (SFC), conventionally using the `*.vue` file extension, is a custom file format that uses an HTML\-like syntax to describe a Vue component. A Vue SFC is syntactically compatible with HTML.

Each `*.vue` file consists of three types of top\-level language blocks: ``, ``, and ``, and optionally additional custom blocks:

vue\`\`\`
\
 \{{ msg }}\
\

\
export default {
 data() {
 return {
 msg: 'Hello world!'
 }
 }
}
\

\
.example {
 color: red;
}
\

\
 This could be e.g. documentation for the component.
\
\`\`\`## Language Blocks [​](#language-blocks)

### `` [​](#template)

* Each `*.vue` file can contain at most one top\-level `` block.
* Contents will be extracted and passed on to `@vue/compiler-dom`, pre\-compiled into JavaScript render functions, and attached to the exported component as its `render` option.

### `` [​](#script)

* Each `*.vue` file can contain at most one `` block (excluding [``](/api/sfc-script-setup)).
* The script is executed as an ES Module.
* The **default export** should be a Vue component options object, either as a plain object or as the return value of [defineComponent](/api/general#definecomponent).

### `` [​](#script-setup)

* Each `*.vue` file can contain at most one `` block (excluding normal ``).
* The script is pre\-processed and used as the component's `setup()` function, which means it will be executed **for each instance of the component**. Top\-level bindings in `` are automatically exposed to the template. For more details, see [dedicated documentation on ``](/api/sfc-script-setup).

### `` [​](#style)

* A single `*.vue` file can contain multiple `` tags.
* A `` tag can have `scoped` or `module` attributes (see [SFC Style Features](/api/sfc-css-features) for more details) to help encapsulate the styles to the current component. Multiple `` tags with different encapsulation modes can be mixed in the same component.

### Custom Blocks [​](#custom-blocks)

Additional custom blocks can be included in a `*.vue` file for any project\-specific needs, for example a `` block. Some real\-world examples of custom blocks include:

* [Gridsome: ``](https://gridsome.org/docs/querying-data/)
* [vite\-plugin\-vue\-gql: ``](https://github.com/wheatjs/vite-plugin-vue-gql)
* [vue\-i18n: ``](https://github.com/intlify/bundle-tools/tree/main/packages/unplugin-vue-i18n#i18n-custom-block)

Handling of Custom Blocks will depend on tooling \- if you want to build your own custom block integrations, see the [SFC custom block integrations tooling section](/guide/scaling-up/tooling#sfc-custom-block-integrations) for more details.

## Automatic Name Inference [​](#automatic-name-inference)

An SFC automatically infers the component's name from its **filename** in the following cases:

* Dev warning formatting
* DevTools inspection
* Recursive self\-reference, e.g. a file named `FooBar.vue` can refer to itself as `` in its template. This has lower priority than explicitly registered/imported components.

## Pre\-Processors [​](#pre-processors)

Blocks can declare pre\-processor languages using the `lang` attribute. The most common case is using TypeScript for the `` block:

template\`\`\`
\
 // use TypeScript
\
\`\`\``lang` can be applied to any block \- for example we can use `` with [Sass](https://sass-lang.com/) and `` with [Pug](https://pugjs.org/api/getting-started.html):

template\`\`\`
\
p {{ msg }}
\

\
 $primary\-color: \#333;
 body {
 color: $primary\-color;
 }
\
\`\`\`Note that integration with various pre\-processors may differ by toolchain. Check out the respective documentation for examples:

* [Vite](https://vitejs.dev/guide/features.html#css-pre-processors)
* [Vue CLI](https://cli.vuejs.org/guide/css.html#pre-processors)
* [webpack \+ vue\-loader](https://vue-loader.vuejs.org/guide/pre-processors.html#using-pre-processors)

## `src` Imports [​](#src-imports)

If you prefer splitting up your `*.vue` components into multiple files, you can use the `src` attribute to import an external file for a language block:

vue\`\`\`
\\
\\
\\
\`\`\`Beware that `src` imports follow the same path resolution rules as webpack module requests, which means:

* Relative paths need to start with `./`
* You can import resources from npm dependencies:

vue\`\`\`
\
\
\`\`\``src` imports also work with custom blocks, e.g.:

vue\`\`\`
\
\
\`\`\`Note

While using aliases in `src`, don't start with `~`, anything after it is interpreted as a module request. This means you can reference assets inside node modules:

vue\`\`\`
\
\`\`\`## Comments [​](#comments)

Inside each block you shall use the comment syntax of the language being used (HTML, CSS, JavaScript, Pug, etc.). For top\-level comments, use HTML comment syntax: ``

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/sfc-spec.md)



## Composables | Vue.js

[Read the full article](https://vuejs.org/guide/reusability/composables)

# Composables [​](#composables)

TIP

This section assumes basic knowledge of Composition API. If you have been learning Vue with Options API only, you can set the API Preference to Composition API (using the toggle at the top of the left sidebar) and re\-read the [Reactivity Fundamentals](/guide/essentials/reactivity-fundamentals) and [Lifecycle Hooks](/guide/essentials/lifecycle) chapters.

## What is a "Composable"? [​](#what-is-a-composable)

In the context of Vue applications, a "composable" is a function that leverages Vue's Composition API to encapsulate and reuse **stateful logic**.

When building frontend applications, we often need to reuse logic for common tasks. For example, we may need to format dates in many places, so we extract a reusable function for that. This formatter function encapsulates **stateless logic**: it takes some input and immediately returns expected output. There are many libraries out there for reusing stateless logic \- for example [lodash](https://lodash.com/) and [date\-fns](https://date-fns.org/), which you may have heard of.

By contrast, stateful logic involves managing state that changes over time. A simple example would be tracking the current position of the mouse on a page. In real\-world scenarios, it could also be more complex logic such as touch gestures or connection status to a database.

## Mouse Tracker Example [​](#mouse-tracker-example)

If we were to implement the mouse tracking functionality using the Composition API directly inside a component, it would look like this:

vue\`\`\`
\
import { ref, onMounted, onUnmounted } from 'vue'

const x = ref(0\)
const y = ref(0\)

function update(event) {
 x.value = event.pageX
 y.value = event.pageY
}

onMounted(() =\> window.addEventListener('mousemove', update))
onUnmounted(() =\> window.removeEventListener('mousemove', update))
\

\Mouse position is at: {{ x }}, {{ y }}\
\`\`\`But what if we want to reuse the same logic in multiple components? We can extract the logic into an external file, as a composable function:

js\`\`\`
// mouse.js
import { ref, onMounted, onUnmounted } from 'vue'

// by convention, composable function names start with "use"
export function useMouse() {
 // state encapsulated and managed by the composable
 const x = ref(0\)
 const y = ref(0\)

 // a composable can update its managed state over time.
 function update(event) {
 x.value = event.pageX
 y.value = event.pageY
 }

 // a composable can also hook into its owner component's
 // lifecycle to setup and teardown side effects.
 onMounted(() =\> window.addEventListener('mousemove', update))
 onUnmounted(() =\> window.removeEventListener('mousemove', update))

 // expose managed state as return value
 return { x, y }
}
\`\`\`And this is how it can be used in components:

vue\`\`\`
\
import { useMouse } from './mouse.js'

const { x, y } = useMouse()
\

\Mouse position is at: {{ x }}, {{ y }}\
\`\`\` Mouse position is at: 0, 0[Try it in the Playground](https://play.vuejs.org/#eNqNkj1rwzAQhv/KocUOGKVzSAIdurVjoQUvJj4XlfgkJNmxMfrvPcmJkkKHLrbu69H7SlrEszFyHFDsxN6drDIeHPrBHGtSvdHWwwKDwzfNHwjQWd1DIbd9jOW3K2qq6aTJxb6pgpl7Dnmg3NS0365YBnLgsTfnxiNHACvUaKe80gTKQeN3sDAIQqjignEhIvKYqMRta1acFVrsKtDEQPLYxuU7cV8Msmg2mdTilIa6gU5p27tYWKKq1c3ENphaPrGFW25+yMXsHWFaFlfiiOSvFIBJjs15QJ5JeWmaL/xYS/Mfpc9YYrPxl52ULOpwhIuiVl9k07Yvsf9VOY+EtizSWfR6xKK6itgkvQ/+fyNs6v4XJXIsPwVL+WprCiL8AEUxw5s=)

As we can see, the core logic remains identical \- all we had to do was move it into an external function and return the state that should be exposed. Just like inside a component, you can use the full range of [Composition API functions](/api/#composition-api) in composables. The same `useMouse()` functionality can now be used in any component.

The cooler part about composables though, is that you can also nest them: one composable function can call one or more other composable functions. This enables us to compose complex logic using small, isolated units, similar to how we compose an entire application using components. In fact, this is why we decided to call the collection of APIs that make this pattern possible Composition API.

For example, we can extract the logic of adding and removing a DOM event listener into its own composable:

js\`\`\`
// event.js
import { onMounted, onUnmounted } from 'vue'

export function useEventListener(target, event, callback) {
 // if you want, you can also make this
 // support selector strings as target
 onMounted(() =\> target.addEventListener(event, callback))
 onUnmounted(() =\> target.removeEventListener(event, callback))
}
\`\`\`And now our `useMouse()` composable can be simplified to:

js\`\`\`
// mouse.js
import { ref } from 'vue'
import { useEventListener } from './event'

export function useMouse() {
 const x = ref(0\)
 const y = ref(0\)

 useEventListener(window, 'mousemove', (event) =\> {
 x.value = event.pageX
 y.value = event.pageY
 })

 return { x, y }
}
\`\`\`TIP

Each component instance calling `useMouse()` will create its own copies of `x` and `y` state so they won't interfere with one another. If you want to manage shared state between components, read the [State Management](/guide/scaling-up/state-management) chapter.

## Async State Example [​](#async-state-example)

The `useMouse()` composable doesn't take any arguments, so let's take a look at another example that makes use of one. When doing async data fetching, we often need to handle different states: loading, success, and error:

vue\`\`\`
\
import { ref } from 'vue'

const data = ref(null)
const error = ref(null)

fetch('...')
 .then((res) =\> res.json())
 .then((json) =\> (data.value = json))
 .catch((err) =\> (error.value = err))
\

\
 \Oops! Error encountered: {{ error.message }}\
 \
 Data loaded:
 \{{ data }}\
 \
 \Loading...\
\
\`\`\`It would be tedious to have to repeat this pattern in every component that needs to fetch data. Let's extract it into a composable:

js\`\`\`
// fetch.js
import { ref } from 'vue'

export function useFetch(url) {
 const data = ref(null)
 const error = ref(null)

 fetch(url)
 .then((res) =\> res.json())
 .then((json) =\> (data.value = json))
 .catch((err) =\> (error.value = err))

 return { data, error }
}
\`\`\`Now in our component we can just do:

vue\`\`\`
\
import { useFetch } from './fetch.js'

const { data, error } = useFetch('...')
\
\`\`\`### Accepting Reactive State [​](#accepting-reactive-state)

`useFetch()` takes a static URL string as input \- so it performs the fetch only once and is then done. What if we want it to re\-fetch whenever the URL changes? In order to achieve this, we need to pass reactive state into the composable function, and let the composable create watchers that perform actions using the passed state.

For example, `useFetch()` should be able to accept a ref:

js\`\`\`
const url = ref('/initial\-url')

const { data, error } = useFetch(url)

// this should trigger a re\-fetch
url.value = '/new\-url'
\`\`\`Or, accept a [getter function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description):

js\`\`\`
// re\-fetch when props.id changes
const { data, error } = useFetch(() =\> \`/posts/${props.id}\`)
\`\`\`We can refactor our existing implementation with the [`watchEffect()`](/api/reactivity-core#watcheffect) and [`toValue()`](/api/reactivity-utilities#tovalue) APIs:

js\`\`\`
// fetch.js
import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
 const data = ref(null)
 const error = ref(null)

 const fetchData = () =\> {
 // reset state before fetching..
 data.value = null
 error.value = null

 fetch(toValue(url))
 .then((res) =\> res.json())
 .then((json) =\> (data.value = json))
 .catch((err) =\> (error.value = err))
 }

 watchEffect(() =\> {
 fetchData()
 })

 return { data, error }
}
\`\`\``toValue()` is an API added in 3\.3\. It is designed to normalize refs or getters into values. If the argument is a ref, it returns the ref's value; if the argument is a function, it will call the function and return its return value. Otherwise, it returns the argument as\-is. It works similarly to [`unref()`](/api/reactivity-utilities#unref), but with special treatment for functions.

Notice that `toValue(url)` is called **inside** the `watchEffect` callback. This ensures that any reactive dependencies accessed during the `toValue()` normalization are tracked by the watcher.

This version of `useFetch()` now accepts static URL strings, refs, and getters, making it much more flexible. The watch effect will run immediately, and will track any dependencies accessed during `toValue(url)`. If no dependencies are tracked (e.g. url is already a string), the effect runs only once; otherwise, it will re\-run whenever a tracked dependency changes.

Here's [the updated version of `useFetch()`](https://play.vuejs.org/#eNp9Vdtu20YQ/ZUpUUA0qpAOjL4YktCbC7Rom8BN8sSHrMihtfZql9iLZEHgv2dml6SpxMiDIWkuZ+acmR2fs1+7rjgEzG6zlaut7Dw49KHbVFruO2M9nMFiu4Ta7LvgsYEeWmv2sKCkxSwoOPwTfb2b/EU5mopHR5GVro12HrbC4UerYA2Lnfeduy3LR2d0p0SNO6MatIU/dbI2DRZUtPSmMa4kgJQuG8qkjvLF28XVaAwRb2wxz69gvZkK/UQ5xUGogBQ/ZpyhEV4sAa01lnpeTwRyApsFWvT2RO6Eea40THBMgfq6NLwlS1/pVZnUJB3ph8c98fNIvwD+MaKBzkQut2xYbYP3RsPhTWvsusokSA0/Vxn8UitZP7GFSX/+8Sz7z1W2OZ9BQt+vypQXS1R+1cgDQciW4iMrimR0wu8270znfoC7SBaJWdAeLTa3QFgxuNijc+IBIy5PPyYOjU19RDEI954/Z/UptKTy6VvqA5XD1AwLTTl/0Aco4s5lV51F5sG+VJJ+v4qxYbmkfiiKYvSvyknPbJnNtoyW+HJpj4Icd22LtV+CN5/ikC4XuNL4HFPaoGsvie3FIqSJp1WIzabl00HxkoyetEVfufhv1kAu3EnX8z0CKEtKofcGzhMb2CItAELL1SPlFMV1pwVj+GROc/vWPoc26oDgdxhfSArlLnbWaBOcOoEzIP3CgbeifqLXLRyICaDBDnVD+3KC7emCSyQ4sifspOx61Hh4Qy/d8BsaOEdkYb1sZS2FoiJKnIC6FbqhsaTVZfk8gDgK6cHLPZowFGUzAQTNWl/BUSrFbzRYHXmSdeAp28RMsI0fyFDaUJg9Spd0SbERZcvZDBRleCPdQMCPh8ARwdRRnBCTjGz5WkT0i0GlSMqixTR6VKyHmmWEHIfV+naSOETyRx8vEYwMv7pa8dJU+hU9Kz2t86ReqjcgaTzCe3oGpEOeD4uyJOcjTXe+obScHwaAi82lo9dC/q/wuyINjrwbuC5uZrS4WAQeyTN9ftOXIVwy537iecoX92kR4q/F1UvqIMsSbq6vo5XF6ekCeEcTauVDFJpuQESvMv53IBXadx3r4KqMrt0w0kwoZY5/R5u3AZejvd5h/fSK/dE9s63K3vN7tQesssnnhX1An9x3//+Hz/R9cu5NExRFf8d5zyIF7jGF/RZ0Q23P4mK3f8XLRmfhg7t79qjdSIobjXLE+Cqju/b7d6i/tHtT3MQ8VrH/Ahstp5A=), with an artificial delay and randomized error for demo purposes.

## Conventions and Best Practices [​](#conventions-and-best-practices)

### Naming [​](#naming)

It is a convention to name composable functions with camelCase names that start with "use".

### Input Arguments [​](#input-arguments)

A composable can accept ref or getter arguments even if it doesn't rely on them for reactivity. If you are writing a composable that may be used by other developers, it's a good idea to handle the case of input arguments being refs or getters instead of raw values. The [`toValue()`](/api/reactivity-utilities#tovalue) utility function will come in handy for this purpose:

js\`\`\`
import { toValue } from 'vue'

function useFeature(maybeRefOrGetter) {
 // If maybeRefOrGetter is a ref or a getter,
 // its normalized value will be returned.
 // Otherwise, it is returned as\-is.
 const value = toValue(maybeRefOrGetter)
}
\`\`\`If your composable creates reactive effects when the input is a ref or a getter, make sure to either explicitly watch the ref / getter with `watch()`, or call `toValue()` inside a `watchEffect()` so that it is properly tracked.

The [useFetch() implementation discussed earlier](#accepting-reactive-state) provides a concrete example of a composable that accepts refs, getters and plain values as input argument.

### Return Values [​](#return-values)

You have probably noticed that we have been exclusively using `ref()` instead of `reactive()` in composables. The recommended convention is for composables to always return a plain, non\-reactive object containing multiple refs. This allows it to be destructured in components while retaining reactivity:

js\`\`\`
// x and y are refs
const { x, y } = useMouse()
\`\`\`Returning a reactive object from a composable will cause such destructures to lose the reactivity connection to the state inside the composable, while the refs will retain that connection.

If you prefer to use returned state from composables as object properties, you can wrap the returned object with `reactive()` so that the refs are unwrapped. For example:

js\`\`\`
const mouse = reactive(useMouse())
// mouse.x is linked to original ref
console.log(mouse.x)
\`\`\`template\`\`\`
Mouse position is at: {{ mouse.x }}, {{ mouse.y }}
\`\`\`### Side Effects [​](#side-effects)

It is OK to perform side effects (e.g. adding DOM event listeners or fetching data) in composables, but pay attention to the following rules:

* If you are working on an application that uses [Server\-Side Rendering](/guide/scaling-up/ssr) (SSR), make sure to perform DOM\-specific side effects in post\-mount lifecycle hooks, e.g. `onMounted()`. These hooks are only called in the browser, so you can be sure that code inside them has access to the DOM.
* Remember to clean up side effects in `onUnmounted()`. For example, if a composable sets up a DOM event listener, it should remove that listener in `onUnmounted()` as we have seen in the `useMouse()` example. It can be a good idea to use a composable that automatically does this for you, like the `useEventListener()` example.

### Usage Restrictions [​](#usage-restrictions)

Composables should only be called in `` or the `setup()` hook. They should also be called **synchronously** in these contexts. In some cases, you can also call them in lifecycle hooks like `onMounted()`.

These restrictions are important because these are the contexts where Vue is able to determine the current active component instance. Access to an active component instance is necessary so that:

1. Lifecycle hooks can be registered to it.
2. Computed properties and watchers can be linked to it, so that they can be disposed when the instance is unmounted to prevent memory leaks.

TIP

`` is the only place where you can call composables **after** using `await`. The compiler automatically restores the active instance context for you after the async operation.

## Extracting Composables for Code Organization [​](#extracting-composables-for-code-organization)

Composables can be extracted not only for reuse, but also for code organization. As the complexity of your components grow, you may end up with components that are too large to navigate and reason about. Composition API gives you the full flexibility to organize your component code into smaller functions based on logical concerns:

vue\`\`\`
\
import { useFeatureA } from './featureA.js'
import { useFeatureB } from './featureB.js'
import { useFeatureC } from './featureC.js'

const { foo, bar } = useFeatureA()
const { baz } = useFeatureB(foo)
const { qux } = useFeatureC(baz)
\
\`\`\`To some extent, you can think of these extracted composables as component\-scoped services that can talk to one another.

## Using Composables in Options API [​](#using-composables-in-options-api)

If you are using Options API, composables must be called inside `setup()`, and the returned bindings must be returned from `setup()` so that they are exposed to `this` and the template:

js\`\`\`
import { useMouse } from './mouse.js'
import { useFetch } from './fetch.js'

export default {
 setup() {
 const { x, y } = useMouse()
 const { data, error } = useFetch('...')
 return { x, y, data, error }
 },
 mounted() {
 // setup() exposed properties can be accessed on \`this\`
 console.log(this.x)
 }
 // ...other options
}
\`\`\`## Comparisons with Other Techniques [​](#comparisons-with-other-techniques)

### vs. Mixins [​](#vs-mixins)

Users coming from Vue 2 may be familiar with the [mixins](/api/options-composition#mixins) option, which also allows us to extract component logic into reusable units. There are three primary drawbacks to mixins:

1. **Unclear source of properties**: when using many mixins, it becomes unclear which instance property is injected by which mixin, making it difficult to trace the implementation and understand the component's behavior. This is also why we recommend using the refs \+ destructure pattern for composables: it makes the property source clear in consuming components.
2. **Namespace collisions**: multiple mixins from different authors can potentially register the same property keys, causing namespace collisions. With composables, you can rename the destructured variables if there are conflicting keys from different composables.
3. **Implicit cross\-mixin communication**: multiple mixins that need to interact with one another have to rely on shared property keys, making them implicitly coupled. With composables, values returned from one composable can be passed into another as arguments, just like normal functions.

For the above reasons, we no longer recommend using mixins in Vue 3\. The feature is kept only for migration and familiarity reasons.

### vs. Renderless Components [​](#vs-renderless-components)

In the component slots chapter, we discussed the [Renderless Component](/guide/components/slots#renderless-components) pattern based on scoped slots. We even implemented the same mouse tracking demo using renderless components.

The main advantage of composables over renderless components is that composables do not incur the extra component instance overhead. When used across an entire application, the amount of extra component instances created by the renderless component pattern can become a noticeable performance overhead.

The recommendation is to use composables when reusing pure logic, and use components when reusing both logic and visual layout.

### vs. React Hooks [​](#vs-react-hooks)

If you have experience with React, you may notice that this looks very similar to custom React hooks. Composition API was in part inspired by React hooks, and Vue composables are indeed similar to React hooks in terms of logic composition capabilities. However, Vue composables are based on Vue's fine\-grained reactivity system, which is fundamentally different from React hooks' execution model. This is discussed in more detail in the [Composition API FAQ](/guide/extras/composition-api-faq#comparison-with-react-hooks).

## Further Reading [​](#further-reading)

* [Reactivity In Depth](/guide/extras/reactivity-in-depth): for a low\-level understanding of how Vue's reactivity system works.
* [State Management](/guide/scaling-up/state-management): for patterns of managing state shared by multiple components.
* [Testing Composables](/guide/scaling-up/testing#testing-composables): tips on unit testing composables.
* [VueUse](https://vueuse.org/): an ever\-growing collection of Vue composables. The source code is also a great learning resource.
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/reusability/composables.md)



## Components Basics | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/component-basics)

# Components Basics [​](#components-basics)

Components allow us to split the UI into independent and reusable pieces, and think about each piece in isolation. It's common for an app to be organized into a tree of nested components:



This is very similar to how we nest native HTML elements, but Vue implements its own component model that allows us to encapsulate custom content and logic in each component. Vue also plays nicely with native Web Components. If you are curious about the relationship between Vue Components and native Web Components, [read more here](/guide/extras/web-components).

## Defining a Component [​](#defining-a-component)

When using a build step, we typically define each Vue component in a dedicated file using the `.vue` extension \- known as a [Single\-File Component](/guide/scaling-up/sfc) (SFC for short):

vue\`\`\`
\
export default {
 data() {
 return {
 count: 0
 }
 }
}
\

\
 \You clicked me {{ count }} times.\
\
\`\`\`vue\`\`\`
\
import { ref } from 'vue'

const count = ref(0\)
\

\
 \You clicked me {{ count }} times.\
\
\`\`\`When not using a build step, a Vue component can be defined as a plain JavaScript object containing Vue\-specific options:

js\`\`\`
export default {
 data() {
 return {
 count: 0
 }
 },
 template: \`
 \
 You clicked me {{ count }} times.
 \\`
}
\`\`\`js\`\`\`
import { ref } from 'vue'

export default {
 setup() {
 const count = ref(0\)
 return { count }
 },
 template: \`
 \
 You clicked me {{ count }} times.
 \\`
 // Can also target an in\-DOM template:
 // template: '\#my\-template\-element'
}
\`\`\`The template is inlined as a JavaScript string here, which Vue will compile on the fly. You can also use an ID selector pointing to an element (usually native `` elements) \- Vue will use its content as the template source.

The example above defines a single component and exports it as the default export of a `.js` file, but you can use named exports to export multiple components from the same file.

## Using a Component [​](#using-a-component)

TIP

We will be using SFC syntax for the rest of this guide \- the concepts around components are the same regardless of whether you are using a build step or not. The [Examples](/examples/) section shows component usage in both scenarios.

To use a child component, we need to import it in the parent component. Assuming we placed our counter component inside a file called `ButtonCounter.vue`, the component will be exposed as the file's default export:

vue\`\`\`
\
import ButtonCounter from './ButtonCounter.vue'

export default {
 components: {
 ButtonCounter
 }
}
\

\
 \Here is a child component!\
 \
\
\`\`\`To expose the imported component to our template, we need to [register](/guide/components/registration) it with the `components` option. The component will then be available as a tag using the key it is registered under.

vue\`\`\`
\
import ButtonCounter from './ButtonCounter.vue'
\

\
 \Here is a child component!\
 \
\
\`\`\`With ``, imported components are automatically made available to the template.

It's also possible to globally register a component, making it available to all components in a given app without having to import it. The pros and cons of global vs. local registration is discussed in the dedicated [Component Registration](/guide/components/registration) section.

Components can be reused as many times as you want:

template\`\`\`
\Here are many child components!\
\
\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqVUE1LxDAQ/StjLqusNHotcfHj4l8QcontLBtsJiGdiFL6301SdrEqyEJyeG9m3ps3k3gIoXlPKFqhxi7awDtN1gUfGR4Ts6cnn4gxwj56B5tGrtgyutEEoAk/6lCPe5MGhqmwnc9KhMRjuxCwFi3UrCk/JU/uGTC6MBjGglgdbnfPGBFM/s7QJ3QHO/TfxC+UzD21d72zPItU8uQrrsWvnKsT/ZW2N2wur45BI3KKdETlFlmphZsF58j/RgdQr3UJuO8G273daVFFtlstahngxSeoNezBIUzTYgPzDGwdjk1VkYvMj4jzF0nwsyQ=)

[Try it in the Playground](https://play.vuejs.org/#eNqVj91KAzEQhV/lmJsqlY3eSlr8ufEVhNys6ZQGNz8kE0GWfXez2SJUsdCLuZiZM9+ZM4qnGLvPQuJBqGySjYxMXOJWe+tiSIznwhz8SyieKWGfgsOqkyfTGbDSXsmFUG9rw+Ti0DPNHavD/faVEqGv5Xr/BXOwww4mVBNPnvOVklXTtKeO8qKhkj++4lb8+fL/mCMS7TEdAy6BtDfBZ65fVgA2s+L67uZMUEC9N0s8msGaj40W7Xa91qKtgbdQ0Ha0gyOM45E+TWDrKHeNIhfMr0DTN4U0me8=)

Notice that when clicking on the buttons, each one maintains its own, separate `count`. That's because each time you use a component, a new **instance** of it is created.

In SFCs, it's recommended to use `PascalCase` tag names for child components to differentiate from native HTML elements. Although native HTML tag names are case\-insensitive, Vue SFC is a compiled format so we are able to use case\-sensitive tag names in it. We are also able to use `/>` to close a tag.

If you are authoring your templates directly in a DOM (e.g. as the content of a native `` element), the template will be subject to the browser's native HTML parsing behavior. In such cases, you will need to use `kebab-case` and explicit closing tags for components:

template\`\`\`
\
\\
\\
\\
\`\`\`See [in\-DOM template parsing caveats](#in-dom-template-parsing-caveats) for more details.

## Passing Props [​](#passing-props)

If we are building a blog, we will likely need a component representing a blog post. We want all the blog posts to share the same visual layout, but with different content. Such a component won't be useful unless you can pass data to it, such as the title and content of the specific post we want to display. That's where props come in.

Props are custom attributes you can register on a component. To pass a title to our blog post component, we must declare it in the list of props this component accepts, using the [`props`](/api/options-state#props) option[`defineProps`](/api/sfc-script-setup#defineprops-defineemits) macro:

vue\`\`\`
\
\
export default {
 props: \['title']
}
\

\
 \{{ title }}\
\
\`\`\`When a value is passed to a prop attribute, it becomes a property on that component instance. The value of that property is accessible within the template and on the component's `this` context, just like any other component property.

vue\`\`\`
\
\
defineProps(\['title'])
\

\
 \{{ title }}\
\
\`\`\``defineProps` is a compile\-time macro that is only available inside `` and does not need to be explicitly imported. Declared props are automatically exposed to the template. `defineProps` also returns an object that contains all the props passed to the component, so that we can access them in JavaScript if needed:

js\`\`\`
const props = defineProps(\['title'])
console.log(props.title)
\`\`\`See also: [Typing Component Props](/guide/typescript/composition-api#typing-component-props) 

If you are not using ``, props should be declared using the `props` option, and the props object will be passed to `setup()` as the first argument:

js\`\`\`
export default {
 props: \['title'],
 setup(props) {
 console.log(props.title)
 }
}
\`\`\`A component can have as many props as you like and, by default, any value can be passed to any prop.

Once a prop is registered, you can pass data to it as a custom attribute, like this:

template\`\`\`
\
\
\
\`\`\`In a typical app, however, you'll likely have an array of posts in your parent component:

js\`\`\`
export default {
 // ...
 data() {
 return {
 posts: \[
 { id: 1, title: 'My journey with Vue' },
 { id: 2, title: 'Blogging with Vue' },
 { id: 3, title: 'Why Vue is so fun' }
 ]
 }
 }
}
\`\`\`js\`\`\`
const posts = ref(\[
 { id: 1, title: 'My journey with Vue' },
 { id: 2, title: 'Blogging with Vue' },
 { id: 3, title: 'Why Vue is so fun' }
])
\`\`\`Then want to render a component for each one, using `v-for`:

template\`\`\`
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9UU1rhDAU/CtDLrawVfpxklRo74We2kPtQdaoaTUJ8bmtiP+9ia6uC2VBgjOZeXnz3sCejAkPnWAx4+3eSkNJqmRjtCU817p81S2hsLpBEEYL4Q1BqoBUid9Jmosi62rC4Nm9dn4lFLXxTGAt5dG482eeUXZ1vdxbQZ1VCwKM0zr3x4KBATKPcbsDSapFjOClx5d2JtHjR1KFN9fTsfbWcXdy+CZKqcqL+vuT/r3qvQqyRatRdMrpF/nn/DNhd7iPR+v8HCDRmDoj4RHxbfyUDjeFto8p8yEh1Rw2ZV4JxN+iP96FMvest8RTTws/gdmQ8HUr7ikere+yHduu62y//y3NWG38xIOpeODyXcoE8OohGYZ5VhhHHjl83sD4B3XgyGI=)

[Try it in the Playground](https://play.vuejs.org/#eNp9kU9PhDAUxL/KpBfWBCH+OZEuid5N9qSHrQezFKhC27RlDSF8d1tYQBP1+N78OpN5HciD1sm54yQj1J6M0A6Wu07nTIpWK+MwwPASI0qjWkQejVbpsVHVQVl30ZJ0WQRHjwFMnpT0gPZLi32w2h2DMEAUGW5iOOEaniF66vGuOiN5j0/hajx7B4zxxt5ubIiphKz+IO828qXugw5hYRXKTnqSydcrJmk61/VF/eB4q5s3x8Pk6FJjauDO16Uye0ZCBwg5d2EkkED2wfuLlogibMOTbMpf9tMwP8jpeiMfRdM1l8Tk+/F++Y6Cl0Lyg1Ha7o7R5Bn9WwSg9X0+DPMxMI409fPP1PELlVmwdQ==)

Notice how [`v-bind` syntax](/api/built-in-directives#v-bind) (`:title="post.title"`) is used to pass dynamic prop values. This is especially useful when you don't know the exact content you're going to render ahead of time.

That's all you need to know about props for now, but once you've finished reading this page and feel comfortable with its content, we recommend coming back later to read the full guide on [Props](/guide/components/props).

## Listening to Events [​](#listening-to-events)

As we develop our `` component, some features may require communicating back up to the parent. For example, we may decide to include an accessibility feature to enlarge the text of blog posts, while leaving the rest of the page at its default size.

In the parent, we can support this feature by adding a `postFontSize` data propertyref:

js\`\`\`
data() {
 return {
 posts: \[
 /\* ... \*/
 ],
 postFontSize: 1
 }
}
\`\`\`js\`\`\`
const posts = ref(\[
 /\* ... \*/
])

const postFontSize = ref(1\)
\`\`\`Which can be used in the template to control the font size of all blog posts:

template\`\`\`
\
 \
\
\`\`\`Now let's add a button to the `` component's template:

vue\`\`\`
\ \-\-\>
\
 \
 \{{ title }}\
 \Enlarge text\
 \
\
\`\`\`The button doesn't do anything yet \- we want clicking the button to communicate to the parent that it should enlarge the text of all posts. To solve this problem, components provide a custom events system. The parent can choose to listen to any event on the child component instance with `v-on` or `@`, just as we would with a native DOM event:

template\`\`\`
\
\`\`\`Then the child component can emit an event on itself by calling the built\-in [**`$emit`** method](/api/component-instance#emit), passing the name of the event:

vue\`\`\`
\ \-\-\>
\
 \
 \{{ title }}\
 \Enlarge text\
 \
\
\`\`\`Thanks to the `@enlarge-text="postFontSize += 0.1"` listener, the parent will receive the event and update the value of `postFontSize`.

[Try it in the Playground](https://play.vuejs.org/#eNqNUsFOg0AQ/ZUJMaGNbbHqidCmmujNxMRED9IDhYWuhV0CQy0S/t1ZYIEmaiRkw8y8N/vmMZVxl6aLY8EM23ByP+Mprl3Bk1RmCPexjJ5ljhBmMgFzYemEIpiuAHAFOzXQgIVeESNUKutL4gsmMLfbBPStVFTP1Bl46E2mup4xLDKhI4CUsMR+1zFABTywYTkD5BgzG8ynEj4kkVgJnxz38Eqaut5jxvXAUCIiLqI/8TcD/m1fKhTwHHIJYSEIr+HbnqikPkqBL/yLSMs23eDooNexel8pQJaksYeMIgAn4EewcyxjtnKNCsK+zbgpXILJEnW30bCIN7ZTPcd5KDNqoWjARWufa+iyfWBlV13wYJRvJtWVJhiKGyZiL4vYHNkJO8wgaQVXi6UGr51+Ndq5LBqMvhyrH9eYGePtOVu3n3YozWSqFsBsVJmt3SzhzVaYY2nm9l82+7GX5zTGjlTM1SyNmy5SeX+7rqr2r0NdOxbFXWVXIEoBGz/m/oHIF0rB5Pz6KTV6aBOgEo7Vsn51ov4GgAAf2A==)

[Try it in the Playground](https://play.vuejs.org/#eNp1Uk1PwkAQ/SuTxqQYgYp6ahaiJngzITHRA/UAZQor7W7TnaK16X93th8UEuHEvPdm5s3bls5Tmo4POTq+I0yYyZTAIOXpLFAySXVGUEKGEVQQZToBl6XukXqO9XahDbXc2OsAO5FlAIEKtWJByqCBqR01WFqiBLnxYTIEkhSjD+5rAV86zxQW8C1pB+88Aaphr73rtXbNVqrtBeV9r/zYFZYHacBoiHLFykB9Xgfq1NmLVvQmf7E1OGFaeE0anAMXhEkarwhtRWIjD+AbKmKcBk4JUdvtn8+6ARcTu87hLuCf6NJpSoDDKNIZj7BtIFUTUuB0tL/HomXHcnOC18d1TF305COqeJVtcUT4Q62mtzSF2/GkE8/E8b1qh8Ljw/if8I7nOkPn9En/+Ug2GEmFi0ynZrB0azOujbfB54kki5+aqumL8bING28Yr4xh+2vePrI39CnuHmZl2TwwVJXwuG6ZdU6kFTyGsQz33HyFvH5wvvyaB80bACwgvKbrYgLVH979DQc=)

We can optionally declare emitted events using the [`emits`](/api/options-state#emits) option[`defineEmits`](/api/sfc-script-setup#defineprops-defineemits) macro:

vue\`\`\`
\
\
export default {
 props: \['title'],
 emits: \['enlarge\-text']
}
\
\`\`\`vue\`\`\`
\
\
defineProps(\['title'])
defineEmits(\['enlarge\-text'])
\
\`\`\`This documents all the events that a component emits and optionally [validates them](/guide/components/events#events-validation). It also allows Vue to avoid implicitly applying them as native listeners to the child component's root element.

Similar to `defineProps`, `defineEmits` is only usable in `` and doesn't need to be imported. It returns an `emit` function that is equivalent to the `$emit` method. It can be used to emit events in the `` section of a component, where `$emit` isn't directly accessible:

vue\`\`\`
\
const emit = defineEmits(\['enlarge\-text'])

emit('enlarge\-text')
\
\`\`\`See also: [Typing Component Emits](/guide/typescript/composition-api#typing-component-emits) 

If you are not using ``, you can declare emitted events using the `emits` option. You can access the `emit` function as a property of the setup context (passed to `setup()` as the second argument):

js\`\`\`
export default {
 emits: \['enlarge\-text'],
 setup(props, ctx) {
 ctx.emit('enlarge\-text')
 }
}
\`\`\`That's all you need to know about custom component events for now, but once you've finished reading this page and feel comfortable with its content, we recommend coming back later to read the full guide on [Custom Events](/guide/components/events).

## Content Distribution with Slots [​](#content-distribution-with-slots)

Just like with HTML elements, it's often useful to be able to pass content to a component, like this:

template\`\`\`
\
 Something bad happened.
\
\`\`\`Which might render something like:

This is an Error for Demo Purposes

Something bad happened.

This can be achieved using Vue's custom `` element:

vue\`\`\`
\
\
 \
 \This is an Error for Demo Purposes\
 \
 \
\

\
.alert\-box {
 /\* ... \*/
}
\
\`\`\`As you'll see above, we use the `` as a placeholder where we want the content to go – and that's it. We're done!

[Try it in the Playground](https://play.vuejs.org/#eNpVUcFOwzAM/RUTDruwFhCaUCmThsQXcO0lbbKtIo0jx52Kpv07TreWouTynl+en52z2oWQnXqrClXGhtrA28q3XUBi2DlL/IED7Ak7WGX5RKQHq8oDVN4Oo9TYve4dwzmxDcp7bz3HAs5/LpfKyy3zuY0Atl1wmm1CXE5SQeLNX9hZPrb+ALU2cNQhWG9NNkrnLKIt89lGPahlyDTVogVAadoTNE7H+F4pnZTrGodKjUUpRyb0h+0nEdKdRL3CW7GmfNY5ZLiiMhfP/ynG0SL/OAuxwWCNMNncbVqSQyrgfrPZvCVcIxkrxFMYIKJrDZA1i8qatGl72ehLGEY6aGNkNwU8P96YWjffB8Lem/Xkvn9NR6qy+fRd14FSgopvmtQmzTT9Toq9VZdfIpa5jQ==)

[Try it in the Playground](https://play.vuejs.org/#eNpVUEtOwzAQvcpgFt3QBBCqUAiRisQJ2GbjxG4a4Xis8aQKqnp37PyUyqv3mZn3fBVH55JLr0Umcl9T6xi85t4VpW07h8RwNJr4Cwc4EXawS9KFiGO70ubpNBcmAmDdOSNZR8T5Yg0IoOQf7DSfW9tAJRWcpXPaapWM1nVt8ObpukY8ie29GHNzAiBX7QVqI73/LIWMzn2FQylGMcieCW1TfBMhPYSoE5zFitLVZ5BhQnkadt6nGKt5/jMafI1Oq8Ak6zW4xrEaDVIGj4fD4SPiCknpQLy4ATyaVgFptVH2JFXb+wze3DDSTioV/iaD1+eZqWT92xD2Vu2X7af3+IJ6G7/UToVigpJnTzwTO42eWDnELsTtH/wUqH4=)

That's all you need to know about slots for now, but once you've finished reading this page and feel comfortable with its content, we recommend coming back later to read the full guide on [Slots](/guide/components/slots).

## Dynamic Components [​](#dynamic-components)

Sometimes, it's useful to dynamically switch between components, like in a tabbed interface:

[Open example in the Playground](https://play.vuejs.org/#eNqNVE2PmzAQ/Ssj9kArLSHbrXpwk1X31mMPvS17cIxJrICNbJMmivLfO/7AEG2jRiDkefP85sNmztlr3y8OA89ItjJMi96+VFJ0vdIWfqqOQ6NVB/midIYj5sn9Sxlrkt9b14RXzXbiMElEO5IAKsmPnljzhg6thbNDmcLdkktrSADAJ/IYlj5MXEc9Z1w8VFNLP30ed2luBy1HC4UHrVH2N90QyJ1kHnUALN1gtLeIQu6juEUMkb8H5sXHqiS+qzK1Cw3Lu76llqMFsKrFAVhLjVlXWc07VWUeR89msFbhhhAWDkWjNJIwPgjp06iy5CV7fgrOOTgKv+XoKIIgpnoGyiymSmZ1wnq9dqJweZ8p/GCtYHtUmBMdLXFitgDnc9ju68b0yxDO1WzRTEcFRLiUJsEqSw3wwi+rMpFDj0psEq5W5ax1aBp7at1y4foWzq5R0hYN7UR7ImCoNIXhWjTfnW+jdM01gaf+CEa1ooYHzvnMVWhaiwEP90t/9HBP61rILQJL3POMHw93VG+FLKzqUYx3c2yjsOaOwNeRO2B8zKHlzBKQWJNH1YHrplV/iiMBOliFILYNK5mOKdSTMviGCTyNojFdTKBoeWNT3s8f/Vpsd7cIV61gjHkXnotR6OqVkJbrQKdsv9VqkDWBh2bpnn8VXaDcHPexE4wFzsojO9eDUOSVPF+65wN/EW7sHRsi5XaFqaexn+EH9Xcpe8zG2eWG3O0/NVzUaeJMk+jGhUXlNPXulw5j8w7t2bi8X32cuf/Vv/wF/SL98A==)

[Open example in the Playground](https://play.vuejs.org/#eNqNVMGOmzAQ/ZURe2BXCiHbrXpwk1X31mMPvS1V5RiTWAEb2SZNhPLvHdvggLZRE6TIM/P8/N5gpk/e2nZ57HhCkrVhWrQWDLdd+1pI0bRKW/iuGg6VVg2ky9wFDp7G8g9lrIl1H80Bb5rtxfFKMcRzUA+aV3AZQKEEhWRKGgus05pL+5NuYeNwj6mTkT4VckRYujVY63GT17twC6/Fr4YjC3kp5DoPNtEgBpY3bU0txwhgXYojsJoasymSkjeqSHweK9vOWoUbXIC/Y1YpjaDH3wt39hMI6TUUSYSQAz8jArPT5Mj+nmIhC6zpAu1TZlEhmXndbBwpXH5NGL6xWrADMsyaMj1lkAzQ92E7mvYe8nCcM24xZApbL5ECiHCSnP73KyseGnvh6V/XedwS2pVjv3C1ziddxNDYc+2WS9fC8E4qJW1W0UbUZwKGSpMZrkX11dW2SpdcE3huT2BULUp44JxPSpmmpegMgU/tyadbWpZC7jCxwj0v+OfTDdU7ITOrWiTjzTS3Vei8IfB5xHZ4PmqoObMEJHryWXXkuqrVn+xEgHZWYRKbh06uLyv4iQq+oIDnkXSQiwKymlc26n75WNdit78FmLWCMeZL+GKMwlKrhLRcBzhlh51WnSwJPFQr9/zLdIZ007w/O6bR4MQe2bseBJMzer5yzwf8MtzbOzYMkNsOY0+HfoZv1d+lZJGMg8fNqdsfbbio4b77uRVv7I0Li8xxZN1PHWbeHdyTWXc/+zgw/8t/+QsROe9h)

The above is made possible by Vue's `` element with the special `is` attribute:

template\`\`\`
\
\\
\`\`\`template\`\`\`
\
\\
\`\`\`In the example above, the value passed to `:is` can contain either:

* the name string of a registered component, OR
* the actual imported component object

You can also use the `is` attribute to create regular HTML elements.

When switching between multiple components with ``, a component will be unmounted when it is switched away from. We can force the inactive components to stay "alive" with the built\-in [`` component](/guide/built-ins/keep-alive).

## in\-DOM Template Parsing Caveats [​](#in-dom-template-parsing-caveats)

If you are writing your Vue templates directly in the DOM, Vue will have to retrieve the template string from the DOM. This leads to some caveats due to browsers' native HTML parsing behavior.

TIP

It should be noted that the limitations discussed below only apply if you are writing your templates directly in the DOM. They do NOT apply if you are using string templates from the following sources:

* Single\-File Components
* Inlined template strings (e.g. `template: '...'`)
* ``
### Case Insensitivity [​](#case-insensitivity)

HTML tags and attribute names are case\-insensitive, so browsers will interpret any uppercase characters as lowercase. That means when you’re using in\-DOM templates, PascalCase component names and camelCased prop names or `v-on` event names all need to use their kebab\-cased (hyphen\-delimited) equivalents:

js\`\`\`
// camelCase in JavaScript
const BlogPost = {
 props: \['postTitle'],
 emits: \['updatePost'],
 template: \`
 \{{ postTitle }}\
 \`
}
\`\`\`template\`\`\`
\
\\
\`\`\`### Self Closing Tags [​](#self-closing-tags)

We have been using self\-closing tags for components in previous code samples:

template\`\`\`
\
\`\`\`This is because Vue's template parser respects `/>` as an indication to end any tag, regardless of its type.

In in\-DOM templates, however, we must always include explicit closing tags:

template\`\`\`
\\
\`\`\`This is because the HTML spec only allows [a few specific elements](https://html.spec.whatwg.org/multipage/syntax.html#void-elements) to omit closing tags, the most common being `` and ``. For all other elements, if you omit the closing tag, the native HTML parser will think you never terminated the opening tag. For example, the following snippet:

template\`\`\`
\ \
\hello\
\`\`\`will be parsed as:

template\`\`\`
\
 \hello\
\ \
\`\`\`### Element Placement Restrictions [​](#element-placement-restrictions)

Some HTML elements, such as ``, ``, `` and `` have restrictions on what elements can appear inside them, and some elements such as ``, ``, and `` can only appear inside certain other elements.

This will lead to issues when using components with elements that have such restrictions. For example:

template\`\`\`
\
 \\
\
\`\`\`The custom component `` will be hoisted out as invalid content, causing errors in the eventual rendered output. We can use the special [`is` attribute](/api/built-in-special-attributes#is) as a workaround:

template\`\`\`
\
 \\
\
\`\`\`TIP

When used on native HTML elements, the value of `is` must be prefixed with `vue:` in order to be interpreted as a Vue component. This is required to avoid confusion with native [customized built\-in elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-customized-builtin-example).

That's all you need to know about in\-DOM template parsing caveats for now \- and actually, the end of Vue's *Essentials*. Congratulations! There's still more to learn, but first, we recommend taking a break to play with Vue yourself \- build something fun, or check out some of the [Examples](/examples/) if you haven't already.

Once you feel comfortable with the knowledge you've just digested, move on with the guide to learn more about components in depth.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/component-basics.md)



## Custom Renderer API | Vue.js

[Read the full article](https://vuejs.org/api/custom-renderer)

# Custom Renderer API [​](#custom-renderer-api)

## createRenderer() [​](#createrenderer)

Creates a custom renderer. By providing platform\-specific node creation and manipulation APIs, you can leverage Vue's core runtime to target non\-DOM environments.

* **Type**

ts\`\`\`
function createRenderer\(
 options: RendererOptions\
): Renderer\

interface Renderer\ {
 render: RootRenderFunction\
 createApp: CreateAppFunction\
}

interface RendererOptions\ {
 patchProp(
 el: HostElement,
 key: string,
 prevValue: any,
 nextValue: any,
 // the rest is unused for most custom renderers
 isSVG?: boolean,
 prevChildren?: VNode\\[],
 parentComponent?: ComponentInternalInstance \| null,
 parentSuspense?: SuspenseBoundary \| null,
 unmountChildren?: UnmountChildrenFn
 ): void
 insert(
 el: HostNode,
 parent: HostElement,
 anchor?: HostNode \| null
 ): void
 remove(el: HostNode): void
 createElement(
 type: string,
 isSVG?: boolean,
 isCustomizedBuiltIn?: string,
 vnodeProps?: (VNodeProps \& { \[key: string]: any }) \| null
 ): HostElement
 createText(text: string): HostNode
 createComment(text: string): HostNode
 setText(node: HostNode, text: string): void
 setElementText(node: HostElement, text: string): void
 parentNode(node: HostNode): HostElement \| null
 nextSibling(node: HostNode): HostNode \| null

 // optional, DOM\-specific
 querySelector?(selector: string): HostElement \| null
 setScopeId?(el: HostElement, id: string): void
 cloneNode?(node: HostNode): HostNode
 insertStaticContent?(
 content: string,
 parent: HostElement,
 anchor: HostNode \| null,
 isSVG: boolean
 ): \[HostNode, HostNode]
}
\`\`\`
* **Example**

js\`\`\`
import { createRenderer } from '@vue/runtime\-core'

const { render, createApp } = createRenderer({
 patchProp,
 insert,
 remove,
 createElement
 // ...
})

// \`render\` is the low\-level API
// \`createApp\` returns an app instance
export { render, createApp }

// re\-export Vue core APIs
export \* from '@vue/runtime\-core'
\`\`\`Vue's own `@vue/runtime-dom` is [implemented using the same API](https://github.com/vuejs/core/blob/main/packages/runtime-dom/src/index.ts). For a simpler implementation, check out [`@vue/runtime-test`](https://github.com/vuejs/core/blob/main/packages/runtime-test/src/index.ts) which is a private package for Vue's own unit testing.
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/custom-renderer.md)



## SFC CSS Features | Vue.js

[Read the full article](https://vuejs.org/api/sfc-css-features)

# SFC CSS Features [​](#sfc-css-features)

## Scoped CSS [​](#scoped-css)

When a `` tag has the `scoped` attribute, its CSS will apply to elements of the current component only. This is similar to the style encapsulation found in Shadow DOM. It comes with some caveats, but doesn't require any polyfills. It is achieved by using PostCSS to transform the following:

vue\`\`\`
\
.example {
 color: red;
}
\

\
 \hi\
\
\`\`\`Into the following:

vue\`\`\`
\
.example\[data\-v\-f3f3eg9] {
 color: red;
}
\

\
 \hi\
\
\`\`\`### Child Component Root Elements [​](#child-component-root-elements)

With `scoped`, the parent component's styles will not leak into child components. However, a child component's root node will be affected by both the parent's scoped CSS and the child's scoped CSS. This is by design so that the parent can style the child root element for layout purposes.

### Deep Selectors [​](#deep-selectors)

If you want a selector in `scoped` styles to be "deep", i.e. affecting child components, you can use the `:deep()` pseudo\-class:

vue\`\`\`
\
.a :deep(.b) {
 /\* ... \*/
}
\
\`\`\`The above will be compiled into:

css\`\`\`
.a\[data\-v\-f3f3eg9] .b {
 /\* ... \*/
}
\`\`\`TIP

DOM content created with `v-html` are not affected by scoped styles, but you can still style them using deep selectors.

### Slotted Selectors [​](#slotted-selectors)

By default, scoped styles do not affect contents rendered by ``, as they are considered to be owned by the parent component passing them in. To explicitly target slot content, use the `:slotted` pseudo\-class:

vue\`\`\`
\
:slotted(div) {
 color: red;
}
\
\`\`\`### Global Selectors [​](#global-selectors)

If you want just one rule to apply globally, you can use the `:global` pseudo\-class rather than creating another `` (see below):

vue\`\`\`
\
:global(.red) {
 color: red;
}
\
\`\`\`### Mixing Local and Global Styles [​](#mixing-local-and-global-styles)

You can also include both scoped and non\-scoped styles in the same component:

vue\`\`\`
\
/\* global styles \*/
\

\
/\* local styles \*/
\
\`\`\`### Scoped Style Tips [​](#scoped-style-tips)

* **Scoped styles do not eliminate the need for classes**. Due to the way browsers render various CSS selectors, `p { color: red }` will be many times slower when scoped (i.e. when combined with an attribute selector). If you use classes or ids instead, such as in `.example { color: red }`, then you virtually eliminate that performance hit.
* **Be careful with descendant selectors in recursive components!** For a CSS rule with the selector `.a .b`, if the element that matches `.a` contains a recursive child component, then all `.b` in that child component will be matched by the rule.

## CSS Modules [​](#css-modules)

A `` tag is compiled as [CSS Modules](https://github.com/css-modules/css-modules) and exposes the resulting CSS classes to the component as an object under the key of `$style`:

vue\`\`\`
\
 \This should be red\
\

\
.red {
 color: red;
}
\
\`\`\`The resulting classes are hashed to avoid collision, achieving the same effect of scoping the CSS to the current component only.

Refer to the [CSS Modules spec](https://github.com/css-modules/css-modules) for more details such as [global exceptions](https://github.com/css-modules/css-modules/blob/master/docs/composition.md#exceptions) and [composition](https://github.com/css-modules/css-modules/blob/master/docs/composition.md#composition).

### Custom Inject Name [​](#custom-inject-name)

You can customize the property key of the injected classes object by giving the `module` attribute a value:

vue\`\`\`
\
 \red\
\

\
.red {
 color: red;
}
\
\`\`\`### Usage with Composition API [​](#usage-with-composition-api)

The injected classes can be accessed in `setup()` and `` via the `useCssModule` API. For `` blocks with custom injection names, `useCssModule` accepts the matching `module` attribute value as the first argument:

js\`\`\`
import { useCssModule } from 'vue'

// inside setup() scope...
// default, returns classes for \
useCssModule()

// named, returns classes for \
useCssModule('classes')
\`\`\`* **Example**

vue\`\`\`
\
import { useCssModule } from 'vue'

const classes = useCssModule()
\

\
 \red\
\

\
.red {
 color: red;
}
\
\`\`\`## `v-bind()` in CSS [​](#v-bind-in-css)

SFC `` tags support linking CSS values to dynamic component state using the `v-bind` CSS function:

vue\`\`\`
\
 \hello\
\

\
export default {
 data() {
 return {
 color: 'red'
 }
 }
}
\

\
.text {
 color: v\-bind(color);
}
\
\`\`\`The syntax works with [``](/api/sfc-script-setup), and supports JavaScript expressions (must be wrapped in quotes):

vue\`\`\`
\
import { ref } from 'vue'
const theme = ref({
 color: 'red',
})
\

\
 \hello\
\

\
p {
 color: v\-bind('theme.color');
}
\
\`\`\`The actual value will be compiled into a hashed CSS custom property, so the CSS is still static. The custom property will be applied to the component's root element via inline styles and reactively updated if the source value changes.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/sfc-css-features.md)



## Provide / Inject | Vue.js

[Read the full article](https://vuejs.org/guide/components/provide-inject)

# Provide / Inject [​](#provide-inject)

> This page assumes you've already read the [Components Basics](/guide/essentials/component-basics). Read that first if you are new to components.

## Prop Drilling [​](#prop-drilling)

Usually, when we need to pass data from the parent to a child component, we use [props](/guide/components/props). However, imagine the case where we have a large component tree, and a deeply nested component needs something from a distant ancestor component. With only props, we would have to pass the same prop across the entire parent chain:



Notice although the `` component may not care about these props at all, it still needs to declare and pass them along just so `` can access them. If there is a longer parent chain, more components would be affected along the way. This is called "props drilling" and definitely isn't fun to deal with.

We can solve props drilling with `provide` and `inject`. A parent component can serve as a **dependency provider** for all its descendants. Any component in the descendant tree, regardless of how deep it is, can **inject** dependencies provided by components up in its parent chain.



## Provide [​](#provide)

To provide data to a component's descendants, use the [`provide()`](/api/composition-api-dependency-injection#provide) function:

vue\`\`\`
\
import { provide } from 'vue'

provide(/\* key \*/ 'message', /\* value \*/ 'hello!')
\
\`\`\`If not using ``, make sure `provide()` is called synchronously inside `setup()`:

js\`\`\`
import { provide } from 'vue'

export default {
 setup() {
 provide(/\* key \*/ 'message', /\* value \*/ 'hello!')
 }
}
\`\`\`The `provide()` function accepts two arguments. The first argument is called the **injection key**, which can be a string or a `Symbol`. The injection key is used by descendant components to lookup the desired value to inject. A single component can call `provide()` multiple times with different injection keys to provide different values.

The second argument is the provided value. The value can be of any type, including reactive state such as refs:

js\`\`\`
import { ref, provide } from 'vue'

const count = ref(0\)
provide('key', count)
\`\`\`Providing reactive values allows the descendant components using the provided value to establish a reactive connection to the provider component.

To provide data to a component's descendants, use the [`provide`](/api/options-composition#provide) option:

js\`\`\`
export default {
 provide: {
 message: 'hello!'
 }
}
\`\`\`For each property in the `provide` object, the key is used by child components to locate the correct value to inject, while the value is what ends up being injected.

If we need to provide per\-instance state, for example data declared via the `data()`, then `provide` must use a function value:

js\`\`\`
export default {
 data() {
 return {
 message: 'hello!'
 }
 },
 provide() {
 // use function syntax so that we can access \`this\`
 return {
 message: this.message
 }
 }
}
\`\`\`However, do note this does **not** make the injection reactive. We will discuss [making injections reactive](#working-with-reactivity) below.

## App\-level Provide [​](#app-level-provide)

In addition to providing data in a component, we can also provide at the app level:

js\`\`\`
import { createApp } from 'vue'

const app = createApp({})

app.provide(/\* key \*/ 'message', /\* value \*/ 'hello!')
\`\`\`App\-level provides are available to all components rendered in the app. This is especially useful when writing [plugins](/guide/reusability/plugins), as plugins typically wouldn't be able to provide values using components.

## Inject [​](#inject)

To inject data provided by an ancestor component, use the [`inject()`](/api/composition-api-dependency-injection#inject) function:

vue\`\`\`
\
import { inject } from 'vue'

const message = inject('message')
\
\`\`\`If the provided value is a ref, it will be injected as\-is and will **not** be automatically unwrapped. This allows the injector component to retain the reactivity connection to the provider component.

[Full provide \+ inject Example with Reactivity](https://play.vuejs.org/#eNqFUUFugzAQ/MrKF1IpxfeIVKp66Kk/8MWFDXYFtmUbpArx967BhURRU9/WOzO7MzuxV+fKcUB2YlWovXYRAsbBvQije2d9hAk8Xo7gvB11gzDDxdseCuIUG+ZN6a7JjZIvVRIlgDCcw+d3pmvTglz1okJ499I0C3qB1dJQT9YRooVaSdNiACWdQ5OICj2WwtTWhAg9hiBbhHNSOxQKu84WT8LkNQ9FBhTHXyg1K75aJHNUROxdJyNSBVBp44YI43NvG+zOgmWWYGt7dcipqPhGZEe2ef07wN3lltD+lWN6tNkV/37+rdKjK2rzhRTt7f3u41xhe37/xJZGAL2PLECXa9NKdD/a6QTTtGnP88LgiXJtYv4BaLHhvg==)

Again, if not using ``, `inject()` should only be called synchronously inside `setup()`:

js\`\`\`
import { inject } from 'vue'

export default {
 setup() {
 const message = inject('message')
 return { message }
 }
}
\`\`\`To inject data provided by an ancestor component, use the [`inject`](/api/options-composition#inject) option:

js\`\`\`
export default {
 inject: \['message'],
 created() {
 console.log(this.message) // injected value
 }
}
\`\`\`Injections are resolved **before** the component's own state, so you can access injected properties in `data()`:

js\`\`\`
export default {
 inject: \['message'],
 data() {
 return {
 // initial data based on injected value
 fullMessage: this.message
 }
 }
}
\`\`\`[Full provide \+ inject example](https://play.vuejs.org/#eNqNkcFqwzAQRH9l0EUthOhuRKH00FO/oO7B2JtERZaEvA4F43+vZCdOTAIJCImRdpi32kG8h7A99iQKobs6msBvpTNt8JHxcTC2wS76FnKrJpVLZelKR39TSUO7qreMoXRA7ZPPkeOuwHByj5v8EqI/moZeXudCIBL30Z0V0FLXVXsqIA9krU8R+XbMR9rS0mqhS4KpDbZiSgrQc5JKQqvlRWzEQnyvuc9YuWbd4eXq+TZn0IvzOeKr8FvsNcaK/R6Ocb9Uc4FvefpE+fMwP0wH8DU7wB77nIo6x6a2hvNEME5D0CpbrjnHf+8excI=)

### Injection Aliasing [​](#injection-aliasing)

When using the array syntax for `inject`, the injected properties are exposed on the component instance using the same key. In the example above, the property was provided under the key `"message"`, and injected as `this.message`. The local key is the same as the injection key.

If we want to inject the property using a different local key, we need to use the object syntax for the `inject` option:

js\`\`\`
export default {
 inject: {
 /\* local key \*/ localMessage: {
 from: /\* injection key \*/ 'message'
 }
 }
}
\`\`\`Here, the component will locate a property provided with the key `"message"`, and then expose it as `this.localMessage`.

### Injection Default Values [​](#injection-default-values)

By default, `inject` assumes that the injected key is provided somewhere in the parent chain. In the case where the key is not provided, there will be a runtime warning.

If we want to make an injected property work with optional providers, we need to declare a default value, similar to props:

js\`\`\`
// \`value\` will be "default value"
// if no data matching "message" was provided
const value = inject('message', 'default value')
\`\`\`In some cases, the default value may need to be created by calling a function or instantiating a new class. To avoid unnecessary computation or side effects in case the optional value is not used, we can use a factory function for creating the default value:

js\`\`\`
const value = inject('key', () =\> new ExpensiveClass(), true)
\`\`\`The third parameter indicates the default value should be treated as a factory function.

js\`\`\`
export default {
 // object syntax is required
 // when declaring default values for injections
 inject: {
 message: {
 from: 'message', // this is optional if using the same key for injection
 default: 'default value'
 },
 user: {
 // use a factory function for non\-primitive values that are expensive
 // to create, or ones that should be unique per component instance.
 default: () =\> ({ name: 'John' })
 }
 }
}
\`\`\`## Working with Reactivity [​](#working-with-reactivity)

When using reactive provide / inject values, **it is recommended to keep any mutations to reactive state inside of the *provider* whenever possible**. This ensures that the provided state and its possible mutations are co\-located in the same component, making it easier to maintain in the future.

There may be times when we need to update the data from an injector component. In such cases, we recommend providing a function that is responsible for mutating the state:

vue\`\`\`
\
\
import { provide, ref } from 'vue'

const location = ref('North Pole')

function updateLocation() {
 location.value = 'South Pole'
}

provide('location', {
 location,
 updateLocation
})
\
\`\`\`vue\`\`\`
\
\
import { inject } from 'vue'

const { location, updateLocation } = inject('location')
\

\
 \{{ location }}\
\
\`\`\`Finally, you can wrap the provided value with [`readonly()`](/api/reactivity-core#readonly) if you want to ensure that the data passed through `provide` cannot be mutated by the injector component.

vue\`\`\`
\
import { ref, provide, readonly } from 'vue'

const count = ref(0\)
provide('read\-only\-count', readonly(count))
\
\`\`\`In order to make injections reactively linked to the provider, we need to provide a computed property using the [computed()](/api/reactivity-core#computed) function:

js\`\`\`
import { computed } from 'vue'

export default {
 data() {
 return {
 message: 'hello!'
 }
 },
 provide() {
 return {
 // explicitly provide a computed property
 message: computed(() =\> this.message)
 }
 }
}
\`\`\`[Full provide \+ inject Example with Reactivity](https://play.vuejs.org/#eNqNUctqwzAQ/JVFFyeQxnfjBEoPPfULqh6EtYlV9EKWTcH43ytZtmPTQA0CsdqZ2dlRT16tPXctkoKUTeWE9VeqhbLGeXirheRwc0ZBds7HKkKzBdBDZZRtPXIYJlzqU40/I4LjjbUyIKmGEWw0at8UgZrUh1PscObZ4ZhQAA596/RcAShsGnbHArIapTRBP74O8Up060wnOO5QmP0eAvZyBV+L5jw1j2tZqsMp8yWRUHhUVjKPoQIohQ460L0ow1FeKJlEKEnttFweijJfiORElhCf5f3umObb0B9PU/I7kk17PJj7FloN/2t7a2Pj/Zkdob+x8gV8ZlMs2de/8+14AXwkBngD9zgVqjg2rNXPvwjD+EdlHilrn8MvtvD1+Q==)

The `computed()` function is typically used in Composition API components, but can also be used to complement certain use cases in Options API. You can learn more about its usage by reading the [Reactivity Fundamentals](/guide/essentials/reactivity-fundamentals) and [Computed Properties](/guide/essentials/computed) with the API Preference set to Composition API.

## Working with Symbol Keys [​](#working-with-symbol-keys)

So far, we have been using string injection keys in the examples. If you are working in a large application with many dependency providers, or you are authoring components that are going to be used by other developers, it is best to use Symbol injection keys to avoid potential collisions.

It's recommended to export the Symbols in a dedicated file:

js\`\`\`
// keys.js
export const myInjectionKey = Symbol()
\`\`\`js\`\`\`
// in provider component
import { provide } from 'vue'
import { myInjectionKey } from './keys.js'

provide(myInjectionKey, {
 /\* data to provide \*/
})
\`\`\`js\`\`\`
// in injector component
import { inject } from 'vue'
import { myInjectionKey } from './keys.js'

const injected = inject(myInjectionKey)
\`\`\`See also: [Typing Provide / Inject](/guide/typescript/composition-api#typing-provide-inject) 

js\`\`\`
// in provider component
import { myInjectionKey } from './keys.js'

export default {
 provide() {
 return {
 \[myInjectionKey]: {
 /\* data to provide \*/
 }
 }
 }
}
\`\`\`js\`\`\`
// in injector component
import { myInjectionKey } from './keys.js'

export default {
 inject: {
 injected: { from: myInjectionKey }
 }
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/provide-inject.md)



## Reactivity Transform | Vue.js

[Read the full article](https://vuejs.org/guide/extras/reactivity-transform)

# Reactivity Transform [​](#reactivity-transform)

Removed Experimental Feature

Reactivity Transform was an experimental feature, and has been removed in the latest 3\.4 release. Please read about [the reasoning here](https://github.com/vuejs/rfcs/discussions/369#discussioncomment-5059028).

If you still intend to use it, it is now available via the [Vue Macros](https://vue-macros.sxzz.moe/features/reactivity-transform.html) plugin.

Composition\-API\-specific

Reactivity Transform is a Composition\-API\-specific feature and requires a build step.

## Refs vs. Reactive Variables [​](#refs-vs-reactive-variables)

Ever since the introduction of the Composition API, one of the primary unresolved questions is the use of refs vs. reactive objects. It's easy to lose reactivity when destructuring reactive objects, while it can be cumbersome to use `.value` everywhere when using refs. Also, `.value` is easy to miss if not using a type system.

[Vue Reactivity Transform](https://github.com/vuejs/core/tree/main/packages/reactivity-transform) is a compile\-time transform that allows us to write code like this:

vue\`\`\`
\
let count = $ref(0\)

console.log(count)

function increment() {
 count\+\+
}
\

\
 \{{ count }}\
\
\`\`\`The `$ref()` method here is a **compile\-time macro**: it is not an actual method that will be called at runtime. Instead, the Vue compiler uses it as a hint to treat the resulting `count` variable as a **reactive variable.**

Reactive variables can be accessed and re\-assigned just like normal variables, but these operations are compiled into refs with `.value`. For example, the `` part of the above component is compiled into:

js\`\`\`
import { ref } from 'vue'

let count = ref(0\)

console.log(count.value)

function increment() {
 count.value\+\+
}
\`\`\`Every reactivity API that returns refs will have a `$`\-prefixed macro equivalent. These APIs include:

* [`ref`](/api/reactivity-core#ref) \-\> `$ref`
* [`computed`](/api/reactivity-core#computed) \-\> `$computed`
* [`shallowRef`](/api/reactivity-advanced#shallowref) \-\> `$shallowRef`
* [`customRef`](/api/reactivity-advanced#customref) \-\> `$customRef`
* [`toRef`](/api/reactivity-utilities#toref) \-\> `$toRef`

These macros are globally available and do not need to be imported when Reactivity Transform is enabled, but you can optionally import them from `vue/macros` if you want to be more explicit:

js\`\`\`
import { $ref } from 'vue/macros'

let count = $ref(0\)
\`\`\`## Destructuring with `$()` [​](#destructuring-with)

It is common for a composition function to return an object of refs, and use destructuring to retrieve these refs. For this purpose, reactivity transform provides the **`$()`** macro:

js\`\`\`
import { useMouse } from '@vueuse/core'

const { x, y } = $(useMouse())

console.log(x, y)
\`\`\`Compiled output:

js\`\`\`
import { toRef } from 'vue'
import { useMouse } from '@vueuse/core'

const \_\_temp = useMouse(),
 x = toRef(\_\_temp, 'x'),
 y = toRef(\_\_temp, 'y')

console.log(x.value, y.value)
\`\`\`Note that if `x` is already a ref, `toRef(__temp, 'x')` will simply return it as\-is and no additional ref will be created. If a destructured value is not a ref (e.g. a function), it will still work \- the value will be wrapped in a ref so the rest of the code works as expected.

`$()` destructure works on both reactive objects **and** plain objects containing refs.

## Convert Existing Refs to Reactive Variables with `$()` [​](#convert-existing-refs-to-reactive-variables-with)

In some cases we may have wrapped functions that also return refs. However, the Vue compiler won't be able to know ahead of time that a function is going to return a ref. In such cases, the `$()` macro can also be used to convert any existing refs into reactive variables:

js\`\`\`
function myCreateRef() {
 return ref(0\)
}

let count = $(myCreateRef())
\`\`\`## Reactive Props Destructure [​](#reactive-props-destructure)

There are two pain points with the current `defineProps()` usage in ``:

1. Similar to `.value`, you need to always access props as `props.x` in order to retain reactivity. This means you cannot destructure `defineProps` because the resulting destructured variables are not reactive and will not update.
2. When using the [type\-only props declaration](/api/sfc-script-setup#type-only-props-emit-declarations), there is no easy way to declare default values for the props. We introduced the `withDefaults()` API for this exact purpose, but it's still clunky to use.

We can address these issues by applying a compile\-time transform when `defineProps` is used with destructuring, similar to what we saw earlier with `$()`:

html\`\`\`
\
 interface Props {
 msg: string
 count?: number
 foo?: string
 }

 const {
 msg,
 // default value just works
 count = 1,
 // local aliasing also just works
 // here we are aliasing \`props.foo\` to \`bar\`
 foo: bar
 } = defineProps\()

 watchEffect(() =\> {
 // will log whenever the props change
 console.log(msg, count, bar)
 })
\
\`\`\`The above will be compiled into the following runtime declaration equivalent:

js\`\`\`
export default {
 props: {
 msg: { type: String, required: true },
 count: { type: Number, default: 1 },
 foo: String
 },
 setup(props) {
 watchEffect(() =\> {
 console.log(props.msg, props.count, props.foo)
 })
 }
}
\`\`\`## Retaining Reactivity Across Function Boundaries [​](#retaining-reactivity-across-function-boundaries)

While reactive variables relieve us from having to use `.value` everywhere, it creates an issue of "reactivity loss" when we pass reactive variables across function boundaries. This can happen in two cases:

### Passing into function as argument [​](#passing-into-function-as-argument)

Given a function that expects a ref as an argument, e.g.:

ts\`\`\`
function trackChange(x: Ref\) {
 watch(x, (x) =\> {
 console.log('x changed!')
 })
}

let count = $ref(0\)
trackChange(count) // doesn't work!
\`\`\`The above case will not work as expected because it compiles to:

ts\`\`\`
let count = ref(0\)
trackChange(count.value)
\`\`\`Here `count.value` is passed as a number, whereas `trackChange` expects an actual ref. This can be fixed by wrapping `count` with `$$()` before passing it:

diff\`\`\`
let count = $ref(0\)
\- trackChange(count)
\+ trackChange($$(count))
\`\`\`The above compiles to:

js\`\`\`
import { ref } from 'vue'

let count = ref(0\)
trackChange(count)
\`\`\`As we can see, `$$()` is a macro that serves as an **escape hint**: reactive variables inside `$$()` will not get `.value` appended.

### Returning inside function scope [​](#returning-inside-function-scope)

Reactivity can also be lost if reactive variables are used directly in a returned expression:

ts\`\`\`
function useMouse() {
 let x = $ref(0\)
 let y = $ref(0\)

 // listen to mousemove...

 // doesn't work!
 return {
 x,
 y
 }
}
\`\`\`The above return statement compiles to:

ts\`\`\`
return {
 x: x.value,
 y: y.value
}
\`\`\`In order to retain reactivity, we should be returning the actual refs, not the current value at return time.

Again, we can use `$$()` to fix this. In this case, `$$()` can be used directly on the returned object \- any reference to reactive variables inside the `$$()` call will retain the reference to their underlying refs:

ts\`\`\`
function useMouse() {
 let x = $ref(0\)
 let y = $ref(0\)

 // listen to mousemove...

 // fixed
 return $$({
 x,
 y
 })
}
\`\`\`### Using `$$()` on destructured props [​](#using-on-destructured-props)

`$$()` works on destructured props since they are reactive variables as well. The compiler will convert it with `toRef` for efficiency:

ts\`\`\`
const { count } = defineProps\()

passAsRef($$(count))
\`\`\`compiles to:

js\`\`\`
setup(props) {
 const \_\_props\_count = toRef(props, 'count')
 passAsRef(\_\_props\_count)
}
\`\`\`## TypeScript Integration  [​](#typescript-integration)

Vue provides typings for these macros (available globally) and all types will work as expected. There are no incompatibilities with standard TypeScript semantics, so the syntax will work with all existing tooling.

This also means the macros can work in any files where valid JS / TS are allowed \- not just inside Vue SFCs.

Since the macros are available globally, their types need to be explicitly referenced (e.g. in a `env.d.ts` file):

ts\`\`\`
/// \
\`\`\`When explicitly importing the macros from `vue/macros`, the type will work without declaring the globals.

## Explicit Opt\-in [​](#explicit-opt-in)

No longer supported in core

The following only applies up to Vue version 3\.3 and below. Support has been removed in Vue core 3\.4 and above, and `@vitejs/plugin-vue` 5\.0 and above. If you intend to continue using the transform, please migrate to [Vue Macros](https://vue-macros.sxzz.moe/features/reactivity-transform.html) instead.

### Vite [​](#vite)

* Requires `@vitejs/plugin-vue@>=2.0.0`
* Applies to SFCs and js(x)/ts(x) files. A fast usage check is performed on files before applying the transform so there should be no performance cost for files not using the macros.
* Note `reactivityTransform` is now a plugin root\-level option instead of nested as `script.refSugar`, since it affects not just SFCs.

js\`\`\`
// vite.config.js
export default {
 plugins: \[
 vue({
 reactivityTransform: true
 })
 ]
}
\`\`\`### `vue-cli` [​](#vue-cli)

* Currently only affects SFCs
* Requires `vue-loader@>=17.0.0`

js\`\`\`
// vue.config.js
module.exports = {
 chainWebpack: (config) =\> {
 config.module
 .rule('vue')
 .use('vue\-loader')
 .tap((options) =\> {
 return {
 ...options,
 reactivityTransform: true
 }
 })
 }
}
\`\`\`### Plain `webpack` \+ `vue-loader` [​](#plain-webpack-vue-loader)

* Currently only affects SFCs
* Requires `vue-loader@>=17.0.0`

js\`\`\`
// webpack.config.js
module.exports = {
 module: {
 rules: \[
 {
 test: /\\.vue$/,
 loader: 'vue\-loader',
 options: {
 reactivityTransform: true
 }
 }
 ]
 }
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/reactivity-transform.md)



## Utility Types | Vue.js

[Read the full article](https://vuejs.org/api/utility-types)

# Utility Types [​](#utility-types)

INFO

This page only lists a few commonly used utility types that may need explanation for their usage. For a full list of exported types, consult the [source code](https://github.com/vuejs/core/blob/main/packages/runtime-core/src/index.ts#L131).

## PropType\ [​](#proptype-t)

Used to annotate a prop with more advanced types when using runtime props declarations.

* **Example**

ts\`\`\`
import type { PropType } from 'vue'

interface Book {
 title: string
 author: string
 year: number
}

export default {
 props: {
 book: {
 // provide more specific type to \`Object\`
 type: Object as PropType\,
 required: true
 }
 }
}
\`\`\`
* **See also** [Guide \- Typing Component Props](/guide/typescript/options-api#typing-component-props)

## MaybeRef\ [​](#mayberef)

* Only supported in 3\.3\+

Alias for `T | Ref`. Useful for annotating arguments of [Composables](/guide/reusability/composables).

## MaybeRefOrGetter\ [​](#maybereforgetter)

* Only supported in 3\.3\+

Alias for `T | Ref | (() => T)`. Useful for annotating arguments of [Composables](/guide/reusability/composables).

## ExtractPropTypes\ [​](#extractproptypes)

Extract prop types from a runtime props options object. The extracted types are internal facing \- i.e. the resolved props received by the component. This means boolean props and props with default values are always defined, even if they are not required.

To extract public facing props, i.e. props that the parent is allowed to pass, use [`ExtractPublicPropTypes`](#extractpublicproptypes).

* **Example**

ts\`\`\`
const propsOptions = {
 foo: String,
 bar: Boolean,
 baz: {
 type: Number,
 required: true
 },
 qux: {
 type: Number,
 default: 1
 }
} as const

type Props = ExtractPropTypes\
// {
// foo?: string,
// bar: boolean,
// baz: number,
// qux: number
// }
\`\`\`

## ExtractPublicPropTypes\ [​](#extractpublicproptypes)

* Only supported in 3\.3\+

Extract prop types from a runtime props options object. The extracted types are public facing \- i.e. the props that the parent is allowed to pass.

* **Example**

ts\`\`\`
const propsOptions = {
 foo: String,
 bar: Boolean,
 baz: {
 type: Number,
 required: true
 },
 qux: {
 type: Number,
 default: 1
 }
} as const

type Props = ExtractPublicPropTypes\
// {
// foo?: string,
// bar?: boolean,
// baz: number,
// qux?: number
// }
\`\`\`

## ComponentCustomProperties [​](#componentcustomproperties)

Used to augment the component instance type to support custom global properties.

* **Example**

ts\`\`\`
import axios from 'axios'

declare module 'vue' {
 interface ComponentCustomProperties {
 $http: typeof axios
 $translate: (key: string) =\> string
 }
}
\`\`\`TIP

Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](/guide/typescript/options-api#augmenting-global-properties) for more details.
* **See also** [Guide \- Augmenting Global Properties](/guide/typescript/options-api#augmenting-global-properties)

## ComponentCustomOptions [​](#componentcustomoptions)

Used to augment the component options type to support custom options.

* **Example**

ts\`\`\`
import { Route } from 'vue\-router'

declare module 'vue' {
 interface ComponentCustomOptions {
 beforeRouteEnter?(to: any, from: any, next: () =\> void): void
 }
}
\`\`\`TIP

Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](/guide/typescript/options-api#augmenting-global-properties) for more details.
* **See also** [Guide \- Augmenting Custom Options](/guide/typescript/options-api#augmenting-custom-options)

## ComponentCustomProps [​](#componentcustomprops)

Used to augment allowed TSX props in order to use non\-declared props on TSX elements.

* **Example**

ts\`\`\`
declare module 'vue' {
 interface ComponentCustomProps {
 hello?: string
 }
}

export {}
\`\`\`tsx\`\`\`
// now works even if hello is not a declared prop
\
\`\`\`TIP

Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](/guide/typescript/options-api#augmenting-global-properties) for more details.

## CSSProperties [​](#cssproperties)

Used to augment allowed values in style property bindings.

* **Example**

Allow any custom CSS property

ts\`\`\`
declare module 'vue' {
 interface CSSProperties {
 \[key: \`\-\-${string}\`]: string
 }
}
\`\`\`tsx\`\`\`
\
\`\`\`html\`\`\`
\\
\`\`\`

TIP

Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](/guide/typescript/options-api#augmenting-global-properties) for more details.

See also

SFC `` tags support linking CSS values to dynamic component state using the `v-bind` CSS function. This allows for custom properties without type augmentation.

* [v\-bind() in CSS](/api/sfc-css-features#v-bind-in-css)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/utility-types.md)



## Server-Side Rendering API | Vue.js

[Read the full article](https://vuejs.org/api/ssr)

# Server\-Side Rendering API [​](#server-side-rendering-api)

## renderToString() [​](#rendertostring)

* **Exported from `vue/server-renderer`**
* **Type**

ts\`\`\`
function renderToString(
 input: App \| VNode,
 context?: SSRContext
): Promise\
\`\`\`
* **Example**

js\`\`\`
import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server\-renderer'

const app = createSSRApp({
 data: () =\> ({ msg: 'hello' }),
 template: \`\{{ msg }}\\`
})

;(async () =\> {
 const html = await renderToString(app)
 console.log(html)
})()
\`\`\`### SSR Context [​](#ssr-context)

You can pass an optional context object, which can be used to record additional data during the render, for example [accessing content of Teleports](/guide/scaling-up/ssr#teleports):

js\`\`\`
const ctx = {}
const html = await renderToString(app, ctx)

console.log(ctx.teleports) // { '\#teleported': 'teleported content' }
\`\`\`Most other SSR APIs on this page also optionally accept a context object. The context object can be accessed in component code via the [useSSRContext](#usessrcontext) helper.
* **See also** [Guide \- Server\-Side Rendering](/guide/scaling-up/ssr)

## renderToNodeStream() [​](#rendertonodestream)

Renders input as a [Node.js Readable stream](https://nodejs.org/api/stream.html#stream_class_stream_readable).

* **Exported from `vue/server-renderer`**
* **Type**

ts\`\`\`
function renderToNodeStream(
 input: App \| VNode,
 context?: SSRContext
): Readable
\`\`\`
* **Example**

js\`\`\`
// inside a Node.js http handler
renderToNodeStream(app).pipe(res)
\`\`\`Note

This method is not supported in the ESM build of `vue/server-renderer`, which is decoupled from Node.js environments. Use [`pipeToNodeWritable`](#pipetonodewritable) instead.

## pipeToNodeWritable() [​](#pipetonodewritable)

Render and pipe to an existing [Node.js Writable stream](https://nodejs.org/api/stream.html#stream_writable_streams) instance.

* **Exported from `vue/server-renderer`**
* **Type**

ts\`\`\`
function pipeToNodeWritable(
 input: App \| VNode,
 context: SSRContext = {},
 writable: Writable
): void
\`\`\`
* **Example**

js\`\`\`
// inside a Node.js http handler
pipeToNodeWritable(app, {}, res)
\`\`\`

## renderToWebStream() [​](#rendertowebstream)

Renders input as a [Web ReadableStream](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API).

* **Exported from `vue/server-renderer`**
* **Type**

ts\`\`\`
function renderToWebStream(
 input: App \| VNode,
 context?: SSRContext
): ReadableStream
\`\`\`
* **Example**

js\`\`\`
// inside an environment with ReadableStream support
return new Response(renderToWebStream(app))
\`\`\`Note

In environments that do not expose `ReadableStream` constructor in the global scope, [`pipeToWebWritable()`](#pipetowebwritable) should be used instead.

## pipeToWebWritable() [​](#pipetowebwritable)

Render and pipe to an existing [Web WritableStream](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream) instance.

* **Exported from `vue/server-renderer`**
* **Type**

ts\`\`\`
function pipeToWebWritable(
 input: App \| VNode,
 context: SSRContext = {},
 writable: WritableStream
): void
\`\`\`
* **Example**

This is typically used in combination with [`TransformStream`](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream):

js\`\`\`
// TransformStream is available in environments such as CloudFlare workers.
// in Node.js, TransformStream needs to be explicitly imported from 'stream/web'
const { readable, writable } = new TransformStream()
pipeToWebWritable(app, {}, writable)

return new Response(readable)
\`\`\`

## renderToSimpleStream() [​](#rendertosimplestream)

Renders input in streaming mode using a simple readable interface.

* **Exported from `vue/server-renderer`**
* **Type**

ts\`\`\`
function renderToSimpleStream(
 input: App \| VNode,
 context: SSRContext,
 options: SimpleReadable
): SimpleReadable

interface SimpleReadable {
 push(content: string \| null): void
 destroy(err: any): void
}
\`\`\`
* **Example**

js\`\`\`
let res = ''

renderToSimpleStream(
 app,
 {},
 {
 push(chunk) {
 if (chunk === null) {
 // done
 console(\`render complete: ${res}\`)
 } else {
 res \+= chunk
 }
 },
 destroy(err) {
 // error encountered
 }
 }
)
\`\`\`

## useSSRContext() [​](#usessrcontext)

A runtime API used to retrieve the context object passed to `renderToString()` or other server render APIs.

* **Type**

ts\`\`\`
function useSSRContext\\>(): T \| undefined
\`\`\`
* **Example**

The retrieved context can be used to attach information that is needed for rendering the final HTML (e.g. head metadata).

vue\`\`\`
\
import { useSSRContext } from 'vue'

// make sure to only call it during SSR
// https://vitejs.dev/guide/ssr.html\#conditional\-logic
if (import.meta.env.SSR) {
 const ctx = useSSRContext()
 // ...attach properties to the context
}
\
\`\`\`

## data\-allow\-mismatch  [​](#data-allow-mismatch)

A special attribute that can be used to suppress [hydration mismatch](/guide/scaling-up/ssr#hydration-mismatch) warnings.

* **Example**

html\`\`\`
\{{ data.toLocaleString() }}\
\`\`\`The value can limit the allowed mismatch to a specific type. Allowed values are:

	+ `text`
	+ `children` (only allows mismatch for direct children)
	+ `class`
	+ `style`
	+ `attribute`If no value is provided, all types of mismatches will be allowed.
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/ssr.md)



## Quick Start | Vue.js

[Read the full article](https://vuejs.org/guide/quick-start)

# Quick Start [​](#quick-start)

## Try Vue Online [​](#try-vue-online)

* To quickly get a taste of Vue, you can try it directly in our [Playground](https://play.vuejs.org/#eNo9jcEKwjAMhl/lt5fpQYfXUQfefAMvvRQbddC1pUuHUPrudg4HIcmXjyRZXEM4zYlEJ+T0iEPgXjn6BB8Zhp46WUZWDjCa9f6w9kAkTtH9CRinV4fmRtZ63H20Ztesqiylphqy3R5UYBqD1UyVAPk+9zkvV1CKbCv9poMLiTEfR2/IXpSoXomqZLtti/IFwVtA9A==).
* If you prefer a plain HTML setup without any build steps, you can use this [JSFiddle](https://jsfiddle.net/yyx990803/2ke1ab0z/) as your starting point.
* If you are already familiar with Node.js and the concept of build tools, you can also try a complete build setup right within your browser on [StackBlitz](https://vite.new/vue).

## Creating a Vue Application [​](#creating-a-vue-application)

Prerequisites

* Familiarity with the command line
* Install [Node.js](https://nodejs.org/) version 18\.3 or higher
In this section we will introduce how to scaffold a Vue [Single Page Application](/guide/extras/ways-of-using-vue#single-page-application-spa) on your local machine. The created project will be using a build setup based on [Vite](https://vitejs.dev) and allow us to use Vue [Single\-File Components](/guide/scaling-up/sfc) (SFCs).

Make sure you have an up\-to\-date version of [Node.js](https://nodejs.org/) installed and your current working directory is the one where you intend to create a project. Run the following command in your command line (without the `$` sign):

npmpnpmyarnbunsh\`\`\`
$ npm create vue@latest
\`\`\`sh\`\`\`
$ pnpm create vue@latest
\`\`\`sh\`\`\`
\# For Yarn (v1\+)
$ yarn create vue

\# For Yarn Modern (v2\+)
$ yarn create vue@latest

\# For Yarn ^v4\.11
$ yarn dlx create\-vue@latest
\`\`\`sh\`\`\`
$ bun create vue@latest
\`\`\`This command will install and execute [create\-vue](https://github.com/vuejs/create-vue), the official Vue project scaffolding tool. You will be presented with prompts for several optional features such as TypeScript and testing support:

\`\`\`
✔ Project name: … \
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes
✔ Add Pinia for state management? … No / Yes
✔ Add Vitest for Unit testing? … No / Yes
✔ Add an End\-to\-End Testing Solution? … No / Cypress / Nightwatch / Playwright
✔ Add ESLint for code quality? … No / Yes
✔ Add Prettier for code formatting? … No / Yes
✔ Add Vue DevTools 7 extension for debugging? (experimental) … No / Yes

Scaffolding project in ./\...
Done.
\`\`\`If you are unsure about an option, simply choose `No` by hitting enter for now. Once the project is created, follow the instructions to install dependencies and start the dev server:

npmpnpmyarnbunsh\`\`\`
$ cd \
$ npm install
$ npm run dev
\`\`\`sh\`\`\`
$ cd \
$ pnpm install
$ pnpm run dev
\`\`\`sh\`\`\`
$ cd \
$ yarn
$ yarn dev
\`\`\`sh\`\`\`
$ cd \
$ bun install
$ bun run dev
\`\`\`You should now have your first Vue project running! Note that the example components in the generated project are written using the [Composition API](/guide/introduction#composition-api) and ``, rather than the [Options API](/guide/introduction#options-api). Here are some additional tips:

* The recommended IDE setup is [Visual Studio Code](https://code.visualstudio.com/) \+ [Vue \- Official extension](https://marketplace.visualstudio.com/items?itemName=Vue.volar). If you use other editors, check out the [IDE support section](/guide/scaling-up/tooling#ide-support).
* More tooling details, including integration with backend frameworks, are discussed in the [Tooling Guide](/guide/scaling-up/tooling).
* To learn more about the underlying build tool Vite, check out the [Vite docs](https://vitejs.dev).
* If you choose to use TypeScript, check out the [TypeScript Usage Guide](/guide/typescript/overview).

When you are ready to ship your app to production, run the following:

npmpnpmyarnbunsh\`\`\`
$ npm run build
\`\`\`sh\`\`\`
$ pnpm run build
\`\`\`sh\`\`\`
$ yarn build
\`\`\`sh\`\`\`
$ bun run build
\`\`\`This will create a production\-ready build of your app in the project's `./dist` directory. Check out the [Production Deployment Guide](/guide/best-practices/production-deployment) to learn more about shipping your app to production.

[Next Steps \>](#next-steps)

## Using Vue from CDN [​](#using-vue-from-cdn)

You can use Vue directly from a CDN via a script tag:

html\`\`\`
\\
\`\`\`Here we are using [unpkg](https://unpkg.com/), but you can also use any CDN that serves npm packages, for example [jsdelivr](https://www.jsdelivr.com/package/npm/vue) or [cdnjs](https://cdnjs.com/libraries/vue). Of course, you can also download this file and serve it yourself.

When using Vue from a CDN, there is no "build step" involved. This makes the setup a lot simpler, and is suitable for enhancing static HTML or integrating with a backend framework. However, you won't be able to use the Single\-File Component (SFC) syntax.

### Using the Global Build [​](#using-the-global-build)

The above link loads the *global build* of Vue, where all top\-level APIs are exposed as properties on the global `Vue` object. Here is a full example using the global build:

html\`\`\`
\\

\{{ message }}\

\
 const { createApp } = Vue

 createApp({
 data() {
 return {
 message: 'Hello Vue!'
 }
 }
 }).mount('\#app')
\
\`\`\`[CodePen Demo \>](https://codepen.io/vuejs-examples/pen/QWJwJLp)

html\`\`\`
\\

\{{ message }}\

\
 const { createApp, ref } = Vue

 createApp({
 setup() {
 const message = ref('Hello vue!')
 return {
 message
 }
 }
 }).mount('\#app')
\
\`\`\`[CodePen Demo \>](https://codepen.io/vuejs-examples/pen/eYQpQEG)

TIP

Many of the examples for Composition API throughout the guide will be using the `` syntax, which requires build tools. If you intend to use Composition API without a build step, consult the usage of the [`setup()` option](/api/composition-api-setup).

### Using the ES Module Build [​](#using-the-es-module-build)

Throughout the rest of the documentation, we will be primarily using [ES modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) syntax. Most modern browsers now support ES modules natively, so we can use Vue from a CDN via native ES modules like this:

html\`\`\`
\{{ message }}\

\
 import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm\-browser.js'

 createApp({
 data() {
 return {
 message: 'Hello Vue!'
 }
 }
 }).mount('\#app')
\
\`\`\`html\`\`\`
\{{ message }}\

\
 import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm\-browser.js'

 createApp({
 setup() {
 const message = ref('Hello Vue!')
 return {
 message
 }
 }
 }).mount('\#app')
\
\`\`\`Notice that we are using ``, and the imported CDN URL is pointing to the **ES modules build** of Vue instead.

[CodePen Demo \>](https://codepen.io/vuejs-examples/pen/VwVYVZO)

[CodePen Demo \>](https://codepen.io/vuejs-examples/pen/MWzazEv)

### Enabling Import maps [​](#enabling-import-maps)

In the above example, we are importing from the full CDN URL, but in the rest of the documentation you will see code like this:

js\`\`\`
import { createApp } from 'vue'
\`\`\`We can teach the browser where to locate the `vue` import by using [Import Maps](https://caniuse.com/import-maps):

html\`\`\`
\
 {
 "imports": {
 "vue": "https://unpkg.com/vue@3/dist/vue.esm\-browser.js"
 }
 }
\

\{{ message }}\

\
 import { createApp } from 'vue'

 createApp({
 data() {
 return {
 message: 'Hello Vue!'
 }
 }
 }).mount('\#app')
\
\`\`\`[CodePen Demo \>](https://codepen.io/vuejs-examples/pen/wvQKQyM)

html\`\`\`
\
 {
 "imports": {
 "vue": "https://unpkg.com/vue@3/dist/vue.esm\-browser.js"
 }
 }
\

\{{ message }}\

\
 import { createApp, ref } from 'vue'

 createApp({
 setup() {
 const message = ref('Hello Vue!')
 return {
 message
 }
 }
 }).mount('\#app')
\
\`\`\`[CodePen Demo \>](https://codepen.io/vuejs-examples/pen/YzRyRYM)

You can also add entries for other dependencies to the import map \- but make sure they point to the ES modules version of the library you intend to use.

Import Maps Browser Support

Import Maps is a relatively new browser feature. Make sure to use a browser within its [support range](https://caniuse.com/import-maps). In particular, it is only supported in Safari 16\.4\+.

Notes on Production Use

The examples so far are using the development build of Vue \- if you intend to use Vue from a CDN in production, make sure to check out the [Production Deployment Guide](/guide/best-practices/production-deployment#without-build-tools).

While it is possible to use Vue without a build system, an alternative approach to consider is using [`vuejs/petite-vue`](https://github.com/vuejs/petite-vue) that could better suit the context where [`jquery/jquery`](https://github.com/jquery/jquery) (in the past) or [`alpinejs/alpine`](https://github.com/alpinejs/alpine) (in the present) might be used instead.

### Splitting Up the Modules [​](#splitting-up-the-modules)

As we dive deeper into the guide, we may need to split our code into separate JavaScript files so that they are easier to manage. For example:

html\`\`\`
\
\\

\
 import { createApp } from 'vue'
 import MyComponent from './my\-component.js'

 createApp(MyComponent).mount('\#app')
\
\`\`\`js\`\`\`
// my\-component.js
export default {
 data() {
 return { count: 0 }
 },
 template: \`\Count is: {{ count }}\\`
}
\`\`\`js\`\`\`
// my\-component.js
import { ref } from 'vue'
export default {
 setup() {
 const count = ref(0\)
 return { count }
 },
 template: \`\Count is: {{ count }}\\`
}
\`\`\`If you directly open the above `index.html` in your browser, you will find that it throws an error because ES modules cannot work over the `file://` protocol, which is the protocol the browser uses when you open a local file.

Due to security reasons, ES modules can only work over the `http://` protocol, which is what the browsers use when opening pages on the web. In order for ES modules to work on our local machine, we need to serve the `index.html` over the `http://` protocol, with a local HTTP server.

To start a local HTTP server, first make sure you have [Node.js](https://nodejs.org/en/) installed, then run `npx serve` from the command line in the same directory where your HTML file is. You can also use any other HTTP server that can serve static files with the correct MIME types.

You may have noticed that the imported component's template is inlined as a JavaScript string. If you are using VS Code, you can install the [es6\-string\-html](https://marketplace.visualstudio.com/items?itemName=Tobermory.es6-string-html) extension and prefix the strings with a `/*html*/` comment to get syntax highlighting for them.

## Next Steps [​](#next-steps)

If you skipped the [Introduction](/guide/introduction), we strongly recommend reading it before moving on to the rest of the documentation.

[Continue with the Guide

The guide walks you through every aspect of the framework in full detail.](/guide/essentials/application)[Try the Tutorial

For those who prefer learning things hands\-on.](/tutorial/)[Check out the Examples

Explore examples of core features and common UI tasks.](/examples/)[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/quick-start.md)



## State Management | Vue.js

[Read the full article](https://vuejs.org/guide/scaling-up/state-management)

# State Management [​](#state-management)

## What is State Management? [​](#what-is-state-management)

Technically, every Vue component instance already "manages" its own reactive state. Take a simple counter component as an example:

vue\`\`\`
\
import { ref } from 'vue'

// state
const count = ref(0\)

// actions
function increment() {
 count.value\+\+
}
\

\
\{{ count }}\
\`\`\`vue\`\`\`
\
export default {
 // state
 data() {
 return {
 count: 0
 }
 },
 // actions
 methods: {
 increment() {
 this.count\+\+
 }
 }
}
\

\
\{{ count }}\
\`\`\`It is a self\-contained unit with the following parts:

* The **state**, the source of truth that drives our app;
* The **view**, a declarative mapping of the **state**;
* The **actions**, the possible ways the state could change in reaction to user inputs from the **view**.

This is a simple representation of the concept of "one\-way data flow":



However, the simplicity starts to break down when we have **multiple components that share a common state**:

1. Multiple views may depend on the same piece of state.
2. Actions from different views may need to mutate the same piece of state.

For case one, a possible workaround is by "lifting" the shared state up to a common ancestor component, and then pass it down as props. However, this quickly gets tedious in component trees with deep hierarchies, leading to another problem known as [Prop Drilling](/guide/components/provide-inject#prop-drilling).

For case two, we often find ourselves resorting to solutions such as reaching for direct parent / child instances via template refs, or trying to mutate and synchronize multiple copies of the state via emitted events. Both of these patterns are brittle and quickly lead to unmaintainable code.

A simpler and more straightforward solution is to extract the shared state out of the components, and manage it in a global singleton. With this, our component tree becomes a big "view", and any component can access the state or trigger actions, no matter where they are in the tree!

## Simple State Management with Reactivity API [​](#simple-state-management-with-reactivity-api)

In Options API, reactive data is declared using the `data()` option. Internally, the object returned by `data()` is made reactive via the [`reactive()`](/api/reactivity-core#reactive) function, which is also available as a public API.

If you have a piece of state that should be shared by multiple instances, you can use [`reactive()`](/api/reactivity-core#reactive) to create a reactive object, and then import it into multiple components:

js\`\`\`
// store.js
import { reactive } from 'vue'

export const store = reactive({
 count: 0
})
\`\`\`vue\`\`\`
\
\
import { store } from './store.js'
\

\From A: {{ store.count }}\
\`\`\`vue\`\`\`
\
\
import { store } from './store.js'
\

\From B: {{ store.count }}\
\`\`\`vue\`\`\`
\
\
import { store } from './store.js'

export default {
 data() {
 return {
 store
 }
 }
}
\

\From A: {{ store.count }}\
\`\`\`vue\`\`\`
\
\
import { store } from './store.js'

export default {
 data() {
 return {
 store
 }
 }
}
\

\From B: {{ store.count }}\
\`\`\`Now whenever the `store` object is mutated, both `` and `` will update their views automatically \- we have a single source of truth now.

However, this also means any component importing `store` can mutate it however they want:

template\`\`\`
\
 \
 From B: {{ store.count }}
 \
\
\`\`\`While this works in simple cases, global state that can be arbitrarily mutated by any component is not going to be very maintainable in the long run. To ensure the state\-mutating logic is centralized like the state itself, it is recommended to define methods on the store with names that express the intention of the actions:

js\`\`\`
// store.js
import { reactive } from 'vue'

export const store = reactive({
 count: 0,
 increment() {
 this.count\+\+
 }
})
\`\`\`template\`\`\`
\
 \
 From B: {{ store.count }}
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNrNkk1uwyAQha8yYpNEiUzXllPVrtRTeJNSqtLGgGBsVbK4ewdwnT9FWWSTFczwmPc+xMhqa4uhl6xklRdOWQQvsbfPrVadNQ7h1dCqpcYaPp3pYFHwQyteXVxKm0tpM0krnm3IgAqUnd3vUFIFUB1Z8bNOkzoVny+wDTuNcZ1gBI/GSQhzqlQX3/5Gng81pA1t33tEo+FF7JX42bYsT1BaONlRguWqZZMU4C261CWMk3EhTK8RQphm8Twse/BscoUsvdqDkTX3kP3nI6aZwcmdQDUcMPJPabX8TQphtCf0RLqd1csxuqQAJTxtYnEUGtIpAH4pn1Ou17FDScOKhT+QNAVM)

[Try it in the Playground](https://play.vuejs.org/#eNrdU8FqhDAU/JVHLruyi+lZ3FIt9Cu82JilaTWR5CkF8d8bE5O1u1so9FYQzAyTvJnRTKTo+3QcOMlIbpgWPT5WUnS90gjPyr4ll1jAWasOdim9UMum3a20vJWWqxSgkvzTyRt+rocWYVpYFoQm8wRsJh+viHLBcyXtk9No2ALkXd/WyC0CyDfW6RVTOiancQM5ku+x7nUxgUGlOcwxn8Ppu7HJ7udqaqz3SYikOQ5aBgT+OA9slt9kasToFnb5OiAqCU+sFezjVBHvRUimeWdT7JOKrFKAl8VvYatdI6RMDRJhdlPtWdQf5mdQP+SHdtyX/IftlH9pJyS1vcQ2NK8ZivFSiL8BsQmmpMG1s1NU79frYA1k8OD+/I3pUA6+CeNdHg6hmoTMX9pPSnk=)

TIP

Note the click handler uses `store.increment()` with parentheses \- this is necessary to call the method with the proper `this` context since it's not a component method.

Although here we are using a single reactive object as a store, you can also share reactive state created using other [Reactivity APIs](/api/reactivity-core) such as `ref()` or `computed()`, or even return global state from a [Composable](/guide/reusability/composables):

js\`\`\`
import { ref } from 'vue'

// global state, created in module scope
const globalCount = ref(1\)

export function useCount() {
 // local state, created per\-component
 const localCount = ref(1\)

 return {
 globalCount,
 localCount
 }
}
\`\`\`The fact that Vue's reactivity system is decoupled from the component model makes it extremely flexible.

## SSR Considerations [​](#ssr-considerations)

If you are building an application that leverages [Server\-Side Rendering (SSR)](/guide/scaling-up/ssr), the above pattern can lead to issues due to the store being a singleton shared across multiple requests. This is discussed in [more details](/guide/scaling-up/ssr#cross-request-state-pollution) in the SSR guide.

## Pinia [​](#pinia)

While our hand\-rolled state management solution will suffice in simple scenarios, there are many more things to consider in large\-scale production applications:

* Stronger conventions for team collaboration
* Integrating with the Vue DevTools, including timeline, in\-component inspection, and time\-travel debugging
* Hot Module Replacement
* Server\-Side Rendering support

[Pinia](https://pinia.vuejs.org) is a state management library that implements all of the above. It is maintained by the Vue core team, and works with both Vue 2 and Vue 3\.

Existing users may be familiar with [Vuex](https://vuex.vuejs.org/), the previous official state management library for Vue. With Pinia serving the same role in the ecosystem, Vuex is now in maintenance mode. It still works, but will no longer receive new features. It is recommended to use Pinia for new applications.

Pinia started out as an exploration of what the next iteration of Vuex could look like, incorporating many ideas from core team discussions for Vuex 5\. Eventually, we realized that Pinia already implements most of what we wanted in Vuex 5, and decided to make it the new recommendation instead.

Compared to Vuex, Pinia provides a simpler API with less ceremony, offers Composition\-API\-style APIs, and most importantly, has solid type inference support when used with TypeScript.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/scaling-up/state-management.md)



## Render Function APIs | Vue.js

[Read the full article](https://vuejs.org/api/render-function)

# Render Function APIs [​](#render-function-apis)

## h() [​](#h)

Creates virtual DOM nodes (vnodes).

* **Type**

ts\`\`\`
// full signature
function h(
 type: string \| Component,
 props?: object \| null,
 children?: Children \| Slot \| Slots
): VNode

// omitting props
function h(type: string \| Component, children?: Children \| Slot): VNode

type Children = string \| number \| boolean \| VNode \| null \| Children\[]

type Slot = () =\> Children

type Slots = { \[name: string]: Slot }
\`\`\`
> Types are simplified for readability.
* **Details**

The first argument can either be a string (for native elements) or a Vue component definition. The second argument is the props to be passed, and the third argument is the children.

When creating a component vnode, the children must be passed as slot functions. A single slot function can be passed if the component expects only the default slot. Otherwise, the slots must be passed as an object of slot functions.

For convenience, the props argument can be omitted when the children is not a slots object.
* **Example**

Creating native elements:

js\`\`\`
import { h } from 'vue'

// all arguments except the type are optional
h('div')
h('div', { id: 'foo' })

// both attributes and properties can be used in props
// Vue automatically picks the right way to assign it
h('div', { class: 'bar', innerHTML: 'hello' })

// class and style have the same object / array
// value support like in templates
h('div', { class: \[foo, { bar }], style: { color: 'red' } })

// event listeners should be passed as onXxx
h('div', { onClick: () =\> {} })

// children can be a string
h('div', { id: 'foo' }, 'hello')

// props can be omitted when there are no props
h('div', 'hello')
h('div', \[h('span', 'hello')])

// children array can contain mixed vnodes and strings
h('div', \['hello', h('span', 'hello')])
\`\`\`Creating components:

js\`\`\`
import Foo from './Foo.vue'

// passing props
h(Foo, {
 // equivalent of some\-prop="hello"
 someProp: 'hello',
 // equivalent of @update="() =\> {}"
 onUpdate: () =\> {}
})

// passing single default slot
h(Foo, () =\> 'default slot')

// passing named slots
// notice the \`null\` is required to avoid
// slots object being treated as props
h(MyComponent, null, {
 default: () =\> 'default slot',
 foo: () =\> h('div', 'foo'),
 bar: () =\> \[h('span', 'one'), h('span', 'two')]
})
\`\`\`
* **See also** [Guide \- Render Functions \- Creating VNodes](/guide/extras/render-function#creating-vnodes)

## mergeProps() [​](#mergeprops)

Merge multiple props objects with special handling for certain props.

* **Type**

ts\`\`\`
function mergeProps(...args: object\[]): object
\`\`\`
* **Details**

`mergeProps()` supports merging multiple props objects with special handling for the following props:

	+ `class`
	+ `style`
	+ `onXxx` event listeners \- multiple listeners with the same name will be merged into an array.If you do not need the merge behavior and want simple overwrites, native object spread can be used instead.
* **Example**

js\`\`\`
import { mergeProps } from 'vue'

const one = {
 class: 'foo',
 onClick: handlerA
}

const two = {
 class: { bar: true },
 onClick: handlerB
}

const merged = mergeProps(one, two)
/\*\*
 {
 class: 'foo bar',
 onClick: \[handlerA, handlerB]
 }
 \*/
\`\`\`

## cloneVNode() [​](#clonevnode)

Clones a vnode.

* **Type**

ts\`\`\`
function cloneVNode(vnode: VNode, extraProps?: object): VNode
\`\`\`
* **Details**

Returns a cloned vnode, optionally with extra props to merge with the original.

Vnodes should be considered immutable once created, and you should not mutate the props of an existing vnode. Instead, clone it with different / extra props.

Vnodes have special internal properties, so cloning them is not as simple as an object spread. `cloneVNode()` handles most of the internal logic.
* **Example**

js\`\`\`
import { h, cloneVNode } from 'vue'

const original = h('div')
const cloned = cloneVNode(original, { id: 'foo' })
\`\`\`

## isVNode() [​](#isvnode)

Checks if a value is a vnode.

* **Type**

ts\`\`\`
function isVNode(value: unknown): boolean
\`\`\`

## resolveComponent() [​](#resolvecomponent)

For manually resolving a registered component by name.

* **Type**

ts\`\`\`
function resolveComponent(name: string): Component \| string
\`\`\`
* **Details**

**Note: you do not need this if you can import the component directly.**

`resolveComponent()` must be called inside either `setup()` or the render function in order to resolve from the correct component context.

If the component is not found, a runtime warning will be emitted, and the name string is returned.
* **Example**

js\`\`\`
import { h, resolveComponent } from 'vue'

export default {
 setup() {
 const ButtonCounter = resolveComponent('ButtonCounter')

 return () =\> {
 return h(ButtonCounter)
 }
 }
}
\`\`\`js\`\`\`
import { h, resolveComponent } from 'vue'

export default {
 render() {
 const ButtonCounter = resolveComponent('ButtonCounter')
 return h(ButtonCounter)
 }
}
\`\`\`
* **See also** [Guide \- Render Functions \- Components](/guide/extras/render-function#components)

## resolveDirective() [​](#resolvedirective)

For manually resolving a registered directive by name.

* **Type**

ts\`\`\`
function resolveDirective(name: string): Directive \| undefined
\`\`\`
* **Details**

**Note: you do not need this if you can import the directive directly.**

`resolveDirective()` must be called inside either `setup()` or the render function in order to resolve from the correct component context.

If the directive is not found, a runtime warning will be emitted, and the function returns `undefined`.
* **See also** [Guide \- Render Functions \- Custom Directives](/guide/extras/render-function#custom-directives)

## withDirectives() [​](#withdirectives)

For adding custom directives to vnodes.

* **Type**

ts\`\`\`
function withDirectives(
 vnode: VNode,
 directives: DirectiveArguments
): VNode

// \[Directive, value, argument, modifiers]
type DirectiveArguments = Array\
\`\`\`
* **Details**

Wraps an existing vnode with custom directives. The second argument is an array of custom directives. Each custom directive is also represented as an array in the form of `[Directive, value, argument, modifiers]`. Tailing elements of the array can be omitted if not needed.
* **Example**

js\`\`\`
import { h, withDirectives } from 'vue'

// a custom directive
const pin = {
 mounted() {
 /\* ... \*/
 },
 updated() {
 /\* ... \*/
 }
}

// \\
const vnode = withDirectives(h('div'), \[
 \[pin, 200, 'top', { animate: true }]
])
\`\`\`
* **See also** [Guide \- Render Functions \- Custom Directives](/guide/extras/render-function#custom-directives)

## withModifiers() [​](#withmodifiers)

For adding built\-in [`v-on` modifiers](/guide/essentials/event-handling#event-modifiers) to an event handler function.

* **Type**

ts\`\`\`
function withModifiers(fn: Function, modifiers: ModifierGuardsKeys\[]): Function
\`\`\`
* **Example**

js\`\`\`
import { h, withModifiers } from 'vue'

const vnode = h('button', {
 // equivalent of v\-on:click.stop.prevent
 onClick: withModifiers(() =\> {
 // ...
 }, \['stop', 'prevent'])
})
\`\`\`
* **See also** [Guide \- Render Functions \- Event Modifiers](/guide/extras/render-function#event-modifiers)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/render-function.md)



## Teleport | Vue.js

[Read the full article](https://vuejs.org/guide/built-ins/teleport)

# Teleport [​](#teleport)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-3-teleport?friend=vuejs "Free Vue.js Teleport Lesson")`` is a built\-in component that allows us to "teleport" a part of a component's template into a DOM node that exists outside the DOM hierarchy of that component.

## Basic Usage [​](#basic-usage)

Sometimes a part of a component's template belongs to it logically, but from a visual standpoint, it should be displayed somewhere else in the DOM, perhaps even outside of the Vue application.

The most common example of this is when building a full\-screen modal. Ideally, we want the code for the modal's button and the modal itself to be written within the same single\-file component, since they are both related to the open / close state of the modal. But that means the modal will be rendered alongside the button, deeply nested in the application's DOM hierarchy. This can create some tricky issues when positioning the modal via CSS.

Consider the following HTML structure.

template\`\`\`
\
 \Vue Teleport Example\
 \
 \
 \
\
\`\`\`And here is the implementation of ``:

vue\`\`\`
\
import { ref } from 'vue'

const open = ref(false)
\

\
 \Open Modal\

 \
 \Hello from the modal!\
 \Close\
 \
\

\
.modal {
 position: fixed;
 z\-index: 999;
 top: 20%;
 left: 50%;
 width: 300px;
 margin\-left: \-150px;
}
\
\`\`\`vue\`\`\`
\
export default {
 data() {
 return {
 open: false
 }
 }
}
\

\
 \Open Modal\

 \
 \Hello from the modal!\
 \Close\
 \
\

\
.modal {
 position: fixed;
 z\-index: 999;
 top: 20%;
 left: 50%;
 width: 300px;
 margin\-left: \-150px;
}
\
\`\`\`The component contains a `` to trigger the opening of the modal, and a `` with a class of `.modal`, which will contain the modal's content and a button to self\-close.

When using this component inside the initial HTML structure, there are a number of potential issues:

* `position: fixed` only places the element relative to the viewport when no ancestor element has `transform`, `perspective` or `filter` property set. If, for example, we intend to animate the ancestor `` with a CSS transform, it would break the modal layout!
* The modal's `z-index` is constrained by its containing elements. If there is another element that overlaps with `` and has a higher `z-index`, it would cover our modal.

`` provides a clean way to work around these, by allowing us to break out of the nested DOM structure. Let's modify `` to use ``:

template\`\`\`
\Open Modal\

\
 \
 \Hello from the modal!\
 \Close\
 \
\
\`\`\`The `to` target of `` expects a CSS selector string or an actual DOM node. Here, we are essentially telling Vue to "**teleport** this template fragment **to** the **`body`** tag".

You can click the button below and inspect the `` tag via your browser's devtools:

Open ModalYou can combine `` with [``](/guide/built-ins/transition) to create animated modals \- see [Example here](/examples/#modal).

TIP

The teleport `to` target must be already in the DOM when the `` component is mounted. Ideally, this should be an element outside the entire Vue application. If targeting another element rendered by Vue, you need to make sure that element is mounted before the ``.

## Using with Components [​](#using-with-components)

`` only alters the rendered DOM structure \- it does not affect the logical hierarchy of the components. That is to say, if `` contains a component, that component will remain a logical child of the parent component containing the ``. Props passing and event emitting will continue to work the same way.

This also means that injections from a parent component work as expected, and that the child component will be nested below the parent component in the Vue Devtools, instead of being placed where the actual content moved to.

## Disabling Teleport [​](#disabling-teleport)

In some cases, we may want to conditionally disable ``. For example, we may want to render a component as an overlay for desktop, but inline on mobile. `` supports the `disabled` prop which can be dynamically toggled:

template\`\`\`
\
 ...
\
\`\`\`We could then dynamically update `isMobile`.

## Multiple Teleports on the Same Target [​](#multiple-teleports-on-the-same-target)

A common use case would be a reusable `` component, with the potential for multiple instances to be active at the same time. For this kind of scenario, multiple `` components can mount their content to the same target element. The order will be a simple append, with later mounts located after earlier ones, but all within the target element.

Given the following usage:

template\`\`\`
\
 \A\
\
\
 \B\
\
\`\`\`The rendered result would be:

html\`\`\`
\
 \A\
 \B\
\
\`\`\`## Deferred Teleport  [​](#deferred-teleport)

In Vue 3\.5 and above, we can use the `defer` prop to defer the target resolving of a Teleport until other parts of the application have mounted. This allows the Teleport to target a container element that is rendered by Vue, but in a later part of the component tree:

template\`\`\`
\...\

\
\\
\`\`\`Note that the target element must be rendered in the same mount / update tick with the Teleport \- i.e. if the `` is only mounted a second later, the Teleport will still report an error. The defer works similarly to the `mounted` lifecycle hook.

---

**Related**

* [`` API reference](/api/built-in-components#teleport)
* [Handling Teleports in SSR](/guide/scaling-up/ssr#teleports)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/built-ins/teleport.md)



## <script setup> | Vue.js

[Read the full article](https://vuejs.org/api/sfc-script-setup)

# \ [​](#script-setup)

`` is a compile\-time syntactic sugar for using Composition API inside Single\-File Components (SFCs). It is the recommended syntax if you are using both SFCs and Composition API. It provides a number of advantages over the normal `` syntax:

* More succinct code with less boilerplate
* Ability to declare props and emitted events using pure TypeScript
* Better runtime performance (the template is compiled into a render function in the same scope, without an intermediate proxy)
* Better IDE type\-inference performance (less work for the language server to extract types from code)

## Basic Syntax [​](#basic-syntax)

To opt\-in to the syntax, add the `setup` attribute to the `` block:

vue\`\`\`
\
console.log('hello script setup')
\
\`\`\`The code inside is compiled as the content of the component's `setup()` function. This means that unlike normal ``, which only executes once when the component is first imported, code inside `` will **execute every time an instance of the component is created**.

### Top\-level bindings are exposed to template [​](#top-level-bindings-are-exposed-to-template)

When using ``, any top\-level bindings (including variables, function declarations, and imports) declared inside `` are directly usable in the template:

vue\`\`\`
\
// variable
const msg = 'Hello!'

// functions
function log() {
 console.log(msg)
}
\

\
 \{{ msg }}\
\
\`\`\`Imports are exposed in the same fashion. This means you can directly use an imported helper function in template expressions without having to expose it via the `methods` option:

vue\`\`\`
\
import { capitalize } from './helpers'
\

\
 \{{ capitalize('hello') }}\
\
\`\`\`## Reactivity [​](#reactivity)

Reactive state needs to be explicitly created using [Reactivity APIs](/api/reactivity-core). Similar to values returned from a `setup()` function, refs are automatically unwrapped when referenced in templates:

vue\`\`\`
\
import { ref } from 'vue'

const count = ref(0\)
\

\
 \{{ count }}\
\
\`\`\`## Using Components [​](#using-components)

Values in the scope of `` can also be used directly as custom component tag names:

vue\`\`\`
\
import MyComponent from './MyComponent.vue'
\

\
 \
\
\`\`\`Think of `MyComponent` as being referenced as a variable. If you have used JSX, the mental model is similar here. The kebab\-case equivalent `` also works in the template \- however PascalCase component tags are strongly recommended for consistency. It also helps differentiating from native custom elements.

### Dynamic Components [​](#dynamic-components)

Since components are referenced as variables instead of registered under string keys, we should use dynamic `:is` binding when using dynamic components inside ``:

vue\`\`\`
\
import Foo from './Foo.vue'
import Bar from './Bar.vue'
\

\
 \
 \
\
\`\`\`Note how the components can be used as variables in a ternary expression.

### Recursive Components [​](#recursive-components)

An SFC can implicitly refer to itself via its filename. E.g. a file named `FooBar.vue` can refer to itself as `` in its template.

Note this has lower priority than imported components. If you have a named import that conflicts with the component's inferred name, you can alias the import:

js\`\`\`
import { FooBar as FooBarChild } from './components'
\`\`\`### Namespaced Components [​](#namespaced-components)

You can use component tags with dots like `` to refer to components nested under object properties. This is useful when you import multiple components from a single file:

vue\`\`\`
\
import \* as Form from './form\-components'
\

\
 \
 \label\
 \
\
\`\`\`## Using Custom Directives [​](#using-custom-directives)

Globally registered custom directives just work as normal. Local custom directives don't need to be explicitly registered with ``, but they must follow the naming scheme `vNameOfDirective`:

vue\`\`\`
\
const vMyDirective = {
 beforeMount: (el) =\> {
 // do something with the element
 }
}
\
\
 \This is a Heading\
\
\`\`\`If you're importing a directive from elsewhere, it can be renamed to fit the required naming scheme:

vue\`\`\`
\
import { myDirective as vMyDirective } from './MyDirective.js'
\
\`\`\`## defineProps() \& defineEmits() [​](#defineprops-defineemits)

To declare options like `props` and `emits` with full type inference support, we can use the `defineProps` and `defineEmits` APIs, which are automatically available inside ``:

vue\`\`\`
\
const props = defineProps({
 foo: String
})

const emit = defineEmits(\['change', 'delete'])
// setup code
\
\`\`\`* `defineProps` and `defineEmits` are **compiler macros** only usable inside ``. They do not need to be imported, and are compiled away when `` is processed.
* `defineProps` accepts the same value as the `props` option, while `defineEmits` accepts the same value as the `emits` option.
* `defineProps` and `defineEmits` provide proper type inference based on the options passed.
* The options passed to `defineProps` and `defineEmits` will be hoisted out of setup into module scope. Therefore, the options cannot reference local variables declared in setup scope. Doing so will result in a compile error. However, it *can* reference imported bindings since they are in the module scope as well.

### Type\-only props/emit declarations [​](#type-only-props-emit-declarations)

Props and emits can also be declared using pure\-type syntax by passing a literal type argument to `defineProps` or `defineEmits`:

ts\`\`\`
const props = defineProps\()

const emit = defineEmits\()

// 3\.3\+: alternative, more succinct syntax
const emit = defineEmits\()
\`\`\`* `defineProps` or `defineEmits` can only use either runtime declaration OR type declaration. Using both at the same time will result in a compile error.
* When using type declaration, the equivalent runtime declaration is automatically generated from static analysis to remove the need for double declaration and still ensure correct runtime behavior.

	+ In dev mode, the compiler will try to infer corresponding runtime validation from the types. For example here `foo: String` is inferred from the `foo: string` type. If the type is a reference to an imported type, the inferred result will be `foo: null` (equal to `any` type) since the compiler does not have information of external files.
	+ In prod mode, the compiler will generate the array format declaration to reduce bundle size (the props here will be compiled into `['foo', 'bar']`)
* In version 3\.2 and below, the generic type parameter for `defineProps()` were limited to a type literal or a reference to a local interface.

This limitation has been resolved in 3\.3\. The latest version of Vue supports referencing imported and a limited set of complex types in the type parameter position. However, because the type to runtime conversion is still AST\-based, some complex types that require actual type analysis, e.g. conditional types, are not supported. You can use conditional types for the type of a single prop, but not the entire props object.

### Reactive Props Destructure  [​](#reactive-props-destructure)

In Vue 3\.5 and above, variables destructured from the return value of `defineProps` are reactive. Vue's compiler automatically prepends `props.` when code in the same `` block accesses variables destructured from `defineProps`:

ts\`\`\`
const { foo } = defineProps(\['foo'])

watchEffect(() =\> {
 // runs only once before 3\.5
 // re\-runs when the "foo" prop changes in 3\.5\+
 console.log(foo)
})
\`\`\`The above is compiled to the following equivalent:

js\`\`\`
const props = defineProps(\['foo'])

watchEffect(() =\> {
 // \`foo\` transformed to \`props.foo\` by the compiler
 console.log(props.foo)
})
\`\`\`In addition, you can use JavaScript's native default value syntax to declare default values for the props. This is particularly useful when using the type\-based props declaration:

ts\`\`\`
interface Props {
 msg?: string
 labels?: string\[]
}

const { msg = 'hello', labels = \['one', 'two'] } = defineProps\()
\`\`\`### Default props values when using type declaration  [​](#default-props-values-when-using-type-declaration)

In 3\.5 and above, default values can be naturally declared when using Reactive Props Destructure. But in 3\.4 and below, Reactive Props Destructure is not enabled by default. In order to declare props default values with type\-based declaration, the `withDefaults` compiler macro is needed:

ts\`\`\`
interface Props {
 msg?: string
 labels?: string\[]
}

const props = withDefaults(defineProps\(), {
 msg: 'hello',
 labels: () =\> \['one', 'two']
})
\`\`\`This will be compiled to equivalent runtime props `default` options. In addition, the `withDefaults` helper provides type checks for the default values, and ensures the returned `props` type has the optional flags removed for properties that do have default values declared.

INFO

Note that default values for mutable reference types (like arrays or objects) should be wrapped in functions when using `withDefaults` to avoid accidental modification and external side effects. This ensures each component instance gets its own copy of the default value. This is **not** necessary when using default values with destructure.

## defineModel() [​](#definemodel)

* Only available in 3\.4\+

This macro can be used to declare a two\-way binding prop that can be consumed via `v-model` from the parent component. Example usage is also discussed in the [Component `v-model`](/guide/components/v-model) guide.

Under the hood, this macro declares a model prop and a corresponding value update event. If the first argument is a literal string, it will be used as the prop name; Otherwise the prop name will default to `"modelValue"`. In both cases, you can also pass an additional object which can include the prop's options and the model ref's value transform options.

js\`\`\`
// declares "modelValue" prop, consumed by parent via v\-model
const model = defineModel()
// OR: declares "modelValue" prop with options
const model = defineModel({ type: String })

// emits "update:modelValue" when mutated
model.value = 'hello'

// declares "count" prop, consumed by parent via v\-model:count
const count = defineModel('count')
// OR: declares "count" prop with options
const count = defineModel('count', { type: Number, default: 0 })

function inc() {
 // emits "update:count" when mutated
 count.value\+\+
}
\`\`\`WARNING

If you have a `default` value for `defineModel` prop and you don't provide any value for this prop from the parent component, it can cause a de\-synchronization between parent and child components. In the example below, the parent's `myRef` is undefined, but the child's `model` is 1:

js\`\`\`
// child component:
const model = defineModel({ default: 1 })

// parent component:
const myRef = ref()
\`\`\`html\`\`\`
\\
\`\`\`### Modifiers and Transformers [​](#modifiers-and-transformers)

To access modifiers used with the `v-model` directive, we can destructure the return value of `defineModel()` like this:

js\`\`\`
const \[modelValue, modelModifiers] = defineModel()

// corresponds to v\-model.trim
if (modelModifiers.trim) {
 // ...
}
\`\`\`When a modifier is present, we likely need to transform the value when reading or syncing it back to the parent. We can achieve this by using the `get` and `set` transformer options:

js\`\`\`
const \[modelValue, modelModifiers] = defineModel({
 // get() omitted as it is not needed here
 set(value) {
 // if the .trim modifier is used, return trimmed value
 if (modelModifiers.trim) {
 return value.trim()
 }
 // otherwise, return the value as\-is
 return value
 }
})
\`\`\`### Usage with TypeScript  [​](#usage-with-typescript)

Like `defineProps` and `defineEmits`, `defineModel` can also receive type arguments to specify the types of the model value and the modifiers:

ts\`\`\`
const modelValue = defineModel\()
// ^? Ref\

// default model with options, required removes possible undefined values
const modelValue = defineModel\({ required: true })
// ^? Ref\

const \[modelValue, modifiers] = defineModel\()
// ^? Record\
\`\`\`## defineExpose() [​](#defineexpose)

Components using `` are **closed by default** \- i.e. the public instance of the component, which is retrieved via template refs or `$parent` chains, will **not** expose any of the bindings declared inside ``.

To explicitly expose properties in a `` component, use the `defineExpose` compiler macro:

vue\`\`\`
\
import { ref } from 'vue'

const a = 1
const b = ref(2\)

defineExpose({
 a,
 b
})
\
\`\`\`When a parent gets an instance of this component via template refs, the retrieved instance will be of the shape `{ a: number, b: number }` (refs are automatically unwrapped just like on normal instances).

## defineOptions() [​](#defineoptions)

* Only supported in 3\.3\+

This macro can be used to declare component options directly inside `` without having to use a separate `` block:

vue\`\`\`
\
defineOptions({
 inheritAttrs: false,
 customOptions: {
 /\* ... \*/
 }
})
\
\`\`\`* This is a macro. The options will be hoisted to module scope and cannot access local variables in `` that are not literal constants.

## defineSlots() [​](#defineslots)

* Only supported in 3\.3\+

This macro can be used to provide type hints to IDEs for slot name and props type checking.

`defineSlots()` only accepts a type parameter and no runtime arguments. The type parameter should be a type literal where the property key is the slot name, and the value type is the slot function. The first argument of the function is the props the slot expects to receive, and its type will be used for slot props in the template. The return type is currently ignored and can be `any`, but we may leverage it for slot content checking in the future.

It also returns the `slots` object, which is equivalent to the `slots` object exposed on the setup context or returned by `useSlots()`.

vue\`\`\`
\
const slots = defineSlots\()
\
\`\`\`## `useSlots()` \& `useAttrs()` [​](#useslots-useattrs)

Usage of `slots` and `attrs` inside `` should be relatively rare, since you can access them directly as `$slots` and `$attrs` in the template. In the rare case where you do need them, use the `useSlots` and `useAttrs` helpers respectively:

vue\`\`\`
\
import { useSlots, useAttrs } from 'vue'

const slots = useSlots()
const attrs = useAttrs()
\
\`\`\``useSlots` and `useAttrs` are actual runtime functions that return the equivalent of `setupContext.slots` and `setupContext.attrs`. They can be used in normal composition API functions as well.

## Usage alongside normal `` [​](#usage-alongside-normal-script)

`` can be used alongside normal ``. A normal `` may be needed in cases where we need to:

* Declare options that cannot be expressed in ``, for example `inheritAttrs` or custom options enabled via plugins (Can be replaced by [`defineOptions`](/api/sfc-script-setup#defineoptions) in 3\.3\+).
* Declaring named exports.
* Run side effects or create objects that should only execute once.

vue\`\`\`
\
// normal \, executed in module scope (only once)
runSideEffectOnce()

// declare additional options
export default {
 inheritAttrs: false,
 customOptions: {}
}
\

\
// executed in setup() scope (for each instance)
\
\`\`\`Support for combining `` and `` in the same component is limited to the scenarios described above. Specifically:

* Do **NOT** use a separate `` section for options that can already be defined using ``, such as `props` and `emits`.
* Variables created inside `` are not added as properties to the component instance, making them inaccessible from the Options API. Mixing APIs in this way is strongly discouraged.

If you find yourself in one of the scenarios that is not supported then you should consider switching to an explicit [`setup()`](/api/composition-api-setup) function, instead of using ``.

## Top\-level `await` [​](#top-level-await)

Top\-level `await` can be used inside ``. The resulting code will be compiled as `async setup()`:

vue\`\`\`
\
const post = await fetch(\`/api/post/1\`).then((r) =\> r.json())
\
\`\`\`In addition, the awaited expression will be automatically compiled in a format that preserves the current component instance context after the `await`.

Note

`async setup()` must be used in combination with [`Suspense`](/guide/built-ins/suspense), which is currently still an experimental feature. We plan to finalize and document it in a future release \- but if you are curious now, you can refer to its [tests](https://github.com/vuejs/core/blob/main/packages/runtime-core/__tests__/components/Suspense.spec.ts) to see how it works.

## Import Statements [​](#imports-statements)

Import statements in vue follow [ECMAScript module specification](https://nodejs.org/api/esm.html). In addition, you can use aliases defined in your build tool configuration:

vue\`\`\`
\
import { ref } from 'vue'
import { componentA } from './Components'
import { componentB } from '@/Components'
import { componentC } from '\~/Components'
\
\`\`\`## Generics  [​](#generics)

Generic type parameters can be declared using the `generic` attribute on the `` tag:

vue\`\`\`
\
defineProps\()
\
\`\`\`The value of `generic` works exactly the same as the parameter list between `` in TypeScript. For example, you can use multiple parameters, `extends` constraints, default types, and reference imported types:

vue\`\`\`
\
import type { Item } from './types'
defineProps\()
\
\`\`\`In order to use a reference to a generic component in a `ref` you need to use the [`vue-component-type-helpers`](https://www.npmjs.com/package/vue-component-type-helpers) library as `InstanceType` won't work.

vue\`\`\`
\
import componentWithoutGenerics from '../component\-without\-generics.vue';
import genericComponent from '../generic\-component.vue';

import type { ComponentExposed } from 'vue\-component\-type\-helpers';

// Works for a component without generics
ref\\>();

ref\\>();
\`\`\`## Restrictions [​](#restrictions)

* Due to the difference in module execution semantics, code inside `` relies on the context of an SFC. When moved into external `.js` or `.ts` files, it may lead to confusion for both developers and tools. Therefore, **``** cannot be used with the `src` attribute.
* `` does not support In\-DOM Root Component Template.([Related Discussion](https://github.com/vuejs/core/issues/8391))
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/sfc-script-setup.md)



## Application API | Vue.js

[Read the full article](https://vuejs.org/api/application)

# Application API [​](#application-api)

## createApp() [​](#createapp)

Creates an application instance.

* **Type**

ts\`\`\`
function createApp(rootComponent: Component, rootProps?: object): App
\`\`\`
* **Details**

The first argument is the root component. The second optional argument is the props to be passed to the root component.
* **Example**

With inline root component:

js\`\`\`
import { createApp } from 'vue'

const app = createApp({
 /\* root component options \*/
})
\`\`\`With imported component:

js\`\`\`
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
\`\`\`
* **See also** [Guide \- Creating a Vue Application](/guide/essentials/application)

## createSSRApp() [​](#createssrapp)

Creates an application instance in [SSR Hydration](/guide/scaling-up/ssr#client-hydration) mode. Usage is exactly the same as `createApp()`.

## app.mount() [​](#app-mount)

Mounts the application instance in a container element.

* **Type**

ts\`\`\`
interface App {
 mount(rootContainer: Element \| string): ComponentPublicInstance
}
\`\`\`
* **Details**

The argument can either be an actual DOM element or a CSS selector (the first matched element will be used). Returns the root component instance.

If the component has a template or a render function defined, it will replace any existing DOM nodes inside the container. Otherwise, if the runtime compiler is available, the `innerHTML` of the container will be used as the template.

In SSR hydration mode, it will hydrate the existing DOM nodes inside the container. If there are [mismatches](/guide/scaling-up/ssr#hydration-mismatch), the existing DOM nodes will be morphed to match the expected output.

For each app instance, `mount()` can only be called once.
* **Example**

js\`\`\`
import { createApp } from 'vue'
const app = createApp(/\* ... \*/)

app.mount('\#app')
\`\`\`Can also mount to an actual DOM element:

js\`\`\`
app.mount(document.body.firstChild)
\`\`\`

## app.unmount() [​](#app-unmount)

Unmounts a mounted application instance, triggering the unmount lifecycle hooks for all components in the application's component tree.

* **Type**

ts\`\`\`
interface App {
 unmount(): void
}
\`\`\`

## app.onUnmount()  [​](#app-onunmount)

Registers a callback to be called when the app is unmounted.

* **Type**

ts\`\`\`
interface App {
 onUnmount(callback: () =\> any): void
}
\`\`\`

## app.component() [​](#app-component)

Registers a global component if passing both a name string and a component definition, or retrieves an already registered one if only the name is passed.

* **Type**

ts\`\`\`
interface App {
 component(name: string): Component \| undefined
 component(name: string, component: Component): this
}
\`\`\`
* **Example**

js\`\`\`
import { createApp } from 'vue'

const app = createApp({})

// register an options object
app.component('my\-component', {
 /\* ... \*/
})

// retrieve a registered component
const MyComponent = app.component('my\-component')
\`\`\`
* **See also** [Component Registration](/guide/components/registration)

## app.directive() [​](#app-directive)

Registers a global custom directive if passing both a name string and a directive definition, or retrieves an already registered one if only the name is passed.

* **Type**

ts\`\`\`
interface App {
 directive(name: string): Directive \| undefined
 directive(name: string, directive: Directive): this
}
\`\`\`
* **Example**

js\`\`\`
import { createApp } from 'vue'

const app = createApp({
 /\* ... \*/
})

// register (object directive)
app.directive('my\-directive', {
 /\* custom directive hooks \*/
})

// register (function directive shorthand)
app.directive('my\-directive', () =\> {
 /\* ... \*/
})

// retrieve a registered directive
const myDirective = app.directive('my\-directive')
\`\`\`
* **See also** [Custom Directives](/guide/reusability/custom-directives)

## app.use() [​](#app-use)

Installs a [plugin](/guide/reusability/plugins).

* **Type**

ts\`\`\`
interface App {
 use(plugin: Plugin, ...options: any\[]): this
}
\`\`\`
* **Details**

Expects the plugin as the first argument, and optional plugin options as the second argument.

The plugin can either be an object with an `install()` method, or just a function that will be used as the `install()` method. The options (second argument of `app.use()`) will be passed along to the plugin's `install()` method.

When `app.use()` is called on the same plugin multiple times, the plugin will be installed only once.
* **Example**

js\`\`\`
import { createApp } from 'vue'
import MyPlugin from './plugins/MyPlugin'

const app = createApp({
 /\* ... \*/
})

app.use(MyPlugin)
\`\`\`
* **See also** [Plugins](/guide/reusability/plugins)

## app.mixin() [​](#app-mixin)

Applies a global mixin (scoped to the application). A global mixin applies its included options to every component instance in the application.

Not Recommended

Mixins are supported in Vue 3 mainly for backwards compatibility, due to their widespread use in ecosystem libraries. Use of mixins, especially global mixins, should be avoided in application code.

For logic reuse, prefer [Composables](/guide/reusability/composables) instead.

* **Type**

ts\`\`\`
interface App {
 mixin(mixin: ComponentOptions): this
}
\`\`\`

## app.provide() [​](#app-provide)

Provide a value that can be injected in all descendant components within the application.

* **Type**

ts\`\`\`
interface App {
 provide\(key: InjectionKey\ \| symbol \| string, value: T): this
}
\`\`\`
* **Details**

Expects the injection key as the first argument, and the provided value as the second. Returns the application instance itself.
* **Example**

js\`\`\`
import { createApp } from 'vue'

const app = createApp(/\* ... \*/)

app.provide('message', 'hello')
\`\`\`Inside a component in the application:

js\`\`\`
import { inject } from 'vue'

export default {
 setup() {
 console.log(inject('message')) // 'hello'
 }
}
\`\`\`js\`\`\`
export default {
 inject: \['message'],
 created() {
 console.log(this.message) // 'hello'
 }
}
\`\`\`
* **See also**

	+ [Provide / Inject](/guide/components/provide-inject)
	+ [App\-level Provide](/guide/components/provide-inject#app-level-provide)
	+ [app.runWithContext()](#app-runwithcontext)

## app.runWithContext() [​](#app-runwithcontext)

* Only supported in 3\.3\+

Execute a callback with the current app as injection context.

* **Type**

ts\`\`\`
interface App {
 runWithContext\(fn: () =\> T): T
}
\`\`\`
* **Details**

Expects a callback function and runs the callback immediately. During the synchronous call of the callback, `inject()` calls are able to look up injections from the values provided by the current app, even when there is no current active component instance. The return value of the callback will also be returned.
* **Example**

js\`\`\`
import { inject } from 'vue'

app.provide('id', 1\)

const injected = app.runWithContext(() =\> {
 return inject('id')
})

console.log(injected) // 1
\`\`\`

## app.version [​](#app-version)

Provides the version of Vue that the application was created with. This is useful inside [plugins](/guide/reusability/plugins), where you might need conditional logic based on different Vue versions.

* **Type**

ts\`\`\`
interface App {
 version: string
}
\`\`\`
* **Example**

Performing a version check inside a plugin:

js\`\`\`
export default {
 install(app) {
 const version = Number(app.version.split('.')\[0])
 if (version \ void
}
\`\`\`
* **Details**

The error handler receives three arguments: the error, the component instance that triggered the error, and an information string specifying the error source type.

It can capture errors from the following sources:

	+ Component renders
	+ Event handlers
	+ Lifecycle hooks
	+ `setup()` function
	+ Watchers
	+ Custom directive hooks
	+ Transition hooksTIP

In production, the 3rd argument (`info`) will be a shortened code instead of the full information string. You can find the code to string mapping in the [Production Error Code Reference](/error-reference/#runtime-errors).
* **Example**

js\`\`\`
app.config.errorHandler = (err, instance, info) =\> {
 // handle error, e.g. report to a service
}
\`\`\`

## app.config.warnHandler [​](#app-config-warnhandler)

Assign a custom handler for runtime warnings from Vue.

* **Type**

ts\`\`\`
interface AppConfig {
 warnHandler?: (
 msg: string,
 instance: ComponentPublicInstance \| null,
 trace: string
 ) =\> void
}
\`\`\`
* **Details**

The warning handler receives the warning message as the first argument, the source component instance as the second argument, and a component trace string as the third.

It can be used to filter out specific warnings to reduce console verbosity. All Vue warnings should be addressed during development, so this is only recommended during debug sessions to focus on specific warnings among many, and should be removed once the debugging is done.

TIP

Warnings only work during development, so this config is ignored in production mode.
* **Example**

js\`\`\`
app.config.warnHandler = (msg, instance, trace) =\> {
 // \`trace\` is the component hierarchy trace
}
\`\`\`

## app.config.performance [​](#app-config-performance)

Set this to `true` to enable component init, compile, render and patch performance tracing in the browser devtool performance/timeline panel. Only works in development mode and in browsers that support the [performance.mark](https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark) API.

* **Type:** `boolean`
* **See also** [Guide \- Performance](/guide/best-practices/performance)

## app.config.compilerOptions [​](#app-config-compileroptions)

Configure runtime compiler options. Values set on this object will be passed to the in\-browser template compiler and affect every component in the configured app. Note you can also override these options on a per\-component basis using the [`compilerOptions` option](/api/options-rendering#compileroptions).

Important

This config option is only respected when using the full build (i.e. the standalone `vue.js` that can compile templates in the browser). If you are using the runtime\-only build with a build setup, compiler options must be passed to `@vue/compiler-dom` via build tool configurations instead.

* For `vue-loader`: [pass via the `compilerOptions` loader option](https://vue-loader.vuejs.org/options.html#compileroptions). Also see [how to configure it in `vue-cli`](https://cli.vuejs.org/guide/webpack.html#modifying-options-of-a-loader).
* For `vite`: [pass via `@vitejs/plugin-vue` options](https://github.com/vitejs/vite-plugin-vue/tree/main/packages/plugin-vue#options).
### app.config.compilerOptions.isCustomElement [​](#app-config-compileroptions-iscustomelement)

Specifies a check method to recognize native custom elements.

* **Type:** `(tag: string) => boolean`
* **Details**

Should return `true` if the tag should be treated as a native custom element. For a matched tag, Vue will render it as a native element instead of attempting to resolve it as a Vue component.

Native HTML and SVG tags don't need to be matched in this function \- Vue's parser recognizes them automatically.
* **Example**

js\`\`\`
// treat all tags starting with 'ion\-' as custom elements
app.config.compilerOptions.isCustomElement = (tag) =\> {
 return tag.startsWith('ion\-')
}
\`\`\`
* **See also** [Vue and Web Components](/guide/extras/web-components)

### app.config.compilerOptions.whitespace [​](#app-config-compileroptions-whitespace)

Adjusts template whitespace handling behavior.

* **Type:** `'condense' | 'preserve'`
* **Default:** `'condense'`
* **Details**

Vue removes / condenses whitespace characters in templates to produce more efficient compiled output. The default strategy is "condense", with the following behavior:

	1. Leading / ending whitespace characters inside an element are condensed into a single space.
	2. Whitespace characters between elements that contain newlines are removed.
	3. Consecutive whitespace characters in text nodes are condensed into a single space.Setting this option to `'preserve'` will disable (2\) and (3\).
* **Example**

js\`\`\`
app.config.compilerOptions.whitespace = 'preserve'
\`\`\`

### app.config.compilerOptions.delimiters [​](#app-config-compileroptions-delimiters)

Adjusts the delimiters used for text interpolation within the template.

* **Type:** `[string, string]`
* **Default:** `['{{', '}}']`
* **Details**

This is typically used to avoid conflicting with server\-side frameworks that also use mustache syntax.
* **Example**

js\`\`\`
// Delimiters changed to ES6 template string style
app.config.compilerOptions.delimiters = \['${', '}']
\`\`\`

### app.config.compilerOptions.comments [​](#app-config-compileroptions-comments)

Adjusts treatment of HTML comments in templates.

* **Type:** `boolean`
* **Default:** `false`
* **Details**

By default, Vue will remove the comments in production. Setting this option to `true` will force Vue to preserve comments even in production. Comments are always preserved during development. This option is typically used when Vue is used with other libraries that rely on HTML comments.
* **Example**

js\`\`\`
app.config.compilerOptions.comments = true
\`\`\`

## app.config.globalProperties [​](#app-config-globalproperties)

An object that can be used to register global properties that can be accessed on any component instance inside the application.

* **Type**

ts\`\`\`
interface AppConfig {
 globalProperties: Record\
}
\`\`\`
* **Details**

This is a replacement of Vue 2's `Vue.prototype` which is no longer present in Vue 3\. As with anything global, this should be used sparingly.

If a global property conflicts with a component’s own property, the component's own property will have higher priority.
* **Usage**

js\`\`\`
app.config.globalProperties.msg = 'hello'
\`\`\`This makes `msg` available inside any component template in the application, and also on `this` of any component instance:

js\`\`\`
export default {
 mounted() {
 console.log(this.msg) // 'hello'
 }
}
\`\`\`
* **See also** [Guide \- Augmenting Global Properties](/guide/typescript/options-api#augmenting-global-properties)

## app.config.optionMergeStrategies [​](#app-config-optionmergestrategies)

An object for defining merging strategies for custom component options.

* **Type**

ts\`\`\`
interface AppConfig {
 optionMergeStrategies: Record\
}

type OptionMergeFunction = (to: unknown, from: unknown) =\> any
\`\`\`
* **Details**

Some plugins / libraries add support for custom component options (by injecting global mixins). These options may require special merging logic when the same option needs to be "merged" from multiple sources (e.g. mixins or component inheritance).

A merge strategy function can be registered for a custom option by assigning it on the `app.config.optionMergeStrategies` object using the option's name as the key.

The merge strategy function receives the value of that option defined on the parent and child instances as the first and second arguments, respectively.
* **Example**

js\`\`\`
const app = createApp({
 // option from self
 msg: 'Vue',
 // option from a mixin
 mixins: \[
 {
 msg: 'Hello '
 }
 ],
 mounted() {
 // merged options exposed on this.$options
 console.log(this.$options.msg)
 }
})

// define a custom merge strategy for \`msg\`
app.config.optionMergeStrategies.msg = (parent, child) =\> {
 return (parent \|\| '') \+ (child \|\| '')
}

app.mount('\#app')
// logs 'Hello Vue'
\`\`\`
* **See also** [Component Instance \- `$options`](/api/component-instance#options)

## app.config.idPrefix  [​](#app-config-idprefix)

Configure a prefix for all IDs generated via [useId()](/api/composition-api-helpers#useid) inside this application.

* **Type:** `string`
* **Default:** `undefined`
* **Example**

js\`\`\`
app.config.idPrefix = 'my\-app'
\`\`\`js\`\`\`
// in a component:
const id1 = useId() // 'my\-app:0'
const id2 = useId() // 'my\-app:1'
\`\`\`

## app.config.throwUnhandledErrorInProduction  [​](#app-config-throwunhandlederrorinproduction)

Force unhandled errors to be thrown in production mode.

* **Type:** `boolean`
* **Default:** `false`
* **Details**

By default, errors thrown inside a Vue application but not explicitly handled have different behavior between development and production modes:

	+ In development, the error is thrown and can possibly crash the application. This is to make the error more prominent so that it can be noticed and fixed during development.
	+ In production, the error will only be logged to the console to minimize the impact to end users. However, this may prevent errors that only happen in production from being caught by error monitoring services.By setting `app.config.throwUnhandledErrorInProduction` to `true`, unhandled errors will be thrown even in production mode.
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/application.md)



## Built-in Directives | Vue.js

[Read the full article](https://vuejs.org/api/built-in-directives)

# Built\-in Directives [​](#built-in-directives)

## v\-text [​](#v-text)

Update the element's text content.

* **Expects:** `string`
* **Details**

`v-text` works by setting the element's [textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent) property, so it will overwrite any existing content inside the element. If you need to update the part of `textContent`, you should use [mustache interpolations](/guide/essentials/template-syntax#text-interpolation) instead.
* **Example**

template\`\`\`
\\
\
\{{msg}}\
\`\`\`
* **See also** [Template Syntax \- Text Interpolation](/guide/essentials/template-syntax#text-interpolation)

## v\-html [​](#v-html)

Update the element's [innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML).

* **Expects:** `string`
* **Details**

Contents of `v-html` are inserted as plain HTML \- Vue template syntax will not be processed. If you find yourself trying to compose templates using `v-html`, try to rethink the solution by using components instead.

Security Note

Dynamically rendering arbitrary HTML on your website can be very dangerous because it can easily lead to [XSS attacks](https://en.wikipedia.org/wiki/Cross-site_scripting). Only use `v-html` on trusted content and **never** on user\-provided content.

In [Single\-File Components](/guide/scaling-up/sfc), `scoped` styles will not apply to content inside `v-html`, because that HTML is not processed by Vue's template compiler. If you want to target `v-html` content with scoped CSS, you can instead use [CSS modules](/api/sfc-css-features#css-modules) or an additional, global `` element with a manual scoping strategy such as BEM.
* **Example**

template\`\`\`
\\
\`\`\`
* **See also** [Template Syntax \- Raw HTML](/guide/essentials/template-syntax#raw-html)

## v\-show [​](#v-show)

Toggle the element's visibility based on the truthy\-ness of the expression value.

* **Expects:** `any`
* **Details**

`v-show` works by setting the `display` CSS property via inline styles, and will try to respect the initial `display` value when the element is visible. It also triggers transitions when its condition changes.
* **See also** [Conditional Rendering \- v\-show](/guide/essentials/conditional#v-show)

## v\-if [​](#v-if)

Conditionally render an element or a template fragment based on the truthy\-ness of the expression value.

* **Expects:** `any`
* **Details**

When a `v-if` element is toggled, the element and its contained directives / components are destroyed and re\-constructed. If the initial condition is falsy, then the inner content won't be rendered at all.

Can be used on `` to denote a conditional block containing only text or multiple elements.

This directive triggers transitions when its condition changes.

When used together, `v-if` has a higher priority than `v-for`. We don't recommend using these two directives together on one element — see the [list rendering guide](/guide/essentials/list#v-for-with-v-if) for details.
* **See also** [Conditional Rendering \- v\-if](/guide/essentials/conditional#v-if)

## v\-else [​](#v-else)

Denote the "else block" for `v-if` or a `v-if` / `v-else-if` chain.

* **Does not expect expression**
* **Details**

	+ Restriction: previous sibling element must have `v-if` or `v-else-if`.
	+ Can be used on `` to denote a conditional block containing only text or multiple elements.
* **Example**

template\`\`\`
\ 0\.5"\>
 Now you see me
\
\
 Now you don't
\
\`\`\`
* **See also** [Conditional Rendering \- v\-else](/guide/essentials/conditional#v-else)

## v\-else\-if [​](#v-else-if)

Denote the "else if block" for `v-if`. Can be chained.

* **Expects:** `any`
* **Details**

	+ Restriction: previous sibling element must have `v-if` or `v-else-if`.
	+ Can be used on `` to denote a conditional block containing only text or multiple elements.
* **Example**

template\`\`\`
\
 A
\
\
 B
\
\
 C
\
\
 Not A/B/C
\
\`\`\`
* **See also** [Conditional Rendering \- v\-else\-if](/guide/essentials/conditional#v-else-if)

## v\-for [​](#v-for)

Render the element or template block multiple times based on the source data.

* **Expects:** `Array | Object | number | string | Iterable`
* **Details**

The directive's value must use the special syntax `alias in expression` to provide an alias for the current element being iterated on:

template\`\`\`
\
 {{ item.text }}
\
\`\`\`Alternatively, you can also specify an alias for the index (or the key if used on an Object):

template\`\`\`
\\
\\
\\
\`\`\`The default behavior of `v-for` will try to patch the elements in\-place without moving them. To force it to reorder elements, you should provide an ordering hint with the `key` special attribute:

template\`\`\`
\
 {{ item.text }}
\
\`\`\``v-for` can also work on values that implement the [Iterable Protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol), including native `Map` and `Set`.
* **See also**

	+ [List Rendering](/guide/essentials/list)

## v\-on [​](#v-on)

Attach an event listener to the element.

* **Shorthand:** `@`
* **Expects:** `Function | Inline Statement | Object (without argument)`
* **Argument:** `event` (optional if using Object syntax)
* **Modifiers**

	+ `.stop` \- call `event.stopPropagation()`.
	+ `.prevent` \- call `event.preventDefault()`.
	+ `.capture` \- add event listener in capture mode.
	+ `.self` \- only trigger handler if event was dispatched from this element.
	+ `.{keyAlias}` \- only trigger handler on certain keys.
	+ `.once` \- trigger handler at most once.
	+ `.left` \- only trigger handler for left button mouse events.
	+ `.right` \- only trigger handler for right button mouse events.
	+ `.middle` \- only trigger handler for middle button mouse events.
	+ `.passive` \- attaches a DOM event with `{ passive: true }`.
* **Details**

The event type is denoted by the argument. The expression can be a method name, an inline statement, or omitted if there are modifiers present.

When used on a normal element, it listens to [**native DOM events**](https://developer.mozilla.org/en-US/docs/Web/Events) only. When used on a custom element component, it listens to **custom events** emitted on that child component.

When listening to native DOM events, the method receives the native event as the only argument. If using inline statement, the statement has access to the special `$event` property: `v-on:click="handle('ok', $event)"`.

`v-on` also supports binding to an object of event / listener pairs without an argument. Note when using the object syntax, it does not support any modifiers.
* **Example**

template\`\`\`
\
\\

\
\\

\
\\

\
\\

\
\\

\
\\

\
\\

\
\\

\
\\

\
\

\
\\

\
\\
\`\`\`Listening to custom events on a child component (the handler is called when "my\-event" is emitted on the child):

template\`\`\`
\

\
\
\`\`\`
* **See also**

	+ [Event Handling](/guide/essentials/event-handling)
	+ [Components \- Custom Events](/guide/essentials/component-basics#listening-to-events)

## v\-bind [​](#v-bind)

Dynamically bind one or more attributes, or a component prop to an expression.

* **Shorthand:**

	+ `:` or `.` (when using `.prop` modifier)
	+ Omitting value (when attribute and bound value has the same name, requires 3\.4\+)
* **Expects:** `any (with argument) | Object (without argument)`
* **Argument:** `attrOrProp (optional)`
* **Modifiers**

	+ `.camel` \- transform the kebab\-case attribute name into camelCase.
	+ `.prop` \- force a binding to be set as a DOM property (3\.2\+).
	+ `.attr` \- force a binding to be set as a DOM attribute (3\.2\+).
* **Usage**

When used to bind the `class` or `style` attribute, `v-bind` supports additional value types such as Array or Objects. See linked guide section below for more details.

When setting a binding on an element, Vue by default checks whether the element has the key defined as a property using an `in` operator check. If the property is defined, Vue will set the value as a DOM property instead of an attribute. This should work in most cases, but you can override this behavior by explicitly using `.prop` or `.attr` modifiers. This is sometimes necessary, especially when [working with custom elements](/guide/extras/web-components#passing-dom-properties).

When used for component prop binding, the prop must be properly declared in the child component.

When used without an argument, can be used to bind an object containing attribute name\-value pairs.
* **Example**

template\`\`\`
\
\

\
\\

\
\

\
\

\
\\

\
\

\
\\
\\
\\

\
\\
\\

\
\\

\
\

\
\

\
\\\\
\`\`\`The `.prop` modifier also has a dedicated shorthand, `.`:

template\`\`\`
\\

\
\\
\`\`\`The `.camel` modifier allows camelizing a `v-bind` attribute name when using in\-DOM templates, e.g. the SVG `viewBox` attribute:

template\`\`\`
\\
\`\`\``.camel` is not needed if you are using string templates, or pre\-compiling the template with a build step.
* **See also**

	+ [Class and Style Bindings](/guide/essentials/class-and-style)
	+ [Components \- Prop Passing Details](/guide/components/props#prop-passing-details)

## v\-model [​](#v-model)

Create a two\-way binding on a form input element or a component.

* **Expects:** varies based on value of form inputs element or output of components
* **Limited to:**

	+ ``
	+ ``
	+ ``
	+ components
* **Modifiers**

	+ [`.lazy`](/guide/essentials/forms#lazy) \- listen to `change` events instead of `input`
	+ [`.number`](/guide/essentials/forms#number) \- cast valid input string to numbers
	+ [`.trim`](/guide/essentials/forms#trim) \- trim input
* **See also**

	+ [Form Input Bindings](/guide/essentials/forms)
	+ [Component Events \- Usage with `v-model`](/guide/components/v-model)

## v\-slot [​](#v-slot)

Denote named slots or scoped slots that expect to receive props.

* **Shorthand:** `#`
* **Expects:** JavaScript expression that is valid in a function argument position, including support for destructuring. Optional \- only needed if expecting props to be passed to the slot.
* **Argument:** slot name (optional, defaults to `default`)
* **Limited to:**

	+ ``
	+ [components](/guide/components/slots#scoped-slots) (for a lone default slot with props)
* **Example**

template\`\`\`
\
\
 \
 Header content
 \

 \
 Default slot content
 \

 \
 Footer content
 \
\

\
\
 \
 \
 {{ slotProps.item.text }}
 \
 \
\

\
\
 Mouse position: {{ x }}, {{ y }}
\
\`\`\`
* **See also**

	+ [Components \- Slots](/guide/components/slots)

## v\-pre [​](#v-pre)

Skip compilation for this element and all its children.

* **Does not expect expression**
* **Details**

Inside the element with `v-pre`, all Vue template syntax will be preserved and rendered as\-is. The most common use case of this is displaying raw mustache tags.
* **Example**

template\`\`\`
\{{ this will not be compiled }}\
\`\`\`

## v\-once [​](#v-once)

Render the element and component once only, and skip future updates.

* **Does not expect expression**
* **Details**

On subsequent re\-renders, the element/component and all its children will be treated as static content and skipped. This can be used to optimize update performance.

template\`\`\`
\
\This will never change: {{msg}}\
\
\
 \Comment\
 \{{msg}}\
\
\
\\
\
\
 \{{i}}\
\
\`\`\`Since 3\.2, you can also memoize part of the template with invalidation conditions using [`v-memo`](#v-memo).
* **See also**

	+ [Data Binding Syntax \- interpolations](/guide/essentials/template-syntax#text-interpolation)
	+ [v\-memo](#v-memo)

## v\-memo [​](#v-memo)

* Only supported in 3\.2\+
* **Expects:** `any[]`
* **Details**

Memoize a sub\-tree of the template. Can be used on both elements and components. The directive expects a fixed\-length array of dependency values to compare for the memoization. If every value in the array was the same as last render, then updates for the entire sub\-tree will be skipped. For example:

template\`\`\`
\
 ...
\
\`\`\`When the component re\-renders, if both `valueA` and `valueB` remain the same, all updates for this `` and its children will be skipped. In fact, even the Virtual DOM VNode creation will also be skipped since the memoized copy of the sub\-tree can be reused.

It is important to specify the memoization array correctly, otherwise we may skip updates that should indeed be applied. `v-memo` with an empty dependency array (`v-memo="[]"`) would be functionally equivalent to `v-once`.

**Usage with `v-for`**

`v-memo` is provided solely for micro optimizations in performance\-critical scenarios and should be rarely needed. The most common case where this may prove helpful is when rendering large `v-for` lists (where `length > 1000`):

template\`\`\`
\
 \ID: {{ item.id }} \- selected: {{ item.id === selected }}\
 \...more child nodes\
\
\`\`\`When the component's `selected` state changes, a large amount of VNodes will be created even though most of the items remained exactly the same. The `v-memo` usage here is essentially saying "only update this item if it went from non\-selected to selected, or the other way around". This allows every unaffected item to reuse its previous VNode and skip diffing entirely. Note we don't need to include `item.id` in the memo dependency array here since Vue automatically infers it from the item's `:key`.

WARNING

When using `v-memo` with `v-for`, make sure they are used on the same element. **`v-memo` does not work inside `v-for`.**

`v-memo` can also be used on components to manually prevent unwanted updates in certain edge cases where the child component update check has been de\-optimized. But again, it is the developer's responsibility to specify correct dependency arrays to avoid skipping necessary updates.
* **See also**

	+ [v\-once](#v-once)

## v\-cloak [​](#v-cloak)

Used to hide un\-compiled template until it is ready.

* **Does not expect expression**
* **Details**

**This directive is only needed in no\-build\-step setups.**

When using in\-DOM templates, there can be a "flash of un\-compiled templates": the user may see raw mustache tags until the mounted component replaces them with rendered content.

`v-cloak` will remain on the element until the associated component instance is mounted. Combined with CSS rules such as `[v-cloak] { display: none }`, it can be used to hide the raw templates until the component is ready.
* **Example**

css\`\`\`
\[v\-cloak] {
 display: none;
}
\`\`\`template\`\`\`
\
 {{ message }}
\
\`\`\`The `` will not be visible until the compilation is done.
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/built-in-directives.md)



## Composition API FAQ | Vue.js

[Read the full article](https://vuejs.org/guide/extras/composition-api-faq)

# Composition API FAQ [​](#composition-api-faq)

TIP

This FAQ assumes prior experience with Vue \- in particular, experience with Vue 2 while primarily using Options API.

## What is Composition API? [​](#what-is-composition-api)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/introduction-to-the-vue-js-3-composition-api?friend=vuejs "Free Composition API Lesson")Composition API is a set of APIs that allows us to author Vue components using imported functions instead of declaring options. It is an umbrella term that covers the following APIs:

* [Reactivity API](/api/reactivity-core), e.g. `ref()` and `reactive()`, that allows us to directly create reactive state, computed state, and watchers.
* [Lifecycle Hooks](/api/composition-api-lifecycle), e.g. `onMounted()` and `onUnmounted()`, that allow us to programmatically hook into the component lifecycle.
* [Dependency Injection](/api/composition-api-dependency-injection), i.e. `provide()` and `inject()`, that allow us to leverage Vue's dependency injection system while using Reactivity APIs.

Composition API is a built\-in feature of Vue 3 and [Vue 2\.7](https://blog.vuejs.org/posts/vue-2-7-naruto.html). For older Vue 2 versions, use the officially maintained [`@vue/composition-api`](https://github.com/vuejs/composition-api) plugin. In Vue 3, it is also primarily used together with the [``](/api/sfc-script-setup) syntax in Single\-File Components. Here's a basic example of a component using Composition API:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

// reactive state
const count = ref(0\)

// functions that mutate state and trigger updates
function increment() {
 count.value\+\+
}

// lifecycle hooks
onMounted(() =\> {
 console.log(\`The initial count is ${count.value}.\`)
})
\

\
 \Count is: {{ count }}\
\
\`\`\`Despite an API style based on function composition, **Composition API is NOT functional programming**. Composition API is based on Vue's mutable, fine\-grained reactivity paradigm, whereas functional programming emphasizes immutability.

If you are interested in learning how to use Vue with Composition API, you can set the site\-wide API preference to Composition API using the toggle at the top of the left sidebar, and then go through the guide from the beginning.

## Why Composition API? [​](#why-composition-api)

### Better Logic Reuse [​](#better-logic-reuse)

The primary advantage of Composition API is that it enables clean, efficient logic reuse in the form of [Composable functions](/guide/reusability/composables). It solves [all the drawbacks of mixins](/guide/reusability/composables#vs-mixins), the primary logic reuse mechanism for Options API.

Composition API's logic reuse capability has given rise to impressive community projects such as [VueUse](https://vueuse.org/), an ever\-growing collection of composable utilities. It also serves as a clean mechanism for easily integrating stateful third\-party services or libraries into Vue's reactivity system, for example [immutable data](/guide/extras/reactivity-in-depth#immutable-data), [state machines](/guide/extras/reactivity-in-depth#state-machines), and [RxJS](/guide/extras/reactivity-in-depth#rxjs).

### More Flexible Code Organization [​](#more-flexible-code-organization)

Many users love that we write organized code by default with Options API: everything has its place based on the option it falls under. However, Options API poses serious limitations when a single component's logic grows beyond a certain complexity threshold. This limitation is particularly prominent in components that need to deal with multiple **logical concerns**, which we have witnessed first hand in many production Vue 2 apps.

Take the folder explorer component from Vue CLI's GUI as an example: this component is responsible for the following logical concerns:

* Tracking current folder state and displaying its content
* Handling folder navigation (opening, closing, refreshing...)
* Handling new folder creation
* Toggling show favorite folders only
* Toggling show hidden folders
* Handling current working directory changes

The [original version](https://github.com/vuejs/vue-cli/blob/a09407dd5b9f18ace7501ddb603b95e31d6d93c0/packages/@vue/cli-ui/src/components/folder/FolderExplorer.vue#L198-L404) of the component was written in Options API. If we give each line of code a color based on the logical concern it is dealing with, this is how it looks:

Notice how code dealing with the same logical concern is forced to be split under different options, located in different parts of the file. In a component that is several hundred lines long, understanding and navigating a single logical concern requires constantly scrolling up and down the file, making it much more difficult than it should be. In addition, if we ever intend to extract a logical concern into a reusable utility, it takes quite a bit of work to find and extract the right pieces of code from different parts of the file.

Here's the same component, before and after the [refactor into Composition API](https://gist.github.com/yyx990803/8854f8f6a97631576c14b63c8acd8f2e):



Notice how the code related to the same logical concern can now be grouped together: we no longer need to jump between different options blocks while working on a specific logical concern. Moreover, we can now move a group of code into an external file with minimal effort, since we no longer need to shuffle the code around in order to extract them. This reduced friction for refactoring is key to the long\-term maintainability in large codebases.

### Better Type Inference [​](#better-type-inference)

In recent years, more and more frontend developers are adopting [TypeScript](https://www.typescriptlang.org/) as it helps us write more robust code, make changes with more confidence, and provides a great development experience with IDE support. However, the Options API, originally conceived in 2013, was designed without type inference in mind. We had to implement some [absurdly complex type gymnastics](https://github.com/vuejs/core/blob/44b95276f5c086e1d88fa3c686a5f39eb5bb7821/packages/runtime-core/src/componentPublicInstance.ts#L132-L165) to make type inference work with the Options API. Even with all this effort, type inference for Options API can still break down for mixins and dependency injection.

This had led many developers who wanted to use Vue with TS to lean towards Class API powered by `vue-class-component`. However, a class\-based API heavily relies on ES decorators, a language feature that was only a stage 2 proposal when Vue 3 was being developed in 2019\. We felt it was too risky to base an official API on an unstable proposal. Since then, the decorators proposal has gone through yet another complete overhaul, and finally reached stage 3 in 2022\. In addition, class\-based API suffers from logic reuse and organization limitations similar to Options API.

In comparison, Composition API utilizes mostly plain variables and functions, which are naturally type friendly. Code written in Composition API can enjoy full type inference with little need for manual type hints. Most of the time, Composition API code will look largely identical in TypeScript and plain JavaScript. This also makes it possible for plain JavaScript users to benefit from partial type inference.

### Smaller Production Bundle and Less Overhead [​](#smaller-production-bundle-and-less-overhead)

Code written in Composition API and `` is also more efficient and minification\-friendly than Options API equivalent. This is because the template in a `` component is compiled as a function inlined in the same scope of the `` code. Unlike property access from `this`, the compiled template code can directly access variables declared inside ``, without an instance proxy in between. This also leads to better minification because all the variable names can be safely shortened.

## Relationship with Options API [​](#relationship-with-options-api)

### Trade\-offs [​](#trade-offs)

Some users moving from Options API found their Composition API code less organized, and concluded that Composition API is "worse" in terms of code organization. We recommend users with such opinions to look at that problem from a different perspective.

It is true that Composition API no longer provides the "guard rails" that guide you to put your code into respective buckets. In return, you get to author component code like how you would write normal JavaScript. This means **you can and should apply any code organization best practices to your Composition API code as you would when writing normal JavaScript**. If you can write well\-organized JavaScript, you should also be able to write well\-organized Composition API code.

Options API does allow you to "think less" when writing component code, which is why many users love it. However, in reducing the mental overhead, it also locks you into the prescribed code organization pattern with no escape hatch, which can make it difficult to refactor or improve code quality in larger scale projects. In this regard, Composition API provides better long term scalability.

### Does Composition API cover all use cases? [​](#does-composition-api-cover-all-use-cases)

Yes in terms of stateful logic. When using Composition API, there are only a few options that may still be needed: `props`, `emits`, `name`, and `inheritAttrs`.

TIP

Since 3\.3 you can directly use `defineOptions` in `` to set the component name or `inheritAttrs` property

If you intend to exclusively use Composition API (along with the options listed above), you can shave a few kbs off your production bundle via a [compile\-time flag](/api/compile-time-flags) that drops Options API related code from Vue. Note this also affects Vue components in your dependencies.

### Can I use both APIs in the same component? [​](#can-i-use-both-apis-in-the-same-component)

Yes. You can use Composition API via the [`setup()`](/api/composition-api-setup) option in an Options API component.

However, we only recommend doing so if you have an existing Options API codebase that needs to integrate with new features / external libraries written with Composition API.

### Will Options API be deprecated? [​](#will-options-api-be-deprecated)

No, we do not have any plan to do so. Options API is an integral part of Vue and the reason many developers love it. We also realize that many of the benefits of Composition API only manifest in larger\-scale projects, and Options API remains a solid choice for many low\-to\-medium\-complexity scenarios.

## Relationship with Class API [​](#relationship-with-class-api)

We no longer recommend using Class API with Vue 3, given that Composition API provides great TypeScript integration with additional logic reuse and code organization benefits.

## Comparison with React Hooks [​](#comparison-with-react-hooks)

Composition API provides the same level of logic composition capabilities as React Hooks, but with some important differences.

React Hooks are invoked repeatedly every time a component updates. This creates a number of caveats that can confuse even seasoned React developers. It also leads to performance optimization issues that can severely affect development experience. Here are some examples:

* Hooks are call\-order sensitive and cannot be conditional.
* Variables declared in a React component can be captured by a hook closure and become "stale" if the developer fails to pass in the correct dependencies array. This leads to React developers relying on ESLint rules to ensure correct dependencies are passed. However, the rule is often not smart enough and over\-compensates for correctness, which leads to unnecessary invalidation and headaches when edge cases are encountered.
* Expensive computations require the use of `useMemo`, which again requires manually passing in the correct dependencies array.
* Event handlers passed to child components cause unnecessary child updates by default, and require explicit `useCallback` as an optimization. This is almost always needed, and again requires a correct dependencies array. Neglecting this leads to over\-rendering apps by default and can cause performance issues without realizing it.
* The stale closure problem, combined with Concurrent features, makes it difficult to reason about when a piece of hooks code is run, and makes working with mutable state that should persist across renders (via `useRef`) cumbersome.

> Note: some of the above issues that are related to memoization can be resolved by the upcoming [React Compiler](https://react.dev/learn/react-compiler).

In comparison, Vue Composition API:

* Invokes `setup()` or `` code only once. This makes the code align better with the intuitions of idiomatic JavaScript usage as there are no stale closures to worry about. Composition API calls are also not sensitive to call order and can be conditional.
* Vue's runtime reactivity system automatically collects reactive dependencies used in computed properties and watchers, so there's no need to manually declare dependencies.
* No need to manually cache callback functions to avoid unnecessary child updates. In general, Vue's fine\-grained reactivity system ensures child components only update when they need to. Manual child\-update optimizations are rarely a concern for Vue developers.

We acknowledge the creativity of React Hooks, and it is a major source of inspiration for Composition API. However, the issues mentioned above do exist in its design and we noticed Vue's reactivity model happens to provide a way around them.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/composition-api-faq.md)



## Options: Misc | Vue.js

[Read the full article](https://vuejs.org/api/options-misc)

# Options: Misc [​](#options-misc)

## name [​](#name)

Explicitly declare a display name for the component.

* **Type**

ts\`\`\`
interface ComponentOptions {
 name?: string
}
\`\`\`
* **Details**

The name of a component is used for the following:

	+ Recursive self\-reference in the component's own template
	+ Display in Vue DevTools' component inspection tree
	+ Display in warning component tracesWhen you use Single\-File Components, the component already infers its own name from the filename. For example, a file named `MyComponent.vue` will have the inferred display name "MyComponent".

Another case is that when a component is registered globally with [`app.component`](/api/application#app-component), the global ID is automatically set as its name.

The `name` option allows you to override the inferred name, or to explicitly provide a name when no name can be inferred (e.g. when not using build tools, or an inlined non\-SFC component).

There is one case where `name` is explicitly necessary: when matching against cacheable components in [``](/guide/built-ins/keep-alive) via its `include / exclude` props.

TIP

Since version 3\.2\.34, a single\-file component using `` will automatically infer its `name` option based on the filename, removing the need to manually declare the name even when used with ``.

## inheritAttrs [​](#inheritattrs)

Controls whether the default component attribute fallthrough behavior should be enabled.

* **Type**

ts\`\`\`
interface ComponentOptions {
 inheritAttrs?: boolean // default: true
}
\`\`\`
* **Details**

By default, parent scope attribute bindings that are not recognized as props will "fallthrough". This means that when we have a single\-root component, these bindings will be applied to the root element of the child component as normal HTML attributes. When authoring a component that wraps a target element or another component, this may not always be the desired behavior. By setting `inheritAttrs` to `false`, this default behavior can be disabled. The attributes are available via the `$attrs` instance property and can be explicitly bound to a non\-root element using `v-bind`.
* **Example**

vue\`\`\`
\
export default {
 inheritAttrs: false,
 props: \['label', 'value'],
 emits: \['input']
}
\

\
 \
 {{ label }}
 \
 \
\
\`\`\`When declaring this option in a component that uses ``, you can use the [`defineOptions`](/api/sfc-script-setup#defineoptions) macro:

vue\`\`\`
\
defineProps(\['label', 'value'])
defineEmits(\['input'])
defineOptions({
 inheritAttrs: false
})
\

\
 \
 {{ label }}
 \
 \
\
\`\`\`
* **See also**

	+ [Fallthrough Attributes](/guide/components/attrs)
	+ [Using `inheritAttrs` in normal ``](/api/sfc-script-setup#usage-alongside-normal-script)

## components [​](#components)

An object that registers components to be made available to the component instance.

* **Type**

ts\`\`\`
interface ComponentOptions {
 components?: { \[key: string]: Component }
}
\`\`\`
* **Example**

js\`\`\`
import Foo from './Foo.vue'
import Bar from './Bar.vue'

export default {
 components: {
 // shorthand
 Foo,
 // register under a different name
 RenamedBar: Bar
 }
}
\`\`\`
* **See also** [Component Registration](/guide/components/registration)

## directives [​](#directives)

An object that registers directives to be made available to the component instance.

* **Type**

ts\`\`\`
interface ComponentOptions {
 directives?: { \[key: string]: Directive }
}
\`\`\`
* **Example**

js\`\`\`
export default {
 directives: {
 // enables v\-focus in template
 focus: {
 mounted(el) {
 el.focus()
 }
 }
 }
}
\`\`\`template\`\`\`
\
\`\`\`
* **See also** [Custom Directives](/guide/reusability/custom-directives)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/options-misc.md)



## Event Handling | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/event-handling)

# Event Handling [​](#event-handling)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/user-events-in-vue-3?friend=vuejs "Free Vue.js Events Lesson")[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-fundamentals-capi-user-events-in-vue-3?friend=vuejs "Free Vue.js Events Lesson")## Listening to Events [​](#listening-to-events)

We can use the `v-on` directive, which we typically shorten to the `@` symbol, to listen to DOM events and run some JavaScript when they're triggered. The usage would be `v-on:click="handler"` or with the shortcut, `@click="handler"`.

The handler value can be one of the following:

1. **Inline handlers:** Inline JavaScript to be executed when the event is triggered (similar to the native `onclick` attribute).
2. **Method handlers:** A property name or path that points to a method defined on the component.

## Inline Handlers [​](#inline-handlers)

Inline handlers are typically used in simple cases, for example:

js\`\`\`
const count = ref(0\)
\`\`\`js\`\`\`
data() {
 return {
 count: 0
 }
}
\`\`\`template\`\`\`
\Add 1\
\Count is: {{ count }}\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNo9jssKgzAURH/lko0tgrbbEqX+Q5fZaLxiqHmQ3LgJ+fdqFZcD58xMYp1z1RqRvRgP0itHEJCia4VR2llPkMDjBBkmbzUUG1oII4y0JhBIGw2hh2Znbo+7MLw+WjZ/C4TaLT3hnogPkcgaeMtFyW8j2GmXpWBtN47w5PWBHLhrPzPCKfWDXRHmPsCAaOBfgSOkdH3IGUhpDBWv9/e8vsZZ/gFFhFJN)

[Try it in the Playground](https://play.vuejs.org/#eNo9jcEKgzAQRH9lyKlF0PYqqdR/6DGXaLYo1RjiRgrivzepIizLzu7sm1XUzuVLIFEKObe+d1wpS183eYahtw4DY1UWMJr15ZpmxYAnDt7uF0BxOwXL5Evc0kbxlmyxxZLFyY2CaXSDZkqKZROYJ4tnO/Tt56HEgckyJaraGNxlsVt2u6teHeF40s20EDo9oyGy+CPIYF1xULBt4H6kOZeFiwBZnOFi+wH0B1hk)

## Method Handlers [​](#method-handlers)

The logic for many event handlers will be more complex though, and likely isn't feasible with inline handlers. That's why `v-on` can also accept the name or path of a component method you'd like to call.

For example:

js\`\`\`
const name = ref('Vue.js')

function greet(event) {
 alert(\`Hello ${name.value}!\`)
 // \`event\` is the native DOM event
 if (event) {
 alert(event.target.tagName)
 }
}
\`\`\`js\`\`\`
data() {
 return {
 name: 'Vue.js'
 }
},
methods: {
 greet(event) {
 // \`this\` inside methods points to the current active instance
 alert(\`Hello ${this.name}!\`)
 // \`event\` is the native DOM event
 if (event) {
 alert(event.target.tagName)
 }
 }
}
\`\`\`template\`\`\`
\
\Greet\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpVj0FLxDAQhf/KMwjtXtq7dBcFQS/qzVMOrWFao2kSkkkvpf/dJIuCEBgm771vZnbx4H23JRJ3YogqaM+IxMlfpNWrd4GxI9CMA3NwK5psbaSVVjkbGXZaCediaJv3RN1XbE5FnZNVrJ3FEoi4pY0sn7BLC0yGArfjMxnjcLsXQrdNJtFxM+Ys0PcYa2CEjuBPylNYb4THtxdUobj0jH/YX3D963gKC5WyvGZ+xR7S5jf01yPzeblhWr2ZmErHw0dizivfK6PV91mKursUl6dSh/4qZ+vQ/+XE8QODonDi)

[Try it in the Playground](https://play.vuejs.org/#eNplUE1LxDAQ/StjEbYL0t5LXRQEvag3Tz00prNtNE1CMilC6X83SUkRhJDJfLz3Jm8tHo2pFo9FU7SOW2Ho0in8MdoSDHhlXhKsnQIYGLHyvL8BLJK3KmcAis3YwOnDY/XlTnt1i2G7i/eMNOnBNRkwWkQqcUFFByVAXUNPk3A9COXEgBkGRgtFDkgDTQjcWxuAwDiJBeMsMcUxszCJlsr+BaXUcLtGwiqut930579KST1IBd5Aqlgie3p/hdTIk+IK//bMGqleEbMjxjC+BZVDIv0+m9CpcNr6MDgkhLORjDBm1H56Iq3ggUvBv++7IhnUFZfnGNt6b4fRtj5wxfYL9p+Sjw==)

A method handler automatically receives the native DOM Event object that triggers it \- in the example above, we are able to access the element dispatching the event via `event.target`.

See also: [Typing Event Handlers](/guide/typescript/composition-api#typing-event-handlers) 

See also: [Typing Event Handlers](/guide/typescript/options-api#typing-event-handlers) 

### Method vs. Inline Detection [​](#method-vs-inline-detection)

The template compiler detects method handlers by checking whether the `v-on` value string is a valid JavaScript identifier or property access path. For example, `foo`, `foo.bar` and `foo['bar']` are treated as method handlers, while `foo()` and `count++` are treated as inline handlers.

## Calling Methods in Inline Handlers [​](#calling-methods-in-inline-handlers)

Instead of binding directly to a method name, we can also call methods in an inline handler. This allows us to pass the method custom arguments instead of the native event:

js\`\`\`
function say(message) {
 alert(message)
}
\`\`\`js\`\`\`
methods: {
 say(message) {
 alert(message)
 }
}
\`\`\`template\`\`\`
\Say hello\
\Say bye\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9jTEOwjAMRa8SeSld6I5CBWdg9ZJGBiJSN2ocpKjq3UmpFDGx+Vn//b/ANYTjOxGcQEc7uyAqkqTQI98TW3ETq2jyYaQYzYNatSArZTzNUn/IK7Ludr2IBYTG4I3QRqKHJFJ6LtY7+zojbIXNk7yfmhahv5msvqS7PfnHGjJVp9w/hu7qKKwfEd1NSg==)

[Try it in the Playground](https://play.vuejs.org/#eNptjUEKwjAQRa8yZFO7sfsSi57B7WzGdjTBtA3NVC2ldzehEFwIw8D7vM9f1cX742tmVSsd2sl6aXDgjx8ngY7vNDuBFQeAnsWMXagToQAEWg49h0APLncDAIUcT5LzlKJsqRBfPF3ljQjCvXcknEj0bRYZBzi3zrbPE6o0UBhblKiaKy1grK52J/oA//23IcmNBD8dXeVBtX0BF0pXsg==)

## Accessing Event Argument in Inline Handlers [​](#accessing-event-argument-in-inline-handlers)

Sometimes we also need to access the original DOM event in an inline handler. You can pass it into a method using the special `$event` variable, or use an inline arrow function:

template\`\`\`
\
\
 Submit
\

\
\ warn('Form cannot be submitted yet.', event)"\>
 Submit
\
\`\`\`js\`\`\`
function warn(message, event) {
 // now we have access to the native event
 if (event) {
 event.preventDefault()
 }
 alert(message)
}
\`\`\`js\`\`\`
methods: {
 warn(message, event) {
 // now we have access to the native event
 if (event) {
 event.preventDefault()
 }
 alert(message)
 }
}
\`\`\`## Event Modifiers [​](#event-modifiers)

It is a very common need to call `event.preventDefault()` or `event.stopPropagation()` inside event handlers. Although we can do this easily inside methods, it would be better if the methods can be purely about data logic rather than having to deal with DOM event details.

To address this problem, Vue provides **event modifiers** for `v-on`. Recall that modifiers are directive postfixes denoted by a dot.

* `.stop`
* `.prevent`
* `.self`
* `.capture`
* `.once`
* `.passive`

template\`\`\`
\
\\

\
\\

\
\\

\
\\

\
\
\...\
\`\`\`TIP

Order matters when using modifiers because the relevant code is generated in the same order. Therefore using `@click.prevent.self` will prevent **click's default action on the element itself and its children**, while `@click.self.prevent` will only prevent click's default action on the element itself.

The `.capture`, `.once`, and `.passive` modifiers mirror the [options of the native `addEventListener` method](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#options):

template\`\`\`
\
\
\
\...\

\
\\

\
\
\
\...\
\`\`\`The `.passive` modifier is typically used with touch event listeners for [improving performance on mobile devices](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#improving_scroll_performance_using_passive_listeners).

TIP

Do not use `.passive` and `.prevent` together, because `.passive` already indicates to the browser that you *do not* intend to prevent the event's default behavior, and you will likely see a warning from the browser if you do so.

## Key Modifiers [​](#key-modifiers)

When listening for keyboard events, we often need to check for specific keys. Vue allows adding key modifiers for `v-on` or `@` when listening for key events:

template\`\`\`
\
\
\`\`\`You can directly use any valid key names exposed via [`KeyboardEvent.key`](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values) as modifiers by converting them to kebab\-case.

template\`\`\`
\
\`\`\`In the above example, the handler will only be called if `$event.key` is equal to `'PageDown'`.

### Key Aliases [​](#key-aliases)

Vue provides aliases for the most commonly used keys:

* `.enter`
* `.tab`
* `.delete` (captures both "Delete" and "Backspace" keys)
* `.esc`
* `.space`
* `.up`
* `.down`
* `.left`
* `.right`

### System Modifier Keys [​](#system-modifier-keys)

You can use the following modifiers to trigger mouse or keyboard event listeners only when the corresponding modifier key is pressed:

* `.ctrl`
* `.alt`
* `.shift`
* `.meta`

Note

On Macintosh keyboards, meta is the command key (⌘). On Windows keyboards, meta is the Windows key (⊞). On Sun Microsystems keyboards, meta is marked as a solid diamond (◆). On certain keyboards, specifically MIT and Lisp machine keyboards and successors, such as the Knight keyboard, space\-cadet keyboard, meta is labeled “META”. On Symbolics keyboards, meta is labeled “META” or “Meta”.

For example:

template\`\`\`
\
\

\
\Do something\
\`\`\`TIP

Note that modifier keys are different from regular keys and when used with `keyup` events, they have to be pressed when the event is emitted. In other words, `keyup.ctrl` will only trigger if you release a key while holding down `ctrl`. It won't trigger if you release the `ctrl` key alone.

### `.exact` Modifier [​](#exact-modifier)

The `.exact` modifier allows control of the exact combination of system modifiers needed to trigger an event.

template\`\`\`
\
\A\

\
\A\

\
\A\
\`\`\`## Mouse Button Modifiers [​](#mouse-button-modifiers)

* `.left`
* `.right`
* `.middle`

These modifiers restrict the handler to events triggered by a specific mouse button.

Note, however, that `.left`, `.right`, and `.middle` modifier names are based on the typical right\-handed mouse layout, but in fact represent "main", "secondary", and "auxiliary" pointing device event triggers, respectively, and not the actual physical buttons. So that for a left\-handed mouse layout the "main" button might physically be the right one but would trigger the `.left` modifier handler. Or a trackpad might trigger the `.left` handler with a one\-finger tap, the `.right` handler with a two\-finger tap, and the `.middle` handler with a three\-finger tap. Similarly, other devices and event sources generating "mouse" events might have trigger modes that are not related to "left" and "right" whatsoever.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/event-handling.md)



## Global API: General | Vue.js

[Read the full article](https://vuejs.org/api/general)

# Global API: General [​](#global-api-general)

## version [​](#version)

Exposes the current version of Vue.

* **Type:** `string`
* **Example**

js\`\`\`
import { version } from 'vue'

console.log(version)
\`\`\`

## nextTick() [​](#nexttick)

A utility for waiting for the next DOM update flush.

* **Type**

ts\`\`\`
function nextTick(callback?: () =\> void): Promise\
\`\`\`
* **Details**

When you mutate reactive state in Vue, the resulting DOM updates are not applied synchronously. Instead, Vue buffers them until the "next tick" to ensure that each component updates only once no matter how many state changes you have made.

`nextTick()` can be used immediately after a state change to wait for the DOM updates to complete. You can either pass a callback as an argument, or await the returned Promise.
* **Example**

vue\`\`\`
\
import { ref, nextTick } from 'vue'

const count = ref(0\)

async function increment() {
 count.value\+\+

 // DOM not yet updated
 console.log(document.getElementById('counter').textContent) // 0

 await nextTick()
 // DOM is now updated
 console.log(document.getElementById('counter').textContent) // 1
}
\

\
 \{{ count }}\
\
\`\`\`vue\`\`\`
\
import { nextTick } from 'vue'

export default {
 data() {
 return {
 count: 0
 }
 },
 methods: {
 async increment() {
 this.count\+\+

 // DOM not yet updated
 console.log(document.getElementById('counter').textContent) // 0

 await nextTick()
 // DOM is now updated
 console.log(document.getElementById('counter').textContent) // 1
 }
 }
}
\

\
 \{{ count }}\
\
\`\`\`
* **See also** [`this.$nextTick()`](/api/component-instance#nexttick)

## defineComponent() [​](#definecomponent)

A type helper for defining a Vue component with type inference.

* **Type**

ts\`\`\`
// options syntax
function defineComponent(
 component: ComponentOptions
): ComponentConstructor

// function syntax (requires 3\.3\+)
function defineComponent(
 setup: ComponentOptions\['setup'],
 extraOptions?: ComponentOptions
): () =\> any
\`\`\`
> Type is simplified for readability.
* **Details**

The first argument expects a component options object. The return value will be the same options object, since the function is essentially a runtime no\-op for type inference purposes only.

Note that the return type is a bit special: it will be a constructor type whose instance type is the inferred component instance type based on the options. This is used for type inference when the returned type is used as a tag in TSX.

You can extract the instance type of a component (equivalent to the type of `this` in its options) from the return type of `defineComponent()` like this:

ts\`\`\`
const Foo = defineComponent(/\* ... \*/)

type FooInstance = InstanceType\
\`\`\`### Function Signature [​](#function-signature)

	+ Only supported in 3\.3\+`defineComponent()` also has an alternative signature that is meant to be used with the Composition API and [render functions or JSX](/guide/extras/render-function).

Instead of passing in an options object, a function is expected instead. This function works the same as the Composition API [`setup()`](/api/composition-api-setup#composition-api-setup) function: it receives the props and the setup context. The return value should be a render function \- both `h()` and JSX are supported:

js\`\`\`
import { ref, h } from 'vue'

const Comp = defineComponent(
 (props) =\> {
 // use Composition API here like in \
 const count = ref(0\)

 return () =\> {
 // render function or JSX
 return h('div', count.value)
 }
 },
 // extra options, e.g. declare props and emits
 {
 props: {
 /\* ... \*/
 }
 }
)
\`\`\`The main use case for this signature is with TypeScript (and in particular with TSX), as it supports generics:

tsx\`\`\`
const Comp = defineComponent(
 \(props: { msg: T; list: T\[] }) =\> {
 // use Composition API here like in \
 const count = ref(0\)

 return () =\> {
 // render function or JSX
 return \{count.value}\
 }
 },
 // manual runtime props declaration is currently still needed.
 {
 props: \['msg', 'list']
 }
)
\`\`\`In the future, we plan to provide a Babel plugin that automatically infers and injects the runtime props (like for `defineProps` in SFCs) so that the runtime props declaration can be omitted.

### Note on webpack Treeshaking [​](#note-on-webpack-treeshaking)

Because `defineComponent()` is a function call, it could look like it would produce side\-effects to some build tools, e.g. webpack. This will prevent the component from being tree\-shaken even when the component is never used.

To tell webpack that this function call is safe to be tree\-shaken, you can add a `/*#__PURE__*/` comment notation before the function call:

js\`\`\`
export default /\*\#\_\_PURE\_\_\*/ defineComponent(/\* ... \*/)
\`\`\`Note this is not necessary if you are using Vite, because Rollup (the underlying production bundler used by Vite) is smart enough to determine that `defineComponent()` is in fact side\-effect\-free without the need for manual annotations.
* **See also** [Guide \- Using Vue with TypeScript](/guide/typescript/overview#general-usage-notes)

## defineAsyncComponent() [​](#defineasynccomponent)

Define an async component which is lazy loaded only when it is rendered. The argument can either be a loader function, or an options object for more advanced control of the loading behavior.

* **Type**

ts\`\`\`
function defineAsyncComponent(
 source: AsyncComponentLoader \| AsyncComponentOptions
): Component

type AsyncComponentLoader = () =\> Promise\

interface AsyncComponentOptions {
 loader: AsyncComponentLoader
 loadingComponent?: Component
 errorComponent?: Component
 delay?: number
 timeout?: number
 suspensible?: boolean
 onError?: (
 error: Error,
 retry: () =\> void,
 fail: () =\> void,
 attempts: number
 ) =\> any
}
\`\`\`
* **See also** [Guide \- Async Components](/guide/components/async)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/general.md)



## Introduction | Vue.js

[Read the full article](https://vuejs.org/guide/)

# Introduction [​](#introduction)

You are reading the documentation for Vue 3!

* Vue 2 support has ended on **Dec 31, 2023**. Learn more about [Vue 2 EOL](https://v2.vuejs.org/eol/).
* Upgrading from Vue 2? Check out the [Migration Guide](https://v3-migration.vuejs.org/).
[Learn Vue with video tutorials on VueMastery.com

](https://www.vuemastery.com/courses/)## What is Vue? [​](#what-is-vue)

Vue (pronounced /vjuː/, like **view**) is a JavaScript framework for building user interfaces. It builds on top of standard HTML, CSS, and JavaScript and provides a declarative, component\-based programming model that helps you efficiently develop user interfaces of any complexity.

Here is a minimal example:

js\`\`\`
import { createApp } from 'vue'

createApp({
 data() {
 return {
 count: 0
 }
 }
}).mount('\#app')
\`\`\`js\`\`\`
import { createApp, ref } from 'vue'

createApp({
 setup() {
 return {
 count: ref(0\)
 }
 }
}).mount('\#app')
\`\`\`template\`\`\`
\
 \
 Count is: {{ count }}
 \
\
\`\`\`**Result**

 Count is: 0The above example demonstrates the two core features of Vue:

* **Declarative Rendering**: Vue extends standard HTML with a template syntax that allows us to declaratively describe HTML output based on JavaScript state.
* **Reactivity**: Vue automatically tracks JavaScript state changes and efficiently updates the DOM when changes happen.

You may already have questions \- don't worry. We will cover every little detail in the rest of the documentation. For now, please read along so you can have a high\-level understanding of what Vue offers.

Prerequisites

The rest of the documentation assumes basic familiarity with HTML, CSS, and JavaScript. If you are totally new to frontend development, it might not be the best idea to jump right into a framework as your first step \- grasp the basics and then come back! You can check your knowledge level with these overviews for [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript), [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) and [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps) if needed. Prior experience with other frameworks helps, but is not required.

## The Progressive Framework [​](#the-progressive-framework)

Vue is a framework and ecosystem that covers most of the common features needed in frontend development. But the web is extremely diverse \- the things we build on the web may vary drastically in form and scale. With that in mind, Vue is designed to be flexible and incrementally adoptable. Depending on your use case, Vue can be used in different ways:

* Enhancing static HTML without a build step
* Embedding as Web Components on any page
* Single\-Page Application (SPA)
* Fullstack / Server\-Side Rendering (SSR)
* Jamstack / Static Site Generation (SSG)
* Targeting desktop, mobile, WebGL, and even the terminal

If you find these concepts intimidating, don't worry! The tutorial and guide only require basic HTML and JavaScript knowledge, and you should be able to follow along without being an expert in any of these.

If you are an experienced developer interested in how to best integrate Vue into your stack, or you are curious about what these terms mean, we discuss them in more detail in [Ways of Using Vue](/guide/extras/ways-of-using-vue).

Despite the flexibility, the core knowledge about how Vue works is shared across all these use cases. Even if you are just a beginner now, the knowledge gained along the way will stay useful as you grow to tackle more ambitious goals in the future. If you are a veteran, you can pick the optimal way to leverage Vue based on the problems you are trying to solve, while retaining the same productivity. This is why we call Vue "The Progressive Framework": it's a framework that can grow with you and adapt to your needs.

## Single\-File Components [​](#single-file-components)

In most build\-tool\-enabled Vue projects, we author Vue components using an HTML\-like file format called **Single\-File Component** (also known as `*.vue` files, abbreviated as **SFC**). A Vue SFC, as the name suggests, encapsulates the component's logic (JavaScript), template (HTML), and styles (CSS) in a single file. Here's the previous example, written in SFC format:

vue\`\`\`
\
export default {
 data() {
 return {
 count: 0
 }
 }
}
\

\
 \Count is: {{ count }}\
\

\
button {
 font\-weight: bold;
}
\
\`\`\`vue\`\`\`
\
import { ref } from 'vue'
const count = ref(0\)
\

\
 \Count is: {{ count }}\
\

\
button {
 font\-weight: bold;
}
\
\`\`\`SFC is a defining feature of Vue and is the recommended way to author Vue components **if** your use case warrants a build setup. You can learn more about the [how and why of SFC](/guide/scaling-up/sfc) in its dedicated section \- but for now, just know that Vue will handle all the build tools setup for you.

## API Styles [​](#api-styles)

Vue components can be authored in two different API styles: **Options API** and **Composition API**.

### Options API [​](#options-api)

With Options API, we define a component's logic using an object of options such as `data`, `methods`, and `mounted`. Properties defined by options are exposed on `this` inside functions, which points to the component instance:

vue\`\`\`
\
export default {
 // Properties returned from data() become reactive state
 // and will be exposed on \`this\`.
 data() {
 return {
 count: 0
 }
 },

 // Methods are functions that mutate state and trigger updates.
 // They can be bound as event handlers in templates.
 methods: {
 increment() {
 this.count\+\+
 }
 },

 // Lifecycle hooks are called at different stages
 // of a component's lifecycle.
 // This function will be called when the component is mounted.
 mounted() {
 console.log(\`The initial count is ${this.count}.\`)
 }
}
\

\
 \Count is: {{ count }}\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNptkMFqxCAQhl9lkB522ZL0HNKlpa/Qo4e1ZpLIGhUdl5bgu9es2eSyIMio833zO7NP56pbRNawNkivHJ25wV9nPUGHvYiaYOYGoK7Bo5CkbgiBBOFy2AkSh2N5APmeojePCkDaaKiBt1KnZUuv3Ky0PppMsyYAjYJgigu0oEGYDsirYUAP0WULhqVrQhptF5qHQhnpcUJD+wyQaSpUd/Xp9NysVY/yT2qE0dprIS/vsds5Mg9mNVbaDofL94jZpUgJXUKBCvAy76ZUXY53CTd5tfX2k7kgnJzOCXIF0P5EImvgQ2olr++cbRE4O3+t6JxvXj0ptXVpye1tvbFY+ge/NJZt)

### Composition API [​](#composition-api)

With Composition API, we define a component's logic using imported API functions. In SFCs, Composition API is typically used with [``](/api/sfc-script-setup). The `setup` attribute is a hint that makes Vue perform compile\-time transforms that allow us to use Composition API with less boilerplate. For example, imports and top\-level variables / functions declared in `` are directly usable in the template.

Here is the same component, with the exact same template, but using Composition API and `` instead:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

// reactive state
const count = ref(0\)

// functions that mutate state and trigger updates
function increment() {
 count.value\+\+
}

// lifecycle hooks
onMounted(() =\> {
 console.log(\`The initial count is ${count.value}.\`)
})
\

\
 \Count is: {{ count }}\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpNkMFqwzAQRH9lMYU4pNg9Bye09NxbjzrEVda2iLwS0spQjP69a+yYHnRYad7MaOfiw/tqSliciybqYDxDRE7+qsiM3gWGGQJ2r+DoyyVivEOGLrgRDkIdFCmqa1G0ms2EELllVKQdRQa9AHBZ+PLtuEm7RCKVd+ChZRjTQqwctHQHDqbvMUDyd7mKip4AGNIBRyQujzArgtW/mlqb8HRSlLcEazrUv9oiDM49xGGvXgp5uT5his5iZV1f3r4HFHvDprVbaxPhZf4XkKub/CDLaep1T7IhGRhHb6WoTADNT2KWpu/aGv24qGKvrIrr5+Z7hnneQnJu6hURvKl3ryL/ARrVkuI=)

### Which to Choose? [​](#which-to-choose)

Both API styles are fully capable of covering common use cases. They are different interfaces powered by the exact same underlying system. In fact, the Options API is implemented on top of the Composition API! The fundamental concepts and knowledge about Vue are shared across the two styles.

The Options API is centered around the concept of a "component instance" (`this` as seen in the example), which typically aligns better with a class\-based mental model for users coming from OOP language backgrounds. It is also more beginner\-friendly by abstracting away the reactivity details and enforcing code organization via option groups.

The Composition API is centered around declaring reactive state variables directly in a function scope and composing state from multiple functions together to handle complexity. It is more free\-form and requires an understanding of how reactivity works in Vue to be used effectively. In return, its flexibility enables more powerful patterns for organizing and reusing logic.

You can learn more about the comparison between the two styles and the potential benefits of Composition API in the [Composition API FAQ](/guide/extras/composition-api-faq).

If you are new to Vue, here's our general recommendation:

* For learning purposes, go with the style that looks easier to understand to you. Again, most of the core concepts are shared between the two styles. You can always pick up the other style later.
* For production use:

	+ Go with Options API if you are not using build tools, or plan to use Vue primarily in low\-complexity scenarios, e.g. progressive enhancement.
	+ Go with Composition API \+ Single\-File Components if you plan to build full applications with Vue.

You don't have to commit to only one style during the learning phase. The rest of the documentation will provide code samples in both styles where applicable, and you can toggle between them at any time using the **API Preference switches** at the top of the left sidebar.

## Still Got Questions? [​](#still-got-questions)

Check out our [FAQ](/about/faq).

## Pick Your Learning Path [​](#pick-your-learning-path)

Different developers have different learning styles. Feel free to pick a learning path that suits your preference \- although we do recommend going over all of the content, if possible!

[Try the Tutorial

For those who prefer learning things hands\-on.](/tutorial/)[Read the Guide

The guide walks you through every aspect of the framework in full detail.](/guide/quick-start)[Check out the Examples

Explore examples of core features and common UI tasks.](/examples/)[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/introduction.md)



## API Reference | Vue.js

[Read the full article](https://vuejs.org/api/)

# API Reference

Filter## Global API

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
## Built\-ins

### Directives

* [v\-text](/api/built-in-directives#v-text)
* [v\-html](/api/built-in-directives#v-html)
* [v\-show](/api/built-in-directives#v-show)
* [v\-if](/api/built-in-directives#v-if)
* [v\-else](/api/built-in-directives#v-else)
* [v\-else\-if](/api/built-in-directives#v-else-if)
* [v\-for](/api/built-in-directives#v-for)
* [v\-on](/api/built-in-directives#v-on)
* [v\-bind](/api/built-in-directives#v-bind)
* [v\-model](/api/built-in-directives#v-model)
* [v\-slot](/api/built-in-directives#v-slot)
* [v\-pre](/api/built-in-directives#v-pre)
* [v\-once](/api/built-in-directives#v-once)
* [v\-memo](/api/built-in-directives#v-memo)
* [v\-cloak](/api/built-in-directives#v-cloak)
### Components

* [\](/api/built-in-components#transition)
* [\](/api/built-in-components#transitiongroup)
* [\](/api/built-in-components#keepalive)
* [\](/api/built-in-components#teleport)
* [\](/api/built-in-components#suspense)
### Special Elements

* [\](/api/built-in-special-elements#component)
* [\](/api/built-in-special-elements#slot)
* [\](/api/built-in-special-elements#template)
### Special Attributes

* [key](/api/built-in-special-attributes#key)
* [ref](/api/built-in-special-attributes#ref)
* [is](/api/built-in-special-attributes#is)
## Single\-File Component

### Syntax Specification

* [Overview](/api/sfc-spec#overview)
* [Language Blocks](/api/sfc-spec#language-blocks)
* [Automatic Name Inference](/api/sfc-spec#automatic-name-inference)
* [Pre\-Processors](/api/sfc-spec#pre-processors)
* [src Imports](/api/sfc-spec#src-imports)
* [Comments](/api/sfc-spec#comments)
### \

* [Basic Syntax](/api/sfc-script-setup#basic-syntax)
* [Reactivity](/api/sfc-script-setup#reactivity)
* [Using Components](/api/sfc-script-setup#using-components)
* [Using Custom Directives](/api/sfc-script-setup#using-custom-directives)
* [defineProps() \& defineEmits()](/api/sfc-script-setup#defineprops-defineemits)
* [defineModel()](/api/sfc-script-setup#definemodel)
* [defineExpose()](/api/sfc-script-setup#defineexpose)
* [defineOptions()](/api/sfc-script-setup#defineoptions)
* [defineSlots()](/api/sfc-script-setup#defineslots)
* [useSlots() \& useAttrs()](/api/sfc-script-setup#useslots-useattrs)
* [Usage alongside normal \](/api/sfc-script-setup#usage-alongside-normal-script)
* [Top\-level await](/api/sfc-script-setup#top-level-await)
* [Import Statements](/api/sfc-script-setup#imports-statements)
* [Generics](/api/sfc-script-setup#generics)
* [Restrictions](/api/sfc-script-setup#restrictions)
### CSS Features

* [Scoped CSS](/api/sfc-css-features#scoped-css)
* [CSS Modules](/api/sfc-css-features#css-modules)
* [v\-bind() in CSS](/api/sfc-css-features#v-bind-in-css)
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
### Server\-Side Rendering

* [renderToString()](/api/ssr#rendertostring)
* [renderToNodeStream()](/api/ssr#rendertonodestream)
* [pipeToNodeWritable()](/api/ssr#pipetonodewritable)
* [renderToWebStream()](/api/ssr#rendertowebstream)
* [pipeToWebWritable()](/api/ssr#pipetowebwritable)
* [renderToSimpleStream()](/api/ssr#rendertosimplestream)
* [useSSRContext()](/api/ssr#usessrcontext)
* [data\-allow\-mismatch](/api/ssr#data-allow-mismatch)
### TypeScript Utility Types

* [PropType\](/api/utility-types#proptype-t)
* [MaybeRef\](/api/utility-types#mayberef)
* [MaybeRefOrGetter\](/api/utility-types#maybereforgetter)
* [ExtractPropTypes\](/api/utility-types#extractproptypes)
* [ExtractPublicPropTypes\](/api/utility-types#extractpublicproptypes)
* [ComponentCustomProperties](/api/utility-types#componentcustomproperties)
* [ComponentCustomOptions](/api/utility-types#componentcustomoptions)
* [ComponentCustomProps](/api/utility-types#componentcustomprops)
* [CSSProperties](/api/utility-types#cssproperties)
### Custom Renderer

* [createRenderer()](/api/custom-renderer#createrenderer)
### Compile\-Time Flags

* [\_\_VUE\_OPTIONS\_API\_\_](/api/compile-time-flags#VUE_OPTIONS_API)
* [\_\_VUE\_PROD\_DEVTOOLS\_\_](/api/compile-time-flags#VUE_PROD_DEVTOOLS)
* [\_\_VUE\_PROD\_HYDRATION\_MISMATCH\_DETAILS\_\_](/api/compile-time-flags#VUE_PROD_HYDRATION_MISMATCH_DETAILS)
* [Configuration Guides](/api/compile-time-flags#configuration-guides)


## Rendering Mechanism | Vue.js

[Read the full article](https://vuejs.org/guide/extras/rendering-mechanism)

# Rendering Mechanism [​](#rendering-mechanism)

How does Vue take a template and turn it into actual DOM nodes? How does Vue update those DOM nodes efficiently? We will attempt to shed some light on these questions here by diving into Vue's internal rendering mechanism.

## Virtual DOM [​](#virtual-dom)

You have probably heard about the term "virtual DOM", which Vue's rendering system is based upon.

The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory and synced with the “real” DOM. The concept was pioneered by [React](https://reactjs.org/), and has been adopted in many other frameworks with different implementations, including Vue.

Virtual DOM is more of a pattern than a specific technology, so there is no one canonical implementation. We can illustrate the idea using a simple example:

js\`\`\`
const vnode = {
 type: 'div',
 props: {
 id: 'hello'
 },
 children: \[
 /\* more vnodes \*/
 ]
}
\`\`\`Here, `vnode` is a plain JavaScript object (a "virtual node") representing a `` element. It contains all the information that we need to create the actual element. It also contains more children vnodes, which makes it the root of a virtual DOM tree.

A runtime renderer can walk a virtual DOM tree and construct a real DOM tree from it. This process is called **mount**.

If we have two copies of virtual DOM trees, the renderer can also walk and compare the two trees, figuring out the differences, and apply those changes to the actual DOM. This process is called **patch**, also known as "diffing" or "reconciliation".

The main benefit of virtual DOM is that it gives the developer the ability to programmatically create, inspect and compose desired UI structures in a declarative way, while leaving the direct DOM manipulation to the renderer.

## Render Pipeline [​](#render-pipeline)

At the high level, this is what happens when a Vue component is mounted:

1. **Compile**: Vue templates are compiled into **render functions**: functions that return virtual DOM trees. This step can be done either ahead\-of\-time via a build step, or on\-the\-fly by using the runtime compiler.
2. **Mount**: The runtime renderer invokes the render functions, walks the returned virtual DOM tree, and creates actual DOM nodes based on it. This step is performed as a [reactive effect](/guide/extras/reactivity-in-depth), so it keeps track of all reactive dependencies that were used.
3. **Patch**: When a dependency used during mount changes, the effect re\-runs. This time, a new, updated Virtual DOM tree is created. The runtime renderer walks the new tree, compares it with the old one, and applies necessary updates to the actual DOM.



## Templates vs. Render Functions [​](#templates-vs-render-functions)

Vue templates are compiled into virtual DOM render functions. Vue also provides APIs that allow us to skip the template compilation step and directly author render functions. Render functions are more flexible than templates when dealing with highly dynamic logic, because you can work with vnodes using the full power of JavaScript.

So why does Vue recommend templates by default? There are a number of reasons:

1. Templates are closer to actual HTML. This makes it easier to reuse existing HTML snippets, apply accessibility best practices, style with CSS, and for designers to understand and modify.
2. Templates are easier to statically analyze due to their more deterministic syntax. This allows Vue's template compiler to apply many compile\-time optimizations to improve the performance of the virtual DOM (which we will discuss below).

In practice, templates are sufficient for most use cases in applications. Render functions are typically only used in reusable components that need to deal with highly dynamic rendering logic. Render function usage is discussed in more detail in [Render Functions \& JSX](/guide/extras/render-function).

## Compiler\-Informed Virtual DOM [​](#compiler-informed-virtual-dom)

The virtual DOM implementation in React and most other virtual\-DOM implementations are purely runtime: the reconciliation algorithm cannot make any assumptions about the incoming virtual DOM tree, so it has to fully traverse the tree and diff the props of every vnode in order to ensure correctness. In addition, even if a part of the tree never changes, new vnodes are always created for them on each re\-render, resulting in unnecessary memory pressure. This is one of the most criticized aspect of virtual DOM: the somewhat brute\-force reconciliation process sacrifices efficiency in return for declarativeness and correctness.

But it doesn't have to be that way. In Vue, the framework controls both the compiler and the runtime. This allows us to implement many compile\-time optimizations that only a tightly\-coupled renderer can take advantage of. The compiler can statically analyze the template and leave hints in the generated code so that the runtime can take shortcuts whenever possible. At the same time, we still preserve the capability for the user to drop down to the render function layer for more direct control in edge cases. We call this hybrid approach **Compiler\-Informed Virtual DOM**.

Below, we will discuss a few major optimizations done by the Vue template compiler to improve the virtual DOM's runtime performance.

### Static Hoisting [​](#static-hoisting)

Quite often there will be parts in a template that do not contain any dynamic bindings:

template\`\`\`
\
 \foo\ \
 \bar\ \
 \{{ dynamic }}\
\
\`\`\`[Inspect in Template Explorer](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2PlxuICA8ZGl2PmZvbzwvZGl2PiA8IS0tIGhvaXN0ZWQgLS0+XG4gIDxkaXY+YmFyPC9kaXY+IDwhLS0gaG9pc3RlZCAtLT5cbiAgPGRpdj57eyBkeW5hbWljIH19PC9kaXY+XG48L2Rpdj5cbiIsIm9wdGlvbnMiOnsiaG9pc3RTdGF0aWMiOnRydWV9fQ==)

The `foo` and `bar` divs are static \- re\-creating vnodes and diffing them on each re\-render is unnecessary. The Vue compiler automatically hoists their vnode creation calls out of the render function, and reuses the same vnodes on every render. The renderer is also able to completely skip diffing them when it notices the old vnode and the new vnode are the same one.

In addition, when there are enough consecutive static elements, they will be condensed into a single "static vnode" that contains the plain HTML string for all these nodes ([Example](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2PlxuICA8ZGl2IGNsYXNzPVwiZm9vXCI+Zm9vPC9kaXY+XG4gIDxkaXYgY2xhc3M9XCJmb29cIj5mb288L2Rpdj5cbiAgPGRpdiBjbGFzcz1cImZvb1wiPmZvbzwvZGl2PlxuICA8ZGl2IGNsYXNzPVwiZm9vXCI+Zm9vPC9kaXY+XG4gIDxkaXYgY2xhc3M9XCJmb29cIj5mb288L2Rpdj5cbiAgPGRpdj57eyBkeW5hbWljIH19PC9kaXY+XG48L2Rpdj4iLCJzc3IiOmZhbHNlLCJvcHRpb25zIjp7ImhvaXN0U3RhdGljIjp0cnVlfX0=)). These static vnodes are mounted by directly setting `innerHTML`. They also cache their corresponding DOM nodes on initial mount \- if the same piece of content is reused elsewhere in the app, new DOM nodes are created using native `cloneNode()`, which is extremely efficient.

### Patch Flags [​](#patch-flags)

For a single element with dynamic bindings, we can also infer a lot of information from it at compile time:

template\`\`\`
\
\\

\
\

\
\{{ dynamic }}\
\`\`\`[Inspect in Template Explorer](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2IDpjbGFzcz1cInsgYWN0aXZlIH1cIj48L2Rpdj5cblxuPGlucHV0IDppZD1cImlkXCIgOnZhbHVlPVwidmFsdWVcIj5cblxuPGRpdj57eyBkeW5hbWljIH19PC9kaXY+Iiwib3B0aW9ucyI6e319)

When generating the render function code for these elements, Vue encodes the type of update each of them needs directly in the vnode creation call:

js\`\`\`
createElementVNode("div", {
 class: \_normalizeClass({ active: \_ctx.active })
}, null, 2 /\* CLASS \*/)
\`\`\`The last argument, `2`, is a [patch flag](https://github.com/vuejs/core/blob/main/packages/shared/src/patchFlags.ts). An element can have multiple patch flags, which will be merged into a single number. The runtime renderer can then check against the flags using [bitwise operations](https://en.wikipedia.org/wiki/Bitwise_operation) to determine whether it needs to do certain work:

js\`\`\`
if (vnode.patchFlag \& PatchFlags.CLASS /\* 2 \*/) {
 // update the element's class
}
\`\`\`Bitwise checks are extremely fast. With the patch flags, Vue is able to do the least amount of work necessary when updating elements with dynamic bindings.

Vue also encodes the type of children a vnode has. For example, a template that has multiple root nodes is represented as a fragment. In most cases, we know for sure that the order of these root nodes will never change, so this information can also be provided to the runtime as a patch flag:

js\`\`\`
export function render() {
 return (\_openBlock(), \_createElementBlock(\_Fragment, null, \[
 /\* children \*/
 ], 64 /\* STABLE\_FRAGMENT \*/))
}
\`\`\`The runtime can thus completely skip child\-order reconciliation for the root fragment.

### Tree Flattening [​](#tree-flattening)

Taking another look at the generated code from the previous example, you'll notice the root of the returned virtual DOM tree is created using a special `createElementBlock()` call:

js\`\`\`
export function render() {
 return (\_openBlock(), \_createElementBlock(\_Fragment, null, \[
 /\* children \*/
 ], 64 /\* STABLE\_FRAGMENT \*/))
}
\`\`\`Conceptually, a "block" is a part of the template that has stable inner structure. In this case, the entire template has a single block because it does not contain any structural directives like `v-if` and `v-for`.

Each block tracks any descendant nodes (not just direct children) that have patch flags. For example:

template\`\`\`
\ \
 \...\ \
 \\ \
 \ \
 \{{ bar }}\ \
 \
\
\`\`\`The result is a flattened array that contains only the dynamic descendant nodes:

\`\`\`
div (block root)
\- div with :id binding
\- div with {{ bar }} binding
\`\`\`When this component needs to re\-render, it only needs to traverse the flattened tree instead of the full tree. This is called **Tree Flattening**, and it greatly reduces the number of nodes that need to be traversed during virtual DOM reconciliation. Any static parts of the template are effectively skipped.

`v-if` and `v-for` directives will create new block nodes:

template\`\`\`
\ \
 \
 \ \
 ...
 \
 \
\
\`\`\`A child block is tracked inside the parent block's array of dynamic descendants. This retains a stable structure for the parent block.

### Impact on SSR Hydration [​](#impact-on-ssr-hydration)

Both patch flags and tree flattening also greatly improve Vue's [SSR Hydration](/guide/scaling-up/ssr#client-hydration) performance:

* Single element hydration can take fast paths based on the corresponding vnode's patch flag.
* Only block nodes and their dynamic descendants need to be traversed during hydration, effectively achieving partial hydration at the template level.
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/rendering-mechanism.md)



## Performance | Vue.js

[Read the full article](https://vuejs.org/guide/best-practices/performance)

# Performance [​](#performance)

## Overview [​](#overview)

Vue is designed to be performant for most common use cases without much need for manual optimizations. However, there are always challenging scenarios where extra fine\-tuning is needed. In this section, we will discuss what you should pay attention to when it comes to performance in a Vue application.

First, let's discuss the two major aspects of web performance:

* **Page Load Performance**: how fast the application shows content and becomes interactive on the initial visit. This is usually measured using web vital metrics like [Largest Contentful Paint (LCP)](https://web.dev/lcp/) and [First Input Delay (FID)](https://web.dev/fid/).
* **Update Performance**: how fast the application updates in response to user input. For example, how fast a list updates when the user types in a search box, or how fast the page switches when the user clicks a navigation link in a Single\-Page Application (SPA).

While it would be ideal to maximize both, different frontend architectures tend to affect how easy it is to attain desired performance in these aspects. In addition, the type of application you are building greatly influences what you should prioritize in terms of performance. Therefore, the first step of ensuring optimal performance is picking the right architecture for the type of application you are building:

* Consult [Ways of Using Vue](/guide/extras/ways-of-using-vue) to see how you can leverage Vue in different ways.
* Jason Miller discusses the types of web applications and their respective ideal implementation / delivery in [Application Holotypes](https://jasonformat.com/application-holotypes/).

## Profiling Options [​](#profiling-options)

To improve performance, we need to first know how to measure it. There are a number of great tools that can help in this regard:

For profiling load performance of production deployments:

* [PageSpeed Insights](https://pagespeed.web.dev/)
* [WebPageTest](https://www.webpagetest.org/)

For profiling performance during local development:

* [Chrome DevTools Performance Panel](https://developer.chrome.com/docs/devtools/evaluate-performance/)
	+ [`app.config.performance`](/api/application#app-config-performance) enables Vue\-specific performance markers in Chrome DevTools' performance timeline.
* [Vue DevTools Extension](/guide/scaling-up/tooling#browser-devtools) also provides a performance profiling feature.

## Page Load Optimizations [​](#page-load-optimizations)

There are many framework\-agnostic aspects for optimizing page load performance \- check out [this web.dev guide](https://web.dev/fast/) for a comprehensive round up. Here, we will primarily focus on techniques that are specific to Vue.

### Choosing the Right Architecture [​](#choosing-the-right-architecture)

If your use case is sensitive to page load performance, avoid shipping it as a pure client\-side SPA. You want your server to be directly sending HTML containing the content the users want to see. Pure client\-side rendering suffers from slow time\-to\-content. This can be mitigated with [Server\-Side Rendering (SSR)](/guide/extras/ways-of-using-vue#fullstack-ssr) or [Static Site Generation (SSG)](/guide/extras/ways-of-using-vue#jamstack-ssg). Check out the [SSR Guide](/guide/scaling-up/ssr) to learn about performing SSR with Vue. If your app doesn't have rich interactivity requirements, you can also use a traditional backend server to render the HTML and enhance it with Vue on the client.

If your main application has to be an SPA, but has marketing pages (landing, about, blog), ship them separately! Your marketing pages should ideally be deployed as static HTML with minimal JS, by using SSG.

### Bundle Size and Tree\-shaking [​](#bundle-size-and-tree-shaking)

One of the most effective ways to improve page load performance is shipping smaller JavaScript bundles. Here are a few ways to reduce bundle size when using Vue:

* Use a build step if possible.

	+ Many of Vue's APIs are ["tree\-shakable"](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking) if bundled via a modern build tool. For example, if you don't use the built\-in `` component, it won't be included in the final production bundle. Tree\-shaking can also remove other unused modules in your source code.
	+ When using a build step, templates are pre\-compiled so we don't need to ship the Vue compiler to the browser. This saves **14kb** min\+gzipped JavaScript and avoids the runtime compilation cost.
* Be cautious of size when introducing new dependencies! In real\-world applications, bloated bundles are most often a result of introducing heavy dependencies without realizing it.

	+ If using a build step, prefer dependencies that offer ES module formats and are tree\-shaking friendly. For example, prefer `lodash-es` over `lodash`.
	+ Check a dependency's size and evaluate whether it is worth the functionality it provides. Note if the dependency is tree\-shaking friendly, the actual size increase will depend on the APIs you actually import from it. Tools like [bundlejs.com](https://bundlejs.com/) can be used for quick checks, but measuring with your actual build setup will always be the most accurate.
* If you are using Vue primarily for progressive enhancement and prefer to avoid a build step, consider using [petite\-vue](https://github.com/vuejs/petite-vue) (only **6kb**) instead.

### Code Splitting [​](#code-splitting)

Code splitting is where a build tool splits the application bundle into multiple smaller chunks, which can then be loaded on demand or in parallel. With proper code splitting, features required at page load can be downloaded immediately, with additional chunks being lazy loaded only when needed, thus improving performance.

Bundlers like Rollup (which Vite is based upon) or webpack can automatically create split chunks by detecting the ESM dynamic import syntax:

js\`\`\`
// lazy.js and its dependencies will be split into a separate chunk
// and only loaded when \`loadLazy()\` is called.
function loadLazy() {
 return import('./lazy.js')
}
\`\`\`Lazy loading is best used on features that are not immediately needed after initial page load. In Vue applications, this can be used in combination with Vue's [Async Component](/guide/components/async) feature to create split chunks for component trees:

js\`\`\`
import { defineAsyncComponent } from 'vue'

// a separate chunk is created for Foo.vue and its dependencies.
// it is only fetched on demand when the async component is
// rendered on the page.
const Foo = defineAsyncComponent(() =\> import('./Foo.vue'))
\`\`\`For applications using Vue Router, it is strongly recommended to use lazy loading for route components. Vue Router has explicit support for lazy loading, separate from `defineAsyncComponent`. See [Lazy Loading Routes](https://router.vuejs.org/guide/advanced/lazy-loading.html) for more details.

## Update Optimizations [​](#update-optimizations)

### Props Stability [​](#props-stability)

In Vue, a child component only updates when at least one of its received props has changed. Consider the following example:

template\`\`\`
\
\`\`\`Inside the `` component, it uses its `id` and `activeId` props to determine whether it is the currently active item. While this works, the problem is that whenever `activeId` changes, **every** `` in the list has to update!

Ideally, only the items whose active status changed should update. We can achieve that by moving the active status computation into the parent, and make `` directly accept an `active` prop instead:

template\`\`\`
\
\`\`\`Now, for most components the `active` prop will remain the same when `activeId` changes, so they no longer need to update. In general, the idea is keeping the props passed to child components as stable as possible.

### `v-once` [​](#v-once)

`v-once` is a built\-in directive that can be used to render content that relies on runtime data but never needs to update. The entire sub\-tree it is used on will be skipped for all future updates. Consult its [API reference](/api/built-in-directives#v-once) for more details.

### `v-memo` [​](#v-memo)

`v-memo` is a built\-in directive that can be used to conditionally skip the update of large sub\-trees or `v-for` lists. Consult its [API reference](/api/built-in-directives#v-memo) for more details.

### Computed Stability [​](#computed-stability)

In Vue 3\.4 and above, a computed property will only trigger effects when its computed value has changed from the previous one. For example, the following `isEven` computed only triggers effects if the returned value has changed from `true` to `false`, or vice\-versa:

js\`\`\`
const count = ref(0\)
const isEven = computed(() =\> count.value % 2 === 0\)

watchEffect(() =\> console.log(isEven.value)) // true

// will not trigger new logs because the computed value stays \`true\`
count.value = 2
count.value = 4
\`\`\`This reduces unnecessary effect triggers, but unfortunately doesn't work if the computed creates a new object on each compute:

js\`\`\`
const computedObj = computed(() =\> {
 return {
 isEven: count.value % 2 === 0
 }
})
\`\`\`Because a new object is created each time, the new value is technically always different from the old value. Even if the `isEven` property remains the same, Vue won't be able to know unless it performs a deep comparison of the old value and the new value. Such comparison could be expensive and likely not worth it.

Instead, we can optimize this by manually comparing the new value with the old value, and conditionally returning the old value if we know nothing has changed:

js\`\`\`
const computedObj = computed((oldValue) =\> {
 const newValue = {
 isEven: count.value % 2 === 0
 }
 if (oldValue \&\& oldValue.isEven === newValue.isEven) {
 return oldValue
 }
 return newValue
})
\`\`\`[Try it in the playground](https://play.vuejs.org/#eNqVVMtu2zAQ/JUFgSZK4UpuczMkow/40AJ9IC3aQ9mDIlG2EokUyKVt1PC/d0lKtoEminMQQC1nZ4c7S+7Yu66L11awGUtNoesOwQi03ZzLuu2URtiBFtUECtV2FkU5gU2OxWpRVaJA2EOlVQuXxHDJJZeFkgYJayVC5hKj6dUxLnzSjZXmV40rZfFrh3Vb/82xVrLH//5DCQNNKPkweNiNVFP+zBsrIJvDjksgGrRahjVAbRZrIWdBVLz2yBfwBrIsg6mD7LncPyryfIVnywupUmz68HOEEqqCI+XFBQzrOKR79MDdx66GCn1jhpQDZx8f0oZ+nBgdRVcH/aMuBt1xZ80qGvGvh/X6nlXwnGpPl6qsLLxTtitzFFTNl0oSN/79AKOCHHQuS5pw4XorbXsr9ImHZN7nHFdx1SilI78MeOJ7Ca+nbvgd+GgomQOv6CNjSQqXaRJuHd03+kHRdg3JoT+A3a7XsfcmpbcWkQS/LZq6uM84C8o5m4fFuOg0CemeOXXX2w2E6ylsgj2gTgeYio/f1l5UEqj+Z3yC7lGuNDlpApswNNTrql7Gd0ZJeqW8TZw5t+tGaMdDXnA2G4acs7xp1OaTj6G2YjLEi5Uo7h+I35mti3H2TQsj9Jp6etjDXC8Fhu3F9y9iS+vDZqtK2xB6ZPNGGNVYpzHA3ltZkuwTnFf70b+1tVz+MIstCmmGQzmh/p56PGf00H4YOfpR7nV8PTxubP8P2GAP9Q==)

Note that you should always perform the full computation before comparing and returning the old value, so that the same dependencies can be collected on every run.

## General Optimizations [​](#general-optimizations)

> The following tips affect both page load and update performance.

### Virtualize Large Lists [​](#virtualize-large-lists)

One of the most common performance issues in all frontend applications is rendering large lists. No matter how performant a framework is, rendering a list with thousands of items **will** be slow due to the sheer number of DOM nodes that the browser needs to handle.

However, we don't necessarily have to render all these nodes upfront. In most cases, the user's screen size can display only a small subset of our large list. We can greatly improve the performance with **list virtualization**, the technique of only rendering the items that are currently in or close to the viewport in a large list.

Implementing list virtualization isn't easy, luckily there are existing community libraries that you can directly use:

* [vue\-virtual\-scroller](https://github.com/Akryum/vue-virtual-scroller)
* [vue\-virtual\-scroll\-grid](https://github.com/rocwang/vue-virtual-scroll-grid)
* [vueuc/VVirtualList](https://github.com/07akioni/vueuc)

### Reduce Reactivity Overhead for Large Immutable Structures [​](#reduce-reactivity-overhead-for-large-immutable-structures)

Vue's reactivity system is deep by default. While this makes state management intuitive, it does create a certain level of overhead when the data size is large, because every property access triggers proxy traps that perform dependency tracking. This typically becomes noticeable when dealing with large arrays of deeply nested objects, where a single render needs to access 100,000\+ properties, so it should only affect very specific use cases.

Vue does provide an escape hatch to opt\-out of deep reactivity by using [`shallowRef()`](/api/reactivity-advanced#shallowref) and [`shallowReactive()`](/api/reactivity-advanced#shallowreactive). Shallow APIs create state that is reactive only at the root level, and exposes all nested objects untouched. This keeps nested property access fast, with the trade\-off being that we must now treat all nested objects as immutable, and updates can only be triggered by replacing the root state:

js\`\`\`
const shallowArray = shallowRef(\[
 /\* big list of deep objects \*/
])

// this won't trigger updates...
shallowArray.value.push(newObject)
// this does:
shallowArray.value = \[...shallowArray.value, newObject]

// this won't trigger updates...
shallowArray.value\[0].foo = 1
// this does:
shallowArray.value = \[
 {
 ...shallowArray.value\[0],
 foo: 1
 },
 ...shallowArray.value.slice(1\)
]
\`\`\`### Avoid Unnecessary Component Abstractions [​](#avoid-unnecessary-component-abstractions)

Sometimes we may create [renderless components](/guide/components/slots#renderless-components) or higher\-order components (i.e. components that render other components with extra props) for better abstraction or code organization. While there is nothing wrong with this, do keep in mind that component instances are much more expensive than plain DOM nodes, and creating too many of them due to abstraction patterns will incur performance costs.

Note that reducing only a few instances won't have noticeable effect, so don't sweat it if the component is rendered only a few times in the app. The best scenario to consider this optimization is again in large lists. Imagine a list of 100 items where each item component contains many child components. Removing one unnecessary component abstraction here could result in a reduction of hundreds of component instances.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/best-practices/performance.md)



## Creating a Vue Application | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/application)

# Creating a Vue Application [​](#creating-a-vue-application)

## The application instance [​](#the-application-instance)

Every Vue application starts by creating a new **application instance** with the [`createApp`](/api/application#createapp) function:

js\`\`\`
import { createApp } from 'vue'

const app = createApp({
 /\* root component options \*/
})
\`\`\`## The Root Component [​](#the-root-component)

The object we are passing into `createApp` is in fact a component. Every app requires a "root component" that can contain other components as its children.

If you are using Single\-File Components, we typically import the root component from another file:

js\`\`\`
import { createApp } from 'vue'
// import the root component App from a single\-file component.
import App from './App.vue'

const app = createApp(App)
\`\`\`While many examples in this guide only need a single component, most real applications are organized into a tree of nested, reusable components. For example, a Todo application's component tree might look like this:

\`\`\`
App (root component)
├─ TodoList
│ └─ TodoItem
│ ├─ TodoDeleteButton
│ └─ TodoEditButton
└─ TodoFooter
 ├─ TodoClearButton
 └─ TodoStatistics
\`\`\`In later sections of the guide, we will discuss how to define and compose multiple components together. Before that, we will focus on what happens inside a single component.

## Mounting the App [​](#mounting-the-app)

An application instance won't render anything until its `.mount()` method is called. It expects a "container" argument, which can either be an actual DOM element or a selector string:

html\`\`\`
\\
\`\`\`js\`\`\`
app.mount('\#app')
\`\`\`The content of the app's root component will be rendered inside the container element. The container element itself is not considered part of the app.

The `.mount()` method should always be called after all app configurations and asset registrations are done. Also note that its return value, unlike the asset registration methods, is the root component instance instead of the application instance.

### In\-DOM Root Component Template [​](#in-dom-root-component-template)

The template for the root component is usually part of the component itself, but it is also possible to provide the template separately by writing it directly inside the mount container:

html\`\`\`
\
 \{{ count }}\
\
\`\`\`js\`\`\`
import { createApp } from 'vue'

const app = createApp({
 data() {
 return {
 count: 0
 }
 }
})

app.mount('\#app')
\`\`\`Vue will automatically use the container's `innerHTML` as the template if the root component does not already have a `template` option.

In\-DOM templates are often used in applications that are [using Vue without a build step](/guide/quick-start#using-vue-from-cdn). They can also be used in conjunction with server\-side frameworks, where the root template might be generated dynamically by the server.

## App Configurations [​](#app-configurations)

The application instance exposes a `.config` object that allows us to configure a few app\-level options, for example, defining an app\-level error handler that captures errors from all descendant components:

js\`\`\`
app.config.errorHandler = (err) =\> {
 /\* handle error \*/
}
\`\`\`The application instance also provides a few methods for registering app\-scoped assets. For example, registering a component:

js\`\`\`
app.component('TodoDeleteButton', TodoDeleteButton)
\`\`\`This makes the `TodoDeleteButton` available for use anywhere in our app. We will discuss registration for components and other types of assets in later sections of the guide. You can also browse the full list of application instance APIs in its [API reference](/api/application).

Make sure to apply all app configurations before mounting the app!

## Multiple application instances [​](#multiple-application-instances)

You are not limited to a single application instance on the same page. The `createApp` API allows multiple Vue applications to co\-exist on the same page, each with its own scope for configuration and global assets:

js\`\`\`
const app1 = createApp({
 /\* ... \*/
})
app1\.mount('\#container\-1')

const app2 = createApp({
 /\* ... \*/
})
app2\.mount('\#container\-2')
\`\`\`If you are using Vue to enhance server\-rendered HTML and only need Vue to control specific parts of a large page, avoid mounting a single Vue application instance on the entire page. Instead, create multiple small application instances and mount them on the elements they are responsible for.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/application.md)



## Animation Techniques | Vue.js

[Read the full article](https://vuejs.org/guide/extras/animation)

# Animation Techniques [​](#animation-techniques)

Vue provides the [``](/guide/built-ins/transition) and [``](/guide/built-ins/transition-group) components for handling enter / leave and list transitions. However, there are many other ways of using animations on the web, even in a Vue application. Here we will discuss a few additional techniques.

## Class\-based Animations [​](#class-based-animations)

For elements that are not entering / leaving the DOM, we can trigger animations by dynamically adding a CSS class:

js\`\`\`
const disabled = ref(false)

function warnDisabled() {
 disabled.value = true
 setTimeout(() =\> {
 disabled.value = false
 }, 1500\)
}
\`\`\`js\`\`\`
export default {
 data() {
 return {
 disabled: false
 }
 },
 methods: {
 warnDisabled() {
 this.disabled = true
 setTimeout(() =\> {
 this.disabled = false
 }, 1500\)
 }
 }
}
\`\`\`template\`\`\`
\
 \Click me\
 \This feature is disabled!\
\
\`\`\`css\`\`\`
.shake {
 animation: shake 0\.82s cubic\-bezier(0\.36, 0\.07, 0\.19, 0\.97\) both;
 transform: translate3d(0, 0, 0\);
}

@keyframes shake {
 10%,
 90% {
 transform: translate3d(\-1px, 0, 0\);
 }

 20%,
 80% {
 transform: translate3d(2px, 0, 0\);
 }

 30%,
 50%,
 70% {
 transform: translate3d(\-4px, 0, 0\);
 }

 40%,
 60% {
 transform: translate3d(4px, 0, 0\);
 }
}
\`\`\`Click me## State\-driven Animations [​](#state-driven-animations)

Some transition effects can be applied by interpolating values, for instance by binding a style to an element while an interaction occurs. Take this example for instance:

js\`\`\`
const x = ref(0\)

function onMousemove(e) {
 x.value = e.clientX
}
\`\`\`js\`\`\`
export default {
 data() {
 return {
 x: 0
 }
 },
 methods: {
 onMousemove(e) {
 this.x = e.clientX
 }
 }
}
\`\`\`template\`\`\`
\
 \Move your mouse across this div...\
 \x: {{ x }}\
\
\`\`\`css\`\`\`
.movearea {
 transition: 0\.3s background\-color ease;
}
\`\`\`Move your mouse across this div...

x: 0

In addition to color, you can also use style bindings to animate transform, width, or height. You can even animate SVG paths using spring physics \- after all, they are all attribute data bindings:

Drag Me[Source code](https://play.vuejs.org/#eNqlVmtv2zYU/SsXboE6mC3bSdwVmpM9MAz9sAIdsA8b5gGhRUrWKpEESTl2DP/3HZKSbbkuUKBA4Ij3ce65D15pP/hZ62TTiEE6WNjMlNqRFa7Rj0tZ1loZR3sygmWu3IgRZarWjROcDpQbVdMbeL45WvKdZHWZ2VbXHZP/LGyWMlPSOloLxoV5L8pi7eiBZrdTr6uEo9L+alhRlLKAPGeVFZ2PdQzwD6CyTWk6oh1+6dBpM2g6isNgch4jWPeCHm4u2Xxkbg2QLrvh8IYeHmm/lARg1xhJTx+moyn9fnfr//nf1/tzzMMfr/dZsj1AnCW7Azhe6J+W8jwsfp2Q7qOypSuV/ELsaMt3Xp3saNxL48yA1Vp4DFg+ojA/0i2ldH/GPqAROcOkzZWpU3oKzxVzYui5wnPS4hz09gZsydc3Us4bidqCZWiD79FQ3ERMgagiydZMFoL/qZpsLSziX4r+mf4LRmgn9ZvsTBOEATjZBjDNCvHXSeiTj8K/wadHR8lv5ZLT8MSnhUFVA5PeyHxHw5YZutCyRW2C9alJLc+jya5n8VmXZsm865MP6hEugp61pevIRUOUDjVouX8hoWsXy8uPF5ThBvtRiGKQGXVPX3OdzozdTov0hGu1QdAR8cYwTzil76e4vrkpA/+Ubt+Fe+ydQzljhotJ3ETYQTg4UWs/qDgRLXi5aQtWMWsflgPuU2OrSiwHUfFTrRoruHqW0B5H9qh1fgyC+Ko6ONdqI6CNA9b3vK4KXo0OiLElfS8h+TVdcKsEC5B9bcgW+dpNcUx1BR09l9ytccASwmkdeoDj/C2OrRPctN9oqQ962nAwz8uqguzV3W/z2S9zOCwm3rILNkG07hmFPgaOGDD3/OiDWEygvWbY7jVESq3bVT6ti1UHkPeiqtQJontaTM46jWMAIJspLTgkybHRcaxXLPtUGNVIPs5UpUxKr/I8/yGo1HZs1wwj4N8T93pLs7f4McWKYdv5F4j/S2bzm2AeKpr6ra63QRCLium87yRouskrj7cuORcyCGtmcKfgCCtijVNBqttEUyxfJIN3UhA7sXVjVpUFFBnqIUwQ56jO2JYvuDUzED3JnlsOd9NpEGJQzNgPSwahVDKirpRBY8aG8bKxKb0LCLhByaqIVTqxYSurKrxhIhulUZrwWIkciPH5ZVxKLvw7toWJjccFT9o2XqL2cjy6z2IlGOe4/rFAp8aUL0HYUoeoF6t78/U72nUEXwvnRYqFuxX153VbqYpHYEy1nySM0GA0iF8q45ppfJUoia+eEG/ZKuxykHZbE6vl9AHj5bgHzmmbTiYZl4n9tNMYwYSLzaRn2O2xweF/7cIdbA==)## Animating with Watchers [​](#animating-with-watchers)

With some creativity, we can use watchers to animate anything based on some numerical state. For example, we can animate the number itself:

js\`\`\`
import { ref, reactive, watch } from 'vue'
import gsap from 'gsap'

const number = ref(0\)
const tweened = reactive({
 number: 0
})

watch(number, (n) =\> {
 gsap.to(tweened, { duration: 0\.5, number: Number(n) \|\| 0 })
})
\`\`\`template\`\`\`
Type a number: \
\{{ tweened.number.toFixed(0\) }}\
\`\`\`js\`\`\`
import gsap from 'gsap'

export default {
 data() {
 return {
 number: 0,
 tweened: 0
 }
 },
 watch: {
 number(n) {
 gsap.to(this, { duration: 0\.5, tweened: Number(n) \|\| 0 })
 }
 }
}
\`\`\`template\`\`\`
Type a number: \
\{{ tweened.toFixed(0\) }}\
\`\`\` Type a number: 0

[Try it in the Playground](https://play.vuejs.org/#eNpNUstygzAM/BWNLyEzBDKd6YWSdHrpsacefSGgJG7xY7BImhL+vTKv9ILllXYlr+jEm3PJpUWRidyXjXIEHql1e2mUdrYh6KDBY8yfoiR1wRiuBZVn6OHYWA0r5q6W2pMv3ISHkBPSlNZ4AtPqAzawC2LRdj3DdEU0WA34qB910sBUnsFWmp6LpRmaRo9UHMLIrGG3h4EBQ/OEbDRpxjx51TYFKWtYKHmOF9WP4Qzs+x22EDoA9NLwmaejC/x+vhBqVxeEfAPIK3WBsi6830lRobZSDDjA580hFIt8roxrCS4bbSuskxFmzhhIAenEy92id1CnzZzfd91szETmZ72rH6zYOej7PA3rYXrKE3GUp//m5KunWx3C5CE6enS0hjZXVKczZXCwdfWyoF79YgZPqBliJ9iGSUTEYlzuRrO9X94a/lUGNTklvBTZvAMpwhYCIMWZyPksTVvjvk9JaXUacq9sSlujFJPnvej/AElH3FQ=)

[Try it in the Playground](https://play.vuejs.org/#eNpNUctugzAQ/JWVLyESj6hSL5Sm6qXHnnr0xYENuAXbwus8Svj3GlxIJEvendHMvgb2bkx6cshyVtiyl4b2XMnO6J6gtsLAsdcdbKZwwxVXeJmpCo/CtQQDVwCVIBFtQwzQI7leLRmAct0B+xx28YLQGVFh5aGAjNM3zvRZUNnkizhII7V6w9xTSjqiRtoYBqhcL0hq5c3S5/hu/blKbzfYwbh9LMWVf0W2zusTws60gnDK6OtqEMTaeSGVcQSnpNMVtmmAXzkLAWeQzarCQNkKaz1zkHWysPthWNryjX/IC1bRbgvjWGTG64rssbQqLF3bKUzvHmH6o1aUnFHWDeVw0G31sqJW/mIOT9h5KEw2m7CYhUsmnV/at9XKX3n24v+E5WxdNmfTbieAs4bI2DzLnDI/dVrqLpu4Nz+/a5GzZYls/AM3dcFx)

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/animation.md)



## Component Events | Vue.js

[Read the full article](https://vuejs.org/guide/components/events)

# Component Events [​](#component-events)

> This page assumes you've already read the [Components Basics](/guide/essentials/component-basics). Read that first if you are new to components.

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/defining-custom-events-emits?friend=vuejs "Free Vue.js Lesson on Defining Custom Events")## Emitting and Listening to Events [​](#emitting-and-listening-to-events)

A component can emit custom events directly in template expressions (e.g. in a `v-on` handler) using the built\-in `$emit` method:

template\`\`\`
\
\Click Me\
\`\`\`The `$emit()` method is also available on the component instance as `this.$emit()`:

js\`\`\`
export default {
 methods: {
 submit() {
 this.$emit('someEvent')
 }
 }
}
\`\`\`The parent can then listen to it using `v-on`:

template\`\`\`
\
\`\`\`The `.once` modifier is also supported on component event listeners:

template\`\`\`
\
\`\`\`Like components and props, event names provide an automatic case transformation. Notice we emitted a camelCase event, but can listen for it using a kebab\-cased listener in the parent. As with [props casing](/guide/components/props#prop-name-casing), we recommend using kebab\-cased event listeners in templates.

TIP

Unlike native DOM events, component emitted events do **not** bubble. You can only listen to the events emitted by a direct child component. If there is a need to communicate between sibling or deeply nested components, use an external event bus or a [global state management solution](/guide/scaling-up/state-management).

## Event Arguments [​](#event-arguments)

It's sometimes useful to emit a specific value with an event. For example, we may want the `` component to be in charge of how much to enlarge the text by. In those cases, we can pass extra arguments to `$emit` to provide this value:

template\`\`\`
\
 Increase by 1
\
\`\`\`Then, when we listen to the event in the parent, we can use an inline arrow function as the listener, which allows us to access the event argument:

template\`\`\`
\ count \+= n" /\>
\`\`\`Or, if the event handler is a method:

template\`\`\`
\
\`\`\`Then the value will be passed as the first parameter of that method:

js\`\`\`
methods: {
 increaseCount(n) {
 this.count \+= n
 }
}
\`\`\`js\`\`\`
function increaseCount(n) {
 count.value \+= n
}
\`\`\`TIP

All extra arguments passed to `$emit()` after the event name will be forwarded to the listener. For example, with `$emit('foo', 1, 2, 3)` the listener function will receive three arguments.

## Declaring Emitted Events [​](#declaring-emitted-events)

A component can explicitly declare the events it will emit using the [`defineEmits()`](/api/sfc-script-setup#defineprops-defineemits) macro[`emits`](/api/options-state#emits) option:

vue\`\`\`
\
defineEmits(\['inFocus', 'submit'])
\
\`\`\`The `$emit` method that we used in the `` isn't accessible within the `` section of a component, but `defineEmits()` returns an equivalent function that we can use instead:

vue\`\`\`
\
const emit = defineEmits(\['inFocus', 'submit'])

function buttonClick() {
 emit('submit')
}
\
\`\`\`The `defineEmits()` macro **cannot** be used inside a function, it must be placed directly within ``, as in the example above.

If you're using an explicit `setup` function instead of ``, events should be declared using the [`emits`](/api/options-state#emits) option, and the `emit` function is exposed on the `setup()` context:

js\`\`\`
export default {
 emits: \['inFocus', 'submit'],
 setup(props, ctx) {
 ctx.emit('submit')
 }
}
\`\`\`As with other properties of the `setup()` context, `emit` can safely be destructured:

js\`\`\`
export default {
 emits: \['inFocus', 'submit'],
 setup(props, { emit }) {
 emit('submit')
 }
}
\`\`\`js\`\`\`
export default {
 emits: \['inFocus', 'submit']
}
\`\`\`The `emits` option and `defineEmits()` macro also support an object syntax. If using TypeScript you can type arguments, which allows us to perform runtime validation of the payload of the emitted events:

vue\`\`\`
\
const emit = defineEmits({
 submit(payload: { email: string, password: string }) {
 // return \`true\` or \`false\` to indicate
 // validation pass / fail
 }
})
\
\`\`\`If you are using TypeScript with ``, it's also possible to declare emitted events using pure type annotations:

vue\`\`\`
\
const emit = defineEmits\()
\
\`\`\`More details: [Typing Component Emits](/guide/typescript/composition-api#typing-component-emits) 

js\`\`\`
export default {
 emits: {
 submit(payload: { email: string, password: string }) {
 // return \`true\` or \`false\` to indicate
 // validation pass / fail
 }
 }
}
\`\`\`See also: [Typing Component Emits](/guide/typescript/options-api#typing-component-emits) 

Although optional, it is recommended to define all emitted events in order to better document how a component should work. It also allows Vue to exclude known listeners from [fallthrough attributes](/guide/components/attrs#v-on-listener-inheritance), avoiding edge cases caused by DOM events manually dispatched by 3rd party code.

TIP

If a native event (e.g., `click`) is defined in the `emits` option, the listener will now only listen to component\-emitted `click` events and no longer respond to native `click` events.

## Events Validation [​](#events-validation)

Similar to prop type validation, an emitted event can be validated if it is defined with the object syntax instead of the array syntax.

To add validation, the event is assigned a function that receives the arguments passed to the `this.$emit``emit` call and returns a boolean to indicate whether the event is valid or not.

vue\`\`\`
\
const emit = defineEmits({
 // No validation
 click: null,

 // Validate submit event
 submit: ({ email, password }) =\> {
 if (email \&\& password) {
 return true
 } else {
 console.warn('Invalid submit event payload!')
 return false
 }
 }
})

function submitForm(email, password) {
 emit('submit', { email, password })
}
\
\`\`\`js\`\`\`
export default {
 emits: {
 // No validation
 click: null,

 // Validate submit event
 submit: ({ email, password }) =\> {
 if (email \&\& password) {
 return true
 } else {
 console.warn('Invalid submit event payload!')
 return false
 }
 }
 },
 methods: {
 submitForm(email, password) {
 this.$emit('submit', { email, password })
 }
 }
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/events.md)



## Tooling | Vue.js

[Read the full article](https://vuejs.org/guide/scaling-up/tooling)

# Tooling [​](#tooling)

## Try It Online [​](#try-it-online)

You don't need to install anything on your machine to try out Vue SFCs \- there are online playgrounds that allow you to do so right in the browser:

* [Vue SFC Playground](https://play.vuejs.org)
	+ Always deployed from latest commit
	+ Designed for inspecting component compilation results
* [Vue \+ Vite on StackBlitz](https://vite.new/vue)
	+ IDE\-like environment running actual Vite dev server in the browser
	+ Closest to local setup

It is also recommended to use these online playgrounds to provide reproductions when reporting bugs.

## Project Scaffolding [​](#project-scaffolding)

### Vite [​](#vite)

[Vite](https://vitejs.dev/) is a lightweight and fast build tool with first\-class Vue SFC support. It is created by Evan You, who is also the author of Vue!

To get started with Vite \+ Vue, simply run:

npmpnpmyarnbunsh\`\`\`
$ npm create vue@latest
\`\`\`sh\`\`\`
$ pnpm create vue@latest
\`\`\`sh\`\`\`
\# For Yarn Modern (v2\+)
$ yarn create vue@latest

\# For Yarn ^v4\.11
$ yarn dlx create\-vue@latest
\`\`\`sh\`\`\`
$ bun create vue@latest
\`\`\`This command will install and execute [create\-vue](https://github.com/vuejs/create-vue), the official Vue project scaffolding tool.

* To learn more about Vite, check out the [Vite docs](https://vitejs.dev).
* To configure Vue\-specific behavior in a Vite project, for example passing options to the Vue compiler, check out the docs for [@vitejs/plugin\-vue](https://github.com/vitejs/vite-plugin-vue/tree/main/packages/plugin-vue#readme).

Both online playgrounds mentioned above also support downloading files as a Vite project.

### Vue CLI [​](#vue-cli)

[Vue CLI](https://cli.vuejs.org/) is the official webpack\-based toolchain for Vue. It is now in maintenance mode and we recommend starting new projects with Vite unless you rely on specific webpack\-only features. Vite will provide superior developer experience in most cases.

For information on migrating from Vue CLI to Vite:

* [Vue CLI \-\> Vite Migration Guide from VueSchool.io](https://vueschool.io/articles/vuejs-tutorials/how-to-migrate-from-vue-cli-to-vite/)
* [Tools / Plugins that help with auto migration](https://github.com/vitejs/awesome-vite#vue-cli)

### Note on In\-Browser Template Compilation [​](#note-on-in-browser-template-compilation)

When using Vue without a build step, component templates are written either directly in the page's HTML or as inlined JavaScript strings. In such cases, Vue needs to ship the template compiler to the browser in order to perform on\-the\-fly template compilation. On the other hand, the compiler would be unnecessary if we pre\-compile the templates with a build step. To reduce client bundle size, Vue provides [different "builds"](https://unpkg.com/browse/vue@3/dist/) optimized for different use cases.

* Build files that start with `vue.runtime.*` are **runtime\-only builds**: they do not include the compiler. When using these builds, all templates must be pre\-compiled via a build step.
* Build files that do not include `.runtime` are **full builds**: they include the compiler and support compiling templates directly in the browser. However, they will increase the payload by \~14kb.

Our default tooling setups use the runtime\-only build since all templates in SFCs are pre\-compiled. If, for some reason, you need in\-browser template compilation even with a build step, you can do so by configuring the build tool to alias `vue` to `vue/dist/vue.esm-bundler.js` instead.

If you are looking for a lighter\-weight alternative for no\-build\-step usage, check out [petite\-vue](https://github.com/vuejs/petite-vue).

## IDE Support [​](#ide-support)

* The recommended IDE setup is [VS Code](https://code.visualstudio.com/) \+ the [Vue \- Official extension](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (previously Volar). The extension provides syntax highlighting, TypeScript support, and intellisense for template expressions and component props.

TIP

Vue \- Official replaces [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur), our previous official VS Code extension for Vue 2\. If you have Vetur currently installed, make sure to disable it in Vue 3 projects.
* [WebStorm](https://www.jetbrains.com/webstorm/) also provides great built\-in support for Vue SFCs.
* Other IDEs that support the [Language Service Protocol](https://microsoft.github.io/language-server-protocol/) (LSP) can also leverage Volar's core functionalities via LSP:

	+ Sublime Text support via [LSP\-Volar](https://github.com/sublimelsp/LSP-volar).
	+ vim / Neovim support via [coc\-volar](https://github.com/yaegassy/coc-volar).
	+ emacs support via [lsp\-mode](https://emacs-lsp.github.io/lsp-mode/page/lsp-volar/)

## Browser Devtools [​](#browser-devtools)

The Vue browser devtools extension allows you to explore a Vue app's component tree, inspect the state of individual components, track state management events, and profile performance.



* [Documentation](https://devtools.vuejs.org/)
* [Chrome Extension](https://chromewebstore.google.com/detail/vuejs-devtools-beta/ljjemllljcmogpfapbkkighbhhppjdbg)
* [Vite Plugin](https://devtools.vuejs.org/guide/vite-plugin)
* [Standalone Electron app](https://devtools.vuejs.org/guide/standalone)

## TypeScript [​](#typescript)

Main article: [Using Vue with TypeScript](/guide/typescript/overview).

* [Vue \- Official extension](https://github.com/vuejs/language-tools) provides type checking for SFCs using `` blocks, including template expressions and cross\-component props validation.
* Use [`vue-tsc`](https://github.com/vuejs/language-tools/tree/master/packages/tsc) for performing the same type checking from the command line, or for generating `d.ts` files for SFCs.

## Testing [​](#testing)

Main article: [Testing Guide](/guide/scaling-up/testing).

* [Cypress](https://www.cypress.io/) is recommended for E2E tests. It can also be used for component testing for Vue SFCs via the [Cypress Component Test Runner](https://docs.cypress.io/guides/component-testing/introduction).
* [Vitest](https://vitest.dev/) is a test runner created by Vue / Vite team members that focuses on speed. It is specifically designed for Vite\-based applications to provide the same instant feedback loop for unit / component testing.
* [Jest](https://jestjs.io/) can be made to work with Vite via [vite\-jest](https://github.com/sodatea/vite-jest). However, this is only recommended if you have existing Jest\-based test suites that you need to migrate over to a Vite\-based setup, as Vitest provides similar functionalities with a much more efficient integration.

## Linting [​](#linting)

The Vue team maintains [eslint\-plugin\-vue](https://github.com/vuejs/eslint-plugin-vue), an [ESLint](https://eslint.org/) plugin that supports SFC\-specific linting rules.

Users previously using Vue CLI may be used to having linters configured via webpack loaders. However when using a Vite\-based build setup, our general recommendation is:

1. `npm install -D eslint eslint-plugin-vue`, then follow `eslint-plugin-vue`'s [configuration guide](https://eslint.vuejs.org/user-guide/#usage).
2. Setup ESLint IDE extensions, for example [ESLint for VS Code](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint), so you get linter feedback right in your editor during development. This also avoids unnecessary linting cost when starting the dev server.
3. Run ESLint as part of the production build command, so you get full linter feedback before shipping to production.
4. (Optional) Setup tools like [lint\-staged](https://github.com/okonet/lint-staged) to automatically lint modified files on git commit.

## Formatting [​](#formatting)

* The [Vue \- Official](https://github.com/vuejs/language-tools) VS Code extension provides formatting for Vue SFCs out of the box.
* Alternatively, [Prettier](https://prettier.io/) provides built\-in Vue SFC formatting support.

## SFC Custom Block Integrations [​](#sfc-custom-block-integrations)

Custom blocks are compiled into imports to the same Vue file with different request queries. It is up to the underlying build tool to handle these import requests.

* If using Vite, a custom Vite plugin should be used to transform matched custom blocks into executable JavaScript. [Example](https://github.com/vitejs/vite-plugin-vue/tree/main/packages/plugin-vue#example-for-transforming-custom-blocks)
* If using Vue CLI or plain webpack, a webpack loader should be configured to transform the matched blocks. [Example](https://vue-loader.vuejs.org/guide/custom-blocks.html)

## Lower\-Level Packages [​](#lower-level-packages)

### `@vue/compiler-sfc` [​](#vue-compiler-sfc)

* [Docs](https://github.com/vuejs/core/tree/main/packages/compiler-sfc)

This package is part of the Vue core monorepo and is always published with the same version as the main `vue` package. It is included as a dependency of the main `vue` package and proxied under `vue/compiler-sfc` so you don't need to install it individually.

The package itself provides lower\-level utilities for processing Vue SFCs and is only meant for tooling authors that need to support Vue SFCs in custom tools.

TIP

Always prefer using this package via the `vue/compiler-sfc` deep import since this ensures its version is in sync with the Vue runtime.

### `@vitejs/plugin-vue` [​](#vitejs-plugin-vue)

* [Docs](https://github.com/vitejs/vite-plugin-vue/tree/main/packages/plugin-vue)

Official plugin that provides Vue SFC support in Vite.

### `vue-loader` [​](#vue-loader)

* [Docs](https://vue-loader.vuejs.org/)

The official loader that provides Vue SFC support in webpack. If you are using Vue CLI, also see [docs on modifying `vue-loader` options in Vue CLI](https://cli.vuejs.org/guide/webpack.html#modifying-options-of-a-loader).

## Other Online Playgrounds [​](#other-online-playgrounds)

* [VueUse Playground](https://play.vueuse.org)
* [Vue \+ Vite on Repl.it](https://replit.com/@templates/VueJS-with-Vite)
* [Vue on CodeSandbox](https://codesandbox.io/p/devbox/github/codesandbox/sandbox-templates/tree/main/vue-vite)
* [Vue on Codepen](https://codepen.io/pen/editor/vue)
* [Vue on WebComponents.dev](https://webcomponents.dev/create/cevue)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/scaling-up/tooling.md)



## Vue and Web Components | Vue.js

[Read the full article](https://vuejs.org/guide/extras/web-components)

# Vue and Web Components [​](#vue-and-web-components)

[Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components) is an umbrella term for a set of web native APIs that allows developers to create reusable custom elements.

We consider Vue and Web Components to be primarily complementary technologies. Vue has excellent support for both consuming and creating custom elements. Whether you are integrating custom elements into an existing Vue application, or using Vue to build and distribute custom elements, you are in good company.

## Using Custom Elements in Vue [​](#using-custom-elements-in-vue)

Vue [scores a perfect 100% in the Custom Elements Everywhere tests](https://custom-elements-everywhere.com/libraries/vue/results/results.html). Consuming custom elements inside a Vue application largely works the same as using native HTML elements, with a few things to keep in mind:

### Skipping Component Resolution [​](#skipping-component-resolution)

By default, Vue will attempt to resolve a non\-native HTML tag as a registered Vue component before falling back to rendering it as a custom element. This will cause Vue to emit a "failed to resolve component" warning during development. To let Vue know that certain elements should be treated as custom elements and skip component resolution, we can specify the [`compilerOptions.isCustomElement` option](/api/application#app-config-compileroptions).

If you are using Vue with a build setup, the option should be passed via build configs since it is a compile\-time option.

#### Example In\-Browser Config [​](#example-in-browser-config)

js\`\`\`
// Only works if using in\-browser compilation.
// If using build tools, see config examples below.
app.config.compilerOptions.isCustomElement = (tag) =\> tag.includes('\-')
\`\`\`#### Example Vite Config [​](#example-vite-config)

js\`\`\`
// vite.config.js
import vue from '@vitejs/plugin\-vue'

export default {
 plugins: \[
 vue({
 template: {
 compilerOptions: {
 // treat all tags with a dash as custom elements
 isCustomElement: (tag) =\> tag.includes('\-')
 }
 }
 })
 ]
}
\`\`\`#### Example Vue CLI Config [​](#example-vue-cli-config)

js\`\`\`
// vue.config.js
module.exports = {
 chainWebpack: (config) =\> {
 config.module
 .rule('vue')
 .use('vue\-loader')
 .tap((options) =\> ({
 ...options,
 compilerOptions: {
 // treat any tag that starts with ion\- as custom elements
 isCustomElement: (tag) =\> tag.startsWith('ion\-')
 }
 }))
 }
}
\`\`\`### Passing DOM Properties [​](#passing-dom-properties)

Since DOM attributes can only be strings, we need to pass complex data to custom elements as DOM properties. When setting props on a custom element, Vue 3 automatically checks DOM\-property presence using the `in` operator and will prefer setting the value as a DOM property if the key is present. This means that, in most cases, you won't need to think about this if the custom element follows the [recommended best practices](https://web.dev/custom-elements-best-practices/).

However, there could be rare cases where the data must be passed as a DOM property, but the custom element does not properly define/reflect the property (causing the `in` check to fail). In this case, you can force a `v-bind` binding to be set as a DOM property using the `.prop` modifier:

template\`\`\`
\\

\
\\
\`\`\`## Building Custom Elements with Vue [​](#building-custom-elements-with-vue)

The primary benefit of custom elements is that they can be used with any framework, or even without a framework. This makes them ideal for distributing components where the end consumer may not be using the same frontend stack, or when you want to insulate the end application from the implementation details of the components it uses.

### defineCustomElement [​](#definecustomelement)

Vue supports creating custom elements using exactly the same Vue component APIs via the [`defineCustomElement`](/api/custom-elements#definecustomelement) method. The method accepts the same argument as [`defineComponent`](/api/general#definecomponent), but instead returns a custom element constructor that extends `HTMLElement`:

template\`\`\`
\\
\`\`\`js\`\`\`
import { defineCustomElement } from 'vue'

const MyVueElement = defineCustomElement({
 // normal Vue component options here
 props: {},
 emits: {},
 template: \`...\`,

 // defineCustomElement only: CSS to be injected into shadow root
 styles: \[\`/\* inlined css \*/\`]
})

// Register the custom element.
// After registration, all \`\\` tags
// on the page will be upgraded.
customElements.define('my\-vue\-element', MyVueElement)

// You can also programmatically instantiate the element:
// (can only be done after registration)
document.body.appendChild(
 new MyVueElement({
 // initial props (optional)
 })
)
\`\`\`#### Lifecycle [​](#lifecycle)

* A Vue custom element will mount an internal Vue component instance inside its shadow root when the element's [`connectedCallback`](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements#using_the_lifecycle_callbacks) is called for the first time.
* When the element's `disconnectedCallback` is invoked, Vue will check whether the element is detached from the document after a microtask tick.

	+ If the element is still in the document, it's a move and the component instance will be preserved;
	+ If the element is detached from the document, it's a removal and the component instance will be unmounted.

#### Props [​](#props)

* All props declared using the `props` option will be defined on the custom element as properties. Vue will automatically handle the reflection between attributes / properties where appropriate.

	+ Attributes are always reflected to corresponding properties.
	+ Properties with primitive values (`string`, `boolean` or `number`) are reflected as attributes.
* Vue also automatically casts props declared with `Boolean` or `Number` types into the desired type when they are set as attributes (which are always strings). For example, given the following props declaration:

js\`\`\`
props: {
 selected: Boolean,
 index: Number
}
\`\`\`And the custom element usage:

template\`\`\`
\\
\`\`\`In the component, `selected` will be cast to `true` (boolean) and `index` will be cast to `1` (number).

#### Events [​](#events)

Events emitted via `this.$emit` or setup `emit` are dispatched as native [CustomEvents](https://developer.mozilla.org/en-US/docs/Web/Events/Creating_and_triggering_events#adding_custom_data_%E2%80%93_customevent) on the custom element. Additional event arguments (payload) will be exposed as an array on the CustomEvent object as its `detail` property.

#### Slots [​](#slots)

Inside the component, slots can be rendered using the `` element as usual. However, when consuming the resulting element, it only accepts [native slots syntax](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots):

* [Scoped slots](/guide/components/slots#scoped-slots) are not supported.
* When passing named slots, use the `slot` attribute instead of the `v-slot` directive:

template\`\`\`
\
 \hello\
\
\`\`\`

#### Provide / Inject [​](#provide-inject)

The [Provide / Inject API](/guide/components/provide-inject#provide-inject) and its [Composition API equivalent](/api/composition-api-dependency-injection#provide) also work between Vue\-defined custom elements. However, note that this works **only between custom elements**. i.e. a Vue\-defined custom element won't be able to inject properties provided by a non\-custom\-element Vue component.

#### App Level Config  [​](#app-level-config)

You can configure the app instance of a Vue custom element using the `configureApp` option:

js\`\`\`
defineCustomElement(MyComponent, {
 configureApp(app) {
 app.config.errorHandler = (err) =\> {
 /\* ... \*/
 }
 }
})
\`\`\`### SFC as Custom Element [​](#sfc-as-custom-element)

`defineCustomElement` also works with Vue Single\-File Components (SFCs). However, with the default tooling setup, the `` inside the SFCs will still be extracted and merged into a single CSS file during production build. When using an SFC as a custom element, it is often desirable to inject the `` tags into the custom element's shadow root instead.

The official SFC toolings support importing SFCs in "custom element mode" (requires `@vitejs/plugin-vue@^1.4.0` or `vue-loader@^16.5.0`). An SFC loaded in custom element mode inlines its `` tags as strings of CSS and exposes them under the component's `styles` option. This will be picked up by `defineCustomElement` and injected into the element's shadow root when instantiated.

To opt\-in to this mode, simply end your component file name with `.ce.vue`:

js\`\`\`
import { defineCustomElement } from 'vue'
import Example from './Example.ce.vue'

console.log(Example.styles) // \["/\* inlined css \*/"]

// convert into custom element constructor
const ExampleElement = defineCustomElement(Example)

// register
customElements.define('my\-example', ExampleElement)
\`\`\`If you wish to customize what files should be imported in custom element mode (for example, treating *all* SFCs as custom elements), you can pass the `customElement` option to the respective build plugins:

* [@vitejs/plugin\-vue](https://github.com/vitejs/vite-plugin-vue/tree/main/packages/plugin-vue#using-vue-sfcs-as-custom-elements)
* [vue\-loader](https://github.com/vuejs/vue-loader/tree/next#v16-only-options)

### Tips for a Vue Custom Elements Library [​](#tips-for-a-vue-custom-elements-library)

When building custom elements with Vue, the elements will rely on Vue's runtime. There is a \~16kb baseline size cost depending on how many features are being used. This means it is not ideal to use Vue if you are shipping a single custom element \- you may want to use vanilla JavaScript, [petite\-vue](https://github.com/vuejs/petite-vue), or frameworks that specialize in small runtime size. However, the base size is more than justifiable if you are shipping a collection of custom elements with complex logic, as Vue will allow each component to be authored with much less code. The more elements you are shipping together, the better the trade\-off.

If the custom elements will be used in an application that is also using Vue, you can choose to externalize Vue from the built bundle so that the elements will be using the same copy of Vue from the host application.

It is recommended to export the individual element constructors to give your users the flexibility to import them on\-demand and register them with desired tag names. You can also export a convenience function to automatically register all elements. Here's an example entry point of a Vue custom element library:

js\`\`\`
// elements.js

import { defineCustomElement } from 'vue'
import Foo from './MyFoo.ce.vue'
import Bar from './MyBar.ce.vue'

const MyFoo = defineCustomElement(Foo)
const MyBar = defineCustomElement(Bar)

// export individual elements
export { MyFoo, MyBar }

export function register() {
 customElements.define('my\-foo', MyFoo)
 customElements.define('my\-bar', MyBar)
}
\`\`\`A consumer can use the elements in a Vue file:

vue\`\`\`
\
import { register } from 'path/to/elements.js'
register()
\

\
 \
 \\
 \
\
\`\`\`Or in any other framework such as one with JSX, and with custom names:

jsx\`\`\`
import { MyFoo, MyBar } from 'path/to/elements.js'

customElements.define('some\-foo', MyFoo)
customElements.define('some\-bar', MyBar)

export function MyComponent() {
 return \
 \
 \\
 \
 \
}
\`\`\`### Vue\-based Web Components and TypeScript [​](#web-components-and-typescript)

When writing Vue SFC templates, you may want to [type check](/guide/scaling-up/tooling#typescript) your Vue components, including those that are defined as custom elements.

Custom elements are registered globally in browsers using their built\-in APIs, and by default they won't have type inference when used in Vue templates. To provide type support for Vue components registered as custom elements, we can register global component typings by augmenting the [`GlobalComponents` interface](https://github.com/vuejs/language-tools/wiki/Global-Component-Types) for type checking in Vue templates (JSX users can augment the [JSX.IntrinsicElements](https://www.typescriptlang.org/docs/handbook/jsx.html#intrinsic-elements) type instead, which is not shown here).

Here is how to define the type for a custom element made with Vue:

typescript\`\`\`
import { defineCustomElement } from 'vue'

// Import the Vue component.
import SomeComponent from './src/components/SomeComponent.ce.vue'

// Turn the Vue component into a Custom Element class.
export const SomeElement = defineCustomElement(SomeComponent)

// Remember to register the element class with the browser.
customElements.define('some\-element', SomeElement)

// Add the new element type to Vue's GlobalComponents type.
declare module 'vue' {
 interface GlobalComponents {
 // Be sure to pass in the Vue component type here 
 // (SomeComponent, \*not\* SomeElement).
 // Custom Elements require a hyphen in their name, 
 // so use the hyphenated element name here.
 'some\-element': typeof SomeComponent
 }
}
\`\`\`## Non\-Vue Web Components and TypeScript [​](#non-vue-web-components-and-typescript)

Here is the recommended way to enable type checking in SFC templates of Custom Elements that are not built with Vue.

NOTE

This approach is one possible way to do it, but it may vary depending on the framework being used to create the custom elements.

Suppose we have a custom element with some JS properties and events defined, and it is shipped in a library called `some-lib`:

ts\`\`\`
// file: some\-lib/src/SomeElement.ts

// Define a class with typed JS properties.
export class SomeElement extends HTMLElement {
 foo: number = 123
 bar: string = 'blah'

 lorem: boolean = false

 // This method should not be exposed to template types.
 someMethod() {
 /\* ... \*/
 }

 // ... implementation details omitted ...
 // ... assume the element dispatches events named "apple\-fell" ...
}

customElements.define('some\-element', SomeElement)

// This is a list of properties of SomeElement that will be selected for type
// checking in framework templates (f.e. Vue SFC templates). Any other
// properties will not be exposed.
export type SomeElementAttributes = 'foo' \| 'bar'

// Define the event types that SomeElement dispatches.
export type SomeElementEvents = {
 'apple\-fell': AppleFellEvent
}

export class AppleFellEvent extends Event {
 /\* ... details omitted ... \*/
}
\`\`\`The implementation details have been omitted, but the important part is that we have type definitions for two things: prop types and event types.

Let's create a type helper for easily registering custom element type definitions in Vue:

ts\`\`\`
// file: some\-lib/src/DefineCustomElement.ts

// We can re\-use this type helper per each element we need to define.
type DefineCustomElement\ = new () =\> ElementType \& {
 // Use $props to define the properties exposed to template type checking. Vue
 // specifically reads prop definitions from the \`$props\` type. Note that we
 // combine the element's props with the global HTML props and Vue's special
 // props.
 /\*\* @deprecated Do not use the $props property on a Custom Element ref, 
 this is for template prop types only. \*/
 $props: HTMLAttributes \&
 Partial\\> \&
 PublicProps

 // Use $emit to specifically define event types. Vue specifically reads event
 // types from the \`$emit\` type. Note that \`$emit\` expects a particular format
 // that we map \`Events\` to.
 /\*\* @deprecated Do not use the $emit property on a Custom Element ref, 
 this is for template prop types only. \*/
 $emit: VueEmit\
}

type EventMap = {
 \[event: string]: Event
}

// This maps an EventMap to the format that Vue's $emit type expects.
type VueEmit\ = EmitFn\ void
}\>
\`\`\`NOTE

We marked `$props` and `$emit` as deprecated so that when we get a `ref` to a custom element we will not be tempted to use these properties, as these properties are for type checking purposes only when it comes to custom elements. These properties do not actually exist on the custom element instances.

Using the type helper we can now select the JS properties that should be exposed for type checking in Vue templates:

ts\`\`\`
// file: some\-lib/src/SomeElement.vue.ts

import {
 SomeElement,
 SomeElementAttributes,
 SomeElementEvents
} from './SomeElement.js'
import type { Component } from 'vue'
import type { DefineCustomElement } from './DefineCustomElement'

// Add the new element type to Vue's GlobalComponents type.
declare module 'vue' {
 interface GlobalComponents {
 'some\-element': DefineCustomElement\
 }
}
\`\`\`Suppose that `some-lib` builds its source TypeScript files into a `dist/` folder. A user of `some-lib` can then import `SomeElement` and use it in a Vue SFC like so:

vue\`\`\`
\
// This will create and register the element with the browser.
import 'some\-lib/dist/SomeElement.js'

// A user that is using TypeScript and Vue should additionally import the
// Vue\-specific type definition (users of other frameworks may import other
// framework\-specific type definitions).
import type {} from 'some\-lib/dist/SomeElement.vue.js'

import { useTemplateRef, onMounted } from 'vue'

const el = useTemplateRef('el')

onMounted(() =\> {
 console.log(
 el.value!.foo,
 el.value!.bar,
 el.value!.lorem,
 el.value!.someMethod()
 )

 // Do not use these props, they are \`undefined\`
 // IDE will show them crossed out
 el.$props
 el.$emit
})
\

\
 \
 \ {
 // The type of \`event\` is inferred here to be \`AppleFellEvent\`
 }
 "
 \>\
\
\`\`\`If an element does not have type definitions, the types of the properties and events can be defined in a more manual fashion:

vue\`\`\`
\
// Suppose that \`some\-lib\` is plain JS without type definitions, and TypeScript
// cannot infer the types:
import { SomeElement } from 'some\-lib'

// We'll use the same type helper as before.
import { DefineCustomElement } from './DefineCustomElement'

type SomeElementProps = { foo?: number; bar?: string }
type SomeElementEvents = { 'apple\-fell': AppleFellEvent }
interface AppleFellEvent extends Event {
 /\* ... \*/
}

// Add the new element type to Vue's GlobalComponents type.
declare module 'vue' {
 interface GlobalComponents {
 'some\-element': DefineCustomElement\
 }
}

// ... same as before, use a reference to the element ...
\

\
 \
\
\`\`\`Custom Element authors should not automatically export framework\-specific custom element type definitions from their libraries, for example they should not export them from an `index.ts` file that also exports the rest of the library, otherwise users will have unexpected module augmentation errors. Users should import the framework\-specific type definition file that they need.

## Web Components vs. Vue Components [​](#web-components-vs-vue-components)

Some developers believe that framework\-proprietary component models should be avoided, and that exclusively using Custom Elements makes an application "future\-proof". Here we will try to explain why we believe that this is an overly simplistic take on the problem.

There is indeed a certain level of feature overlap between Custom Elements and Vue Components: they both allow us to define reusable components with data passing, event emitting, and lifecycle management. However, Web Components APIs are relatively low\-level and bare\-bones. To build an actual application, we need quite a few additional capabilities which the platform does not cover:

* A declarative and efficient templating system;
* A reactive state management system that facilitates cross\-component logic extraction and reuse;
* A performant way to render the components on the server and hydrate them on the client (SSR), which is important for SEO and [Web Vitals metrics such as LCP](https://web.dev/vitals/). Native custom elements SSR typically involves simulating the DOM in Node.js and then serializing the mutated DOM, while Vue SSR compiles into string concatenation whenever possible, which is much more efficient.

Vue's component model is designed with these needs in mind as a coherent system.

With a competent engineering team, you could probably build the equivalent on top of native Custom Elements \- but this also means you are taking on the long\-term maintenance burden of an in\-house framework, while losing out on the ecosystem and community benefits of a mature framework like Vue.

There are also frameworks built using Custom Elements as the basis of their component model, but they all inevitably have to introduce their proprietary solutions to the problems listed above. Using these frameworks entails buying into their technical decisions on how to solve these problems \- which, despite what may be advertised, doesn't automatically insulate you from potential future churns.

There are also some areas where we find custom elements to be limiting:

* Eager slot evaluation hinders component composition. Vue's [scoped slots](/guide/components/slots#scoped-slots) are a powerful mechanism for component composition, which can't be supported by custom elements due to native slots' eager nature. Eager slots also mean the receiving component cannot control when or whether to render a piece of slot content.
* Shipping custom elements with shadow DOM scoped CSS today requires embedding the CSS inside JavaScript so that they can be injected into shadow roots at runtime. They also result in duplicated styles in markup in SSR scenarios. There are [platform features](https://github.com/whatwg/html/pull/4898/) being worked on in this area \- but as of now they are not yet universally supported, and there are still production performance / SSR concerns to be addressed. In the meanwhile, Vue SFCs provide [CSS scoping mechanisms](/api/sfc-css-features) that support extracting the styles into plain CSS files.

Vue will always stay up to date with the latest standards in the web platform, and we will happily leverage whatever the platform provides if it makes our job easier. However, our goal is to provide solutions that work well and work today. That means we have to incorporate new platform features with a critical mindset \- and that involves filling the gaps where the standards fall short while that is still the case.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/web-components.md)



## Options: Composition | Vue.js

[Read the full article](https://vuejs.org/api/options-composition)

# Options: Composition [​](#options-composition)

## provide [​](#provide)

Provide values that can be injected by descendant components.

* **Type**

ts\`\`\`
interface ComponentOptions {
 provide?: object \| ((this: ComponentPublicInstance) =\> object)
}
\`\`\`
* **Details**

`provide` and [`inject`](#inject) are used together to allow an ancestor component to serve as a dependency injector for all its descendants, regardless of how deep the component hierarchy is, as long as they are in the same parent chain.

The `provide` option should be either an object or a function that returns an object. This object contains the properties that are available for injection into its descendants. You can use Symbols as keys in this object.
* **Example**

Basic usage:

js\`\`\`
const s = Symbol()

export default {
 provide: {
 foo: 'foo',
 \[s]: 'bar'
 }
}
\`\`\`Using a function to provide per\-component state:

js\`\`\`
export default {
 data() {
 return {
 msg: 'foo'
 }
 }
 provide() {
 return {
 msg: this.msg
 }
 }
}
\`\`\`Note in the above example, the provided `msg` will NOT be reactive. See [Working with Reactivity](/guide/components/provide-inject#working-with-reactivity) for more details.
* **See also** [Provide / Inject](/guide/components/provide-inject)

## inject [​](#inject)

Declare properties to inject into the current component by locating them from ancestor providers.

* **Type**

ts\`\`\`
interface ComponentOptions {
 inject?: ArrayInjectOptions \| ObjectInjectOptions
}

type ArrayInjectOptions = string\[]

type ObjectInjectOptions = {
 \[key: string \| symbol]:
 \| string
 \| symbol
 \| { from?: string \| symbol; default?: any }
}
\`\`\`
* **Details**

The `inject` option should be either:

	+ An array of strings, or
	+ An object where the keys are the local binding name and the value is either:
		- The key (string or Symbol) to search for in available injections, or
		- An object where:
			* The `from` property is the key (string or Symbol) to search for in available injections, and
			* The `default` property is used as fallback value. Similar to props default values, a factory function is needed for object types to avoid value sharing between multiple component instances.An injected property will be `undefined` if neither a matching property nor a default value was provided.

Note that injected bindings are NOT reactive. This is intentional. However, if the injected value is a reactive object, properties on that object do remain reactive. See [Working with Reactivity](/guide/components/provide-inject#working-with-reactivity) for more details.
* **Example**

Basic usage:

js\`\`\`
export default {
 inject: \['foo'],
 created() {
 console.log(this.foo)
 }
}
\`\`\`Using an injected value as the default for a prop:

js\`\`\`
const Child = {
 inject: \['foo'],
 props: {
 bar: {
 default() {
 return this.foo
 }
 }
 }
}
\`\`\`Using an injected value as data entry:

js\`\`\`
const Child = {
 inject: \['foo'],
 data() {
 return {
 bar: this.foo
 }
 }
}
\`\`\`Injections can be optional with default value:

js\`\`\`
const Child = {
 inject: {
 foo: { default: 'foo' }
 }
}
\`\`\`If it needs to be injected from a property with a different name, use `from` to denote the source property:

js\`\`\`
const Child = {
 inject: {
 foo: {
 from: 'bar',
 default: 'foo'
 }
 }
}
\`\`\`Similar to prop defaults, you need to use a factory function for non\-primitive values:

js\`\`\`
const Child = {
 inject: {
 foo: {
 from: 'bar',
 default: () =\> \[1, 2, 3]
 }
 }
}
\`\`\`
* **See also** [Provide / Inject](/guide/components/provide-inject)

## mixins [​](#mixins)

An array of option objects to be mixed into the current component.

* **Type**

ts\`\`\`
interface ComponentOptions {
 mixins?: ComponentOptions\[]
}
\`\`\`
* **Details**

The `mixins` option accepts an array of mixin objects. These mixin objects can contain instance options like normal instance objects, and they will be merged against the eventual options using the certain option merging logic. For example, if your mixin contains a `created` hook and the component itself also has one, both functions will be called.

Mixin hooks are called in the order they are provided, and called before the component's own hooks.

No Longer Recommended

In Vue 2, mixins were the primary mechanism for creating reusable chunks of component logic. While mixins continue to be supported in Vue 3, [Composable functions using Composition API](/guide/reusability/composables) is now the preferred approach for code reuse between components.
* **Example**

js\`\`\`
const mixin = {
 created() {
 console.log(1\)
 }
}

createApp({
 created() {
 console.log(2\)
 },
 mixins: \[mixin]
})

// =\> 1
// =\> 2
\`\`\`

## extends [​](#extends)

A "base class" component to extend from.

* **Type**

ts\`\`\`
interface ComponentOptions {
 extends?: ComponentOptions
}
\`\`\`
* **Details**

Allows one component to extend another, inheriting its component options.

From an implementation perspective, `extends` is almost identical to `mixins`. The component specified by `extends` will be treated as though it were the first mixin.

However, `extends` and `mixins` express different intents. The `mixins` option is primarily used to compose chunks of functionality, whereas `extends` is primarily concerned with inheritance.

As with `mixins`, any options (except for `setup()`) will be merged using the relevant merge strategy.
* **Example**

js\`\`\`
const CompA = { ... }

const CompB = {
 extends: CompA,
 ...
}
\`\`\`Not Recommended for Composition API

`extends` is designed for Options API and does not handle the merging of the `setup()` hook.

In Composition API, the preferred mental model for logic reuse is "compose" over "inheritance". If you have logic from a component that needs to be reused in another one, consider extracting the relevant logic into a [Composable](/guide/reusability/composables#composables).

If you still intend to "extend" a component using Composition API, you can call the base component's `setup()` in the extending component's `setup()`:

js\`\`\`
import Base from './Base.js'
export default {
 extends: Base,
 setup(props, ctx) {
 return {
 ...Base.setup(props, ctx),
 // local bindings
 }
 }
}
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/options-composition.md)



## Reactivity API: Core | Vue.js

[Read the full article](https://vuejs.org/api/reactivity-core)

# Reactivity API: Core [​](#reactivity-api-core)

See also

To better understand the Reactivity APIs, it is recommended to read the following chapters in the guide:

* [Reactivity Fundamentals](/guide/essentials/reactivity-fundamentals) (with the API preference set to Composition API)
* [Reactivity in Depth](/guide/extras/reactivity-in-depth)
## ref() [​](#ref)

Takes an inner value and returns a reactive and mutable ref object, which has a single property `.value` that points to the inner value.

* **Type**

ts\`\`\`
function ref\(value: T): Ref\\>

interface Ref\ {
 value: T
}
\`\`\`
* **Details**

The ref object is mutable \- i.e. you can assign new values to `.value`. It is also reactive \- i.e. any read operations to `.value` are tracked, and write operations will trigger associated effects.

If an object is assigned as a ref's value, the object is made deeply reactive with [reactive()](#reactive). This also means if the object contains nested refs, they will be deeply unwrapped.

To avoid the deep conversion, use [`shallowRef()`](/api/reactivity-advanced#shallowref) instead.
* **Example**

js\`\`\`
const count = ref(0\)
console.log(count.value) // 0

count.value = 1
console.log(count.value) // 1
\`\`\`
* **See also**

	+ [Guide \- Reactivity Fundamentals with `ref()`](/guide/essentials/reactivity-fundamentals#ref)
	+ [Guide \- Typing `ref()`](/guide/typescript/composition-api#typing-ref)

## computed() [​](#computed)

Takes a [getter function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description) and returns a readonly reactive [ref](#ref) object for the returned value from the getter. It can also take an object with `get` and `set` functions to create a writable ref object.

* **Type**

ts\`\`\`
// read\-only
function computed\(
 getter: (oldValue: T \| undefined) =\> T,
 // see "Computed Debugging" link below
 debuggerOptions?: DebuggerOptions
): Readonly\\>\>

// writable
function computed\(
 options: {
 get: (oldValue: T \| undefined) =\> T
 set: (value: T) =\> void
 },
 debuggerOptions?: DebuggerOptions
): Ref\
\`\`\`
* **Example**

Creating a readonly computed ref:

js\`\`\`
const count = ref(1\)
const plusOne = computed(() =\> count.value \+ 1\)

console.log(plusOne.value) // 2

plusOne.value\+\+ // error
\`\`\`Creating a writable computed ref:

js\`\`\`
const count = ref(1\)
const plusOne = computed({
 get: () =\> count.value \+ 1,
 set: (val) =\> {
 count.value = val \- 1
 }
})

plusOne.value = 1
console.log(count.value) // 0
\`\`\`Debugging:

js\`\`\`
const plusOne = computed(() =\> count.value \+ 1, {
 onTrack(e) {
 debugger
 },
 onTrigger(e) {
 debugger
 }
})
\`\`\`
* **See also**

	+ [Guide \- Computed Properties](/guide/essentials/computed)
	+ [Guide \- Computed Debugging](/guide/extras/reactivity-in-depth#computed-debugging)
	+ [Guide \- Typing `computed()`](/guide/typescript/composition-api#typing-computed)
	+ [Guide \- Performance \- Computed Stability](/guide/best-practices/performance#computed-stability)

## reactive() [​](#reactive)

Returns a reactive proxy of the object.

* **Type**

ts\`\`\`
function reactive\(target: T): UnwrapNestedRefs\
\`\`\`
* **Details**

The reactive conversion is "deep": it affects all nested properties. A reactive object also deeply unwraps any properties that are [refs](#ref) while maintaining reactivity.

It should also be noted that there is no ref unwrapping performed when the ref is accessed as an element of a reactive array or a native collection type like `Map`.

To avoid the deep conversion and only retain reactivity at the root level, use [shallowReactive()](/api/reactivity-advanced#shallowreactive) instead.

The returned object and its nested objects are wrapped with [ES Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) and **not** equal to the original objects. It is recommended to work exclusively with the reactive proxy and avoid relying on the original object.
* **Example**

Creating a reactive object:

js\`\`\`
const obj = reactive({ count: 0 })
obj.count\+\+
\`\`\`Ref unwrapping:

ts\`\`\`
const count = ref(1\)
const obj = reactive({ count })

// ref will be unwrapped
console.log(obj.count === count.value) // true

// it will update \`obj.count\`
count.value\+\+
console.log(count.value) // 2
console.log(obj.count) // 2

// it will also update \`count\` ref
obj.count\+\+
console.log(obj.count) // 3
console.log(count.value) // 3
\`\`\`Note that refs are **not** unwrapped when accessed as array or collection elements:

js\`\`\`
const books = reactive(\[ref('Vue 3 Guide')])
// need .value here
console.log(books\[0].value)

const map = reactive(new Map(\[\['count', ref(0\)]]))
// need .value here
console.log(map.get('count').value)
\`\`\`When assigning a [ref](#ref) to a `reactive` property, that ref will also be automatically unwrapped:

ts\`\`\`
const count = ref(1\)
const obj = reactive({})

obj.count = count

console.log(obj.count) // 1
console.log(obj.count === count.value) // true
\`\`\`
* **See also**

	+ [Guide \- Reactivity Fundamentals](/guide/essentials/reactivity-fundamentals)
	+ [Guide \- Typing `reactive()`](/guide/typescript/composition-api#typing-reactive)

## readonly() [​](#readonly)

Takes an object (reactive or plain) or a [ref](#ref) and returns a readonly proxy to the original.

* **Type**

ts\`\`\`
function readonly\(
 target: T
): DeepReadonly\\>
\`\`\`
* **Details**

A readonly proxy is deep: any nested property accessed will be readonly as well. It also has the same ref\-unwrapping behavior as `reactive()`, except the unwrapped values will also be made readonly.

To avoid the deep conversion, use [shallowReadonly()](/api/reactivity-advanced#shallowreadonly) instead.
* **Example**

js\`\`\`
const original = reactive({ count: 0 })

const copy = readonly(original)

watchEffect(() =\> {
 // works for reactivity tracking
 console.log(copy.count)
})

// mutating original will trigger watchers relying on the copy
original.count\+\+

// mutating the copy will fail and result in a warning
copy.count\+\+ // warning!
\`\`\`

## watchEffect() [​](#watcheffect)

Runs a function immediately while reactively tracking its dependencies and re\-runs it whenever the dependencies are changed.

* **Type**

ts\`\`\`
function watchEffect(
 effect: (onCleanup: OnCleanup) =\> void,
 options?: WatchEffectOptions
): WatchHandle

type OnCleanup = (cleanupFn: () =\> void) =\> void

interface WatchEffectOptions {
 flush?: 'pre' \| 'post' \| 'sync' // default: 'pre'
 onTrack?: (event: DebuggerEvent) =\> void
 onTrigger?: (event: DebuggerEvent) =\> void
}

interface WatchHandle {
 (): void // callable, same as \`stop\`
 pause: () =\> void
 resume: () =\> void
 stop: () =\> void
}
\`\`\`
* **Details**

The first argument is the effect function to be run. The effect function receives a function that can be used to register a cleanup callback. The cleanup callback will be called right before the next time the effect is re\-run, and can be used to clean up invalidated side effects, e.g. a pending async request (see example below).

The second argument is an optional options object that can be used to adjust the effect's flush timing or to debug the effect's dependencies.

By default, watchers will run just prior to component rendering. Setting `flush: 'post'` will defer the watcher until after component rendering. See [Callback Flush Timing](/guide/essentials/watchers#callback-flush-timing) for more information. In rare cases, it might be necessary to trigger a watcher immediately when a reactive dependency changes, e.g. to invalidate a cache. This can be achieved using `flush: 'sync'`. However, this setting should be used with caution, as it can lead to problems with performance and data consistency if multiple properties are being updated at the same time.

The return value is a handle function that can be called to stop the effect from running again.
* **Example**

js\`\`\`
const count = ref(0\)

watchEffect(() =\> console.log(count.value))
// \-\> logs 0

count.value\+\+
// \-\> logs 1
\`\`\`Stopping the watcher:

js\`\`\`
const stop = watchEffect(() =\> {})

// when the watcher is no longer needed:
stop()
\`\`\`Pausing / resuming the watcher: 

js\`\`\`
const { stop, pause, resume } = watchEffect(() =\> {})

// temporarily pause the watcher
pause()

// resume later
resume()

// stop
stop()
\`\`\`Side effect cleanup:

js\`\`\`
watchEffect(async (onCleanup) =\> {
 const { response, cancel } = doAsyncWork(newId)
 // \`cancel\` will be called if \`id\` changes, cancelling
 // the previous request if it hasn't completed yet
 onCleanup(cancel)
 data.value = await response
})
\`\`\`Side effect cleanup in 3\.5\+:

js\`\`\`
import { onWatcherCleanup } from 'vue'

watchEffect(async () =\> {
 const { response, cancel } = doAsyncWork(newId)
 // \`cancel\` will be called if \`id\` changes, cancelling
 // the previous request if it hasn't completed yet
 onWatcherCleanup(cancel)
 data.value = await response
})
\`\`\`Options:

js\`\`\`
watchEffect(() =\> {}, {
 flush: 'post',
 onTrack(e) {
 debugger
 },
 onTrigger(e) {
 debugger
 }
})
\`\`\`
* **See also**

	+ [Guide \- Watchers](/guide/essentials/watchers#watcheffect)
	+ [Guide \- Watcher Debugging](/guide/extras/reactivity-in-depth#watcher-debugging)

## watchPostEffect() [​](#watchposteffect)

Alias of [`watchEffect()`](#watcheffect) with `flush: 'post'` option.

## watchSyncEffect() [​](#watchsynceffect)

Alias of [`watchEffect()`](#watcheffect) with `flush: 'sync'` option.

## watch() [​](#watch)

Watches one or more reactive data sources and invokes a callback function when the sources change.

* **Type**

ts\`\`\`
// watching single source
function watch\(
 source: WatchSource\,
 callback: WatchCallback\,
 options?: WatchOptions
): WatchHandle

// watching multiple sources
function watch\(
 sources: WatchSource\\[],
 callback: WatchCallback\,
 options?: WatchOptions
): WatchHandle

type WatchCallback\ = (
 value: T,
 oldValue: T,
 onCleanup: (cleanupFn: () =\> void) =\> void
) =\> void

type WatchSource\ =
 \| Ref\ // ref
 \| (() =\> T) // getter
 \| (T extends object ? T : never) // reactive object

interface WatchOptions extends WatchEffectOptions {
 immediate?: boolean // default: false
 deep?: boolean \| number // default: false
 flush?: 'pre' \| 'post' \| 'sync' // default: 'pre'
 onTrack?: (event: DebuggerEvent) =\> void
 onTrigger?: (event: DebuggerEvent) =\> void
 once?: boolean // default: false (3\.4\+)
}

interface WatchHandle {
 (): void // callable, same as \`stop\`
 pause: () =\> void
 resume: () =\> void
 stop: () =\> void
}
\`\`\`
> Types are simplified for readability.
* **Details**

`watch()` is lazy by default \- i.e. the callback is only called when the watched source has changed.

The first argument is the watcher's **source**. The source can be one of the following:

	+ A getter function that returns a value
	+ A ref
	+ A reactive object
	+ ...or an array of the above.The second argument is the callback that will be called when the source changes. The callback receives three arguments: the new value, the old value, and a function for registering a side effect cleanup callback. The cleanup callback will be called right before the next time the effect is re\-run, and can be used to clean up invalidated side effects, e.g. a pending async request.

When watching multiple sources, the callback receives two arrays containing new / old values corresponding to the source array.

The third optional argument is an options object that supports the following options:

	+ **`immediate`**: trigger the callback immediately on watcher creation. Old value will be `undefined` on the first call.
	+ **`deep`**: force deep traversal of the source if it is an object, so that the callback fires on deep mutations. In 3\.5\+, this can also be a number indicating the max traversal depth. See [Deep Watchers](/guide/essentials/watchers#deep-watchers).
	+ **`flush`**: adjust the callback's flush timing. See [Callback Flush Timing](/guide/essentials/watchers#callback-flush-timing) and [`watchEffect()`](/api/reactivity-core#watcheffect).
	+ **`onTrack / onTrigger`**: debug the watcher's dependencies. See [Watcher Debugging](/guide/extras/reactivity-in-depth#watcher-debugging).
	+ **`once`**: (3\.4\+) run the callback only once. The watcher is automatically stopped after the first callback run.Compared to [`watchEffect()`](#watcheffect), `watch()` allows us to:

	+ Perform the side effect lazily;
	+ Be more specific about what state should trigger the watcher to re\-run;
	+ Access both the previous and current value of the watched state.
* **Example**

Watching a getter:

js\`\`\`
const state = reactive({ count: 0 })
watch(
 () =\> state.count,
 (count, prevCount) =\> {
 /\* ... \*/
 }
)
\`\`\`Watching a ref:

js\`\`\`
const count = ref(0\)
watch(count, (count, prevCount) =\> {
 /\* ... \*/
})
\`\`\`When watching multiple sources, the callback receives arrays containing new / old values corresponding to the source array:

js\`\`\`
watch(\[fooRef, barRef], (\[foo, bar], \[prevFoo, prevBar]) =\> {
 /\* ... \*/
})
\`\`\`When using a getter source, the watcher only fires if the getter's return value has changed. If you want the callback to fire even on deep mutations, you need to explicitly force the watcher into deep mode with `{ deep: true }`. Note in deep mode, the new value and the old will be the same object if the callback was triggered by a deep mutation:

js\`\`\`
const state = reactive({ count: 0 })
watch(
 () =\> state,
 (newValue, oldValue) =\> {
 // newValue === oldValue
 },
 { deep: true }
)
\`\`\`When directly watching a reactive object, the watcher is automatically in deep mode:

js\`\`\`
const state = reactive({ count: 0 })
watch(state, () =\> {
 /\* triggers on deep mutation to state \*/
})
\`\`\``watch()` shares the same flush timing and debugging options with [`watchEffect()`](#watcheffect):

js\`\`\`
watch(source, callback, {
 flush: 'post',
 onTrack(e) {
 debugger
 },
 onTrigger(e) {
 debugger
 }
})
\`\`\`Stopping the watcher:

js\`\`\`
const stop = watch(source, callback)

// when the watcher is no longer needed:
stop()
\`\`\`Pausing / resuming the watcher: 

js\`\`\`
const { stop, pause, resume } = watch(() =\> {})

// temporarily pause the watcher
pause()

// resume later
resume()

// stop
stop()
\`\`\`Side effect cleanup:

js\`\`\`
watch(id, async (newId, oldId, onCleanup) =\> {
 const { response, cancel } = doAsyncWork(newId)
 // \`cancel\` will be called if \`id\` changes, cancelling
 // the previous request if it hasn't completed yet
 onCleanup(cancel)
 data.value = await response
})
\`\`\`Side effect cleanup in 3\.5\+:

js\`\`\`
import { onWatcherCleanup } from 'vue'

watch(id, async (newId) =\> {
 const { response, cancel } = doAsyncWork(newId)
 onWatcherCleanup(cancel)
 data.value = await response
})
\`\`\`
* **See also**

	+ [Guide \- Watchers](/guide/essentials/watchers)
	+ [Guide \- Watcher Debugging](/guide/extras/reactivity-in-depth#watcher-debugging)

## onWatcherCleanup()  [​](#onwatchercleanup)

Register a cleanup function to be executed when the current watcher is about to re\-run. Can only be called during the synchronous execution of a `watchEffect` effect function or `watch` callback function (i.e. it cannot be called after an `await` statement in an async function.)

* **Type**

ts\`\`\`
function onWatcherCleanup(
 cleanupFn: () =\> void,
 failSilently?: boolean
): void
\`\`\`
* **Example**

ts\`\`\`
import { watch, onWatcherCleanup } from 'vue'

watch(id, (newId) =\> {
 const { response, cancel } = doAsyncWork(newId)
 // \`cancel\` will be called if \`id\` changes, cancelling
 // the previous request if it hasn't completed yet
 onWatcherCleanup(cancel)
})
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/reactivity-core.md)



## TypeScript with Composition API | Vue.js

[Read the full article](https://vuejs.org/guide/typescript/composition-api)

# TypeScript with Composition API [​](#typescript-with-composition-api)

> This page assumes you've already read the overview on [Using Vue with TypeScript](/guide/typescript/overview).

## Typing Component Props [​](#typing-component-props)

### Using `` [​](#using-script-setup)

When using ``, the `defineProps()` macro supports inferring the props types based on its argument:

vue\`\`\`
\
const props = defineProps({
 foo: { type: String, required: true },
 bar: Number
})

props.foo // string
props.bar // number \| undefined
\
\`\`\`This is called "runtime declaration", because the argument passed to `defineProps()` will be used as the runtime `props` option.

However, it is usually more straightforward to define props with pure types via a generic type argument:

vue\`\`\`
\
const props = defineProps\()
\
\`\`\`This is called "type\-based declaration". The compiler will try to do its best to infer the equivalent runtime options based on the type argument. In this case, our second example compiles into the exact same runtime options as the first example.

You can use either type\-based declaration OR runtime declaration, but you cannot use both at the same time.

We can also move the props types into a separate interface:

vue\`\`\`
\
interface Props {
 foo: string
 bar?: number
}

const props = defineProps\()
\
\`\`\`This also works if `Props` is imported from an external source. This feature requires TypeScript to be a peer dependency of Vue.

vue\`\`\`
\
import type { Props } from './foo'

const props = defineProps\()
\
\`\`\`#### Syntax Limitations [​](#syntax-limitations)

In version 3\.2 and below, the generic type parameter for `defineProps()` were limited to a type literal or a reference to a local interface.

This limitation has been resolved in 3\.3\. The latest version of Vue supports referencing imported and a limited set of complex types in the type parameter position. However, because the type to runtime conversion is still AST\-based, some complex types that require actual type analysis, e.g. conditional types, are not supported. You can use conditional types for the type of a single prop, but not the entire props object.

### Props Default Values [​](#props-default-values)

When using type\-based declaration, we lose the ability to declare default values for the props. This can be resolved by using [Reactive Props Destructure](/guide/components/props#reactive-props-destructure) :

ts\`\`\`
interface Props {
 msg?: string
 labels?: string\[]
}

const { msg = 'hello', labels = \['one', 'two'] } = defineProps\()
\`\`\`In 3\.4 and below, Reactive Props Destructure is not enabled by default. An alternative is to use the `withDefaults` compiler macro:

ts\`\`\`
interface Props {
 msg?: string
 labels?: string\[]
}

const props = withDefaults(defineProps\(), {
 msg: 'hello',
 labels: () =\> \['one', 'two']
})
\`\`\`This will be compiled to equivalent runtime props `default` options. In addition, the `withDefaults` helper provides type checks for the default values, and ensures the returned `props` type has the optional flags removed for properties that do have default values declared.

INFO

Note that default values for mutable reference types (like arrays or objects) should be wrapped in functions when using `withDefaults` to avoid accidental modification and external side effects. This ensures each component instance gets its own copy of the default value. This is **not** necessary when using default values with destructure.

### Without `` [​](#without-script-setup)

If not using ``, it is necessary to use `defineComponent()` to enable props type inference. The type of the props object passed to `setup()` is inferred from the `props` option.

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 props: {
 message: String
 },
 setup(props) {
 props.message // \
interface Book {
 title: string
 author: string
 year: number
}

const props = defineProps\()
\
\`\`\`For runtime declaration, we can use the `PropType` utility type:

ts\`\`\`
import type { PropType } from 'vue'

const props = defineProps({
 book: Object as PropType\
})
\`\`\`This works in much the same way if we're specifying the `props` option directly:

ts\`\`\`
import { defineComponent } from 'vue'
import type { PropType } from 'vue'

export default defineComponent({
 props: {
 book: Object as PropType\
 }
})
\`\`\`The `props` option is more commonly used with the Options API, so you'll find more detailed examples in the guide to [TypeScript with Options API](/guide/typescript/options-api#typing-component-props). The techniques shown in those examples also apply to runtime declarations using `defineProps()`.

## Typing Component Emits [​](#typing-component-emits)

In ``, the `emit` function can also be typed using either runtime declaration OR type declaration:

vue\`\`\`
\
// runtime
const emit = defineEmits(\['change', 'update'])

// options based
const emit = defineEmits({
 change: (id: number) =\> {
 // return \`true\` or \`false\` to indicate
 // validation pass / fail
 },
 update: (value: string) =\> {
 // return \`true\` or \`false\` to indicate
 // validation pass / fail
 }
})

// type\-based
const emit = defineEmits\()

// 3\.3\+: alternative, more succinct syntax
const emit = defineEmits\()
\
\`\`\`The type argument can be one of the following:

1. A callable function type, but written as a type literal with [Call Signatures](https://www.typescriptlang.org/docs/handbook/2/functions.html#call-signatures). It will be used as the type of the returned `emit` function.
2. A type literal where the keys are the event names, and values are array / tuple types representing the additional accepted parameters for the event. The example above is using named tuples so each argument can have an explicit name.

As we can see, the type declaration gives us much finer\-grained control over the type constraints of emitted events.

When not using ``, `defineComponent()` is able to infer the allowed events for the `emit` function exposed on the setup context:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 emits: \['change'],
 setup(props, { emit }) {
 emit('change') // \
const year = ref(2020\)

// =\> TS Error: Type 'string' is not assignable to type 'number'.
year.value = '2020'
\`\`\`Sometimes we may need to specify complex types for a ref's inner value. We can do that by using the `Ref` type:

ts\`\`\`
import { ref } from 'vue'
import type { Ref } from 'vue'

const year: Ref\ = ref('2020')

year.value = 2020 // ok!
\`\`\`Or, by passing a generic argument when calling `ref()` to override the default inference:

ts\`\`\`
// resulting type: Ref\
const year = ref\('2020')

year.value = 2020 // ok!
\`\`\`If you specify a generic type argument but omit the initial value, the resulting type will be a union type that includes `undefined`:

ts\`\`\`
// inferred type: Ref\
const n = ref\()
\`\`\`## Typing `reactive()` [​](#typing-reactive)

`reactive()` also implicitly infers the type from its argument:

ts\`\`\`
import { reactive } from 'vue'

// inferred type: { title: string }
const book = reactive({ title: 'Vue 3 Guide' })
\`\`\`To explicitly type a `reactive` property, we can use interfaces:

ts\`\`\`
import { reactive } from 'vue'

interface Book {
 title: string
 year?: number
}

const book: Book = reactive({ title: 'Vue 3 Guide' })
\`\`\`TIP

It's not recommended to use the generic argument of `reactive()` because the returned type, which handles nested ref unwrapping, is different from the generic argument type.

## Typing `computed()` [​](#typing-computed)

`computed()` infers its type based on the getter's return value:

ts\`\`\`
import { ref, computed } from 'vue'

const count = ref(0\)

// inferred type: ComputedRef\
const double = computed(() =\> count.value \* 2\)

// =\> TS Error: Property 'split' does not exist on type 'number'
const result = double.value.split('')
\`\`\`You can also specify an explicit type via a generic argument:

ts\`\`\`
const double = computed\(() =\> {
 // type error if this doesn't return a number
})
\`\`\`## Typing Event Handlers [​](#typing-event-handlers)

When dealing with native DOM events, it might be useful to type the argument we pass to the handler correctly. Let's take a look at this example:

vue\`\`\`
\
function handleChange(event) {
 // \`event\` implicitly has \`any\` type
 console.log(event.target.value)
}
\

\
 \
\
\`\`\`Without type annotation, the `event` argument will implicitly have a type of `any`. This will also result in a TS error if `"strict": true` or `"noImplicitAny": true` are used in `tsconfig.json`. It is therefore recommended to explicitly annotate the argument of event handlers. In addition, you may need to use type assertions when accessing the properties of `event`:

ts\`\`\`
function handleChange(event: Event) {
 console.log((event.target as HTMLInputElement).value)
}
\`\`\`## Typing Provide / Inject [​](#typing-provide-inject)

Provide and inject are usually performed in separate components. To properly type injected values, Vue provides an `InjectionKey` interface, which is a generic type that extends `Symbol`. It can be used to sync the type of the injected value between the provider and the consumer:

ts\`\`\`
import { provide, inject } from 'vue'
import type { InjectionKey } from 'vue'

const key = Symbol() as InjectionKey\

provide(key, 'foo') // providing non\-string value will result in error

const foo = inject(key) // type of foo: string \| undefined
\`\`\`It's recommended to place the injection key in a separate file so that it can be imported in multiple components.

When using string injection keys, the type of the injected value will be `unknown`, and needs to be explicitly declared via a generic type argument:

ts\`\`\`
const foo = inject\('foo') // type: string \| undefined
\`\`\`Notice the injected value can still be `undefined`, because there is no guarantee that a provider will provide this value at runtime.

The `undefined` type can be removed by providing a default value:

ts\`\`\`
const foo = inject\('foo', 'bar') // type: string
\`\`\`If you are sure that the value is always provided, you can also force cast the value:

ts\`\`\`
const foo = inject('foo') as string
\`\`\`## Typing Template Refs [​](#typing-template-refs)

With Vue 3\.5 and `@vue/language-tools` 2\.1 (powering both the IDE language service and `vue-tsc`), the type of refs created by `useTemplateRef()` in SFCs can be **automatically inferred** for static refs based on what element the matching `ref` attribute is used on.

In cases where auto\-inference is not possible, you can still cast the template ref to an explicit type via the generic argument:

ts\`\`\`
const el = useTemplateRef\('el')
\`\`\`Usage before 3\.5Template refs should be created with an explicit generic type argument and an initial value of `null`:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

const el = ref\(null)

onMounted(() =\> {
 el.value?.focus()
})
\

\
 \
\
\`\`\`To get the right DOM interface you can check pages like [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#technical_summary).

Note that for strict type safety, it is necessary to use optional chaining or type guards when accessing `el.value`. This is because the initial ref value is `null` until the component is mounted, and it can also be set to `null` if the referenced element is unmounted by `v-if`.

## Typing Component Template Refs [​](#typing-component-template-refs)

With Vue 3\.5 and `@vue/language-tools` 2\.1 (powering both the IDE language service and `vue-tsc`), the type of refs created by `useTemplateRef()` in SFCs can be **automatically inferred** for static refs based on what element or component the matching `ref` attribute is used on.

In cases where auto\-inference is not possible (e.g. non\-SFC usage or dynamic components), you can still cast the template ref to an explicit type via the generic argument.

In order to get the instance type of an imported component, we need to first get its type via `typeof`, then use TypeScript's built\-in `InstanceType` utility to extract its instance type:

vue\`\`\`
\
\
import { useTemplateRef } from 'vue'
import Foo from './Foo.vue'
import Bar from './Bar.vue'

type FooType = InstanceType\
type BarType = InstanceType\

const compRef = useTemplateRef\('comp')
\

\
 \ 0\.5 ? Foo : Bar" ref="comp" /\>
\
\`\`\`In cases where the exact type of the component isn't available or isn't important, `ComponentPublicInstance` can be used instead. This will only include properties that are shared by all components, such as `$el`:

ts\`\`\`
import { useTemplateRef } from 'vue'
import type { ComponentPublicInstance } from 'vue'

const child = useTemplateRef\('child')
\`\`\`In cases where the component referenced is a [generic component](/guide/typescript/overview#generic-components), for instance `MyGenericModal`:

vue\`\`\`
\
\
import { ref } from 'vue'

const content = ref\(null)

const open = (newContent: ContentType) =\> (content.value = newContent)

defineExpose({
 open
})
\
\`\`\`It needs to be referenced using `ComponentExposed` from the [`vue-component-type-helpers`](https://www.npmjs.com/package/vue-component-type-helpers) library as `InstanceType` won't work.

vue\`\`\`
\
\
import { useTemplateRef } from 'vue'
import MyGenericModal from './MyGenericModal.vue'
import type { ComponentExposed } from 'vue\-component\-type\-helpers'

const modal = useTemplateRef\\>('modal')

const openModal = () =\> {
 modal.value?.open('newValue')
}
\
\`\`\`Note that with `@vue/language-tools` 2\.1\+, static template refs' types can be automatically inferred and the above is only needed in edge cases.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/typescript/composition-api.md)



## Compile-Time Flags | Vue.js

[Read the full article](https://vuejs.org/api/compile-time-flags)

# Compile\-Time Flags [​](#compile-time-flags)

TIP

Compile\-time flags only apply when using the `esm-bundler` build of Vue (i.e. `vue/dist/vue.esm-bundler.js`).

When using Vue with a build step, it is possible to configure a number of compile\-time flags to enable / disable certain features. The benefit of using compile\-time flags is that features disabled this way can be removed from the final bundle via tree\-shaking.

Vue will work even if these flags are not explicitly configured. However, it is recommended to always configure them so that the relevant features can be properly removed when possible.

See [Configuration Guides](#configuration-guides) on how to configure them depending on your build tool.

## `__VUE_OPTIONS_API__` [​](#VUE_OPTIONS_API)

* **Default:** `true`

Enable / disable Options API support. Disabling this will result in smaller bundles, but may affect compatibility with 3rd party libraries if they rely on Options API.

## `__VUE_PROD_DEVTOOLS__` [​](#VUE_PROD_DEVTOOLS)

* **Default:** `false`

Enable / disable devtools support in production builds. This will result in more code included in the bundle, so it is recommended to only enable this for debugging purposes.

## `__VUE_PROD_HYDRATION_MISMATCH_DETAILS__` [​](#VUE_PROD_HYDRATION_MISMATCH_DETAILS)

* **Default:** `false`

Enable/disable detailed warnings for hydration mismatches in production builds. This will result in more code included in the bundle, so it is recommended to only enable this for debugging purposes.
* Only available in 3\.4\+

## Configuration Guides [​](#configuration-guides)

### Vite [​](#vite)

`@vitejs/plugin-vue` automatically provides default values for these flags. To change the default values, use Vite's [`define` config option](https://vitejs.dev/config/shared-options.html#define):

js\`\`\`
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
 define: {
 // enable hydration mismatch details in production build
 \_\_VUE\_PROD\_HYDRATION\_MISMATCH\_DETAILS\_\_: 'true'
 }
})
\`\`\`### vue\-cli [​](#vue-cli)

`@vue/cli-service` automatically provides default values for some of these flags. To configure /change the values:

js\`\`\`
// vue.config.js
module.exports = {
 chainWebpack: (config) =\> {
 config.plugin('define').tap((definitions) =\> {
 Object.assign(definitions\[0], {
 \_\_VUE\_OPTIONS\_API\_\_: 'true',
 \_\_VUE\_PROD\_DEVTOOLS\_\_: 'false',
 \_\_VUE\_PROD\_HYDRATION\_MISMATCH\_DETAILS\_\_: 'false'
 })
 return definitions
 })
 }
}
\`\`\`### webpack [​](#webpack)

Flags should be defined using webpack's [DefinePlugin](https://webpack.js.org/plugins/define-plugin/):

js\`\`\`
// webpack.config.js
module.exports = {
 // ...
 plugins: \[
 new webpack.DefinePlugin({
 \_\_VUE\_OPTIONS\_API\_\_: 'true',
 \_\_VUE\_PROD\_DEVTOOLS\_\_: 'false',
 \_\_VUE\_PROD\_HYDRATION\_MISMATCH\_DETAILS\_\_: 'false'
 })
 ]
}
\`\`\`### Rollup [​](#rollup)

Flags should be defined using [@rollup/plugin\-replace](https://github.com/rollup/plugins/tree/master/packages/replace):

js\`\`\`
// rollup.config.js
import replace from '@rollup/plugin\-replace'

export default {
 plugins: \[
 replace({
 \_\_VUE\_OPTIONS\_API\_\_: 'true',
 \_\_VUE\_PROD\_DEVTOOLS\_\_: 'false',
 \_\_VUE\_PROD\_HYDRATION\_MISMATCH\_DETAILS\_\_: 'false'
 })
 ]
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/compile-time-flags.md)



## Accessibility | Vue.js

[Read the full article](https://vuejs.org/guide/best-practices/accessibility)

# Accessibility [​](#accessibility)

Web accessibility (also known as a11y) refers to the practice of creating websites that can be used by anyone — be that a person with a disability, a slow connection, outdated or broken hardware or simply someone in an unfavorable environment. For example, adding subtitles to a video would help both your deaf and hard\-of\-hearing users and your users who are in a loud environment and can't hear their phone. Similarly, making sure your text isn't too low contrast will help both your low\-vision users and your users who are trying to use their phone in bright sunlight.

Ready to start but aren’t sure where?

Checkout the [Planning and managing web accessibility guide](https://www.w3.org/WAI/planning-and-managing/) provided by [World Wide Web Consortium (W3C)](https://www.w3.org/)

## Skip link [​](#skip-link)

You should add a link at the top of each page that goes directly to the main content area so users can skip content that is repeated on multiple Web pages.

Typically this is done on the top of `App.vue` as it will be the first focusable element on all your pages:

template\`\`\`
\
 \
 \Skip to main content\
 \
\
\`\`\`To hide the link unless it is focused, you can add the following style:

css\`\`\`
.skip\-link {
 white\-space: nowrap;
 margin: 1em auto;
 top: 0;
 position: fixed;
 left: 50%;
 margin\-left: \-72px;
 opacity: 0;
}
.skip\-link:focus {
 opacity: 1;
 background\-color: white;
 padding: 0\.5em;
 border: 1px solid black;
}
\`\`\`Once a user changes route, bring focus back to the skip link. This can be achieved by calling focus on the skip link's template ref (assuming usage of `vue-router`):

vue\`\`\`
\
export default {
 watch: {
 $route() {
 this.$refs.skipLink.focus()
 }
 }
}
\
\`\`\`vue\`\`\`
\
import { ref, watch } from 'vue'
import { useRoute } from 'vue\-router'

const route = useRoute()
const skipLink = ref()

watch(
 () =\> route.path,
 () =\> {
 skipLink.value.focus()
 }
)
\
\`\`\`[Read documentation on skip link to main content](https://www.w3.org/WAI/WCAG21/Techniques/general/G1.html)

## Content Structure [​](#content-structure)

One of the most important pieces of accessibility is making sure that design can support accessible implementation. Design should consider not only color contrast, font selection, text sizing, and language, but also how the content is structured in the application.

### Headings [​](#headings)

Users can navigate an application through headings. Having descriptive headings for every section of your application makes it easier for users to predict the content of each section. When it comes to headings, there are a couple of recommended accessibility practices:

* Nest headings in their ranking order: `` \- ``
* Don’t skip headings within a section
* Use actual heading tags instead of styling text to give the visual appearance of headings

[Read more about headings](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-descriptive.html)

template\`\`\`
\
 \Main title\
 \
 \ Section Title \
 \Section Subtitle\
 \
 \
 \
 \ Section Title \
 \Section Subtitle\
 \
 \Section Subtitle\
 \
 \
\
\`\`\`### Landmarks [​](#landmarks)

[Landmarks](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/landmark_role) provide programmatic access to sections within an application. Users who rely on assistive technology can navigate to each section of the application and skip over content. You can use [ARIA roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles) to help you achieve this.

| HTML | ARIA Role | Landmark Purpose |
| --- | --- | --- |
| header | role="banner" | Prime heading: title of the page |
| nav | role="navigation" | Collection of links suitable for use when navigating the document or related documents |
| main | role="main" | The main or central content of the document. |
| footer | role="contentinfo" | Information about the parent document: footnotes/copyrights/links to privacy statement |
| aside | role="complementary" | Supports the main content, yet is separated and meaningful on its own content |
| search | role="search" | This section contains the search functionality for the application |
| form | role="form" | Collection of form\-associated elements |
| section | role="region" | Content that is relevant and that users will likely want to navigate to. Label must be provided for this element |

[Read more about landmarks](https://www.w3.org/TR/wai-aria-1.2/#landmark_roles)

## Semantic Forms [​](#semantic-forms)

When creating a form, you can use the following elements: ``, ``, ``, ``, and ``

Labels are typically placed on top or to the left of the form fields:

template\`\`\`
\
 \
 \{{ item.label }}: \
 \
 \
 \Submit\
\
\`\`\`Notice how you can include `autocomplete='on'` on the form element and it will apply to all inputs in your form. You can also set different [values for autocomplete attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) for each input.

### Labels [​](#labels)

Provide labels to describe the purpose of all form control; linking `for` and `id`:

template\`\`\`
\Name: \
\
\`\`\`If you inspect this element in your Chrome DevTools and open the Accessibility tab inside the Elements tab, you will see how the input gets its name from the label:



Warning:

Though you might have seen labels wrapping the input fields like this:

template\`\`\`
\
 Name:
 \
\
\`\`\`Explicitly setting the labels with a matching id is better supported by assistive technology.

#### `aria-label` [​](#aria-label)

You can also give the input an accessible name with [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label).

template\`\`\`
\Name: \
\
\`\`\`Feel free to inspect this element in Chrome DevTools to see how the accessible name has changed:



#### `aria-labelledby` [​](#aria-labelledby)

Using [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-labelledby) is similar to `aria-label` except it is used if the label text is visible on screen. It is paired to other elements by their `id` and you can link multiple `id`s:

template\`\`\`
\
 \Billing\
 \
 \Name: \
 \
 \
 \Submit\
\
\`\`\`

#### `aria-describedby` [​](#aria-describedby)

[aria\-describedby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby) is used the same way as `aria-labelledby` except provides a description with additional information that the user might need. This can be used to describe the criteria for any input:

template\`\`\`
\
 \Billing\
 \
 \Full Name: \
 \
 \Please provide first and last name.\
 \
 \Submit\
\
\`\`\`You can see the description by inspecting Chrome DevTools:



### Placeholder [​](#placeholder)

Avoid using placeholders as they can confuse many users.

One of the issues with placeholders is that they don't meet the [color contrast criteria](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) by default; fixing the color contrast makes the placeholder look like pre\-populated data in the input fields. Looking at the following example, you can see that the Last Name placeholder which meets the color contrast criteria looks like pre\-populated data:



template\`\`\`
\
 \
 \{{ item.label }}: \
 \
 \
 \Submit\
\
\`\`\`css\`\`\`
/\* https://www.w3schools.com/howto/howto\_css\_placeholder.asp \*/

\#lastName::placeholder {
 /\* Chrome, Firefox, Opera, Safari 10\.1\+ \*/
 color: black;
 opacity: 1; /\* Firefox \*/
}

\#lastName:\-ms\-input\-placeholder {
 /\* Internet Explorer 10\-11 \*/
 color: black;
}

\#lastName::\-ms\-input\-placeholder {
 /\* Microsoft Edge \*/
 color: black;
}
\`\`\`It is best to provide all the information the user needs to fill out forms outside any inputs.

### Instructions [​](#instructions)

When adding instructions for your input fields, make sure to link it correctly to the input. You can provide additional instructions and bind multiple ids inside an [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-labelledby). This allows for more flexible design.

template\`\`\`
\
 \Using aria\-labelledby\
 \Current Date: \
 \
 \MM/DD/YYYY\
\
\`\`\`Alternatively, you can attach the instructions to the input with [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby):

template\`\`\`
\
 \Using aria\-describedby\
 \Date of Birth: \
 \
 \MM/DD/YYYY\
\
\`\`\`### Hiding Content [​](#hiding-content)

Usually it is not recommended to visually hide labels, even if the input has an accessible name. However, if the functionality of the input can be understood with surrounding content, then we can hide the visual label.

Let's look at this search field:

template\`\`\`
\
 \Search: \
 \
 \Search\
\
\`\`\`We can do this because the search button will help visual users identify the purpose of the input field.

We can use CSS to visually hide elements but keep them available for assistive technology:

css\`\`\`
.hidden\-visually {
 position: absolute;
 overflow: hidden;
 white\-space: nowrap;
 margin: 0;
 padding: 0;
 height: 1px;
 width: 1px;
 clip: rect(0 0 0 0\);
 clip\-path: inset(100%);
}
\`\`\`#### `aria-hidden="true"` [​](#aria-hidden-true)

Adding `aria-hidden="true"` will hide the element from assistive technology but leave it visually available for other users. Do not use it on focusable elements, purely on decorative, duplicated or offscreen content.

template\`\`\`
\This is not hidden from screen readers.\
\This is hidden from screen readers.\
\`\`\`### Buttons [​](#buttons)

When using buttons inside a form, you must set the type to prevent submitting the form. You can also use an input to create buttons:

template\`\`\`
\
 \
 \Cancel\
 \Submit\

 \
 \
 \
\
\`\`\`### Functional Images [​](#functional-images)

You can use this technique to create functional images.

* Input fields

	+ These images will act as a submit type button on formstemplate\`\`\`
\
 \Search: \
 \
 \
\
\`\`\`
* Icons

template\`\`\`
\
 \Search: \
 \
 \
 \\
 \Search\
 \
\
\`\`\`## Standards [​](#standards)

The World Wide Web Consortium (W3C) Web Accessibility Initiative (WAI) develops web accessibility standards for the different components:

* [User Agent Accessibility Guidelines (UAAG)](https://www.w3.org/WAI/standards-guidelines/uaag/)
	+ web browsers and media players, including some aspects of assistive technologies
* [Authoring Tool Accessibility Guidelines (ATAG)](https://www.w3.org/WAI/standards-guidelines/atag/)
	+ authoring tools
* [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)
	+ web content \- used by developers, authoring tools, and accessibility evaluation tools

### Web Content Accessibility Guidelines (WCAG) [​](#web-content-accessibility-guidelines-wcag)

[WCAG 2\.1](https://www.w3.org/TR/WCAG21/) extends on [WCAG 2\.0](https://www.w3.org/TR/WCAG20/) and allows implementation of new technologies by addressing changes to the web. The W3C encourages use of the most current version of WCAG when developing or updating Web accessibility policies.

#### WCAG 2\.1 Four Main Guiding Principles (abbreviated as POUR): [​](#wcag-2-1-four-main-guiding-principles-abbreviated-as-pour)

* [Perceivable](https://www.w3.org/TR/WCAG21/#perceivable)
	+ Users must be able to perceive the information being presented
* [Operable](https://www.w3.org/TR/WCAG21/#operable)
	+ Interface forms, controls, and navigation are operable
* [Understandable](https://www.w3.org/TR/WCAG21/#understandable)
	+ Information and the operation of user interface must be understandable to all users
* [Robust](https://www.w3.org/TR/WCAG21/#robust)
	+ Users must be able to access the content as technologies advance

#### Web Accessibility Initiative – Accessible Rich Internet Applications (WAI\-ARIA) [​](#web-accessibility-initiative-–-accessible-rich-internet-applications-wai-aria)

W3C's WAI\-ARIA provides guidance on how to build dynamic content and advanced user interface controls.

* [Accessible Rich Internet Applications (WAI\-ARIA) 1\.2](https://www.w3.org/TR/wai-aria-1.2/)
* [WAI\-ARIA Authoring Practices 1\.2](https://www.w3.org/TR/wai-aria-practices-1.2/)

## Resources [​](#resources)

### Documentation [​](#documentation)

* [WCAG 2\.0](https://www.w3.org/TR/WCAG20/)
* [WCAG 2\.1](https://www.w3.org/TR/WCAG21/)
* [Accessible Rich Internet Applications (WAI\-ARIA) 1\.2](https://www.w3.org/TR/wai-aria-1.2/)
* [WAI\-ARIA Authoring Practices 1\.2](https://www.w3.org/TR/wai-aria-practices-1.2/)

### Assistive Technologies [​](#assistive-technologies)

* Screen Readers
	+ [NVDA](https://www.nvaccess.org/download/)
	+ [VoiceOver](https://www.apple.com/accessibility/mac/vision/)
	+ [JAWS](https://www.freedomscientific.com/products/software/jaws/?utm_term=jaws%20screen%20reader&utm_source=adwords&utm_campaign=All+Products&utm_medium=ppc&hsa_tgt=kwd-394361346638&hsa_cam=200218713&hsa_ad=296201131673&hsa_kw=jaws%20screen%20reader&hsa_grp=52663682111&hsa_net=adwords&hsa_mt=e&hsa_src=g&hsa_acc=1684996396&hsa_ver=3&gclid=Cj0KCQjwnv71BRCOARIsAIkxW9HXKQ6kKNQD0q8a_1TXSJXnIuUyb65KJeTWmtS6BH96-5he9dsNq6oaAh6UEALw_wcB)
	+ [ChromeVox](https://chrome.google.com/webstore/detail/chromevox-classic-extensi/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en)
* Zooming Tools
	+ [MAGic](https://www.freedomscientific.com/products/software/magic/)
	+ [ZoomText](https://www.freedomscientific.com/products/software/zoomtext/)
	+ [Magnifier](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)

### Testing [​](#testing)

* Automated Tools
	+ [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)
	+ [WAVE](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh)
	+ [ARC Toolkit](https://chrome.google.com/webstore/detail/arc-toolkit/chdkkkccnlfncngelccgbgfmjebmkmce?hl=en-US)
* Color Tools
	+ [WebAim Color Contrast](https://webaim.org/resources/contrastchecker/)
	+ [WebAim Link Color Contrast](https://webaim.org/resources/linkcontrastchecker)
* Other Helpful Tools
	+ [HeadingMap](https://chrome.google.com/webstore/detail/headingsmap/flbjommegcjonpdmenkdiocclhjacmbi?hl=en%E2%80%A6)
	+ [Color Oracle](https://colororacle.org)
	+ [NerdeFocus](https://chrome.google.com/webstore/detail/nerdefocus/lpfiljldhgjecfepfljnbjnbjfhennpd?hl=en-US%E2%80%A6)
	+ [Visual Aria](https://chrome.google.com/webstore/detail/visual-aria/lhbmajchkkmakajkjenkchhnhbadmhmk?hl=en-US)
	+ [Silktide Website Accessibility Simulator](https://chrome.google.com/webstore/detail/silktide-website-accessib/okcpiimdfkpkjcbihbmhppldhiebhhaf?hl=en-US)

### Users [​](#users)

The World Health Organization estimates that 15% of the world's population has some form of disability, 2\-4% of them severely so. That is an estimated 1 billion people worldwide; making people with disabilities the largest minority group in the world.

There are a huge range of disabilities, which can be divided roughly into four categories:

* *[Visual](https://webaim.org/articles/visual/)* \- These users can benefit from the use of screen readers, screen magnification, controlling screen contrast, or braille display.
* *[Auditory](https://webaim.org/articles/auditory/)* \- These users can benefit from captioning, transcripts or sign language video.
* *[Motor](https://webaim.org/articles/motor/)* \- These users can benefit from a range of [assistive technologies for motor impairments](https://webaim.org/articles/motor/assistive): voice recognition software, eye tracking, single\-switch access, head wand, sip and puff switch, oversized trackball mouse, adaptive keyboard or other assistive technologies.
* *[Cognitive](https://webaim.org/articles/cognitive/)* \- These users can benefit from supplemental media, structural organization of content, clear and simple writing.

Check out the following links from WebAim to understand from users:

* [Web Accessibility Perspectives: Explore the Impact and Benefits for Everyone](https://www.w3.org/WAI/perspective-videos/)
* [Stories of Web Users](https://www.w3.org/WAI/people-use-web/user-stories/)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/best-practices/accessibility.md)



## Reactivity in Depth | Vue.js

[Read the full article](https://vuejs.org/guide/extras/reactivity-in-depth)

# Reactivity in Depth [​](#reactivity-in-depth)

One of Vue’s most distinctive features is the unobtrusive reactivity system. Component state consists of reactive JavaScript objects. When you modify them, the view updates. It makes state management simple and intuitive, but it’s also important to understand how it works to avoid some common gotchas. In this section, we are going to dig into some of the lower\-level details of Vue’s reactivity system.

## What is Reactivity? [​](#what-is-reactivity)

This term comes up in programming quite a bit these days, but what do people mean when they say it? Reactivity is a programming paradigm that allows us to adjust to changes in a declarative manner. The canonical example that people usually show, because it’s a great one, is an Excel spreadsheet:

|  | A | B | C |
| --- | --- | --- | --- |
| 0 | 1 |  |  |
| 1 | 2 |  |  |
| 2 | 3 |  |  |

Here cell A2 is defined via a formula of `= A0 + A1` (you can click on A2 to view or edit the formula), so the spreadsheet gives us 3\. No surprises there. But if you update A0 or A1, you'll notice that A2 automagically updates too.

JavaScript doesn’t usually work like this. If we were to write something comparable in JavaScript:

js\`\`\`
let A0 = 1
let A1 = 2
let A2 = A0 \+ A1

console.log(A2\) // 3

A0 = 2
console.log(A2\) // Still 3
\`\`\`When we mutate `A0`, `A2` does not change automatically.

So how would we do this in JavaScript? First, in order to re\-run the code that updates `A2`, let's wrap it in a function:

js\`\`\`
let A2

function update() {
 A2 = A0 \+ A1
}
\`\`\`Then, we need to define a few terms:

* The `update()` function produces a **side effect**, or **effect** for short, because it modifies the state of the program.
* `A0` and `A1` are considered **dependencies** of the effect, as their values are used to perform the effect. The effect is said to be a **subscriber** to its dependencies.

What we need is a magic function that can invoke `update()` (the **effect**) whenever `A0` or `A1` (the **dependencies**) change:

js\`\`\`
whenDepsChange(update)
\`\`\`This `whenDepsChange()` function has the following tasks:

1. Track when a variable is read. E.g. when evaluating the expression `A0 + A1`, both `A0` and `A1` are read.
2. If a variable is read when there is a currently running effect, make that effect a subscriber to that variable. E.g. because `A0` and `A1` are read when `update()` is being executed, `update()` becomes a subscriber to both `A0` and `A1` after the first call.
3. Detect when a variable is mutated. E.g. when `A0` is assigned a new value, notify all its subscriber effects to re\-run.

## How Reactivity Works in Vue [​](#how-reactivity-works-in-vue)

We can't really track the reading and writing of local variables like in the example. There's just no mechanism for doing that in vanilla JavaScript. What we **can** do though, is intercept the reading and writing of **object properties**.

There are two ways of intercepting property access in JavaScript: [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description) / [setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#description) and [Proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy). Vue 2 used getter / setters exclusively due to browser support limitations. In Vue 3, Proxies are used for reactive objects and getter / setters are used for refs. Here's some pseudo\-code that illustrates how they work:

js\`\`\`
function reactive(obj) {
 return new Proxy(obj, {
 get(target, key) {
 track(target, key)
 return target\[key]
 },
 set(target, key, value) {
 target\[key] = value
 trigger(target, key)
 }
 })
}

function ref(value) {
 const refObject = {
 get value() {
 track(refObject, 'value')
 return value
 },
 set value(newValue) {
 value = newValue
 trigger(refObject, 'value')
 }
 }
 return refObject
}
\`\`\`TIP

Code snippets here and below are meant to explain the core concepts in the simplest form possible, so many details are omitted, and edge cases ignored.

This explains a few [limitations of reactive objects](/guide/essentials/reactivity-fundamentals#limitations-of-reactive) that we have discussed in the fundamentals section:

* When you assign or destructure a reactive object's property to a local variable, accessing or assigning to that variable is non\-reactive because it no longer triggers the get / set proxy traps on the source object. Note this "disconnect" only affects the variable binding \- if the variable points to a non\-primitive value such as an object, mutating the object would still be reactive.
* The returned proxy from `reactive()`, although behaving just like the original, has a different identity if we compare it to the original using the `===` operator.

Inside `track()`, we check whether there is a currently running effect. If there is one, we lookup the subscriber effects (stored in a Set) for the property being tracked, and add the effect to the Set:

js\`\`\`
// This will be set right before an effect is about
// to be run. We'll deal with this later.
let activeEffect

function track(target, key) {
 if (activeEffect) {
 const effects = getSubscribersForProperty(target, key)
 effects.add(activeEffect)
 }
}
\`\`\`Effect subscriptions are stored in a global `WeakMap>>` data structure. If no subscribing effects Set was found for a property (tracked for the first time), it will be created. This is what the `getSubscribersForProperty()` function does, in short. For simplicity, we will skip its details.

Inside `trigger()`, we again lookup the subscriber effects for the property. But this time we invoke them instead:

js\`\`\`
function trigger(target, key) {
 const effects = getSubscribersForProperty(target, key)
 effects.forEach((effect) =\> effect())
}
\`\`\`Now let's circle back to the `whenDepsChange()` function:

js\`\`\`
function whenDepsChange(update) {
 const effect = () =\> {
 activeEffect = effect
 update()
 activeEffect = null
 }
 effect()
}
\`\`\`It wraps the raw `update` function in an effect that sets itself as the current active effect before running the actual update. This enables `track()` calls during the update to locate the current active effect.

At this point, we have created an effect that automatically tracks its dependencies, and re\-runs whenever a dependency changes. We call this a **Reactive Effect**.

Vue provides an API that allows you to create reactive effects: [`watchEffect()`](/api/reactivity-core#watcheffect). In fact, you may have noticed that it works pretty similarly to the magical `whenDepsChange()` in the example. We can now rework the original example using actual Vue APIs:

js\`\`\`
import { ref, watchEffect } from 'vue'

const A0 = ref(0\)
const A1 = ref(1\)
const A2 = ref()

watchEffect(() =\> {
 // tracks A0 and A1
 A2\.value = A0\.value \+ A1\.value
})

// triggers the effect
A0\.value = 2
\`\`\`Using a reactive effect to mutate a ref isn't the most interesting use case \- in fact, using a computed property makes it more declarative:

js\`\`\`
import { ref, computed } from 'vue'

const A0 = ref(0\)
const A1 = ref(1\)
const A2 = computed(() =\> A0\.value \+ A1\.value)

A0\.value = 2
\`\`\`Internally, `computed` manages its invalidation and re\-computation using a reactive effect.

So what's an example of a common and useful reactive effect? Well, updating the DOM! We can implement simple "reactive rendering" like this:

js\`\`\`
import { ref, watchEffect } from 'vue'

const count = ref(0\)

watchEffect(() =\> {
 document.body.innerHTML = \`Count is: ${count.value}\`
})

// updates the DOM
count.value\+\+
\`\`\`In fact, this is pretty close to how a Vue component keeps the state and the DOM in sync \- each component instance creates a reactive effect to render and update the DOM. Of course, Vue components use much more efficient ways to update the DOM than `innerHTML`. This is discussed in [Rendering Mechanism](/guide/extras/rendering-mechanism).

The `ref()`, `computed()` and `watchEffect()` APIs are all part of the Composition API. If you have only been using Options API with Vue so far, you'll notice that Composition API is closer to how Vue's reactivity system works under the hood. In fact, in Vue 3 the Options API is implemented on top of the Composition API. All property access on the component instance (`this`) triggers getter / setters for reactivity tracking, and options like `watch` and `computed` invoke their Composition API equivalents internally.

## Runtime vs. Compile\-time Reactivity [​](#runtime-vs-compile-time-reactivity)

Vue's reactivity system is primarily runtime\-based: the tracking and triggering are all performed while the code is running directly in the browser. The pros of runtime reactivity are that it can work without a build step, and there are fewer edge cases. On the other hand, this makes it constrained by the syntax limitations of JavaScript, leading to the need of value containers like Vue refs.

Some frameworks, such as [Svelte](https://svelte.dev/), choose to overcome such limitations by implementing reactivity during compilation. It analyzes and transforms the code in order to simulate reactivity. The compilation step allows the framework to alter the semantics of JavaScript itself \- for example, implicitly injecting code that performs dependency analysis and effect triggering around access to locally defined variables. The downside is that such transforms require a build step, and altering JavaScript semantics is essentially creating a language that looks like JavaScript but compiles into something else.

The Vue team did explore this direction via an experimental feature called [Reactivity Transform](/guide/extras/reactivity-transform), but in the end we have decided that it would not be a good fit for the project due to [the reasoning here](https://github.com/vuejs/rfcs/discussions/369#discussioncomment-5059028).

## Reactivity Debugging [​](#reactivity-debugging)

It's great that Vue's reactivity system automatically tracks dependencies, but in some cases we may want to figure out exactly what is being tracked, or what is causing a component to re\-render.

### Component Debugging Hooks [​](#component-debugging-hooks)

We can debug what dependencies are used during a component's render and which dependency is triggering an update using the `renderTracked``onRenderTracked` and `renderTriggered``onRenderTriggered` lifecycle hooks. Both hooks will receive a debugger event which contains information on the dependency in question. It is recommended to place a `debugger` statement in the callbacks to interactively inspect the dependency:

vue\`\`\`
\
import { onRenderTracked, onRenderTriggered } from 'vue'

onRenderTracked((event) =\> {
 debugger
})

onRenderTriggered((event) =\> {
 debugger
})
\
\`\`\`js\`\`\`
export default {
 renderTracked(event) {
 debugger
 },
 renderTriggered(event) {
 debugger
 }
}
\`\`\`TIP

Component debug hooks only work in development mode.

The debug event objects have the following type:

ts\`\`\`
type DebuggerEvent = {
 effect: ReactiveEffect
 target: object
 type:
 \| TrackOpTypes /\* 'get' \| 'has' \| 'iterate' \*/
 \| TriggerOpTypes /\* 'set' \| 'add' \| 'delete' \| 'clear' \*/
 key: any
 newValue?: any
 oldValue?: any
 oldTarget?: Map\ \| Set\
}
\`\`\`### Computed Debugging [​](#computed-debugging)

We can debug computed properties by passing `computed()` a second options object with `onTrack` and `onTrigger` callbacks:

* `onTrack` will be called when a reactive property or ref is tracked as a dependency.
* `onTrigger` will be called when the watcher callback is triggered by the mutation of a dependency.

Both callbacks will receive debugger events in the [same format](#debugger-event) as component debug hooks:

js\`\`\`
const plusOne = computed(() =\> count.value \+ 1, {
 onTrack(e) {
 // triggered when count.value is tracked as a dependency
 debugger
 },
 onTrigger(e) {
 // triggered when count.value is mutated
 debugger
 }
})

// access plusOne, should trigger onTrack
console.log(plusOne.value)

// mutate count.value, should trigger onTrigger
count.value\+\+
\`\`\`TIP

`onTrack` and `onTrigger` computed options only work in development mode.

### Watcher Debugging [​](#watcher-debugging)

Similar to `computed()`, watchers also support the `onTrack` and `onTrigger` options:

js\`\`\`
watch(source, callback, {
 onTrack(e) {
 debugger
 },
 onTrigger(e) {
 debugger
 }
})

watchEffect(callback, {
 onTrack(e) {
 debugger
 },
 onTrigger(e) {
 debugger
 }
})
\`\`\`TIP

`onTrack` and `onTrigger` watcher options only work in development mode.

## Integration with External State Systems [​](#integration-with-external-state-systems)

Vue's reactivity system works by deeply converting plain JavaScript objects into reactive proxies. The deep conversion can be unnecessary or sometimes unwanted when integrating with external state management systems (e.g. if an external solution also uses Proxies).

The general idea of integrating Vue's reactivity system with an external state management solution is to hold the external state in a [`shallowRef`](/api/reactivity-advanced#shallowref). A shallow ref is only reactive when its `.value` property is accessed \- the inner value is left intact. When the external state changes, replace the ref value to trigger updates.

### Immutable Data [​](#immutable-data)

If you are implementing an undo / redo feature, you likely want to take a snapshot of the application's state on every user edit. However, Vue's mutable reactivity system isn't best suited for this if the state tree is large, because serializing the entire state object on every update can be expensive in terms of both CPU and memory costs.

[Immutable data structures](https://en.wikipedia.org/wiki/Persistent_data_structure) solve this by never mutating the state objects \- instead, it creates new objects that share the same, unchanged parts with old ones. There are different ways of using immutable data in JavaScript, but we recommend using [Immer](https://immerjs.github.io/immer/) with Vue because it allows you to use immutable data while keeping the more ergonomic, mutable syntax.

We can integrate Immer with Vue via a simple composable:

js\`\`\`
import { produce } from 'immer'
import { shallowRef } from 'vue'

export function useImmer(baseState) {
 const state = shallowRef(baseState)
 const update = (updater) =\> {
 state.value = produce(state.value, updater)
 }

 return \[state, update]
}
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9VMFu2zAM/RXNl6ZAYnfoTlnSdRt66DBsQ7vtEuXg2YyjRpYEUU5TBPn3UZLtuE1RH2KLfCIfycfsk8/GpNsGkmkyw8IK4xiCa8wVV6I22jq2Zw3CbV2DZQe2srpmZ2km/PmMK8a4KrRCxxbCQY1j1pgyd3DrD0s27++OFh689z/0OOEkTBlPvkNuFfvbAE/Gra/UilzOko0Mh2A+ufcHwd9ij8KtWUjwMsAqlxgjcLU854qrVaMKJ7RiTleVDBRHQpWwO4/xB8xHoRg2v+oyh/MioJepT0ClvTsxhnSUi1LOsthN6iMdCGgkBacTY7NGhjd9ScG2k5W2c56M9rG6ceBPdbOWm1AxO0/a+uiZFjJHpFv7Fj10XhdSFBtyntTJkzaxf/ZtQnYguoFNJkUkmAWGs2xAm47onqT/jPWHxjjYuUkJhba57+yUSaFg4tZWN9X6Y9eIcC8ZJ1FQkzo36QNqRZILQXjroAqnXb+9LQzVD3vtnMFpljXKbKq00HWU3/X7i/QivcxKgS5aUglVXjxNAGvK8KnWZSNJWa0KDoGChzmk3L28jSVcQX1o1d1puwfgOpdSP97BqsfQxhCCK9gFTC+tXu7/coR7R71rxRWXBL2FpHOMOAAeYVGJhBvFL3s+kGKIkW5zSfKfd+RHA2u3gzZEpML9y9JS06YtAq5DLFmOMWXsjkM6rET1YjzUcSMk2J/G1/h8TKGOb8HmV7bdQbqzhmLziv0Bd3Govywg2O1x8Umvua3ARffN/Q/S1sDZDfMN5x2glo3nGGFfGlUS7QEusL0NcxWq+o03OwcKu6Ke/+fwhIb89Y3Sj3Qv0w+9xg7/AWfvyMs=)

### State Machines [​](#state-machines)

[State Machine](https://en.wikipedia.org/wiki/Finite-state_machine) is a model for describing all the possible states an application can be in, and all the possible ways it can transition from one state to another. While it may be overkill for simple components, it can help make complex state flows more robust and manageable.

One of the most popular state machine implementations in JavaScript is [XState](https://xstate.js.org/). Here's a composable that integrates with it:

js\`\`\`
import { createMachine, interpret } from 'xstate'
import { shallowRef } from 'vue'

export function useMachine(options) {
 const machine = createMachine(options)
 const state = shallowRef(machine.initialState)
 const service = interpret(machine)
 .onTransition((newState) =\> (state.value = newState))
 .start()
 const send = (event) =\> service.send(event)

 return \[state, send]
}
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp1U81unDAQfpWRL7DSFqqqUiXEJumhyqVVpDa3ugcKZtcJjC1syEqId8/YBu/uIRcEM9/P/DGz71pn0yhYwUpTD1JbMMKO+o6j7LUaLMwwGvGrqk8SBSzQDqqHJMv7EMleTMIRgGOt0Fj4a2xlxZ5EsPkHhytuOjucbApIrDoeO5HsfQCllVVHUYlVbeW0xr2OKcCzHCwkKQAK3fP56fHx5w/irSyqbfFMgA+h0cKBHZYey45jmYfeqWv6sKLXHbnTF0D5f7RWITzUnaxfD5y5ztIkSCY7zjwKYJ5DyVlf2fokTMrZ5sbZDu6Bs6e25QwK94b0svgKyjwYkEyZR2e2Z2H8n/pK04wV0oL8KEjWJwxncTicnb23C3F2slabIs9H1K/HrFZ9HrIPX7Mv37LPuTC5xEacSfa+V83YEW+bBfleFkuW8QbqQZDEuso9rcOKQQ/CxosIHnQLkWJOVdept9+ijSA6NEJwFGePaUekAdFwr65EaRcxu9BbOKq1JDqnmzIi9oL0RRDu4p1u/ayH9schrhlimGTtOLGnjeJRAJnC56FCQ3SFaYriLWjA4Q7SsPOp6kYnEXMbldKDTW/ssCFgKiaB1kusBWT+rkLYjQiAKhkHvP2j3IqWd5iMQ+M=)

### RxJS [​](#rxjs)

[RxJS](https://rxjs.dev/) is a library for working with asynchronous event streams. The [VueUse](https://vueuse.org/) library provides the [`@vueuse/rxjs`](https://vueuse.org/rxjs/readme.html) add\-on for connecting RxJS streams with Vue's reactivity system.

## Connection to Signals [​](#connection-to-signals)

Quite a few other frameworks have introduced reactivity primitives similar to refs from Vue's Composition API, under the term "signals":

* [Solid Signals](https://www.solidjs.com/docs/latest/api#createsignal)
* [Angular Signals](https://angular.dev/guide/signals)
* [Preact Signals](https://preactjs.com/guide/v10/signals/)
* [Qwik Signals](https://qwik.builder.io/docs/components/state/#usesignal)

Fundamentally, signals are the same kind of reactivity primitive as Vue refs. It's a value container that provides dependency tracking on access, and side\-effect triggering on mutation. This reactivity\-primitive\-based paradigm isn't a particularly new concept in the frontend world: it dates back to implementations like [Knockout observables](https://knockoutjs.com/documentation/observables.html) and [Meteor Tracker](https://docs.meteor.com/api/tracker.html) from more than a decade ago. Vue Options API and the React state management library [MobX](https://mobx.js.org/) are also based on the same principles, but hide the primitives behind object properties.

Although not a necessary trait for something to qualify as signals, today the concept is often discussed alongside the rendering model where updates are performed through fine\-grained subscriptions. Due to the use of Virtual DOM, Vue currently [relies on compilers to achieve similar optimizations](/guide/extras/rendering-mechanism#compiler-informed-virtual-dom). However, we are also exploring a new Solid\-inspired compilation strategy, called [Vapor Mode](https://github.com/vuejs/core-vapor), that does not rely on Virtual DOM and takes more advantage of Vue's built\-in reactivity system.

### API Design Trade\-Offs [​](#api-design-trade-offs)

The design of Preact and Qwik's signals are very similar to Vue's [shallowRef](/api/reactivity-advanced#shallowref): all three provide a mutable interface via the `.value` property. We will focus the discussion on Solid and Angular signals.

#### Solid Signals [​](#solid-signals)

Solid's `createSignal()` API design emphasizes read / write segregation. Signals are exposed as a read\-only getter and a separate setter:

js\`\`\`
const \[count, setCount] = createSignal(0\)

count() // access the value
setCount(1\) // update the value
\`\`\`Notice how the `count` signal can be passed down without the setter. This ensures that the state can never be mutated unless the setter is also explicitly exposed. Whether this safety guarantee justifies the more verbose syntax could be subject to the requirement of the project and personal taste \- but in case you prefer this API style, you can easily replicate it in Vue:

js\`\`\`
import { shallowRef, triggerRef } from 'vue'

export function createSignal(value, options) {
 const r = shallowRef(value)
 const get = () =\> r.value
 const set = (v) =\> {
 r.value = typeof v === 'function' ? v(r.value) : v
 if (options?.equals === false) triggerRef(r)
 }
 return \[get, set]
}
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpdUk1TgzAQ/Ss7uQAjgr12oNXxH+ix9IAYaDQkMV/qMPx3N6G0Uy9Msu/tvn2PTORJqcI7SrakMp1myoKh1qldI9iopLYwQadpa+krG0TLYYZeyxGSojSSs/d7E8vFh0ka0YhOCmPh0EknbB4mPYfTEeqbIelD1oiqXPRQCS+WjoojAW8A1Wmzm1A39KYZzHNVYiUib85aKeCx46z7rBuySqQe6h14uINN1pDIBWACVUcqbGwtl17EqvIiR3LyzwcmcXFuTi3n8vuF9jlYzYaBajxfMsDcomv6E/m9E51luN2NV99yR3OQKkAmgykss+SkMZerxMLEZFZ4oBYJGAA600VEryAaD6CPaJwJKwnr9ldR2WMedV1Dsi6WwB58emZlsAV/zqmH9LzfvqBfruUmNvZ4QN7VearjenP4aHwmWsABt4x/+tiImcx/z27Jqw==)

#### Angular Signals [​](#angular-signals)

Angular is undergoing some fundamental changes by foregoing dirty\-checking and introducing its own implementation of a reactivity primitive. The Angular Signal API looks like this:

js\`\`\`
const count = signal(0\)

count() // access the value
count.set(1\) // set new value
count.update((v) =\> v \+ 1\) // update based on previous value
\`\`\`Again, we can easily replicate the API in Vue:

js\`\`\`
import { shallowRef } from 'vue'

export function signal(initialValue) {
 const r = shallowRef(initialValue)
 const s = () =\> r.value
 s.set = (value) =\> {
 r.value = value
 }
 s.update = (updater) =\> {
 r.value = updater(r.value)
 }
 return s
}
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9Ul1v0zAU/SuWX9ZCSRh7m9IKGHuAB0AD8WQJZclt6s2xLX+ESlH+O9d2krbr1Df7nnPu17k9/aR11nmgt7SwleHaEQvO6w2TvNXKONITyxtZihWpVKu9g5oMZGtUS66yvJSNF6V5lyjZk71ikslKSeuQ7qUj61G+eL+cgFr5RwGITAkXiyVZb5IAn2/IB+QWeeoHO8GPg1aL0gH+CCl215u7mJ3bW9L3s3IYihyxifMlFRpJqewL1qN3TknysRK8el4zGjNlXtdYa9GFrjryllwvGY18QrisDLQgXZTnSX8pF64zzD7pDWDghbbI5/Hoip7tFL05eLErhVD/HmB75Edpyd8zc9DUaAbso3TrZeU4tjfawSV3vBR/SuFhSfrQUXLHBMvmKqe8A8siK7lmsi5gAbJhWARiIGD9hM7BIfHSgjGaHljzlDyGF2MEPQs6g5dpcAIm8Xs+2XxODTgUn0xVYdJ5RxPhKOd4gdMsA/rgLEq3vEEHlEQPYrbgaqu5APNDh6KWUTyuZC2jcWvfYswZD6spXu2gen4l/mT3Icboz3AWpgNGZ8yVBttM8P2v77DH9wy2qvYC2RfAB7BK+NBjon32ssa2j3ix26/xsrhsftv7vQNpp6FCo4E5RD6jeE93F0Y/tHuT3URd2OLwHyXleRY=)

Compared to Vue refs, Solid and Angular's getter\-based API style provide some interesting trade\-offs when used in Vue components:

* `()` is slightly less verbose than `.value`, but updating the value is more verbose.
* There is no ref\-unwrapping: accessing values always require `()`. This makes value access consistent everywhere. This also means you can pass raw signals down as component props.

Whether these API styles suit you is to some extent subjective. Our goal here is to demonstrate the underlying similarity and trade\-offs between these different API designs. We also want to show that Vue is flexible: you are not really locked into the existing APIs. Should it be necessary, you can create your own reactivity primitive API to suit more specific needs.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/reactivity-in-depth.md)



## Template Refs | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/template-refs)

# Template Refs [​](#template-refs)

While Vue's declarative rendering model abstracts away most of the direct DOM operations for you, there may still be cases where we need direct access to the underlying DOM elements. To achieve this, we can use the special `ref` attribute:

template\`\`\`
\
\`\`\``ref` is a special attribute, similar to the `key` attribute discussed in the `v-for` chapter. It allows us to obtain a direct reference to a specific DOM element or child component instance after it's mounted. This may be useful when you want to, for example, programmatically focus an input on component mount, or initialize a 3rd party library on an element.

## Accessing the Refs [​](#accessing-the-refs)

To obtain the reference with Composition API, we can use the [`useTemplateRef()`](/api/composition-api-helpers#usetemplateref)  helper:

vue\`\`\`
\
import { useTemplateRef, onMounted } from 'vue'

// the first argument must match the ref value in the template
const input = useTemplateRef('my\-input')

onMounted(() =\> {
 input.value.focus()
})
\

\
 \
\
\`\`\`When using TypeScript, Vue's IDE support and `vue-tsc` will automatically infer the type of `input.value` based on what element or component the matching `ref` attribute is used on.

Usage before 3\.5In versions before 3\.5 where `useTemplateRef()` was not introduced, we need to declare a ref with a name that matches the template ref attribute's value:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

// declare a ref to hold the element reference
// the name must match template ref value
const input = ref(null)

onMounted(() =\> {
 input.value.focus()
})
\

\
 \
\
\`\`\`If not using ``, make sure to also return the ref from `setup()`:

js\`\`\`
export default {
 setup() {
 const input = ref(null)
 // ...
 return {
 input
 }
 }
}
\`\`\`The resulting ref is exposed on `this.$refs`:

vue\`\`\`
\
export default {
 mounted() {
 this.$refs.input.focus()
 }
}
\

\
 \
\
\`\`\`Note that you can only access the ref **after the component is mounted.** If you try to access `$refs.input``input` in a template expression, it will be `undefined``null` on the first render. This is because the element doesn't exist until after the first render!

If you are trying to watch the changes of a template ref, make sure to account for the case where the ref has `null` value:

js\`\`\`
watchEffect(() =\> {
 if (input.value) {
 input.value.focus()
 } else {
 // not mounted yet, or the element was unmounted (e.g. by v\-if)
 }
})
\`\`\`See also: [Typing Template Refs](/guide/typescript/composition-api#typing-template-refs) 

## Refs inside `v-for` [​](#refs-inside-v-for)

> Requires v3\.5 or above

When `ref` is used inside `v-for`, the corresponding ref should contain an Array value, which will be populated with the elements after mount:

vue\`\`\`
\
import { ref, useTemplateRef, onMounted } from 'vue'

const list = ref(\[
 /\* ... \*/
])

const itemRefs = useTemplateRef('items')

onMounted(() =\> console.log(itemRefs.value))
\

\
 \
 \
 {{ item }}
 \
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9UsluwjAQ/ZWRLwQpDepyQoDUIg6t1EWUW91DFAZq6tiWF4oU5d87dtgqVRyyzLw3b+aN3bB7Y4ptQDZkI1dZYTw49MFMuBK10dZDAxZXOQSHC6yNLD3OY6zVsw7K4xJaWFldQ49UelxxVWnlPEhBr3GszT6uc7jJ4fazf4KFx5p0HFH+Kme9CLle4h6bZFkfxhNouAIoJVqfHQSKbSkDFnVpMhEpovC481NNVcr3SaWlZzTovJErCqgydaMIYBRk+tKfFLC9Wmk75iyqg1DJBWfRxT7pONvTAZom2YC23QsMpOg0B0l0NDh2YjnzjpyvxLrYOK1o3ckLZ5WujSBHr8YL2gxnw85lxEop9c9TynkbMD/kqy+svv/Jb9wu5jh7s+jQbpGzI+ZLu0byEuHZ+wvt6Ays9TJIYl8A5+i0DHHGjvYQ1JLGPuOlaR/TpRFqvXCzHR2BO5iKg0Zmm/ic0W2ZXrB+Gve2uEt1dJKs/QXbwePE)

Usage before 3\.5In versions before 3\.5 where `useTemplateRef()` was not introduced, we need to declare a ref with a name that matches the template ref attribute's value. The ref should also contain an array value:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

const list = ref(\[
 /\* ... \*/
])

const itemRefs = ref(\[])

onMounted(() =\> console.log(itemRefs.value))
\

\
 \
 \
 {{ item }}
 \
 \
\
\`\`\`When `ref` is used inside `v-for`, the resulting ref value will be an array containing the corresponding elements:

vue\`\`\`
\
export default {
 data() {
 return {
 list: \[
 /\* ... \*/
 ]
 }
 },
 mounted() {
 console.log(this.$refs.items)
 }
}
\

\
 \
 \
 {{ item }}
 \
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpFjk0KwjAQha/yCC4Uaou6kyp4DuOi2KkGYhKSiQildzdNa4WQmTc/37xeXJwr35HEUdTh7pXjszT0cdYzWuqaqBm9NEDbcLPeTDngiaM3PwVoFfiI667AvsDhNpWHMQzF+L9sNEztH3C3JlhNpbaPNT9VKFeeulAqplfY5D1p0qurxVQSqel0w5QUUEedY8q0wnvbWX+SYgRAmWxIiuSzm4tBinkc6HvkuSE7TIBKq4lZZWhdLZfE8AWp4l3T)

It should be noted that the ref array does **not** guarantee the same order as the source array.

## Function Refs [​](#function-refs)

Instead of a string key, the `ref` attribute can also be bound to a function, which will be called on each component update and gives you full flexibility on where to store the element reference. The function receives the element reference as the first argument:

template\`\`\`
\ { /\* assign el to a property or ref \*/ }"\>
\`\`\`Note we are using a dynamic `:ref` binding so we can pass it a function instead of a ref name string. When the element is unmounted, the argument will be `null`. You can, of course, use a method instead of an inline function.

## Ref on Component [​](#ref-on-component)

> This section assumes knowledge of [Components](/guide/essentials/component-basics). Feel free to skip it and come back later.

`ref` can also be used on a child component. In this case the reference will be that of a component instance:

vue\`\`\`
\
import { useTemplateRef, onMounted } from 'vue'
import Child from './Child.vue'

const childRef = useTemplateRef('child')

onMounted(() =\> {
 // childRef.value will hold an instance of \
})
\

\
 \
\
\`\`\`Usage before 3\.5vue\`\`\`
\
import { ref, onMounted } from 'vue'
import Child from './Child.vue'

const child = ref(null)

onMounted(() =\> {
 // child.value will hold an instance of \
})
\

\
 \
\
\`\`\`vue\`\`\`
\
import Child from './Child.vue'

export default {
 components: {
 Child
 },
 mounted() {
 // this.$refs.child will hold an instance of \
 }
}
\

\
 \
\
\`\`\`If the child component is using Options API or not using ``, theThe referenced instance will be identical to the child component's `this`, which means the parent component will have full access to every property and method of the child component. This makes it easy to create tightly coupled implementation details between the parent and the child, so component refs should be only used when absolutely needed \- in most cases, you should try to implement parent / child interactions using the standard props and emit interfaces first.

An exception here is that components using `` are **private by default**: a parent component referencing a child component using `` won't be able to access anything unless the child component chooses to expose a public interface using the `defineExpose` macro:

vue\`\`\`
\
import { ref } from 'vue'

const a = 1
const b = ref(2\)

// Compiler macros, such as defineExpose, don't need to be imported
defineExpose({
 a,
 b
})
\
\`\`\`When a parent gets an instance of this component via template refs, the retrieved instance will be of the shape `{ a: number, b: number }` (refs are automatically unwrapped just like on normal instances).

Note that defineExpose must be called before any await operation. Otherwise, properties and methods exposed after the await operation will not be accessible.

See also: [Typing Component Template Refs](/guide/typescript/composition-api#typing-component-template-refs) 

The `expose` option can be used to limit the access to a child instance:

js\`\`\`
export default {
 expose: \['publicData', 'publicMethod'],
 data() {
 return {
 publicData: 'foo',
 privateData: 'bar'
 }
 },
 methods: {
 publicMethod() {
 /\* ... \*/
 },
 privateMethod() {
 /\* ... \*/
 }
 }
}
\`\`\`In the above example, a parent referencing this component via template ref will only be able to access `publicData` and `publicMethod`.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/template-refs.md)



## Watchers | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/watchers)

# Watchers [​](#watchers)

## Basic Example [​](#basic-example)

Computed properties allow us to declaratively compute derived values. However, there are cases where we need to perform "side effects" in reaction to state changes \- for example, mutating the DOM, or changing another piece of state based on the result of an async operation.

With the Options API, we can use the [`watch` option](/api/options-state#watch) to trigger a function whenever a reactive property changes:

js\`\`\`
export default {
 data() {
 return {
 question: '',
 answer: 'Questions usually contain a question mark. ;\-)',
 loading: false
 }
 },
 watch: {
 // whenever question changes, this function will run
 question(newQuestion, oldQuestion) {
 if (newQuestion.includes('?')) {
 this.getAnswer()
 }
 }
 },
 methods: {
 async getAnswer() {
 this.loading = true
 this.answer = 'Thinking...'
 try {
 const res = await fetch('https://yesno.wtf/api')
 this.answer = (await res.json()).answer
 } catch (error) {
 this.answer = 'Error! Could not reach the API. ' \+ error
 } finally {
 this.loading = false
 }
 }
 }
}
\`\`\`template\`\`\`
\
 Ask a yes/no question:
 \
\
\{{ answer }}\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9VE1v2zAM/SucLnaw1D70lqUbsiKH7rB1W4++aDYdq5ElTx9xgiD/fbT8lXZFAQO2+Mgn8pH0mW2aJjl4ZCu2trkRjfucKTw22jgosOReOjhnCqDgjseL/hvAoPNGjSeAvx6tE1qtIIqWo5Er26Ih088BteCt51KeINfKcaGAT5FQc7NP4NPNYiaQmhdC7VZQcmlxMF+61yUcWu7yajVmkabQVqjwgGZmzSuudmiX4CphofQqD+ZWSAnGqz5y9I4VtmOuS9CyGA9T3QCihGu3RKhc+gJtHH2JFld+EG5Mdug2QYZ4MSKhgBd11OgqXdipEm5PKoer0Jk2kA66wB044/EF1GtOSPRUCbUnryRJosnFnK4zpC5YR7205M9bLhyUSIrGUeVcY1dpekKrdNK6MuWNiKYKXt8V98FElDxbknGxGLCpZMi7VkGMxmjzv0pz1tvO4QPcay8LULoj5RToKoTN40MCEXyEQDJTl0KFmXpNOqsUxudN+TNFzzqdJp8ODutGcod0Alg34QWwsXsaVtIjVXqe9h5bC9V4B4ebWhco7zI24hmDVSEs/yOxIPOQEFnTnjzt2emS83nYFrhcevM6nRJhS+Ys9aoUu6Av7WqoNWO5rhsh0fxownplbBqhjJEmuv0WbN2UDNtDMRXm+zfsz/bY2TL2SH1Ec8CMTZjjhqaxh7e/v+ORvieQqvaSvN8Bf6HV0veSdG5fvSoo7Su/kO1D3f13SKInuz06VHYsahzzfl0yRj+s+3dKn9O9TW7HPrPLP624lFU=)

The `watch` option also supports a dot\-delimited path as the key:

js\`\`\`
export default {
 watch: {
 // Note: only simple paths. Expressions are not supported.
 'some.nested.key'(newValue) {
 // ...
 }
 }
}
\`\`\`With Composition API, we can use the [`watch` function](/api/reactivity-core#watch) to trigger a callback whenever a piece of reactive state changes:

vue\`\`\`
\
import { ref, watch } from 'vue'

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;\-)')
const loading = ref(false)

// watch works directly on a ref
watch(question, async (newQuestion, oldQuestion) =\> {
 if (newQuestion.includes('?')) {
 loading.value = true
 answer.value = 'Thinking...'
 try {
 const res = await fetch('https://yesno.wtf/api')
 answer.value = (await res.json()).answer
 } catch (error) {
 answer.value = 'Error! Could not reach the API. ' \+ error
 } finally {
 loading.value = false
 }
 }
})
\

\
 \
 Ask a yes/no question:
 \
 \
 \{{ answer }}\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9U8Fy0zAQ/ZVFF9tDah96C2mZ0umhHKBAj7oIe52oUSQjyXEyGf87KytyoDC9JPa+p+e3b1cndtd15b5HtmQrV1vZeXDo++6Wa7nrjPVwAovtAgbh6w2M0Fqzg4xOZFxzXRvtPPzq0XlpNNwEbp5lRUKEdgPaVP925jnoXS+UOgKxvJAaxEVjJ+y2hA9XxUVFGdFIvT7LtEI5JIzrqjrbGozdOmikxdqTKqmIQOV6gvOkvQDhjrqGXOOQvCzAqCa9FHBzCyeuAWT7F6uUulZ9gy7PPmZFETmQjJV7oXoke972GJHY+Axkzxupt4FalhRcYHh7TDIQcqA+LTriikFIDy0G59nG+84tq+qITpty8G0lOhmSiedefSaPZ0mnfHFG50VRRkbkj1BPceVorbFzF/+6fQj4O7g3vWpAm6Ao6JzfINw9PZaQwXuYNJJuK/U0z1nxdTLT0M7s8Ec/I3WxquLS0brRi8ddp4RHegNYhR0M/Du3pXFSAJU285osI7aSuus97K92pkF1w1nCOYNlI534qbCh8tkOVasoXkV1+sjplLZ0HGN5Vc1G2IJ5R8Np5XpKlK7J1CJntdl1UqH92k0bzdkyNc8ZRWGGz1MtbMQi1esN1tv/1F/cIdQ4e6LJod0jZzPmhV2jj/DDjy94oOcZpK57Rew3wO/ojOpjJIH2qdcN2f6DN7l9nC47RfTsHg4etUtNpZUeJz5ndPPv32j9Yve6vE6DZuNvu1R2Tg==)

### Watch Source Types [​](#watch-source-types)

`watch`'s first argument can be different types of reactive "sources": it can be a ref (including computed refs), a reactive object, a [getter function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description), or an array of multiple sources:

js\`\`\`
const x = ref(0\)
const y = ref(0\)

// single ref
watch(x, (newX) =\> {
 console.log(\`x is ${newX}\`)
})

// getter
watch(
 () =\> x.value \+ y.value,
 (sum) =\> {
 console.log(\`sum of x \+ y is: ${sum}\`)
 }
)

// array of multiple sources
watch(\[x, () =\> y.value], (\[newX, newY]) =\> {
 console.log(\`x is ${newX} and y is ${newY}\`)
})
\`\`\`Do note that you can't watch a property of a reactive object like this:

js\`\`\`
const obj = reactive({ count: 0 })

// this won't work because we are passing a number to watch()
watch(obj.count, (count) =\> {
 console.log(\`Count is: ${count}\`)
})
\`\`\`Instead, use a getter:

js\`\`\`
// instead, use a getter:
watch(
 () =\> obj.count,
 (count) =\> {
 console.log(\`Count is: ${count}\`)
 }
)
\`\`\`## Deep Watchers [​](#deep-watchers)

`watch` is shallow by default: the callback will only trigger when the watched property has been assigned a new value \- it won't trigger on nested property changes. If you want the callback to fire on all nested mutations, you need to use a deep watcher:

js\`\`\`
export default {
 watch: {
 someObject: {
 handler(newValue, oldValue) {
 // Note: \`newValue\` will be equal to \`oldValue\` here
 // on nested mutations as long as the object itself
 // hasn't been replaced.
 },
 deep: true
 }
 }
}
\`\`\`When you call `watch()` directly on a reactive object, it will implicitly create a deep watcher \- the callback will be triggered on all nested mutations:

js\`\`\`
const obj = reactive({ count: 0 })

watch(obj, (newValue, oldValue) =\> {
 // fires on nested property mutations
 // Note: \`newValue\` will be equal to \`oldValue\` here
 // because they both point to the same object!
})

obj.count\+\+
\`\`\`This should be differentiated with a getter that returns a reactive object \- in the latter case, the callback will only fire if the getter returns a different object:

js\`\`\`
watch(
 () =\> state.someObject,
 () =\> {
 // fires only when state.someObject is replaced
 }
)
\`\`\`You can, however, force the second case into a deep watcher by explicitly using the `deep` option:

js\`\`\`
watch(
 () =\> state.someObject,
 (newValue, oldValue) =\> {
 // Note: \`newValue\` will be equal to \`oldValue\` here
 // \*unless\* state.someObject has been replaced
 },
 { deep: true }
)
\`\`\`In Vue 3\.5\+, the `deep` option can also be a number indicating the max traversal depth \- i.e. how many levels should Vue traverse an object's nested properties.

Use with Caution

Deep watch requires traversing all nested properties in the watched object, and can be expensive when used on large data structures. Use it only when necessary and beware of the performance implications.

## Eager Watchers [​](#eager-watchers)

`watch` is lazy by default: the callback won't be called until the watched source has changed. But in some cases we may want the same callback logic to be run eagerly \- for example, we may want to fetch some initial data, and then re\-fetch the data whenever relevant state changes.

We can force a watcher's callback to be executed immediately by declaring it using an object with a `handler` function and the `immediate: true` option:

js\`\`\`
export default {
 // ...
 watch: {
 question: {
 handler(newQuestion) {
 // this will be run immediately on component creation.
 },
 // force eager callback execution
 immediate: true
 }
 }
 // ...
}
\`\`\`The initial execution of the handler function will happen just before the `created` hook. Vue will have already processed the `data`, `computed`, and `methods` options, so those properties will be available on the first invocation.

We can force a watcher's callback to be executed immediately by passing the `immediate: true` option:

js\`\`\`
watch(
 source,
 (newValue, oldValue) =\> {
 // executed immediately, then again when \`source\` changes
 },
 { immediate: true }
)
\`\`\`## Once Watchers [​](#once-watchers)

* Only supported in 3\.4\+

Watcher's callback will execute whenever the watched source changes. If you want the callback to trigger only once when the source changes, use the `once: true` option.

js\`\`\`
export default {
 watch: {
 source: {
 handler(newValue, oldValue) {
 // when \`source\` changes, triggers only once
 },
 once: true
 }
 }
}
\`\`\`js\`\`\`
watch(
 source,
 (newValue, oldValue) =\> {
 // when \`source\` changes, triggers only once
 },
 { once: true }
)
\`\`\`## `watchEffect()` [​](#watcheffect)

It is common for the watcher callback to use exactly the same reactive state as the source. For example, consider the following code, which uses a watcher to load a remote resource whenever the `todoId` ref changes:

js\`\`\`
const todoId = ref(1\)
const data = ref(null)

watch(
 todoId,
 async () =\> {
 const response = await fetch(
 \`https://jsonplaceholder.typicode.com/todos/${todoId.value}\`
 )
 data.value = await response.json()
 },
 { immediate: true }
)
\`\`\`In particular, notice how the watcher uses `todoId` twice, once as the source and then again inside the callback.

This can be simplified with [`watchEffect()`](/api/reactivity-core#watcheffect). `watchEffect()` allows us to track the callback's reactive dependencies automatically. The watcher above can be rewritten as:

js\`\`\`
watchEffect(async () =\> {
 const response = await fetch(
 \`https://jsonplaceholder.typicode.com/todos/${todoId.value}\`
 )
 data.value = await response.json()
})
\`\`\`Here, the callback will run immediately, there's no need to specify `immediate: true`. During its execution, it will automatically track `todoId.value` as a dependency (similar to computed properties). Whenever `todoId.value` changes, the callback will be run again. With `watchEffect()`, we no longer need to pass `todoId` explicitly as the source value.

You can check out [this example](/examples/#fetching-data) of `watchEffect()` and reactive data\-fetching in action.

For examples like these, with only one dependency, the benefit of `watchEffect()` is relatively small. But for watchers that have multiple dependencies, using `watchEffect()` removes the burden of having to maintain the list of dependencies manually. In addition, if you need to watch several properties in a nested data structure, `watchEffect()` may prove more efficient than a deep watcher, as it will only track the properties that are used in the callback, rather than recursively tracking all of them.

TIP

`watchEffect` only tracks dependencies during its **synchronous** execution. When using it with an async callback, only properties accessed before the first `await` tick will be tracked.

### `watch` vs. `watchEffect` [​](#watch-vs-watcheffect)

`watch` and `watchEffect` both allow us to reactively perform side effects. Their main difference is the way they track their reactive dependencies:

* `watch` only tracks the explicitly watched source. It won't track anything accessed inside the callback. In addition, the callback only triggers when the source has actually changed. `watch` separates dependency tracking from the side effect, giving us more precise control over when the callback should fire.
* `watchEffect`, on the other hand, combines dependency tracking and side effect into one phase. It automatically tracks every reactive property accessed during its synchronous execution. This is more convenient and typically results in terser code, but makes its reactive dependencies less explicit.
## Side Effect Cleanup [​](#side-effect-cleanup)

Sometimes we may perform side effects, e.g. asynchronous requests, in a watcher:

js\`\`\`
watch(id, (newId) =\> {
 fetch(\`/api/${newId}\`).then(() =\> {
 // callback logic
 })
})
\`\`\`js\`\`\`
export default {
 watch: {
 id(newId) {
 fetch(\`/api/${newId}\`).then(() =\> {
 // callback logic
 })
 }
 }
}
\`\`\`But what if `id` changes before the request completes? When the previous request completes, it will still fire the callback with an ID value that is already stale. Ideally, we want to be able to cancel the stale request when `id` changes to a new value.

We can use the [`onWatcherCleanup()`](/api/reactivity-core#onwatchercleanup)  API to register a cleanup function that will be called when the watcher is invalidated and is about to re\-run:

js\`\`\`
import { watch, onWatcherCleanup } from 'vue'

watch(id, (newId) =\> {
 const controller = new AbortController()

 fetch(\`/api/${newId}\`, { signal: controller.signal }).then(() =\> {
 // callback logic
 })

 onWatcherCleanup(() =\> {
 // abort stale request
 controller.abort()
 })
})
\`\`\`js\`\`\`
import { onWatcherCleanup } from 'vue'

export default {
 watch: {
 id(newId) {
 const controller = new AbortController()

 fetch(\`/api/${newId}\`, { signal: controller.signal }).then(() =\> {
 // callback logic
 })

 onWatcherCleanup(() =\> {
 // abort stale request
 controller.abort()
 })
 }
 }
}
\`\`\`Note that `onWatcherCleanup` is only supported in Vue 3\.5\+ and must be called during the synchronous execution of a `watchEffect` effect function or `watch` callback function: you cannot call it after an `await` statement in an async function.

Alternatively, an `onCleanup` function is also passed to watcher callbacks as the 3rd argument, and to the `watchEffect` effect function as the first argument:

js\`\`\`
watch(id, (newId, oldId, onCleanup) =\> {
 // ...
 onCleanup(() =\> {
 // cleanup logic
 })
})

watchEffect((onCleanup) =\> {
 // ...
 onCleanup(() =\> {
 // cleanup logic
 })
})
\`\`\`js\`\`\`
export default {
 watch: {
 id(newId, oldId, onCleanup) {
 // ...
 onCleanup(() =\> {
 // cleanup logic
 })
 }
 }
}
\`\`\`This works in versions before 3\.5\. In addition, `onCleanup` passed via function argument is bound to the watcher instance so it is not subject to the synchronously constraint of `onWatcherCleanup`.

## Callback Flush Timing [​](#callback-flush-timing)

When you mutate reactive state, it may trigger both Vue component updates and watcher callbacks created by you.

Similar to component updates, user\-created watcher callbacks are batched to avoid duplicate invocations. For example, we probably don't want a watcher to fire a thousand times if we synchronously push a thousand items into an array being watched.

By default, a watcher's callback is called **after** parent component updates (if any), and **before** the owner component's DOM updates. This means if you attempt to access the owner component's own DOM inside a watcher callback, the DOM will be in a pre\-update state.

### Post Watchers [​](#post-watchers)

If you want to access the owner component's DOM in a watcher callback **after** Vue has updated it, you need to specify the `flush: 'post'` option:

js\`\`\`
export default {
 // ...
 watch: {
 key: {
 handler() {},
 flush: 'post'
 }
 }
}
\`\`\`js\`\`\`
watch(source, callback, {
 flush: 'post'
})

watchEffect(callback, {
 flush: 'post'
})
\`\`\`Post\-flush `watchEffect()` also has a convenience alias, `watchPostEffect()`:

js\`\`\`
import { watchPostEffect } from 'vue'

watchPostEffect(() =\> {
 /\* executed after Vue updates \*/
})
\`\`\`### Sync Watchers [​](#sync-watchers)

It's also possible to create a watcher that fires synchronously, before any Vue\-managed updates:

js\`\`\`
export default {
 // ...
 watch: {
 key: {
 handler() {},
 flush: 'sync'
 }
 }
}
\`\`\`js\`\`\`
watch(source, callback, {
 flush: 'sync'
})

watchEffect(callback, {
 flush: 'sync'
})
\`\`\`Sync `watchEffect()` also has a convenience alias, `watchSyncEffect()`:

js\`\`\`
import { watchSyncEffect } from 'vue'

watchSyncEffect(() =\> {
 /\* executed synchronously upon reactive data change \*/
})
\`\`\`Use with Caution

Sync watchers do not have batching and triggers every time a reactive mutation is detected. It's ok to use them to watch simple boolean values, but avoid using them on data sources that might be synchronously mutated many times, e.g. arrays.

## `this.$watch()` [​](#this-watch)

It's also possible to imperatively create watchers using the [`$watch()` instance method](/api/component-instance#watch):

js\`\`\`
export default {
 created() {
 this.$watch('question', (newQuestion) =\> {
 // ...
 })
 }
}
\`\`\`This is useful when you need to conditionally set up a watcher, or only watch something in response to user interaction. It also allows you to stop the watcher early.

## Stopping a Watcher [​](#stopping-a-watcher)

Watchers declared using the `watch` option or the `$watch()` instance method are automatically stopped when the owner component is unmounted, so in most cases you don't need to worry about stopping the watcher yourself.

In the rare case where you need to stop a watcher before the owner component unmounts, the `$watch()` API returns a function for that:

js\`\`\`
const unwatch = this.$watch('foo', callback)

// ...when the watcher is no longer needed:
unwatch()
\`\`\`Watchers declared synchronously inside `setup()` or `` are bound to the owner component instance, and will be automatically stopped when the owner component is unmounted. In most cases, you don't need to worry about stopping the watcher yourself.

The key here is that the watcher must be created **synchronously**: if the watcher is created in an async callback, it won't be bound to the owner component and must be stopped manually to avoid memory leaks. Here's an example:

vue\`\`\`
\
import { watchEffect } from 'vue'

// this one will be automatically stopped
watchEffect(() =\> {})

// ...this one will not!
setTimeout(() =\> {
 watchEffect(() =\> {})
}, 100\)
\
\`\`\`To manually stop a watcher, use the returned handle function. This works for both `watch` and `watchEffect`:

js\`\`\`
const unwatch = watchEffect(() =\> {})

// ...later, when no longer needed
unwatch()
\`\`\`Note that there should be very few cases where you need to create watchers asynchronously, and synchronous creation should be preferred whenever possible. If you need to wait for some async data, you can make your watch logic conditional instead:

js\`\`\`
// data to be loaded asynchronously
const data = ref(null)

watchEffect(() =\> {
 if (data.value) {
 // do something when data is loaded
 }
})
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/watchers.md)



## Custom Elements API | Vue.js

[Read the full article](https://vuejs.org/api/custom-elements)

# Custom Elements API [​](#custom-elements-api)

## defineCustomElement() [​](#definecustomelement)

This method accepts the same argument as [`defineComponent`](#definecomponent), but instead returns a native [Custom Element](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) class constructor.

* **Type**

ts\`\`\`
function defineCustomElement(
 component:
 \| (ComponentOptions \& CustomElementsOptions)
 \| ComponentOptions\['setup'],
 options?: CustomElementsOptions
): {
 new (props?: object): HTMLElement
}

interface CustomElementsOptions {
 styles?: string\[]

 // the following options are 3\.5\+
 configureApp?: (app: App) =\> void
 shadowRoot?: boolean
 nonce?: string
}
\`\`\`
> Type is simplified for readability.
* **Details**

In addition to normal component options, `defineCustomElement()` also supports a number of options that are custom\-elements\-specific:

	+ **`styles`**: an array of inlined CSS strings for providing CSS that should be injected into the element's shadow root.
	+ **`configureApp`** : a function that can be used to configure the Vue app instance for the custom element.
	+ **`shadowRoot`** : `boolean`, defaults to `true`. Set to `false` to render the custom element without a shadow root. This means `` in custom element SFCs will no longer be encapsulated.
	+ **`nonce`** : `string`, if provided, will be set as the `nonce` attribute on style tags injected to the shadow root.Note that instead of being passed as part of the component itself, these options can also be passed via a second argument:

js\`\`\`
import Element from './MyElement.ce.vue'

defineCustomElement(Element, {
 configureApp(app) {
 // ...
 }
})
\`\`\`The return value is a custom element constructor that can be registered using [`customElements.define()`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/define).
* **Example**

js\`\`\`
import { defineCustomElement } from 'vue'

const MyVueElement = defineCustomElement({
 /\* component options \*/
})

// Register the custom element.
customElements.define('my\-vue\-element', MyVueElement)
\`\`\`
* **See also**

	+ [Guide \- Building Custom Elements with Vue](/guide/extras/web-components#building-custom-elements-with-vue)
	+ Also note that `defineCustomElement()` requires [special config](/guide/extras/web-components#sfc-as-custom-element) when used with Single\-File Components.

## useHost()  [​](#usehost)

A Composition API helper that returns the host element of the current Vue custom element.

## useShadowRoot()  [​](#useshadowroot)

A Composition API helper that returns the shadow root of the current Vue custom element.

## this.$host  [​](#this-host)

An Options API property that exposes the host element of the current Vue custom element.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/custom-elements.md)



## Transition | Vue.js

[Read the full article](https://vuejs.org/guide/built-ins/transition)

# Transition [​](#transition)

Vue offers two built\-in components that can help work with transitions and animations in response to changing state:

* `` for applying animations when an element or component is entering and leaving the DOM. This is covered on this page.
* `` for applying animations when an element or component is inserted into, removed from, or moved within a `v-for` list. This is covered in [the next chapter](/guide/built-ins/transition-group).

Aside from these two components, we can also apply animations in Vue using other techniques such as toggling CSS classes or state\-driven animations via style bindings. These additional techniques are covered in the [Animation Techniques](/guide/extras/animation) chapter.

## The `` Component [​](#the-transition-component)

`` is a built\-in component: this means it is available in any component's template without having to register it. It can be used to apply enter and leave animations on elements or components passed to it via its default slot. The enter or leave can be triggered by one of the following:

* Conditional rendering via `v-if`
* Conditional display via `v-show`
* Dynamic components toggling via the `` special element
* Changing the special `key` attribute

This is an example of the most basic usage:

template\`\`\`
\Toggle\
\
 \hello\
\
\`\`\`css\`\`\`
/\* we will explain what these classes do next! \*/
.v\-enter\-active,
.v\-leave\-active {
 transition: opacity 0\.5s ease;
}

.v\-enter\-from,
.v\-leave\-to {
 opacity: 0;
}
\`\`\`Toggle Fadehello

[Try it in the Playground](https://play.vuejs.org/#eNpVkEFuwyAQRa8yZZNWqu1sunFJ1N4hSzYUjRNUDAjGVJHluxcCipIV/OG/pxEr+/a+TwuykfGogvYEEWnxR2H17F0gWCHgBBtMwc2wy9WdsMIqZ2OuXtwfHErhlcKCb8LyoVoynwPh7I0kzAmA/yxEzsKXMlr9HgRr9Es5BTue3PlskA+1VpFTkDZq0i3niYfU6anRmbqgMY4PZeH8OjwBfHhYIMdIV1OuferQEoZOKtIJ328TgzJhm8BabHR3jeC8VJqusO8/IqCM+CnsVqR3V/mfRxO5amnkCPuK5B+6rcG2fydshks=)

[Try it in the Playground](https://play.vuejs.org/#eNpVkMFuAiEQhl9lyqlNuouXXrZo2nfwuBeKs0qKQGBAjfHdZZfVrAmB+f/M/2WGK/v1vs0JWcdEVEF72vQWz94Fgh0OMhmCa28BdpLk+0etAQJSCvahAOLBnTqgkLA6t/EpVzmCP7lFEB69kYRFAYi/ROQs/Cij1f+6ZyMG1vA2vj3bbN1+b1Dw2lYj2yBt1KRnXRwPudHDnC6pAxrjBPe1n78EBF8MUGSkixnLNjdoCUMjFemMn5NjUGacnboqPVkdOC+Vpgus2q8IKCN+T+suWENwxyWJXKXMyQ5WNVJ+aBqD3e6VSYoi)

TIP

`` only supports a single element or component as its slot content. If the content is a component, the component must also have only one single root element.

When an element in a `` component is inserted or removed, this is what happens:

1. Vue will automatically sniff whether the target element has CSS transitions or animations applied. If it does, a number of [CSS transition classes](#transition-classes) will be added / removed at appropriate timings.
2. If there are listeners for [JavaScript hooks](#javascript-hooks), these hooks will be called at appropriate timings.
3. If no CSS transitions / animations are detected and no JavaScript hooks are provided, the DOM operations for insertion and/or removal will be executed on the browser's next animation frame.

## CSS\-Based Transitions [​](#css-based-transitions)

### Transition Classes [​](#transition-classes)

There are six classes applied for enter / leave transitions.



1. `v-enter-from`: Starting state for enter. Added before the element is inserted, removed one frame after the element is inserted.
2. `v-enter-active`: Active state for enter. Applied during the entire entering phase. Added before the element is inserted, removed when the transition/animation finishes. This class can be used to define the duration, delay and easing curve for the entering transition.
3. `v-enter-to`: Ending state for enter. Added one frame after the element is inserted (at the same time `v-enter-from` is removed), removed when the transition/animation finishes.
4. `v-leave-from`: Starting state for leave. Added immediately when a leaving transition is triggered, removed after one frame.
5. `v-leave-active`: Active state for leave. Applied during the entire leaving phase. Added immediately when a leaving transition is triggered, removed when the transition/animation finishes. This class can be used to define the duration, delay and easing curve for the leaving transition.
6. `v-leave-to`: Ending state for leave. Added one frame after a leaving transition is triggered (at the same time `v-leave-from` is removed), removed when the transition/animation finishes.

`v-enter-active` and `v-leave-active` give us the ability to specify different easing curves for enter / leave transitions, which we'll see an example of in the following sections.

### Named Transitions [​](#named-transitions)

A transition can be named via the `name` prop:

template\`\`\`
\
 ...
\
\`\`\`For a named transition, its transition classes will be prefixed with its name instead of `v`. For example, the applied class for the above transition will be `fade-enter-active` instead of `v-enter-active`. The CSS for the fade transition should look like this:

css\`\`\`
.fade\-enter\-active,
.fade\-leave\-active {
 transition: opacity 0\.5s ease;
}

.fade\-enter\-from,
.fade\-leave\-to {
 opacity: 0;
}
\`\`\`### CSS Transitions [​](#css-transitions)

`` is most commonly used in combination with [native CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions), as seen in the basic example above. The `transition` CSS property is a shorthand that allows us to specify multiple aspects of a transition, including properties that should be animated, duration of the transition, and [easing curves](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function).

Here is a more advanced example that transitions multiple properties, with different durations and easing curves for enter and leave:

template\`\`\`
\
 \hello\
\
\`\`\`css\`\`\`
/\*
 Enter and leave animations can use different
 durations and timing functions.
\*/
.slide\-fade\-enter\-active {
 transition: all 0\.3s ease\-out;
}

.slide\-fade\-leave\-active {
 transition: all 0\.8s cubic\-bezier(1, 0\.5, 0\.8, 1\);
}

.slide\-fade\-enter\-from,
.slide\-fade\-leave\-to {
 transform: translateX(20px);
 opacity: 0;
}
\`\`\`Toggle Slide \+ Fadehello

[Try it in the Playground](https://play.vuejs.org/#eNqFkc9uwjAMxl/F6wXQKIVNk1AX0HbZC4zDDr2E4EK0NIkStxtDvPviFQ0OSFzyx/m+n+34kL16P+lazMpMRBW0J4hIrV9WVjfeBYIDBKzhCHVwDQySdFDZyipnY5Lu3BcsWDCk0OKosqLoKcmfLoSNN5KQbyTWLZGz8KKMVp+LKju573ivsuXKbbcG4d3oDcI9vMkNiqL3JD+AWAVpoyadGFY2yATW5nVSJj9rkspDl+v6hE/hHRrjRMEdpdfiDEkBUVxWaEWkveHj5AzO0RKGXCrSHcKBIfSPKEEaA9PJYwSUEXPX0nNlj8y6RBiUHd5AzCOodq1VvsYfjWE4G6fgEy/zMcxG17B9ZTyX8bV85C5y1S40ZX/kdj+GD1P/zVQA56XStC9h2idJI/z7huz4CxoVvE4=)

[Try it in the Playground](https://play.vuejs.org/#eNqFkc1uwjAMgF/F6wk0SmHTJNQFtF32AuOwQy+hdSFamkSJ08EQ776EbMAkJKTIf7I/O/Y+ezVm3HvMyoy52gpDi0rh1mhL0GDLvSTYVwqg4cQHw2QDWCRv1Z8H4Db6qwSyHlPkEFUQ4bHixA0OYWckJ4wesZUn0gpeainqz3mVRQzM4S7qKlss9XotEd6laBDu4Y03yIpUE+oB2NJy5QSJwFC8w0iIuXkbMkN9moUZ6HPR/uJDeINSalaYxCjOkBBgxeWEijnayWiOz+AcFaHNeU2ix7QCOiFK4FLCZPzoALnDXHt6Pq7hP0Ii7/EGYuag9itR5yv8FmgH01EIPkUxG8F0eA2bJmut7kbX+pG+6NVq28WTBTN+92PwMDHbSAXQhteCdiVMUpNwwuMassMP8kfAJQ==)

### CSS Animations [​](#css-animations)

[Native CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations) are applied in the same way as CSS transitions, with the difference being that `*-enter-from` is not removed immediately after the element is inserted, but on an `animationend` event.

For most CSS animations, we can simply declare them under the `*-enter-active` and `*-leave-active` classes. Here's an example:

template\`\`\`
\
 \
 Hello here is some bouncy text!
 \
\
\`\`\`css\`\`\`
.bounce\-enter\-active {
 animation: bounce\-in 0\.5s;
}
.bounce\-leave\-active {
 animation: bounce\-in 0\.5s reverse;
}
@keyframes bounce\-in {
 0% {
 transform: scale(0\);
 }
 50% {
 transform: scale(1\.25\);
 }
 100% {
 transform: scale(1\);
 }
}
\`\`\`Toggle Hello here is some bouncy text! 

[Try it in the Playground](https://play.vuejs.org/#eNqNksGOgjAQhl9lJNmoBwRNvCAa97YP4JFLbQZsLG3TDqzG+O47BaOezCYkpfB9/0wHbsm3c4u+w6RIyiC9cgQBqXO7yqjWWU9wA4813KH2toUpo9PKVEZaExg92V/YRmBGvsN5ZcpsTGGfN4St04Iw7qg8dkTWwF5qJc/bKnnYk7hWye5gm0ZjmY0YKwDlwQsTFCnWjGiRpaPtjETG43smHPSpqh9pVQKBrjpyrfCNMilZV8Aqd5cNEF4oFVo1pgCJhtBvnjEAP6i1hRN6BBUg2BZhKHUdvMmjWhYHE9dXY/ygzN4PasqhB75djM2mQ7FUSFI9wi0GCJ6uiHYxVsFUGcgX67CpzP0lahQ9/k/kj9CjDzgG7M94rT1PLLxhQ0D+Na4AFI9QW98WEKTQOMvnLAOwDrD+wC0Xq/Ubusw/sU+QL/45hskk9z8Bddbn)

[Try it in the Playground](https://play.vuejs.org/#eNqNUs2OwiAQfpWxySZ66I8mXioa97YP4LEXrNNKpEBg2tUY330pqOvJmBBgyPczP1yTb2OyocekTJirrTC0qRSejbYEB2x4LwmulQI4cOLTWbwDWKTeqkcE4I76twSyPcaX23j4zS+WP3V9QNgZyQnHiNi+J9IKtrUU9WldJaMMrGEynlWy2em2lcjyCPMUALazXDlBwtMU79CT9rpXNXp4tGYGhlQ0d7UqAUcXOeI6bluhUtKmhEVhzisgPFPKpWhVCTUqQrt6ygD8oJQajmgRhAOnO4RgdQm8yd0tNzGv/D8x/8Dy10IVCzn4axaTTYNZymsSA8YuciU6PrLL6IKpUFBkS7cKXXwQJfIBPyP6IQ1oHUaB7QkvjfUdcy+wIFB8PeZIYwmNtl0JruYSp8XMk+/TXL7BzbPF8gU6L95hn8D4OUJnktsfM1vavg==)

### Custom Transition Classes [​](#custom-transition-classes)

You can also specify custom transition classes by passing the following props to ``:

* `enter-from-class`
* `enter-active-class`
* `enter-to-class`
* `leave-from-class`
* `leave-active-class`
* `leave-to-class`

These will override the conventional class names. This is especially useful when you want to combine Vue's transition system with an existing CSS animation library, such as [Animate.css](https://daneden.github.io/animate.css/):

template\`\`\`
\
\
 \hello\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqNUctuwjAQ/BXXF9oDsZB6ogbRL6hUcbSEjLMhpn7JXtNWiH/vhqS0R3zxPmbWM+szf02pOVXgSy6LyTYhK4A1rVWwPsWM7MwydOzCuhw9mxF0poIKJoZC0D5+stUAeMRc4UkFKcYpxKcEwSenEYYM5b4ixsA2xlnzsVJ8Yj8Mt+LrbTwcHEgxwojCmNxmHYpFG2kaoxO0B2KaWjD6uXG6FCiKj00ICHmuDdoTjD2CavJBCna7KWjZrYK61b9cB5pI93P3sQYDbxXf7aHHccpVMolO7DS33WSQjPXgXJRi2Cl1xZ8nKkjxf0dBFvx2Q7iZtq94j5jKUgjThmNpjIu17ZzO0JjohT7qL+HsvohJWWNKEc/NolncKt6Goar4y/V7rg/wyw9zrLOy)

[Try it in the Playground](https://play.vuejs.org/#eNqNUcFuwjAM/RUvp+1Ao0k7sYDYF0yaOFZCJjU0LE2ixGFMiH9f2gDbcVKU2M9+tl98Fm8hNMdMYi5U0tEEXraOTsFHho52mC3DuXUAHTI+PlUbIBLn6G4eQOr91xw4ZqrIZXzKVY6S97rFYRqCRabRY7XNzN7BSlujPxetGMvAAh7GtxXLtd/vLSlZ0woFQK0jumTY+FJt7ORwoMLUObEfZtpiSpRaUYPkmOIMNZsj1VhJRWeGMsFmczU6uCOMHd64lrCQ/s/d+uw0vWf+MPuea5Vp5DJ0gOPM7K4Ci7CerPVKhipJ/moqgJJ//8ipxN92NFdmmLbSip45pLmUunOH1Gjrc7ezGKnRfpB4wJO0ZpvkdbJGpyRfmufm+Y4Mxo1oK16n9UwNxOUHwaK3iQ==)

### Using Transitions and Animations Together [​](#using-transitions-and-animations-together)

Vue needs to attach event listeners in order to know when a transition has ended. It can either be `transitionend` or `animationend`, depending on the type of CSS rules applied. If you are only using one or the other, Vue can automatically detect the correct type.

However, in some cases you may want to have both on the same element, for example having a CSS animation triggered by Vue, along with a CSS transition effect on hover. In these cases, you will have to explicitly declare the type you want Vue to care about by passing the `type` prop, with a value of either `animation` or `transition`:

template\`\`\`
\...\
\`\`\`### Nested Transitions and Explicit Transition Durations [​](#nested-transitions-and-explicit-transition-durations)

Although the transition classes are only applied to the direct child element in ``, we can transition nested elements using nested CSS selectors:

template\`\`\`
\
 \
 \
 Hello
 \
 \
\
\`\`\`css\`\`\`
/\* rules that target nested elements \*/
.nested\-enter\-active .inner,
.nested\-leave\-active .inner {
 transition: all 0\.3s ease\-in\-out;
}

.nested\-enter\-from .inner,
.nested\-leave\-to .inner {
 transform: translateX(30px);
 opacity: 0;
}

/\* ... other necessary CSS omitted \*/
\`\`\`We can even add a transition delay to the nested element on enter, which creates a staggered enter animation sequence:

css\`\`\`
/\* delay enter of nested element for staggered effect \*/
.nested\-enter\-active .inner {
 transition\-delay: 0\.25s;
}
\`\`\`However, this creates a small issue. By default, the `` component attempts to automatically figure out when the transition has finished by listening to the **first** `transitionend` or `animationend` event on the root transition element. With a nested transition, the desired behavior should be waiting until the transitions of all inner elements have finished.

In such cases you can specify an explicit transition duration (in milliseconds) using the `duration` prop on the `` component. The total duration should match the delay plus transition duration of the inner element:

template\`\`\`
\...\
\`\`\`ToggleHello[Try it in the Playground](https://play.vuejs.org/#eNqVVd9v0zAQ/leO8LAfrE3HNKSFbgKmSYMHQNAHkPLiOtfEm2NHttN2mvq/c7bTNi1jgFop9t13d9995ziPyfumGc5bTLJkbLkRjQOLrm2uciXqRhsHj2BwBiuYGV3DAUEPcpUrrpUlaKUXcOkBh860eJSrcRqzUDxtHNaNZA5pBzCets5pBe+4FPz+Mk+66Bf+mSdXE12WEsdphMWQiWHKCicoLCtaw/yKIs/PR3kCitVIG4XWYUEJfATFFGIO84GYdRUIyCWzlra6dWg2wA66dgqlts7c+d8tSqk34JTQ6xqb9TjdUiTDOO21TFvrHqRfDkPpExiGKvBITjdl/L40ulVFBi8R8a3P17CiEKrM4GzULIOlFmpQoSgrl8HpKFpX3kFZu2y0BNhJxznvwaJCA1TEYcC4E3MkKp1VIptjZ43E3KajDJiUMBqeWUBmcUBUqJGYOT2GAiV7gJAA9Iy4GyoBKLH2z+N0W3q/CMC2yCCkyajM63Mbc+9z9mfvZD+b071MM23qLC69+j8PvX5HQUDdMC6cL7BOTtQXCJwpas/qHhWIBdYtWGgtDWNttWTmThu701pf1W6+v1Hd8Xbz+k+VQxmv8i7Fv1HZn+g/iv2nRkjzbd6npf/Rkz49DifQ3dLZBBYOJzC4rqgCwsUbmLYlCAUVU4XsCd1NrCeRHcYXb1IJC/RX2hEYCwJTvHYVMZoavbBI09FmU+LiFSzIh0AIXy1mqZiFKaKCmVhiEVJ7GftHZTganUZ56EYLL3FykjhL195MlMM7qxXdmEGDPOG6boRE86UJVPMki+p4H01WLz4Fm78hSdBo5xXy+yfsd3bpbXny1SA1M8c82fgcMyW66L75/hmXtN44a120ktDPOL+h1bL1HCPsA42DaPdwge3HcO/TOCb2ZumQJtA15Yl65Crg84S+BdfPtL6lezY8C3GkZ7L6Bc1zNR0=)

If necessary, you can also specify separate values for enter and leave durations using an object:

template\`\`\`
\...\
\`\`\`### Performance Considerations [​](#performance-considerations)

You may notice that the animations shown above are mostly using properties like `transform` and `opacity`. These properties are efficient to animate because:

1. They do not affect the document layout during the animation, so they do not trigger expensive CSS layout calculation on every animation frame.
2. Most modern browsers can leverage GPU hardware acceleration when animating `transform`.

In comparison, properties like `height` or `margin` will trigger CSS layout, so they are much more expensive to animate, and should be used with caution.

## JavaScript Hooks [​](#javascript-hooks)

You can hook into the transition process with JavaScript by listening to events on the `` component:

html\`\`\`
\
 \
\
\`\`\`js\`\`\`
// called before the element is inserted into the DOM.
// use this to set the "enter\-from" state of the element
function onBeforeEnter(el) {}

// called one frame after the element is inserted.
// use this to start the entering animation.
function onEnter(el, done) {
 // call the done callback to indicate transition end
 // optional if used in combination with CSS
 done()
}

// called when the enter transition has finished.
function onAfterEnter(el) {}

// called when the enter transition is cancelled before completion.
function onEnterCancelled(el) {}

// called before the leave hook.
// Most of the time, you should just use the leave hook
function onBeforeLeave(el) {}

// called when the leave transition starts.
// use this to start the leaving animation.
function onLeave(el, done) {
 // call the done callback to indicate transition end
 // optional if used in combination with CSS
 done()
}

// called when the leave transition has finished and the
// element has been removed from the DOM.
function onAfterLeave(el) {}

// only available with v\-show transitions
function onLeaveCancelled(el) {}
\`\`\`js\`\`\`
export default {
 // ...
 methods: {
 // called before the element is inserted into the DOM.
 // use this to set the "enter\-from" state of the element
 onBeforeEnter(el) {},

 // called one frame after the element is inserted.
 // use this to start the animation.
 onEnter(el, done) {
 // call the done callback to indicate transition end
 // optional if used in combination with CSS
 done()
 },

 // called when the enter transition has finished.
 onAfterEnter(el) {},

 // called when the enter transition is cancelled before completion.
 onEnterCancelled(el) {},

 // called before the leave hook.
 // Most of the time, you should just use the leave hook.
 onBeforeLeave(el) {},

 // called when the leave transition starts.
 // use this to start the leaving animation.
 onLeave(el, done) {
 // call the done callback to indicate transition end
 // optional if used in combination with CSS
 done()
 },

 // called when the leave transition has finished and the
 // element has been removed from the DOM.
 onAfterLeave(el) {},

 // only available with v\-show transitions
 onLeaveCancelled(el) {}
 }
}
\`\`\`These hooks can be used in combination with CSS transitions / animations or on their own.

When using JavaScript\-only transitions, it is usually a good idea to add the `:css="false"` prop. This explicitly tells Vue to skip auto CSS transition detection. Aside from being slightly more performant, this also prevents CSS rules from accidentally interfering with the transition:

template\`\`\`
\
 ...
\
\`\`\`With `:css="false"`, we are also fully responsible for controlling when the transition ends. In this case, the `done` callbacks are required for the `@enter` and `@leave` hooks. Otherwise, the hooks will be called synchronously and the transition will finish immediately.

Here's a demo using the [GSAP library](https://gsap.com/) to perform the animations. You can, of course, use any other animation library you want, for example [Anime.js](https://animejs.com/) or [Motion One](https://motion.dev/):

Toggle[Try it in the Playground](https://play.vuejs.org/#eNqNVMtu2zAQ/JUti8I2YD3i1GigKmnaorcCveTQArpQFCWzlkiCpBwHhv+9Sz1qKYckJ3FnlzvD2YVO5KvW4aHlJCGpZUZoB5a7Vt9lUjRaGQcnMLyEM5RGNbDA0sX/VGWpHnB/xEQmmZIWe+zUI9z6m0tnWr7ymbKVzAklQclvvFSG/5COmyWvV3DKJHTdQiRHZN0jAJbRmv9OIA432/UE+jODlKZMuKcErnx8RrazP8woR7I1FEryKaVTU8aiNdRfwWZTQtQwi1HAGF/YB4BTyxNY8JpaJ1go5K/WLTfhdg1Xq8V4SX5Xja65w0ovaCJ8Jvsnpwc+l525F2XH4ac3Cj8mcB3HbxE9qnvFMRzJ0K3APuhIjPefmTTyvWBAGvWbiDuIgeNYRh3HCCDNW+fQmHtWC7a/zciwaO/8NyN3D6qqap5GfVnXAC89GCqt8Bp77vu827+A+53AJrOFzMhQdMnO8dqPpMO74Yx4wqxFtKS1HbBOMdIX4gAMffVp71+Qq2NG4BCIcngBKk8jLOvfGF30IpBGEwcwtO6p9sdwbNXPIadsXxnVyiKB9x83+c3N9WePN9RUQgZO6QQ2sT524KMo3M5Pf4h3XFQ7NwFyZQpuAkML0doEtvEHhPvRDPRkTfq/QNDgRvy1SuIvpFOSDQmbkWTckf7hHsjIzjltkyhqpd5XIVNN5HNfGlW09eAcMp3J+R+pEn7L)

[Try it in the Playground](https://play.vuejs.org/#eNqNVFFvmzAQ/is3pimNlABNF61iaddt2tukvfRhk/xiwIAXsJF9pKmq/PedDTSwh7ZSFLjvzvd9/nz4KfjatuGhE0ES7GxmZIu3TMmm1QahtLyFwugGFu51wRQAU+Lok7koeFcjPDk058gvlv07gBHYGTVGALbSDwmg6USPnNzjtHL/jcBK5zZxxQwZavVNFNqIHwqF8RUAWs2jn4IffCfqQz+mik5lKLWi3GT1hagHRU58aAUSshpV2YzX4ncCcbjZDp099GcG6ZZnEh8TuPR8S0/oTJhQjmQryLUSU0rUU8a8M9wtoWZTQtIwi0nAGJ/ZB0BwKxJYiJpblFko1a8OLzbhdgWXy8WzP99109YCqdIJmgifyfYuzmUzfFF2HH56o/BjAldx/BbRo7pXHKMjGbrl1IcciWn9fyaNfC8YsIueR5wCFFTGUVAEsEs7pOmDu6yW2f6GBW5o4QbeuScLbu91WdZiF/VlvgEtujdcWek09tx3qZ+/tXAzQU1mA8mCoeicneO1OxKP9yM+4ElmLaEFr+2AecVEn8sDZOSrSzv/1qk+sgAOa1kMOyDlu4jK+j1GZ70E7KKJAxRafKzdazi26s8h5dm+NLpTeQLvP27S6+urz/7T5aaUao26TWATt0cPPsgcK3f6Q1wJWVY4AVJtcmHWhueyo89+G38guD+agT5YBf39s25oIv5arehu8krYkLAs8BeG86DfuANYUCG2NomiTrX7Msx0E7ncl0bnXT04566M4PQPykWaWw==)

## Reusable Transitions [​](#reusable-transitions)

Transitions can be reused through Vue's component system. To create a reusable transition, we can create a component that wraps the `` component and passes down the slot content:

vue\`\`\`
\
\
// JavaScript hooks logic...
\

\
 \
 \
 \\ \
 \
\

\
/\*
 Necessary CSS...
 Note: avoid using \ here since it
 does not apply to slot content.
\*/
\
\`\`\`Now `MyTransition` can be imported and used just like the built\-in version:

template\`\`\`
\
 \Hello\
\
\`\`\`## Transition on Appear [​](#transition-on-appear)

If you also want to apply a transition on the initial render of a node, you can add the `appear` prop:

template\`\`\`
\
 ...
\
\`\`\`## Transition Between Elements [​](#transition-between-elements)

In addition to toggling an element with `v-if` / `v-show`, we can also transition between two elements using `v-if` / `v-else` / `v-else-if`, as long as we make sure that there is only one element being shown at any given moment:

template\`\`\`
\
 \Edit\
 \Save\
 \Cancel\
\
\`\`\`Click to cycle through states: Edit [Try it in the Playground](https://play.vuejs.org/#eNqdk8tu2zAQRX9loI0SoLLcFN2ostEi6BekmwLa0NTYJkKRBDkSYhj+9wxJO3ZegBGu+Lhz7syQ3Bd/nJtNIxZN0QbplSMISKNbdkYNznqCPXhcwwHW3g5QsrTsTGekNYGgt/KBBCEsouimDGLCvrztTFtnGGN4QTg4zbK4ojY4YSDQTuOiKwbhN8pUXm221MDd3D11xfJeK/kIZEHupEagrbfjZssxzAgNs5nALIC2VxNILUJg1IpMxWmRUAY9U6IZ2/3zwgRFyhowYoieQaseq9ElDaTRrkYiVkyVWrPiXNdiAcequuIkPo3fMub5Sg4l9oqSevmXZ22dwR8YoQ74kdsL4Go7ZTbR74HT/KJfJlxleGrG8l4YifqNYVuf251vqOYr4llbXz4C06b75+ns1a3BPsb0KrBy14Aymnerlbby8Vc8cTajG35uzFITpu0t5ufzHQdeH6LBsezEO0eJVbB6pBiVVLPTU6jQEPpKyMj8dnmgkQs+HmQcvVTIQK1hPrv7GQAFt9eO9Bk6fZ8Ub52Qiri8eUo+4dbWD02exh79v/nBP+H2PStnwz/jelJ1geKvk/peHJ4BoRZYow==)

## Transition Modes [​](#transition-modes)

In the previous example, the entering and leaving elements are animated at the same time, and we had to make them `position: absolute` to avoid the layout issue when both elements are present in the DOM.

However, in some cases this isn't an option, or simply isn't the desired behavior. We may want the leaving element to be animated out first, and for the entering element to only be inserted **after** the leaving animation has finished. Orchestrating such animations manually would be very complicated \- luckily, we can enable this behavior by passing `` a `mode` prop:

template\`\`\`
\
 ...
\
\`\`\`Here's the previous demo with `mode="out-in"`:

Click to cycle through states: Edit `` also supports `mode="in-out"`, although it's much less frequently used.

## Transition Between Components [​](#transition-between-components)

`` can also be used around [dynamic components](/guide/essentials/component-basics#dynamic-components):

template\`\`\`
\
 \\
\
\`\`\` A  B Component A[Try it in the Playground](https://play.vuejs.org/#eNqtksFugzAMhl/F4tJNKtDLLoxWKnuDacdcUnC3SCGJiMmEqr77EkgLbXfYYZyI8/v77dinZG9M5npMiqS0dScMgUXqzY4p0RrdEZzAfnEp9fc7HuEMx063sPIZq6viTbdmHy+yfDwF5K2guhFUUcBUnkNvcelBGrjTooHaC7VCRXBAoT6hQTRyAH2w2DlsmKq1sgS8JuEwUCfxdgF7Gqt5ZqrMp+58X/5A2BrJCcOJSskPKP0v+K8UyvQENBjcsqTjjdAsAZe2ukHpI3dm/q5wXPZBPFqxZAf7gCrzGfufDlVwqB4cPjqurCChFSjeBvGRN+iTA9afdE+pUD43FjG/bSHsb667Mr9qJot89vCBMl8+oiotDTL8ZsE39UnYpRN0fQlK5A5jEE6BSVdiAdrwWtAAm+zFAnKLr0ydA3pJDDt0x/PrMrJifgGbKdFPfCwpWU+TuWz5omzfVCNcfJJ5geL8pqtFn5E07u7fSHFOj6TzDyUDNEM=)

[Try it in the Playground](https://play.vuejs.org/#eNqtks9ugzAMxl/F4tJNamGXXVhWqewVduSSgStFCkkUDFpV9d0XJyn9t8MOkxBg5/Pvi+Mci51z5TxhURdi7LxytG2NGpz1BB92cDvYezvAqqxixNLVjaC5ETRZ0Br8jpIe93LSBMfWAHRBYQ0aGms4Jvw6Q05rFvSS5NNzEgN4pMmbcwQgO1Izsj5CalhFRLDj1RN/wis8olpaCQHh4LQk5IiEll+owy+XCGXcREAHh+9t4WWvbFvAvBlsjzpk7gx5TeqJtdG4LbawY5KoLtR/NGjYoHkw+PTSjIqUNWDkwOK97DHUMjVEdqKNMqE272E5dajV+JvpVlSLJllUF4+QENX1ERox0kHzb8m+m1CEfpOgYYgpqVHOmJNpgLQQa7BOdooO8FK+joByxLc4tlsiX6s7HtnEyvU1vKTCMO+4pWKdBnO+0FfbDk31as5HsvR+Hl9auuozk+J1/hspz+mRdPoBYtonzg==)

## Dynamic Transitions [​](#dynamic-transitions)

`` props like `name` can also be dynamic! It allows us to dynamically apply different transitions based on state change:

template\`\`\`
\
 \
\
\`\`\`This can be useful when you've defined CSS transitions / animations using Vue's transition class conventions and want to switch between them.

You can also apply different behavior in JavaScript transition hooks based on the current state of your component. Finally, the ultimate way of creating dynamic transitions is through [reusable transition components](#reusable-transitions) that accept props to change the nature of the transition(s) to be used. It may sound cheesy, but the only limit really is your imagination.

## Transitions with the Key Attribute [​](#transitions-with-the-key-attribute)

Sometimes you need to force the re\-render of a DOM element in order for a transition to occur.

Take this counter component for example:

vue\`\`\`
\
import { ref } from 'vue';
const count = ref(0\);

setInterval(() =\> count.value\+\+, 1000\);
\

\
 \
 \{{ count }}\
 \
\
\`\`\`vue\`\`\`
\
export default {
 data() {
 return {
 count: 1,
 interval: null 
 }
 },
 mounted() {
 this.interval = setInterval(() =\> {
 this.count\+\+;
 }, 1000\)
 },
 beforeDestroy() {
 clearInterval(this.interval)
 }
}
\

\
 \
 \{{ count }}\
 \
\
\`\`\`If we had excluded the `key` attribute, only the text node would be updated and thus no transition would occur. However, with the `key` attribute in place, Vue knows to create a new `span` element whenever `count` changes and thus the `Transition` component has 2 different elements to transition between.

[Try it in the Playground](https://play.vuejs.org/#eNp9UsFu2zAM/RVCl6Zo4nhYd/GcAtvQQ3fYhq1HXTSFydTKkiDJbjLD/z5KMrKgLXoTHx/5+CiO7JNz1dAja1gbpFcuQsDYuxtuVOesjzCCxx1MsPO2gwuiXnzkhhtpTYggbW8ibBJlUV/mBJXfmYh+EHqxuITNDYzcQGFWBPZ4dUXEaQnv6jrXtOuiTJoUROycFhEpAmi3agCpRQgbzp68cA49ZyV174UJKiprckxIcMJA84hHImc9oo7jPOQ0kQ4RSvH6WXW7JiV6teszfQpDPGqEIK3DLSGpQbazsyaugvqLDVx77JIhbqp5wsxwtrRvPFI7NWDhEGtYYVrQSsgELzOiUQw4I2Vh8TRgA9YJqeIR6upDABQh9TpTAPE7WN3HlxLp084Foi3N54YN1KWEVpOMkkO2ZJHsmp3aVw/BGjqMXJE22jml0X93STRw1pReKSe0tk9fMxZ9nzwVXP5B+fgK/hAOCePsh8dAt4KcnXJR+D3S16X07a9veKD3KdnZba+J/UbyJ+Zl0IyF9rk3Wxr7jJenvcvnrcz+PtweItKuZ1Np0MScMp8zOvkvb1j/P+776jrX0UbZ9A+fYSTP)

[Try it in the Playground](https://play.vuejs.org/#eNp9U8tu2zAQ/JUFTwkSyw6aXlQ7QB85pIe2aHPUhZHWDhOKJMiVYtfwv3dJSpbbBgEMWJydndkdUXvx0bmi71CUYhlqrxzdVAa3znqCBtey0wT7ygA0kuTZeX4G8EidN+MJoLadoRKuLkdAGULfS12C6bSGDB/i3yFx2tiAzaRIjyoUYxesICDdDaczZq1uJrNETY4XFx8G5Uu4WiwW55PBA66txy8YyNvdZFNrlP4o/Jdpbq4M/5bzYxZ8IGydloR8Alg2qmcVGcKqEi9eOoe+EqnExXsvTVCkrBkQxoKTBspn3HFDmprp+32ODA4H9mLCKDD/R2E5Zz9+Ws5PpuBjoJ1GCLV12DASJdKGa2toFtRvLOHaY8vx8DrFMGdiOJvlS48sp3rMHGb1M4xRzGQdYU6REY6rxwHJGdJxwBKsk7WiHSyK9wFQhqh14gDyIVjd0f8Wa2/bUwOyWXwQLGGRWzicuChvKC4F8bpmrTbFU7CGL2zqiJm2Tmn03100DZUox5ddCam1ffmaMPJd3Cnj9SPWz6/gT2EbsUr88Bj4VmAljjWSfoP88mL59tc33PLzsdjaptPMfqP4E1MYPGOmfepMw2Of8NK0d238+JTZ3IfbLSFnPSwVB53udyX4q/38xurTuO+K6/Fqi8MffqhR/A==)

---

**Related**

* [`` API reference](/api/built-in-components#transition)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/built-ins/transition.md)



## Server-Side Rendering (SSR) | Vue.js

[Read the full article](https://vuejs.org/guide/scaling-up/ssr)

# Server\-Side Rendering (SSR) [​](#server-side-rendering-ssr)

## Overview [​](#overview)

### What is SSR? [​](#what-is-ssr)

Vue.js is a framework for building client\-side applications. By default, Vue components produce and manipulate DOM in the browser as output. However, it is also possible to render the same components into HTML strings on the server, send them directly to the browser, and finally "hydrate" the static markup into a fully interactive app on the client.

A server\-rendered Vue.js app can also be considered "isomorphic" or "universal", in the sense that the majority of your app's code runs on both the server **and** the client.

### Why SSR? [​](#why-ssr)

Compared to a client\-side Single\-Page Application (SPA), the advantage of SSR primarily lies in:

* **Faster time\-to\-content**: this is more prominent on slow internet or slow devices. Server\-rendered markup doesn't need to wait until all JavaScript has been downloaded and executed to be displayed, so your user will see a fully\-rendered page sooner. In addition, data fetching is done on the server\-side for the initial visit, which likely has a faster connection to your database than the client. This generally results in improved [Core Web Vitals](https://web.dev/vitals/) metrics, better user experience, and can be critical for applications where time\-to\-content is directly associated with conversion rate.
* **Unified mental model**: you get to use the same language and the same declarative, component\-oriented mental model for developing your entire app, instead of jumping back and forth between a backend templating system and a frontend framework.
* **Better SEO**: the search engine crawlers will directly see the fully rendered page.

TIP

As of now, Google and Bing can index synchronous JavaScript applications just fine. Synchronous being the key word there. If your app starts with a loading spinner, then fetches content via Ajax, the crawler will not wait for you to finish. This means if you have content fetched asynchronously on pages where SEO is important, SSR might be necessary.

There are also some trade\-offs to consider when using SSR:

* Development constraints. Browser\-specific code can only be used inside certain lifecycle hooks; some external libraries may need special treatment to be able to run in a server\-rendered app.
* More involved build setup and deployment requirements. Unlike a fully static SPA that can be deployed on any static file server, a server\-rendered app requires an environment where a Node.js server can run.
* More server\-side load. Rendering a full app in Node.js is going to be more CPU\-intensive than just serving static files, so if you expect high traffic, be prepared for corresponding server load and wisely employ caching strategies.

Before using SSR for your app, the first question you should ask is whether you actually need it. It mostly depends on how important time\-to\-content is for your app. For example, if you are building an internal dashboard where an extra few hundred milliseconds on initial load doesn't matter that much, SSR would be an overkill. However, in cases where time\-to\-content is absolutely critical, SSR can help you achieve the best possible initial load performance.

### SSR vs. SSG [​](#ssr-vs-ssg)

**Static Site Generation (SSG)**, also referred to as pre\-rendering, is another popular technique for building fast websites. If the data needed to server\-render a page is the same for every user, then instead of rendering the page every time a request comes in, we can render it only once, ahead of time, during the build process. Pre\-rendered pages are generated and served as static HTML files.

SSG retains the same performance characteristics of SSR apps: it provides great time\-to\-content performance. At the same time, it is cheaper and easier to deploy than SSR apps because the output is static HTML and assets. The keyword here is **static**: SSG can only be applied to pages providing static data, i.e. data that is known at build time and can not change between requests. Every time the data changes, a new deployment is needed.

If you're only investigating SSR to improve the SEO of a handful of marketing pages (e.g. `/`, `/about`, `/contact`, etc.), then you probably want SSG instead of SSR. SSG is also great for content\-based websites such as documentation sites or blogs. In fact, this website you are reading right now is statically generated using [VitePress](https://vitepress.dev/), a Vue\-powered static site generator.

## Basic Tutorial [​](#basic-tutorial)

### Rendering an App [​](#rendering-an-app)

Let's take a look at the most bare\-bones example of Vue SSR in action.

1. Create a new directory and `cd` into it
2. Run `npm init -y`
3. Add `"type": "module"` in `package.json` so that Node.js runs in [ES modules mode](https://nodejs.org/api/esm.html#modules-ecmascript-modules).
4. Run `npm install vue`
5. Create an `example.js` file:

js\`\`\`
// this runs in Node.js on the server.
import { createSSRApp } from 'vue'
// Vue's server\-rendering API is exposed under \`vue/server\-renderer\`.
import { renderToString } from 'vue/server\-renderer'

const app = createSSRApp({
 data: () =\> ({ count: 1 }),
 template: \`\{{ count }}\\`
})

renderToString(app).then((html) =\> {
 console.log(html)
})
\`\`\`Then run:

sh\`\`\`
\> node example.js
\`\`\`It should print the following to the command line:

\`\`\`
\1\
\`\`\`[`renderToString()`](/api/ssr#rendertostring) takes a Vue app instance and returns a Promise that resolves to the rendered HTML of the app. It is also possible to stream rendering using the [Node.js Stream API](https://nodejs.org/api/stream.html) or [Web Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API). Check out the [SSR API Reference](/api/ssr) for full details.

We can then move the Vue SSR code into a server request handler, which wraps the application markup with the full page HTML. We will be using [`express`](https://expressjs.com/) for the next steps:

* Run `npm install express`
* Create the following `server.js` file:

js\`\`\`
import express from 'express'
import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server\-renderer'

const server = express()

server.get('/', (req, res) =\> {
 const app = createSSRApp({
 data: () =\> ({ count: 1 }),
 template: \`\{{ count }}\\`
 })

 renderToString(app).then((html) =\> {
 res.send(\`
 \
 \
 \
 \Vue SSR Example\
 \
 \
 \${html}\
 \
 \
 \`)
 })
})

server.listen(3000, () =\> {
 console.log('ready')
})
\`\`\`Finally, run `node server.js` and visit `http://localhost:3000`. You should see the page working with the button.

[Try it on StackBlitz](https://stackblitz.com/fork/vue-ssr-example-basic?file=index.js)

### Client Hydration [​](#client-hydration)

If you click the button, you'll notice the number doesn't change. The HTML is completely static on the client since we are not loading Vue in the browser.

To make the client\-side app interactive, Vue needs to perform the **hydration** step. During hydration, it creates the same Vue application that was run on the server, matches each component to the DOM nodes it should control, and attaches DOM event listeners.

To mount an app in hydration mode, we need to use [`createSSRApp()`](/api/application#createssrapp) instead of `createApp()`:

js\`\`\`
// this runs in the browser.
import { createSSRApp } from 'vue'

const app = createSSRApp({
 // ...same app as on server
})

// mounting an SSR app on the client assumes
// the HTML was pre\-rendered and will perform
// hydration instead of mounting new DOM nodes.
app.mount('\#app')
\`\`\`### Code Structure [​](#code-structure)

Notice how we need to reuse the same app implementation as on the server. This is where we need to start thinking about code structure in an SSR app \- how do we share the same application code between the server and the client?

Here we will demonstrate the most bare\-bones setup. First, let's split the app creation logic into a dedicated file, `app.js`:

js\`\`\`
// app.js (shared between server and client)
import { createSSRApp } from 'vue'

export function createApp() {
 return createSSRApp({
 data: () =\> ({ count: 1 }),
 template: \`\{{ count }}\\`
 })
}
\`\`\`This file and its dependencies are shared between the server and the client \- we call them **universal code**. There are a number of things you need to pay attention to when writing universal code, as we will [discuss below](#writing-ssr-friendly-code).

Our client entry imports the universal code, creates the app, and performs the mount:

js\`\`\`
// client.js
import { createApp } from './app.js'

createApp().mount('\#app')
\`\`\`And the server uses the same app creation logic in the request handler:

js\`\`\`
// server.js (irrelevant code omitted)
import { createApp } from './app.js'

server.get('/', (req, res) =\> {
 const app = createApp()
 renderToString(app).then(html =\> {
 // ...
 })
})
\`\`\`In addition, in order to load the client files in the browser, we also need to:

1. Serve client files by adding `server.use(express.static('.'))` in `server.js`.
2. Load the client entry by adding `` to the HTML shell.
3. Support usage like `import * from 'vue'` in the browser by adding an [Import Map](https://github.com/WICG/import-maps) to the HTML shell.

[Try the completed example on StackBlitz](https://stackblitz.com/fork/vue-ssr-example?file=index.js). The button is now interactive!

## Higher Level Solutions [​](#higher-level-solutions)

Moving from the example to a production\-ready SSR app involves a lot more. We will need to:

* Support Vue SFCs and other build step requirements. In fact, we will need to coordinate two builds for the same app: one for the client, and one for the server.

TIP

Vue components are compiled differently when used for SSR \- templates are compiled into string concatenations instead of Virtual DOM render functions for more efficient rendering performance.
* In the server request handler, render the HTML with the correct client\-side asset links and optimal resource hints. We may also need to switch between SSR and SSG mode, or even mix both in the same app.
* Manage routing, data fetching, and state management stores in a universal manner.

A complete implementation would be quite complex and depends on the build toolchain you have chosen to work with. Therefore, we highly recommend going with a higher\-level, opinionated solution that abstracts away the complexity for you. Below we will introduce a few recommended SSR solutions in the Vue ecosystem.

### Nuxt [​](#nuxt)

[Nuxt](https://nuxt.com/) is a higher\-level framework built on top of the Vue ecosystem which provides a streamlined development experience for writing universal Vue applications. Better yet, you can also use it as a static site generator! We highly recommend giving it a try.

### Quasar [​](#quasar)

[Quasar](https://quasar.dev) is a complete Vue\-based solution that allows you to target SPA, SSR, PWA, mobile app, desktop app, and browser extension all using one codebase. It not only handles the build setup, but also provides a full collection of Material Design compliant UI components.

### Vite SSR [​](#vite-ssr)

Vite provides built\-in [support for Vue server\-side rendering](https://vitejs.dev/guide/ssr.html), but it is intentionally low\-level. If you wish to go directly with Vite, check out [vite\-plugin\-ssr](https://vite-plugin-ssr.com/), a community plugin that abstracts away many challenging details for you.

You can also find an example Vue \+ Vite SSR project using manual setup [here](https://github.com/vitejs/vite-plugin-vue/tree/main/playground/ssr-vue), which can serve as a base to build upon. Note this is only recommended if you are experienced with SSR / build tools and really want to have complete control over the higher\-level architecture.

## Writing SSR\-friendly Code [​](#writing-ssr-friendly-code)

Regardless of your build setup or higher\-level framework choice, there are some principles that apply in all Vue SSR applications.

### Reactivity on the Server [​](#reactivity-on-the-server)

During SSR, each request URL maps to a desired state of our application. There is no user interaction and no DOM updates, so reactivity is unnecessary on the server. By default, reactivity is disabled during SSR for better performance.

### Component Lifecycle Hooks [​](#component-lifecycle-hooks)

Since there are no dynamic updates, lifecycle hooks such as `mounted``onMounted` or `updated``onUpdated` will **NOT** be called during SSR and will only be executed on the client. The only hooks that are called during SSR are `beforeCreate` and `created`

You should avoid code that produces side effects that need cleanup in `beforeCreate` and `created``setup()` or the root scope of ``. An example of such side effects is setting up timers with `setInterval`. In client\-side only code we may setup a timer and then tear it down in `beforeUnmount``onBeforeUnmount` or `unmounted``onUnmounted`. However, because the unmount hooks will never be called during SSR, the timers will stay around forever. To avoid this, move your side\-effect code into `mounted``onMounted` instead.

### Access to Platform\-Specific APIs [​](#access-to-platform-specific-apis)

Universal code cannot assume access to platform\-specific APIs, so if your code directly uses browser\-only globals like `window` or `document`, they will throw errors when executed in Node.js, and vice\-versa.

For tasks that are shared between server and client but with different platform APIs, it's recommended to wrap the platform\-specific implementations inside a universal API, or use libraries that do this for you. For example, you can use [`node-fetch`](https://github.com/node-fetch/node-fetch) to use the same fetch API on both server and client.

For browser\-only APIs, the common approach is to lazily access them inside client\-only lifecycle hooks such as `mounted``onMounted`.

Note that if a third\-party library is not written with universal usage in mind, it could be tricky to integrate it into a server\-rendered app. You *might* be able to get it working by mocking some of the globals, but it would be hacky and may interfere with the environment detection code of other libraries.

### Cross\-Request State Pollution [​](#cross-request-state-pollution)

In the State Management chapter, we introduced a [simple state management pattern using Reactivity APIs](/guide/scaling-up/state-management#simple-state-management-with-reactivity-api). In an SSR context, this pattern requires some additional adjustments.

The pattern declares shared state in a JavaScript module's root scope. This makes them **singletons** \- i.e. there is only one instance of the reactive object throughout the entire lifecycle of our application. This works as expected in a pure client\-side Vue application, since the modules in our application are initialized fresh for each browser page visit.

However, in an SSR context, the application modules are typically initialized only once on the server, when the server boots up. The same module instances will be reused across multiple server requests, and so will our singleton state objects. If we mutate the shared singleton state with data specific to one user, it can be accidentally leaked to a request from another user. We call this **cross\-request state pollution.**

We can technically re\-initialize all the JavaScript modules on each request, just like we do in browsers. However, initializing JavaScript modules can be costly, so this would significantly affect server performance.

The recommended solution is to create a new instance of the entire application \- including the router and global stores \- on each request. Then, instead of directly importing it in our components, we provide the shared state using [app\-level provide](/guide/components/provide-inject#app-level-provide) and inject it in components that need it:

js\`\`\`
// app.js (shared between server and client)
import { createSSRApp } from 'vue'
import { createStore } from './store.js'

// called on each request
export function createApp() {
 const app = createSSRApp(/\* ... \*/)
 // create new instance of store per request
 const store = createStore(/\* ... \*/)
 // provide store at the app level
 app.provide('store', store)
 // also expose store for hydration purposes
 return { app, store }
}
\`\`\`State Management libraries like Pinia are designed with this in mind. Consult [Pinia's SSR guide](https://pinia.vuejs.org/ssr/) for more details.

### Hydration Mismatch [​](#hydration-mismatch)

If the DOM structure of the pre\-rendered HTML does not match the expected output of the client\-side app, there will be a hydration mismatch error. Hydration mismatch is most commonly introduced by the following causes:

1. The template contains invalid HTML nesting structure, and the rendered HTML got "corrected" by the browser's native HTML parsing behavior. For example, a common gotcha is that [`` cannot be placed inside ``](https://stackoverflow.com/questions/8397852/why-cant-the-p-tag-contain-a-div-tag-inside-it):

html\`\`\`
\\hi\\
\`\`\`If we produce this in our server\-rendered HTML, the browser will terminate the first `` when `` is encountered and parse it into the following DOM structure:

html\`\`\`
\\
\hi\
\\
\`\`\`
2. The data used during render contains randomly generated values. Since the same application will run twice \- once on the server, and once on the client \- the random values are not guaranteed to be the same between the two runs. There are two ways to avoid random\-value\-induced mismatches:

	1. Use `v-if` \+ `onMounted` to render the part that depends on random values only on the client. Your framework may also have built\-in features to make this easier, for example the `` component in VitePress.
	2. Use a random number generator library that supports generating with seeds, and guarantee the server run and the client run are using the same seed (e.g. by including the seed in serialized state and retrieving it on the client).
3. The server and the client are in different time zones. Sometimes, we may want to convert a timestamp into the user's local time. However, the timezone during the server run and the timezone during the client run are not always the same, and we may not reliably know the user's timezone during the server run. In such cases, the local time conversion should also be performed as a client\-only operation.

When Vue encounters a hydration mismatch, it will attempt to automatically recover and adjust the pre\-rendered DOM to match the client\-side state. This will lead to some rendering performance loss due to incorrect nodes being discarded and new nodes being mounted, but in most cases, the app should continue to work as expected. That said, it is still best to eliminate hydration mismatches during development.

#### Suppressing Hydration Mismatches  [​](#suppressing-hydration-mismatches)

In Vue 3\.5\+, it is possible to selectively suppress inevitable hydration mismatches by using the [`data-allow-mismatch`](/api/ssr#data-allow-mismatch) attribute.

### Custom Directives [​](#custom-directives)

Since most custom directives involve direct DOM manipulation, they are ignored during SSR. However, if you want to specify how a custom directive should be rendered (i.e. what attributes it should add to the rendered element), you can use the `getSSRProps` directive hook:

js\`\`\`
const myDirective = {
 mounted(el, binding) {
 // client\-side implementation:
 // directly update the DOM
 el.id = binding.value
 },
 getSSRProps(binding) {
 // server\-side implementation:
 // return the props to be rendered.
 // getSSRProps only receives the directive binding.
 return {
 id: binding.value
 }
 }
}
\`\`\`### Teleports [​](#teleports)

Teleports require special handling during SSR. If the rendered app contains Teleports, the teleported content will not be part of the rendered string. An easier solution is to conditionally render the Teleport on mount.

If you do need to hydrate teleported content, they are exposed under the `teleports` property of the ssr context object:

js\`\`\`
const ctx = {}
const html = await renderToString(app, ctx)

console.log(ctx.teleports) // { '\#teleported': 'teleported content' }
\`\`\`You need to inject the teleport markup into the correct location in your final page HTML similar to how you need to inject the main app markup.

TIP

Avoid targeting `body` when using Teleports and SSR together \- usually, `` will contain other server\-rendered content which makes it impossible for Teleports to determine the correct starting location for hydration.

Instead, prefer a dedicated container, e.g. `` which contains only teleported content.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/scaling-up/ssr.md)



## Introduction | Vue.js

[Read the full article](https://vuejs.org/guide/introduction)

# Introduction [​](#introduction)

You are reading the documentation for Vue 3!

* Vue 2 support has ended on **Dec 31, 2023**. Learn more about [Vue 2 EOL](https://v2.vuejs.org/eol/).
* Upgrading from Vue 2? Check out the [Migration Guide](https://v3-migration.vuejs.org/).
[Learn Vue with video tutorials on VueMastery.com

](https://www.vuemastery.com/courses/)## What is Vue? [​](#what-is-vue)

Vue (pronounced /vjuː/, like **view**) is a JavaScript framework for building user interfaces. It builds on top of standard HTML, CSS, and JavaScript and provides a declarative, component\-based programming model that helps you efficiently develop user interfaces of any complexity.

Here is a minimal example:

js\`\`\`
import { createApp } from 'vue'

createApp({
 data() {
 return {
 count: 0
 }
 }
}).mount('\#app')
\`\`\`js\`\`\`
import { createApp, ref } from 'vue'

createApp({
 setup() {
 return {
 count: ref(0\)
 }
 }
}).mount('\#app')
\`\`\`template\`\`\`
\
 \
 Count is: {{ count }}
 \
\
\`\`\`**Result**

 Count is: 0The above example demonstrates the two core features of Vue:

* **Declarative Rendering**: Vue extends standard HTML with a template syntax that allows us to declaratively describe HTML output based on JavaScript state.
* **Reactivity**: Vue automatically tracks JavaScript state changes and efficiently updates the DOM when changes happen.

You may already have questions \- don't worry. We will cover every little detail in the rest of the documentation. For now, please read along so you can have a high\-level understanding of what Vue offers.

Prerequisites

The rest of the documentation assumes basic familiarity with HTML, CSS, and JavaScript. If you are totally new to frontend development, it might not be the best idea to jump right into a framework as your first step \- grasp the basics and then come back! You can check your knowledge level with these overviews for [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript), [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) and [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps) if needed. Prior experience with other frameworks helps, but is not required.

## The Progressive Framework [​](#the-progressive-framework)

Vue is a framework and ecosystem that covers most of the common features needed in frontend development. But the web is extremely diverse \- the things we build on the web may vary drastically in form and scale. With that in mind, Vue is designed to be flexible and incrementally adoptable. Depending on your use case, Vue can be used in different ways:

* Enhancing static HTML without a build step
* Embedding as Web Components on any page
* Single\-Page Application (SPA)
* Fullstack / Server\-Side Rendering (SSR)
* Jamstack / Static Site Generation (SSG)
* Targeting desktop, mobile, WebGL, and even the terminal

If you find these concepts intimidating, don't worry! The tutorial and guide only require basic HTML and JavaScript knowledge, and you should be able to follow along without being an expert in any of these.

If you are an experienced developer interested in how to best integrate Vue into your stack, or you are curious about what these terms mean, we discuss them in more detail in [Ways of Using Vue](/guide/extras/ways-of-using-vue).

Despite the flexibility, the core knowledge about how Vue works is shared across all these use cases. Even if you are just a beginner now, the knowledge gained along the way will stay useful as you grow to tackle more ambitious goals in the future. If you are a veteran, you can pick the optimal way to leverage Vue based on the problems you are trying to solve, while retaining the same productivity. This is why we call Vue "The Progressive Framework": it's a framework that can grow with you and adapt to your needs.

## Single\-File Components [​](#single-file-components)

In most build\-tool\-enabled Vue projects, we author Vue components using an HTML\-like file format called **Single\-File Component** (also known as `*.vue` files, abbreviated as **SFC**). A Vue SFC, as the name suggests, encapsulates the component's logic (JavaScript), template (HTML), and styles (CSS) in a single file. Here's the previous example, written in SFC format:

vue\`\`\`
\
export default {
 data() {
 return {
 count: 0
 }
 }
}
\

\
 \Count is: {{ count }}\
\

\
button {
 font\-weight: bold;
}
\
\`\`\`vue\`\`\`
\
import { ref } from 'vue'
const count = ref(0\)
\

\
 \Count is: {{ count }}\
\

\
button {
 font\-weight: bold;
}
\
\`\`\`SFC is a defining feature of Vue and is the recommended way to author Vue components **if** your use case warrants a build setup. You can learn more about the [how and why of SFC](/guide/scaling-up/sfc) in its dedicated section \- but for now, just know that Vue will handle all the build tools setup for you.

## API Styles [​](#api-styles)

Vue components can be authored in two different API styles: **Options API** and **Composition API**.

### Options API [​](#options-api)

With Options API, we define a component's logic using an object of options such as `data`, `methods`, and `mounted`. Properties defined by options are exposed on `this` inside functions, which points to the component instance:

vue\`\`\`
\
export default {
 // Properties returned from data() become reactive state
 // and will be exposed on \`this\`.
 data() {
 return {
 count: 0
 }
 },

 // Methods are functions that mutate state and trigger updates.
 // They can be bound as event handlers in templates.
 methods: {
 increment() {
 this.count\+\+
 }
 },

 // Lifecycle hooks are called at different stages
 // of a component's lifecycle.
 // This function will be called when the component is mounted.
 mounted() {
 console.log(\`The initial count is ${this.count}.\`)
 }
}
\

\
 \Count is: {{ count }}\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNptkMFqxCAQhl9lkB522ZL0HNKlpa/Qo4e1ZpLIGhUdl5bgu9es2eSyIMio833zO7NP56pbRNawNkivHJ25wV9nPUGHvYiaYOYGoK7Bo5CkbgiBBOFy2AkSh2N5APmeojePCkDaaKiBt1KnZUuv3Ky0PppMsyYAjYJgigu0oEGYDsirYUAP0WULhqVrQhptF5qHQhnpcUJD+wyQaSpUd/Xp9NysVY/yT2qE0dprIS/vsds5Mg9mNVbaDofL94jZpUgJXUKBCvAy76ZUXY53CTd5tfX2k7kgnJzOCXIF0P5EImvgQ2olr++cbRE4O3+t6JxvXj0ptXVpye1tvbFY+ge/NJZt)

### Composition API [​](#composition-api)

With Composition API, we define a component's logic using imported API functions. In SFCs, Composition API is typically used with [``](/api/sfc-script-setup). The `setup` attribute is a hint that makes Vue perform compile\-time transforms that allow us to use Composition API with less boilerplate. For example, imports and top\-level variables / functions declared in `` are directly usable in the template.

Here is the same component, with the exact same template, but using Composition API and `` instead:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

// reactive state
const count = ref(0\)

// functions that mutate state and trigger updates
function increment() {
 count.value\+\+
}

// lifecycle hooks
onMounted(() =\> {
 console.log(\`The initial count is ${count.value}.\`)
})
\

\
 \Count is: {{ count }}\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpNkMFqwzAQRH9lMYU4pNg9Bye09NxbjzrEVda2iLwS0spQjP69a+yYHnRYad7MaOfiw/tqSliciybqYDxDRE7+qsiM3gWGGQJ2r+DoyyVivEOGLrgRDkIdFCmqa1G0ms2EELllVKQdRQa9AHBZ+PLtuEm7RCKVd+ChZRjTQqwctHQHDqbvMUDyd7mKip4AGNIBRyQujzArgtW/mlqb8HRSlLcEazrUv9oiDM49xGGvXgp5uT5his5iZV1f3r4HFHvDprVbaxPhZf4XkKub/CDLaep1T7IhGRhHb6WoTADNT2KWpu/aGv24qGKvrIrr5+Z7hnneQnJu6hURvKl3ryL/ARrVkuI=)

### Which to Choose? [​](#which-to-choose)

Both API styles are fully capable of covering common use cases. They are different interfaces powered by the exact same underlying system. In fact, the Options API is implemented on top of the Composition API! The fundamental concepts and knowledge about Vue are shared across the two styles.

The Options API is centered around the concept of a "component instance" (`this` as seen in the example), which typically aligns better with a class\-based mental model for users coming from OOP language backgrounds. It is also more beginner\-friendly by abstracting away the reactivity details and enforcing code organization via option groups.

The Composition API is centered around declaring reactive state variables directly in a function scope and composing state from multiple functions together to handle complexity. It is more free\-form and requires an understanding of how reactivity works in Vue to be used effectively. In return, its flexibility enables more powerful patterns for organizing and reusing logic.

You can learn more about the comparison between the two styles and the potential benefits of Composition API in the [Composition API FAQ](/guide/extras/composition-api-faq).

If you are new to Vue, here's our general recommendation:

* For learning purposes, go with the style that looks easier to understand to you. Again, most of the core concepts are shared between the two styles. You can always pick up the other style later.
* For production use:

	+ Go with Options API if you are not using build tools, or plan to use Vue primarily in low\-complexity scenarios, e.g. progressive enhancement.
	+ Go with Composition API \+ Single\-File Components if you plan to build full applications with Vue.

You don't have to commit to only one style during the learning phase. The rest of the documentation will provide code samples in both styles where applicable, and you can toggle between them at any time using the **API Preference switches** at the top of the left sidebar.

## Still Got Questions? [​](#still-got-questions)

Check out our [FAQ](/about/faq).

## Pick Your Learning Path [​](#pick-your-learning-path)

Different developers have different learning styles. Feel free to pick a learning path that suits your preference \- although we do recommend going over all of the content, if possible!

[Try the Tutorial

For those who prefer learning things hands\-on.](/tutorial/)[Read the Guide

The guide walks you through every aspect of the framework in full detail.](/guide/quick-start)[Check out the Examples

Explore examples of core features and common UI tasks.](/examples/)[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/introduction.md)



## Form Input Bindings | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/forms)

# Form Input Bindings [​](#form-input-bindings)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/user-inputs-vue-devtools-in-vue-3?friend=vuejs "Free Lesson on User Inputs with Vue.js")[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-fundamentals-capi-user-inputs-in-vue?friend=vuejs "Free Lesson on User Inputs with Vue.js")When dealing with forms on the frontend, we often need to sync the state of form input elements with corresponding state in JavaScript. It can be cumbersome to manually wire up value bindings and change event listeners:

template\`\`\`
\ text = event.target.value"\>
\`\`\`The `v-model` directive helps us simplify the above to:

template\`\`\`
\
\`\`\`In addition, `v-model` can be used on inputs of different types, ``, and `` elements. It automatically expands to different DOM property and event pairs based on the element it is used on:

* `` with text types and `` elements use `value` property and `input` event;
* `` and `` use `checked` property and `change` event;
* `` uses `value` as a prop and `change` as an event.

Note

`v-model` will ignore the initial `value`, `checked` or `selected` attributes found on any form elements. It will always treat the current bound JavaScript state as the source of truth. You should declare the initial value on the JavaScript side, using the [`data`](/api/options-state#data) option[reactivity APIs](/api/reactivity-core#reactivity-api-core).

## Basic Usage [​](#basic-usage)

### Text [​](#text)

template\`\`\`
\Message is: {{ message }}\
\
\`\`\`Message is: 

[Try it in the Playground](https://play.vuejs.org/#eNo9jUEOgyAQRa8yYUO7aNkbNOkBegM2RseWRGACoxvC3TumxuX/+f+9ql5Ez31D1SlbpuyJoSBvNLjoA6XMUCHjAg2WnAJomWoXXZxSLAwBSxk/CP2xuWl9d9GaP0YAEhgDrSOjJABLw/s8+NJBrde/NWsOpWPrI20M+yOkGdfeqXPiFAhowm9aZ8zS4+wPv/RGjtZcJtV+YpNK1g==)

[Try it in the Playground](https://play.vuejs.org/#eNo9jdEKwjAMRX8l9EV90L2POvAD/IO+lDVqoetCmw6h9N/NmBuEJPeSc1PVg+i2FFS90nlMnngwEb80JwaHL1sCQzURwFm258u2AyTkkuKuACbM2b6xh9Nps9o6pEnp7ggWwThRsIyiADQNz40En3uodQ+C1nRHK8HaRyoMy3WaHYa7Uf8To0CCRvzMwWESH51n4cXvBNTd8Um1H0FuTq0=)

Note

For languages that require an [IME](https://en.wikipedia.org/wiki/Input_method) (Chinese, Japanese, Korean etc.), you'll notice that `v-model` doesn't get updated during IME composition. If you want to respond to these updates as well, use your own `input` event listener and `value` binding instead of using `v-model`.

### Multiline Text [​](#multiline-text)

template\`\`\`
\Multiline message is:\
\{{ message }}\
\\
\`\`\`Multiline message is:[Try it in the Playground](https://play.vuejs.org/#eNo9jktuwzAMRK9CaON24XrvKgZ6gN5AG8FmGgH6ECKdJjB891D5LYec9zCb+SH6Oq9oRmN5roEEGGWlyeWQqFSBDSoeYYdjLQk6rXYuuzyXzAIJmf0fwqF1Prru02U7PDQq0CCYKHrBlsQy+Tz9rlFCDBnfdOBRqfa7twhYrhEPzvyfgmCvnxlHoIp9w76dmbbtDe+7HdpaBQUv4it6OPepLBjV8Gw5AzpjxlOJC1a9+2WB1IZQRGhWVqsdXgb1tfDcbvYbJDRqLQ==)

[Try it in the Playground](https://play.vuejs.org/#eNo9jk2OwyAMha9isenMIpN9hok0B+gN2FjBbZEIscDpj6LcvaZpKiHg2X6f32L+mX+uM5nO2DLkwNK7RHeesoCnE85RYHEJwKPg1/f2B8gkc067AhipFDxTB4fDVlrro5ce237AKoRGjihUldjCmPqjLgkxJNoxEEqnrtp7TTEUeUT6c+Z2CUKNdgbdxZmaavt1pl+Wj3ldbcubUegumAnh2oyTp6iE95QzoDEGukzRU9Y6eg9jDcKRoFKLUm27E5RXxTu7WZ89/G4E)

Note that interpolation inside `` won't work. Use `v-model` instead.

template\`\`\`
\
\{{ text }}\

\
\\
\`\`\`### Checkbox [​](#checkbox)

Single checkbox, boolean value:

template\`\`\`
\
\{{ checked }}\
\`\`\`false[Try it in the Playground](https://play.vuejs.org/#eNpVjssKgzAURH/lko3tonVfotD/yEaTKw3Ni3gjLSH/3qhUcDnDnMNk9gzhviRkD8ZnGXUgmJFS6IXTNvhIkCHiBAWm6C00ddoIJ5z0biaQL5RvVNCtmwvFhFfheLuLqqIGQhvMQLgm4tqFREDfgJ1gGz36j2Cg1TkvN+sVmn+JqnbtrjDDiAYmH09En/PxphTebqsK8PY4wMoPslBUxQ==)

[Try it in the Playground](https://play.vuejs.org/#eNpVjtEKgzAMRX8l9Gl72Po+OmH/0ZdqI5PVNnSpOEr/fVVREEKSc0kuN4sX0X1KKB5Cfbs4EDfa40whMljsTXIMWXsAa9hcrtsOEJFT9DsBdG/sPmgfwDHhJpZl1FZLycO6AuNIzjAuxGrwlBj4R/jUYrVpw6wFDPbM020MFt0uoq2a3CycadFBH+Lpo8l5jwWlKLle1QcljwCi/AH7gFic)

We can also bind multiple checkboxes to the same array or [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) value:

js\`\`\`
const checkedNames = ref(\[])
\`\`\`js\`\`\`
export default {
 data() {
 return {
 checkedNames: \[]
 }
 }
}
\`\`\`template\`\`\`
\Checked names: {{ checkedNames }}\

\
\Jack\

\
\John\

\
\Mike\
\`\`\`Checked names: \[]JackJohnMikeIn this case, the `checkedNames` array will always contain the values from the currently checked boxes.

[Try it in the Playground](https://play.vuejs.org/#eNqVkUtqwzAURbfy0CTtoNU8KILSWaHdQNWBIj8T1fohyybBeO+RbOc3i2e+vHvuMWggHyG89x2SLWGtijokaDF1gQunbfAxwQARaxihjt7CJlc3wgmnvGsTqAOqBqsfabGFXSm+/P69CsfovJVXckhog5EJcwJgle7558yBK+AWhuFxaRwZLbVCZ0K70CVIp4A7Qabi3h8FAV3l/C9Vk797abpy/lrim/UVmkt/Gc4HOv+EkXs0UPt4XeCFZHQ6lM4TZn9w9+YlrjFPCC/kKrPVDd6Zv5e4wjwv8ELezIxeX4qMZwHduAs=)

[Try it in the Playground](https://play.vuejs.org/#eNqVUc1qxCAQfpXBU3tovS9WKL0V2hdoenDjLGtjVNwxbAl592rMpru3DYjO5/cnOLLXEJ6HhGzHxKmNJpBsHJ6DjwQaDypZgrFxAFqRenisM0BEStFdEEB7xLZD/al6PO3g67veT+XIW16Cr+kZEPbBKsKMAIQ2g3yrAeBqwjjeRMI0CV5kxZ0dxoVEQL8BXxo2C/f+3DAwOuMf1XZ5HpRNhX5f4FPvNdqLfgnOBK+PsGqPFg4+rgmyOAWfiaK5o9kf3XXzArc0zxZZnJuae9PhVfPHAjc01wRZnP/Ngq8/xaY/yMW74g==)

### Radio [​](#radio)

template\`\`\`
\Picked: {{ picked }}\

\
\One\

\
\Two\
\`\`\`Picked: OneTwo[Try it in the Playground](https://play.vuejs.org/#eNqFkDFuwzAMRa9CaHE7tNoDxUBP0A4dtTgWDQiRJUKmHQSG7x7KhpMMAbLxk3z/g5zVD9H3NKI6KDO02RPDgDxSbaPvKWWGGTJ2sECXUw+VrFY22timODCQb8/o4FhWPqrfiNWnjUZvRmIhgrGn0DCKAjDOT/XfCh1gnnd+WYwukwJYNj7SyMBXwqNVuXE+WQXeiUgRpZyaMJaR5BX11SeHQfTmJi1dnNiE5oQBupR3shbC6LX9Posvpdyz/jf1OksOe85ayVqIR5bR9z+o5Qbc6oCk)

[Try it in the Playground](https://play.vuejs.org/#eNqNkEEOAiEMRa/SsFEXyt7gJJ5AFy5ng1ITIgLBMmomc3eLOONSEwJ9Lf//pL3YxrjqMoq1ULdTspGa1uMjhkRg8KyzI+hbD2A06fmi1gAJKSc/EkC0pwuaNcx2Hme1OZSHLz5KTtYMhNfoNGEhUsZ2zf6j7vuPEQyDkmVSBPzJ+pgJ6Blx04qkjQ2tAGsYgkcuO+1yGXF6oeU1GHTM1Y1bsoY5fUQH55BGZcMKJd/t31l0L+WYdaj0V9Zb2bDim6XktAcxvADR+YWb)

### Select [​](#select)

Single select:

template\`\`\`
\Selected: {{ selected }}\

\
 \Please select one\
 \A\
 \B\
 \C\
\
\`\`\`Selected: Please select oneABC[Try it in the Playground](https://play.vuejs.org/#eNp1j7EOgyAQhl/lwmI7tO4Nmti+QJOuLFTPxASBALoQ3r2H2jYOjvff939wkTXWXucJ2Y1x37rBBvAYJlsLPYzWuAARHPaQoHdmhILQQmihW6N9RhW2ATuoMnQqirPQvFw9ZKAh4GiVDEgTAPdW6hpeW+sGMf4VKVEz73Mvs8sC5stoOlSVYF9SsEVGiLFhMBq6wcu3IsUs1YREEvFUKD1udjAaebnS+27dHOT3g/yxy+nHywM08PJ3KksfXwJ2dA==)

[Try it in the Playground](https://play.vuejs.org/#eNp1j1ELgyAUhf/KxZe2h633cEHbHxjstReXdxCYSt5iEP333XIJPQSinuN3jjqJyvvrOKAohAxN33oqa4tf73oCjR81GIKptgBakTqd4x6gRxp6uymAgAYbQl1AlkVvXhaeeMg8NbMg7LxRhKwAZPDKlvBK8WlKXTDPnFzOI7naMF46p9HcarFxtVgBRpyn1lnQbVBvwwWjMgMyycTToAr47wZnUeaR3mfL6sC/H/iPnc/vXS9gIfP0UTH/ACgWeYE=)

Note

If the initial value of your `v-model` expression does not match any of the options, the `` element will render in an "unselected" state. On iOS this will cause the user not being able to select the first item because iOS does not fire a change event in this case. It is therefore recommended to provide a disabled option with an empty value, as demonstrated in the example above.

Multiple select (bound to array):

template\`\`\`
\Selected: {{ selected }}\

\
 \A\
 \B\
 \C\
\
\`\`\`Selected: \[]ABC[Try it in the Playground](https://play.vuejs.org/#eNp1kL2OwjAQhF9l5Ya74i7QBhMJeARKTIESIyz5Z5VsAsjyu7NOQEBB5xl/M7vaKNaI/0OvRSlkV7cGCTpNPVbKG4ehJYjQ6hMkOLXBwYzRmfLK18F3GbW6Jt3AKkM/+8Ov8rKYeriBBWmH9kiaFYBszFDtHpkSYnwVpCSL/JtDDE4+DH8uNNqulHiCSoDrLRm0UyWzAckEX61l8Xh9+psv/vbD563HCSxk8bY0y45u47AJ2D/HHyDm4MU0dC5hMZ/jdal8Gg8wJkS6A3nRew4=)

[Try it in the Playground](https://play.vuejs.org/#eNp1UEEOgjAQ/MqmJz0oeMVKgj7BI3AgdI1NCjSwIIbwdxcqRA4mTbsznd2Z7CAia49diyIQsslrbSlMSuxtVRMofGStIRiSEkBllO32rgaokdq6XBBAgwZzQhVAnDpunB6++EhvncyAsLAmI2QEIJXuwvvaPAzrJBhH6U2/UxMLHQ/doagUmksiFmEioOCU2ho3krWVJV2VYSS9b7Xlr3/424bn1LMDA+n9hGbY0Hs2c4J4sU/dPl5a0TOAk+/b/rwsYO4Q4wdtRX7l)

Select options can be dynamically rendered with `v-for`:

js\`\`\`
const selected = ref('A')

const options = ref(\[
 { text: 'One', value: 'A' },
 { text: 'Two', value: 'B' },
 { text: 'Three', value: 'C' }
])
\`\`\`js\`\`\`
export default {
 data() {
 return {
 selected: 'A',
 options: \[
 { text: 'One', value: 'A' },
 { text: 'Two', value: 'B' },
 { text: 'Three', value: 'C' }
 ]
 }
 }
}
\`\`\`template\`\`\`
\
 \
 {{ option.text }}
 \
\

\Selected: {{ selected }}\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNplkMFugzAQRH9l5YtbKYU7IpFoP6CH9lb3EMGiWgLbMguthPzvXduEJMqNYUazb7yKxrlimVFUop5arx3BhDS7kzJ6dNYTrOCxhwC9tyNIjkpllGmtmWJ0wJawg2MMPclGPl9N60jzx+Z9KQPcRfhHFch3g/IAy3mYkVUjIRzu/M9fe+O/Pvo/Hm8b3jihzDdfr8s8gwewIBzdcCZkBVBnXFheRtvhcFTiwq9ECnAkQ3Okt54Dm9TmskYJqNLR3SyS3BsYct3CRYSFwGCpusx/M0qZTydKRXWnl9PHBlPFhv1lQ6jL6MZl+xoR/gFjPZTD)

[Try it in the Playground](https://play.vuejs.org/#eNp1kMFqxCAQhl9l8JIWtsk92IVtH6CH9lZ7COssDbgqZpJdCHn3nWiUXBZE/Mdvxv93Fifv62lE0Qo5nEPv6ags3r0LBBov3WgIZmUBdEfdy2s6AwSkMdisAAY0eCbULVSn6pCrzlPv7NDCb64AzEB4J+a+LFYHmDozYuyCpfTtqJ+b21Efz6j/gPtpn8xl7C8douaNl2xKUhaEV286QlYAMgWB6e3qNJp3JXIyJSLASErFyMUFBjbZ2xxXCWijkXJZR1kmsPF5g+s1ACybWdmkarLSpKejS0VS99Pxu3wzT8jOuF026+2arKQRywOBGJfE)

## Value Bindings [​](#value-bindings)

For radio, checkbox and select options, the `v-model` binding values are usually static strings (or booleans for checkbox):

template\`\`\`
\
\

\
\

\
\
 \ABC\
\
\`\`\`But sometimes we may want to bind the value to a dynamic property on the current active instance. We can use `v-bind` to achieve that. In addition, using `v-bind` allows us to bind the input value to non\-string values.

### Checkbox [​](#checkbox-1)

template\`\`\`
\
\`\`\``true-value` and `false-value` are Vue\-specific attributes that only work with `v-model`. Here the `toggle` property's value will be set to `'yes'` when the box is checked, and set to `'no'` when unchecked. You can also bind them to dynamic values using `v-bind`:

template\`\`\`
\
\`\`\`Tip

The `true-value` and `false-value` attributes don't affect the input's `value` attribute, because browsers don't include unchecked boxes in form submissions. To guarantee that one of two values is submitted in a form (e.g. "yes" or "no"), use radio inputs instead.

### Radio [​](#radio-1)

template\`\`\`
\
\
\`\`\``pick` will be set to the value of `first` when the first radio input is checked, and set to the value of `second` when the second one is checked.

### Select Options [​](#select-options)

template\`\`\`
\
 \
 \123\
\
\`\`\``v-model` supports value bindings of non\-string values as well! In the above example, when the option is selected, `selected` will be set to the object literal value of `{ number: 123 }`.

## Modifiers [​](#modifiers)

### `.lazy` [​](#lazy)

By default, `v-model` syncs the input with the data after each `input` event (with the exception of IME composition as [stated above](#vmodel-ime-tip)). You can add the `lazy` modifier to instead sync after `change` events:

template\`\`\`
\
\
\`\`\`### `.number` [​](#number)

If you want user input to be automatically typecast as a number, you can add the `number` modifier to your `v-model` managed inputs:

template\`\`\`
\
\`\`\`If the value cannot be parsed with `parseFloat()`, then the original (string) value is used instead. In particular, if the input is empty (for instance after the user clearing the input field), an empty string is returned. This behavior differs from the [DOM property `valueAsNumber`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement#valueasnumber).

The `number` modifier is applied automatically if the input has `type="number"`.

### `.trim` [​](#trim)

If you want whitespace from user input to be trimmed automatically, you can add the `trim` modifier to your `v-model`\-managed inputs:

template\`\`\`
\
\`\`\`## `v-model` with Components [​](#v-model-with-components)

> If you're not yet familiar with Vue's components, you can skip this for now.

HTML's built\-in input types won't always meet your needs. Fortunately, Vue components allow you to build reusable inputs with completely customized behavior. These inputs even work with `v-model`! To learn more, read about [Usage with `v-model`](/guide/components/v-model) in the Components guide.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/forms.md)



## Render Functions & JSX | Vue.js

[Read the full article](https://vuejs.org/guide/extras/render-function)

# Render Functions \& JSX [​](#render-functions-jsx)

Vue recommends using templates to build applications in the vast majority of cases. However, there are situations where we need the full programmatic power of JavaScript. That's where we can use the **render function**.

> If you are new to the concept of virtual DOM and render functions, make sure to read the [Rendering Mechanism](/guide/extras/rendering-mechanism) chapter first.

## Basic Usage [​](#basic-usage)

### Creating Vnodes [​](#creating-vnodes)

Vue provides an `h()` function for creating vnodes:

js\`\`\`
import { h } from 'vue'

const vnode = h(
 'div', // type
 { id: 'foo', class: 'bar' }, // props
 \[
 /\* children \*/
 ]
)
\`\`\``h()` is short for **hyperscript** \- which means "JavaScript that produces HTML (hypertext markup language)". This name is inherited from conventions shared by many virtual DOM implementations. A more descriptive name could be `createVNode()`, but a shorter name helps when you have to call this function many times in a render function.

The `h()` function is designed to be very flexible:

js\`\`\`
// all arguments except the type are optional
h('div')
h('div', { id: 'foo' })

// both attributes and properties can be used in props
// Vue automatically picks the right way to assign it
h('div', { class: 'bar', innerHTML: 'hello' })

// props modifiers such as \`.prop\` and \`.attr\` can be added
// with \`.\` and \`^\` prefixes respectively
h('div', { '.name': 'some\-name', '^width': '100' })

// class and style have the same object / array
// value support that they have in templates
h('div', { class: \[foo, { bar }], style: { color: 'red' } })

// event listeners should be passed as onXxx
h('div', { onClick: () =\> {} })

// children can be a string
h('div', { id: 'foo' }, 'hello')

// props can be omitted when there are no props
h('div', 'hello')
h('div', \[h('span', 'hello')])

// children array can contain mixed vnodes and strings
h('div', \['hello', h('span', 'hello')])
\`\`\`The resulting vnode has the following shape:

js\`\`\`
const vnode = h('div', { id: 'foo' }, \[])

vnode.type // 'div'
vnode.props // { id: 'foo' }
vnode.children // \[]
vnode.key // null
\`\`\`Note

The full `VNode` interface contains many other internal properties, but it is strongly recommended to avoid relying on any properties other than the ones listed here. This avoids unintended breakage in case the internal properties are changed.

### Declaring Render Functions [​](#declaring-render-functions)

When using templates with Composition API, the return value of the `setup()` hook is used to expose data to the template. When using render functions, however, we can directly return the render function instead:

js\`\`\`
import { ref, h } from 'vue'

export default {
 props: {
 /\* ... \*/
 },
 setup(props) {
 const count = ref(1\)

 // return the render function
 return () =\> h('div', props.msg \+ count.value)
 }
}
\`\`\`The render function is declared inside `setup()` so it naturally has access to the props and any reactive state declared in the same scope.

In addition to returning a single vnode, you can also return strings or arrays:

js\`\`\`
export default {
 setup() {
 return () =\> 'hello world!'
 }
}
\`\`\`js\`\`\`
import { h } from 'vue'

export default {
 setup() {
 // use an array to return multiple root nodes
 return () =\> \[
 h('div'),
 h('div'),
 h('div')
 ]
 }
}
\`\`\`TIP

Make sure to return a function instead of directly returning values! The `setup()` function is called only once per component, while the returned render function will be called multiple times.

We can declare render functions using the `render` option:

js\`\`\`
import { h } from 'vue'

export default {
 data() {
 return {
 msg: 'hello'
 }
 },
 render() {
 return h('div', this.msg)
 }
}
\`\`\`The `render()` function has access to the component instance via `this`.

In addition to returning a single vnode, you can also return strings or arrays:

js\`\`\`
export default {
 render() {
 return 'hello world!'
 }
}
\`\`\`js\`\`\`
import { h } from 'vue'

export default {
 render() {
 // use an array to return multiple root nodes
 return \[
 h('div'),
 h('div'),
 h('div')
 ]
 }
}
\`\`\`If a render function component doesn't need any instance state, they can also be declared directly as a function for brevity:

js\`\`\`
function Hello() {
 return 'hello world!'
}
\`\`\`That's right, this is a valid Vue component! See [Functional Components](#functional-components) for more details on this syntax.

### Vnodes Must Be Unique [​](#vnodes-must-be-unique)

All vnodes in the component tree must be unique. That means the following render function is invalid:

js\`\`\`
function render() {
 const p = h('p', 'hi')
 return h('div', \[
 // Yikes \- duplicate vnodes!
 p,
 p
 ])
}
\`\`\`If you really want to duplicate the same element/component many times, you can do so with a factory function. For example, the following render function is a perfectly valid way of rendering 20 identical paragraphs:

js\`\`\`
function render() {
 return h(
 'div',
 Array.from({ length: 20 }).map(() =\> {
 return h('p', 'hi')
 })
 )
}
\`\`\`## JSX / TSX [​](#jsx-tsx)

[JSX](https://facebook.github.io/jsx/) is an XML\-like extension to JavaScript that allows us to write code like this:

jsx\`\`\`
const vnode = \hello\
\`\`\`Inside JSX expressions, use curly braces to embed dynamic values:

jsx\`\`\`
const vnode = \hello, {userName}\
\`\`\``create-vue` and Vue CLI both have options for scaffolding projects with pre\-configured JSX support. If you are configuring JSX manually, please refer to the documentation of [`@vue/babel-plugin-jsx`](https://github.com/vuejs/jsx-next) for details.

Although first introduced by React, JSX actually has no defined runtime semantics and can be compiled into various different outputs. If you have worked with JSX before, do note that **Vue JSX transform is different from React's JSX transform**, so you can't use React's JSX transform in Vue applications. Some notable differences from React JSX include:

* You can use HTML attributes such as `class` and `for` as props \- no need to use `className` or `htmlFor`.
* Passing children to components (i.e. slots) [works differently](#passing-slots).

Vue's type definition also provides type inference for TSX usage. When using TSX, make sure to specify `"jsx": "preserve"` in `tsconfig.json` so that TypeScript leaves the JSX syntax intact for Vue JSX transform to process.

### JSX Type Inference [​](#jsx-type-inference)

Similar to the transform, Vue's JSX also needs different type definitions.

Starting in Vue 3\.4, Vue no longer implicitly registers the global `JSX` namespace. To instruct TypeScript to use Vue's JSX type definitions, make sure to include the following in your `tsconfig.json`:

json\`\`\`
{
 "compilerOptions": {
 "jsx": "preserve",
 "jsxImportSource": "vue"
 // ...
 }
}
\`\`\`You can also opt\-in per file by adding a `/* @jsxImportSource vue */` comment at the top of the file.

If there is code that depends on the presence of the global `JSX` namespace, you can retain the exact pre\-3\.4 global behavior by explicitly importing or referencing `vue/jsx` in your project, which registers the global `JSX` namespace.

## Render Function Recipes [​](#render-function-recipes)

Below we will provide some common recipes for implementing template features as their equivalent render functions / JSX.

### `v-if` [​](#v-if)

Template:

template\`\`\`
\
 \yes\
 \no\
\
\`\`\`Equivalent render function / JSX:

js\`\`\`
h('div', \[ok.value ? h('div', 'yes') : h('span', 'no')])
\`\`\`jsx\`\`\`
\{ok.value ? \yes\ : \no\}\
\`\`\`js\`\`\`
h('div', \[this.ok ? h('div', 'yes') : h('span', 'no')])
\`\`\`jsx\`\`\`
\{this.ok ? \yes\ : \no\}\
\`\`\`### `v-for` [​](#v-for)

Template:

template\`\`\`
\
 \
 {{ text }}
 \
\
\`\`\`Equivalent render function / JSX:

js\`\`\`
h(
 'ul',
 // assuming \`items\` is a ref with array value
 items.value.map(({ id, text }) =\> {
 return h('li', { key: id }, text)
 })
)
\`\`\`jsx\`\`\`
\
 {items.value.map(({ id, text }) =\> {
 return \{text}\
 })}
\
\`\`\`js\`\`\`
h(
 'ul',
 this.items.map(({ id, text }) =\> {
 return h('li', { key: id }, text)
 })
)
\`\`\`jsx\`\`\`
\
 {this.items.map(({ id, text }) =\> {
 return \{text}\
 })}
\
\`\`\`### `v-on` [​](#v-on)

Props with names that start with `on` followed by an uppercase letter are treated as event listeners. For example, `onClick` is the equivalent of `@click` in templates.

js\`\`\`
h(
 'button',
 {
 onClick(event) {
 /\* ... \*/
 }
 },
 'Click Me'
)
\`\`\`jsx\`\`\`
\ {
 /\* ... \*/
 }}
\>
 Click Me
\
\`\`\`#### Event Modifiers [​](#event-modifiers)

For the `.passive`, `.capture`, and `.once` event modifiers, they can be concatenated after the event name using camelCase.

For example:

js\`\`\`
h('input', {
 onClickCapture() {
 /\* listener in capture mode \*/
 },
 onKeyupOnce() {
 /\* triggers only once \*/
 },
 onMouseoverOnceCapture() {
 /\* once \+ capture \*/
 }
})
\`\`\`jsx\`\`\`
\ {}}
 onKeyupOnce={() =\> {}}
 onMouseoverOnceCapture={() =\> {}}
/\>
\`\`\`For other event and key modifiers, the [`withModifiers`](/api/render-function#withmodifiers) helper can be used:

js\`\`\`
import { withModifiers } from 'vue'

h('div', {
 onClick: withModifiers(() =\> {}, \['self'])
})
\`\`\`jsx\`\`\`
\ {}, \['self'])} /\>
\`\`\`### Components [​](#components)

To create a vnode for a component, the first argument passed to `h()` should be the component definition. This means when using render functions, it is unnecessary to register components \- you can just use the imported components directly:

js\`\`\`
import Foo from './Foo.vue'
import Bar from './Bar.jsx'

function render() {
 return h('div', \[h(Foo), h(Bar)])
}
\`\`\`jsx\`\`\`
function render() {
 return (
 \
 \
 \
 \
 )
}
\`\`\`As we can see, `h` can work with components imported from any file format as long as it's a valid Vue component.

Dynamic components are straightforward with render functions:

js\`\`\`
import Foo from './Foo.vue'
import Bar from './Bar.jsx'

function render() {
 return ok.value ? h(Foo) : h(Bar)
}
\`\`\`jsx\`\`\`
function render() {
 return ok.value ? \ : \
}
\`\`\`If a component is registered by name and cannot be imported directly (for example, globally registered by a library), it can be programmatically resolved by using the [`resolveComponent()`](/api/render-function#resolvecomponent) helper.

### Rendering Slots [​](#rendering-slots)

In render functions, slots can be accessed from the `setup()` context. Each slot on the `slots` object is a **function that returns an array of vnodes**:

js\`\`\`
export default {
 props: \['message'],
 setup(props, { slots }) {
 return () =\> \[
 // default slot:
 // \\\
 h('div', slots.default()),

 // named slot:
 // \\\
 h(
 'div',
 slots.footer({
 text: props.message
 })
 )
 ]
 }
}
\`\`\`JSX equivalent:

jsx\`\`\`
// default
\{slots.default()}\

// named
\{slots.footer({ text: props.message })}\
\`\`\`In render functions, slots can be accessed from [`this.$slots`](/api/component-instance#slots):

js\`\`\`
export default {
 props: \['message'],
 render() {
 return \[
 // \\\
 h('div', this.$slots.default()),

 // \\\
 h(
 'div',
 this.$slots.footer({
 text: this.message
 })
 )
 ]
 }
}
\`\`\`JSX equivalent:

jsx\`\`\`
// \\\
\{this.$slots.default()}\

// \\\
\{this.$slots.footer({ text: this.message })}\
\`\`\`### Passing Slots [​](#passing-slots)

Passing children to components works a bit differently from passing children to elements. Instead of an array, we need to pass either a slot function, or an object of slot functions. Slot functions can return anything a normal render function can return \- which will always be normalized to arrays of vnodes when accessed in the child component.

js\`\`\`
// single default slot
h(MyComponent, () =\> 'hello')

// named slots
// notice the \`null\` is required to avoid
// the slots object being treated as props
h(MyComponent, null, {
 default: () =\> 'default slot',
 foo: () =\> h('div', 'foo'),
 bar: () =\> \[h('span', 'one'), h('span', 'two')]
})
\`\`\`JSX equivalent:

jsx\`\`\`
// default
\{() =\> 'hello'}\

// named
\{{
 default: () =\> 'default slot',
 foo: () =\> \foo\,
 bar: () =\> \[\one\, \two\]
}}\
\`\`\`Passing slots as functions allows them to be invoked lazily by the child component. This leads to the slot's dependencies being tracked by the child instead of the parent, which results in more accurate and efficient updates.

### Scoped Slots [​](#scoped-slots)

To render a scoped slot in the parent component, a slot is passed to the child. Notice how the slot now has a parameter `text`. The slot will be called in the child component and the data from the child component will be passed up to the parent component.

js\`\`\`
// parent component
export default {
 setup() {
 return () =\> h(MyComp, null, {
 default: ({ text }) =\> h('p', text)
 })
 }
}
\`\`\`Remember to pass `null` so the slots will not be treated as props.

js\`\`\`
// child component
export default {
 setup(props, { slots }) {
 const text = ref('hi')
 return () =\> h('div', null, slots.default({ text: text.value }))
 }
}
\`\`\`JSX equivalent:

jsx\`\`\`
\{{
 default: ({ text }) =\> \{ text }\ 
}}\
\`\`\`### Built\-in Components [​](#built-in-components)

[Built\-in components](/api/built-in-components) such as ``, ``, ``, `` and `` must be imported for use in render functions:

js\`\`\`
import { h, KeepAlive, Teleport, Transition, TransitionGroup } from 'vue'

export default {
 setup () {
 return () =\> h(Transition, { mode: 'out\-in' }, /\* ... \*/)
 }
}
\`\`\`js\`\`\`
import { h, KeepAlive, Teleport, Transition, TransitionGroup } from 'vue'

export default {
 render () {
 return h(Transition, { mode: 'out\-in' }, /\* ... \*/)
 }
}
\`\`\`### `v-model` [​](#v-model)

The `v-model` directive is expanded to `modelValue` and `onUpdate:modelValue` props during template compilation—we will have to provide these props ourselves:

js\`\`\`
export default {
 props: \['modelValue'],
 emits: \['update:modelValue'],
 setup(props, { emit }) {
 return () =\>
 h(SomeComponent, {
 modelValue: props.modelValue,
 'onUpdate:modelValue': (value) =\> emit('update:modelValue', value)
 })
 }
}
\`\`\`js\`\`\`
export default {
 props: \['modelValue'],
 emits: \['update:modelValue'],
 render() {
 return h(SomeComponent, {
 modelValue: this.modelValue,
 'onUpdate:modelValue': (value) =\> this.$emit('update:modelValue', value)
 })
 }
}
\`\`\`### Custom Directives [​](#custom-directives)

Custom directives can be applied to a vnode using [`withDirectives`](/api/render-function#withdirectives):

js\`\`\`
import { h, withDirectives } from 'vue'

// a custom directive
const pin = {
 mounted() { /\* ... \*/ },
 updated() { /\* ... \*/ }
}

// \\
const vnode = withDirectives(h('div'), \[
 \[pin, 200, 'top', { animate: true }]
])
\`\`\`If the directive is registered by name and cannot be imported directly, it can be resolved using the [`resolveDirective`](/api/render-function#resolvedirective) helper.

### Template Refs [​](#template-refs)

With the Composition API, template refs are created by passing the `ref()` itself as a prop to the vnode:

js\`\`\`
import { h, ref } from 'vue'

export default {
 setup() {
 const divEl = ref()

 // \
 return () =\> h('div', { ref: divEl })
 }
}
\`\`\`With the Options API, template refs are created by passing the ref name as a string in the vnode props:

js\`\`\`
export default {
 render() {
 // \
 return h('div', { ref: 'divEl' })
 }
}
\`\`\`## Functional Components [​](#functional-components)

Functional components are an alternative form of component that don't have any state of their own. They act like pure functions: props in, vnodes out. They are rendered without creating a component instance (i.e. no `this`), and without the usual component lifecycle hooks.

To create a functional component we use a plain function, rather than an options object. The function is effectively the `render` function for the component.

The signature of a functional component is the same as the `setup()` hook:

js\`\`\`
function MyComponent(props, { slots, emit, attrs }) {
 // ...
}
\`\`\`As there is no `this` reference for a functional component, Vue will pass in the `props` as the first argument:

js\`\`\`
function MyComponent(props, context) {
 // ...
}
\`\`\`The second argument, `context`, contains three properties: `attrs`, `emit`, and `slots`. These are equivalent to the instance properties [`$attrs`](/api/component-instance#attrs), [`$emit`](/api/component-instance#emit), and [`$slots`](/api/component-instance#slots) respectively.

Most of the usual configuration options for components are not available for functional components. However, it is possible to define [`props`](/api/options-state#props) and [`emits`](/api/options-state#emits) by adding them as properties:

js\`\`\`
MyComponent.props = \['value']
MyComponent.emits = \['click']
\`\`\`If the `props` option is not specified, then the `props` object passed to the function will contain all attributes, the same as `attrs`. The prop names will not be normalized to camelCase unless the `props` option is specified.

For functional components with explicit `props`, [attribute fallthrough](/guide/components/attrs) works much the same as with normal components. However, for functional components that don't explicitly specify their `props`, only the `class`, `style`, and `onXxx` event listeners will be inherited from the `attrs` by default. In either case, `inheritAttrs` can be set to `false` to disable attribute inheritance:

js\`\`\`
MyComponent.inheritAttrs = false
\`\`\`Functional components can be registered and consumed just like normal components. If you pass a function as the first argument to `h()`, it will be treated as a functional component.

### Typing Functional Components [​](#typing-functional-components)

Functional Components can be typed based on whether they are named or anonymous. [Vue \- Official extension](https://github.com/vuejs/language-tools) also supports type checking properly typed functional components when consuming them in SFC templates.

**Named Functional Component**

tsx\`\`\`
import type { SetupContext } from 'vue'
type FComponentProps = {
 message: string
}

type Events = {
 sendMessage(message: string): void
}

function FComponent(
 props: FComponentProps,
 context: SetupContext\
) {
 return (
 \ context.emit('sendMessage', props.message)}\>
 {props.message} {' '}
 \
 )
}

FComponent.props = {
 message: {
 type: String,
 required: true
 }
}

FComponent.emits = {
 sendMessage: (value: unknown) =\> typeof value === 'string'
}
\`\`\`**Anonymous Functional Component**

tsx\`\`\`
import type { FunctionalComponent } from 'vue'

type FComponentProps = {
 message: string
}

type Events = {
 sendMessage(message: string): void
}

const FComponent: FunctionalComponent\ = (
 props,
 context
) =\> {
 return (
 \ context.emit('sendMessage', props.message)}\>
   {props.message} {' '}
 \
 )
}

FComponent.props = {
 message: {
 type: String,
 required: true
 }
}

FComponent.emits = {
 sendMessage: (value) =\> typeof value === 'string'
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/extras/render-function.md)



## Computed Properties | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/computed)

# Computed Properties [​](#computed-properties)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/computed-properties-in-vue-3?friend=vuejs "Free Vue.js Computed Properties Lesson")[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-fundamentals-capi-computed-properties-in-vue-with-the-composition-api?friend=vuejs "Free Vue.js Computed Properties Lesson")## Basic Example [​](#basic-example)

In\-template expressions are very convenient, but they are meant for simple operations. Putting too much logic in your templates can make them bloated and hard to maintain. For example, if we have an object with a nested array:

js\`\`\`
export default {
 data() {
 return {
 author: {
 name: 'John Doe',
 books: \[
 'Vue 2 \- Advanced Guide',
 'Vue 3 \- Basic Guide',
 'Vue 4 \- The Mystery'
 ]
 }
 }
 }
}
\`\`\`js\`\`\`
const author = reactive({
 name: 'John Doe',
 books: \[
 'Vue 2 \- Advanced Guide',
 'Vue 3 \- Basic Guide',
 'Vue 4 \- The Mystery'
 ]
})
\`\`\`And we want to display different messages depending on if `author` already has some books or not:

template\`\`\`
\Has published books:\
\{{ author.books.length \> 0 ? 'Yes' : 'No' }}\
\`\`\`At this point, the template is getting a bit cluttered. We have to look at it for a second before realizing that it performs a calculation depending on `author.books`. More importantly, we probably don't want to repeat ourselves if we need to include this calculation in the template more than once.

That's why for complex logic that includes reactive data, it is recommended to use a **computed property**. Here's the same example, refactored:

js\`\`\`
export default {
 data() {
 return {
 author: {
 name: 'John Doe',
 books: \[
 'Vue 2 \- Advanced Guide',
 'Vue 3 \- Basic Guide',
 'Vue 4 \- The Mystery'
 ]
 }
 }
 },
 computed: {
 // a computed getter
 publishedBooksMessage() {
 // \`this\` points to the component instance
 return this.author.books.length \> 0 ? 'Yes' : 'No'
 }
 }
}
\`\`\`template\`\`\`
\Has published books:\
\{{ publishedBooksMessage }}\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFkN1KxDAQhV/l0JsqaFfUq1IquwiKsF6JINaLbDNui20S8rO4lL676c82eCFCIDOZMzkzXxetlUoOjqI0ykypa2XzQtC3ktqC0ydzjUVXCIAzy87OpxjQZJ0WpwxgzlZSp+EBEKylFPGTrATuJcUXobST8sukeA8vQPzqCNe4xJofmCiJ48HV/FfbLLrxog0zdfmn4tYrXirC9mgs6WMcBB+nsJ+C8erHH0rZKmeJL0sot2tqUxHfDONuyRi2p4BggWCr2iQTgGTcLGlI7G2FHFe4Q/xGJoYn8SznQSbTQviTrRboPrHUqoZZ8hmQqfyRmTDFTC1bqalsFBN5183o/3NG33uvoWUwXYyi/gdTEpwK)

Here we have declared a computed property `publishedBooksMessage`.

Try to change the value of the `books` array in the application `data` and you will see how `publishedBooksMessage` is changing accordingly.

You can data\-bind to computed properties in templates just like a normal property. Vue is aware that `this.publishedBooksMessage` depends on `this.author.books`, so it will update any bindings that depend on `this.publishedBooksMessage` when `this.author.books` changes.

See also: [Typing Computed Properties](/guide/typescript/options-api#typing-computed-properties) 

vue\`\`\`
\
import { reactive, computed } from 'vue'

const author = reactive({
 name: 'John Doe',
 books: \[
 'Vue 2 \- Advanced Guide',
 'Vue 3 \- Basic Guide',
 'Vue 4 \- The Mystery'
 ]
})

// a computed ref
const publishedBooksMessage = computed(() =\> {
 return author.books.length \> 0 ? 'Yes' : 'No'
})
\

\
 \Has published books:\
 \{{ publishedBooksMessage }}\
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp1kE9Lw0AQxb/KI5dtoTainkoaaREUoZ5EEONhm0ybYLO77J9CCfnuzta0vdjbzr6Zeb95XbIwZroPlMySzJW2MR6OfDB5oZrWaOvRwZIsfbOnCUrdmuCpQo+N1S0ET4pCFarUynnI4GttMT9PjLpCAUq2NIN41bXCkyYxiZ9rrX/cDF/xDYiPQLjDDRbVXqqSHZ5DUw2tg3zP8lK6pvxHe2DtvSasDs6TPTAT8F2ofhzh0hTygm5pc+I1Yb1rXE3VMsKsyDm5JcY/9Y5GY8xzHI+wnIpVw4nTI/10R2rra+S4xSPEJzkBvvNNs310ztK/RDlLLjy1Zic9cQVkJn+R7gIwxJGlMXiWnZEq77orhH3Pq2NH9DjvTfpfSBSbmA==)

Here we have declared a computed property `publishedBooksMessage`. The `computed()` function expects to be passed a [getter function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description), and the returned value is a **computed ref**. Similar to normal refs, you can access the computed result as `publishedBooksMessage.value`. Computed refs are also auto\-unwrapped in templates so you can reference them without `.value` in template expressions.

A computed property automatically tracks its reactive dependencies. Vue is aware that the computation of `publishedBooksMessage` depends on `author.books`, so it will update any bindings that depend on `publishedBooksMessage` when `author.books` changes.

See also: [Typing Computed](/guide/typescript/composition-api#typing-computed) 

## Computed Caching vs. Methods [​](#computed-caching-vs-methods)

You may have noticed we can achieve the same result by invoking a method in the expression:

template\`\`\`
\{{ calculateBooksMessage() }}\
\`\`\`js\`\`\`
// in component
methods: {
 calculateBooksMessage() {
 return this.author.books.length \> 0 ? 'Yes' : 'No'
 }
}
\`\`\`js\`\`\`
// in component
function calculateBooksMessage() {
 return author.books.length \> 0 ? 'Yes' : 'No'
}
\`\`\`Instead of a computed property, we can define the same function as a method. For the end result, the two approaches are indeed exactly the same. However, the difference is that **computed properties are cached based on their reactive dependencies.** A computed property will only re\-evaluate when some of its reactive dependencies have changed. This means as long as `author.books` has not changed, multiple access to `publishedBooksMessage` will immediately return the previously computed result without having to run the getter function again.

This also means the following computed property will never update, because `Date.now()` is not a reactive dependency:

js\`\`\`
computed: {
 now() {
 return Date.now()
 }
}
\`\`\`js\`\`\`
const now = computed(() =\> Date.now())
\`\`\`In comparison, a method invocation will **always** run the function whenever a re\-render happens.

Why do we need caching? Imagine we have an expensive computed property `list`, which requires looping through a huge array and doing a lot of computations. Then we may have other computed properties that in turn depend on `list`. Without caching, we would be executing `list`’s getter many more times than necessary! In cases where you do not want caching, use a method call instead.

## Writable Computed [​](#writable-computed)

Computed properties are by default getter\-only. If you attempt to assign a new value to a computed property, you will receive a runtime warning. In the rare cases where you need a "writable" computed property, you can create one by providing both a getter and a setter:

js\`\`\`
export default {
 data() {
 return {
 firstName: 'John',
 lastName: 'Doe'
 }
 },
 computed: {
 fullName: {
 // getter
 get() {
 return this.firstName \+ ' ' \+ this.lastName
 },
 // setter
 set(newValue) {
 // Note: we are using destructuring assignment syntax here.
 \[this.firstName, this.lastName] = newValue.split(' ')
 }
 }
 }
}
\`\`\`Now when you run `this.fullName = 'John Doe'`, the setter will be invoked and `this.firstName` and `this.lastName` will be updated accordingly.

vue\`\`\`
\
import { ref, computed } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

const fullName = computed({
 // getter
 get() {
 return firstName.value \+ ' ' \+ lastName.value
 },
 // setter
 set(newValue) {
 // Note: we are using destructuring assignment syntax here.
 \[firstName.value, lastName.value] = newValue.split(' ')
 }
})
\
\`\`\`Now when you run `fullName.value = 'John Doe'`, the setter will be invoked and `firstName` and `lastName` will be updated accordingly.

## Getting the Previous Value [​](#previous)

* Only supported in 3\.4\+

In case you need it, you can get the previous value returned by the computed property accessing the first argument of the getter:

js\`\`\`
export default {
 data() {
 return {
 count: 2
 }
 },
 computed: {
 // This computed will return the value of count when it's less or equal to 3\.
 // When count is \>=4, the last value that fulfilled our condition will be returned
 // instead until count is less or equal to 3
 alwaysSmall(previous) {
 if (this.count \
import { ref, computed } from 'vue'

const count = ref(2\)

// This computed will return the value of count when it's less or equal to 3\.
// When count is \>=4, the last value that fulfilled our condition will be returned
// instead until count is less or equal to 3
const alwaysSmall = computed((previous) =\> {
 if (count.value \
\`\`\`In case you're using a writable computed:

js\`\`\`
export default {
 data() {
 return {
 count: 2
 }
 },
 computed: {
 alwaysSmall: {
 get(previous) {
 if (this.count \
import { ref, computed } from 'vue'

const count = ref(2\)

const alwaysSmall = computed({
 get(previous) {
 if (count.value \
\`\`\`## Best Practices [​](#best-practices)

### Getters should be side\-effect free [​](#getters-should-be-side-effect-free)

It is important to remember that computed getter functions should only perform pure computation and be free of side effects. For example, **don't mutate other state, make async requests, or mutate the DOM inside a computed getter!** Think of a computed property as declaratively describing how to derive a value based on other values \- its only responsibility should be computing and returning that value. Later in the guide we will discuss how we can perform side effects in reaction to state changes with [watchers](/guide/essentials/watchers).

### Avoid mutating computed value [​](#avoid-mutating-computed-value)

The returned value from a computed property is derived state. Think of it as a temporary snapshot \- every time the source state changes, a new snapshot is created. It does not make sense to mutate a snapshot, so a computed return value should be treated as read\-only and never be mutated \- instead, update the source state it depends on to trigger new computations.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/computed.md)



## Slots | Vue.js

[Read the full article](https://vuejs.org/guide/components/slots)

# Slots [​](#slots)

> This page assumes you've already read the [Components Basics](/guide/essentials/component-basics). Read that first if you are new to components.

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-3-component-slots?friend=vuejs "Free Vue.js Slots Lesson")## Slot Content and Outlet [​](#slot-content-and-outlet)

We have learned that components can accept props, which can be JavaScript values of any type. But how about template content? In some cases, we may want to pass a template fragment to a child component, and let the child component render the fragment within its own template.

For example, we may have a `` component that supports usage like this:

template\`\`\`
\
 Click me! \
\
\`\`\`The template of `` looks like this:

template\`\`\`
\
 \\ \
\
\`\`\`The `` element is a **slot outlet** that indicates where the parent\-provided **slot content** should be rendered.



And the final rendered DOM:

html\`\`\`
\Click me!\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpdUdlqAyEU/ZVbQ0kLMdNsXabTQFvoV8yLcRkkjopLSQj596oTwqRvnuM9y9UT+rR2/hs5qlHjqZM2gOch2m2rZW+NC/BDND1+xRCMBuFMD9N5NeKyeNrqphrUSZdA4L1VJPCEAJrRdCEAvpWke+g5NHcYg1cmADU6cB0A4zzThmYckqimupqiGfpXILe/zdwNhaki3n+0SOR5vAu6ReU++efUajtqYGJQ/FIg5w8Wt9FlOx+OKh/nV1c4ZVNqlHE1TIQQ7xnvCN13zkTNalBSc+Jw5wiTac2H1WLDeDeDyXrJVm9LWG7uE3hev3AhHge1cYwnO200L4QljEnd1bCxB1g82UNhe+I6qQs5kuGcE30NrxeaRudzOWtkemeXuHP5tLIKOv8BN+mw3w==)

[Try it in the Playground](https://play.vuejs.org/#eNpdUdtOwzAM/RUThAbSurIbl1ImARJf0ZesSapoqROlKdo07d9x0jF1SHmIT+xzcY7sw7nZTy9Zwcqu9tqFTYW6ddYH+OZYHz77ECyC8raFySwfYXFsUiFAhXKfBoRUvDcBjhGtLbGgxNAVcLziOlVIp8wvelQE2TrDg6QKoBx1JwDgy+h6B62E8ibLoDM2kAAGoocsiz1VKMfmCCrzCymbsn/GY95rze1grja8694rpmJ/tg1YsfRO/FE134wc2D4YeTYQ9QeKa+mUrgsHE6+zC+vfjoz1Bdwqpd5iveX1rvG2R1GA0Si5zxrPhaaY98v5WshmCrerhVi+LmCxvqPiafUslXoYpq0XkuiQ1p4Ax4XQ2BSwdnuYP7p9QlvuG40JHI1lUaenv3o5w3Xvu2jOWU179oQNn5aisNMvLBvDOg==)

With slots, the `` is responsible for rendering the outer `` (and its fancy styling), while the inner content is provided by the parent component.

Another way to understand slots is by comparing them to JavaScript functions:

js\`\`\`
// parent component passing slot content
FancyButton('Click me!')

// FancyButton renders slot content in its own template
function FancyButton(slotContent) {
 return \`\
 ${slotContent}
 \\`
}
\`\`\`Slot content is not just limited to text. It can be any valid template content. For example, we can pass in multiple elements, or even other components:

template\`\`\`
\
 \Click me!\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp1UmtOwkAQvspQYtCEgrx81EqCJibeoX+W7bRZaHc3+1AI4QyewH8ewvN4Aa/gbgtNIfFf5+vMfI/ZXbCQcvBmMYiCWFPFpAGNxsp5wlkphTLwQjjdPlljBIdMiRJ6g2EL88O9pnnxjlqU+EpbzS3s0BwPaypH4gqDpSyIQVcBxK3VFQDwXDC6hhJdlZi4zf3fRKwl4aDNtsDHJKCiECqiW8KTYH5c1gEnwnUdJ9rCh/XeM6Z42AgN+sFZAj6+Ux/LOjFaEK2diMz3h0vjNfj/zokuhPFU3lTdfcpShVOZcJ+DZgHs/HxtCrpZlj34eknoOlfC8jSCgnEkKswVSRlyczkZzVLM+9CdjtPJ/RjGswtX3ExvMcuu6mmhUnTruOBYAZKkKeN5BDO5gdG13FRoSVTOeAW2xkLPY3UEdweYWqW9OCkYN6gctq9uXllx2Z09CJ9dJwzBascI7nBYihWDldUGMqEgdTVIq6TQqCEMfUpNSD+fX7/fH+3b7P8AdGP6wA==)

[Try it in the Playground](https://play.vuejs.org/#eNptUltu2zAQvMpGQZEWsOzGiftQ1QBpgQK9g35oaikwkUiCj9aGkTPkBPnLIXKeXCBXyJKKBdoIoA/tYGd3doa74tqY+b+ARVXUjltp/FWj5GC09fCHKb79FbzXCoTVA5zNFxkWaWdT8/V/dHrAvzxrzrC3ZoBG4SYRWhQs9B52EeWapihU3lWwyxfPDgbfNYq+ejEppcLjYHrmkSqAOqMmAOB3L/ktDEhV4+v8gMR/l1M7wxQ4v+3xZ1Nw3Wtb8S1TTXG1H3cCJIO69oxc5mLUcrSrXkxSi1lxZGT0//CS9Wg875lzJELE/nLto4bko69dr31cFc8auw+3JHvSEfQ7nwbsHY9HwakQ4kes14zfdlYH1VbQS4XMlp1lraRMPl6cr1rsZnB6uWwvvi9hufpAxZfLryjEp5GtbYs0TlGICTCsbaXqKliZDZx/NpuEDsx2UiUwo5VxT6Dkv73BPFgXxRktlUdL2Jh6OoW8O3pX0buTsoTgaCNQcDjoGwk3wXkQ2tJLGzSYYI126KAso0uTSc8Pjy9P93k2d6+NyRKa)

By using slots, our `` is more flexible and reusable. We can now use it in different places with different inner content, but all with the same fancy styling.

Vue components' slot mechanism is inspired by the [native Web Component `` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot), but with additional capabilities that we will see later.

## Render Scope [​](#render-scope)

Slot content has access to the data scope of the parent component, because it is defined in the parent. For example:

template\`\`\`
\{{ message }}\
\{{ message }}\
\`\`\`Here both `{{ message }}` interpolations will render the same content.

Slot content does **not** have access to the child component's data. Expressions in Vue templates can only access the scope it is defined in, consistent with JavaScript's lexical scoping. In other words:

> Expressions in the parent template only have access to the parent scope; expressions in the child template only have access to the child scope.

## Fallback Content [​](#fallback-content)

There are cases when it's useful to specify fallback (i.e. default) content for a slot, to be rendered only when no content is provided. For example, in a `` component:

template\`\`\`
\
 \\
\
\`\`\`We might want the text "Submit" to be rendered inside the `` if the parent didn't provide any slot content. To make "Submit" the fallback content, we can place it in between the `` tags:

template\`\`\`
\
 \
 Submit \
 \
\
\`\`\`Now when we use `` in a parent component, providing no content for the slot:

template\`\`\`
\
\`\`\`This will render the fallback content, "Submit":

html\`\`\`
\Submit\
\`\`\`But if we provide content:

template\`\`\`
\Save\
\`\`\`Then the provided content will be rendered instead:

html\`\`\`
\Save\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp1kMsKwjAQRX9lzMaNbfcSC/oL3WbT1ikU8yKZFEX8d5MGgi2YVeZxZ86dN7taWy8B2ZlxP7rZEnikYFuhZ2WNI+jCoGa6BSKjYXJGwbFufpNJfhSaN1kflTEgVFb2hDEC4IeqguARpl7KoR8fQPgkqKpc3Wxo1lxRWWeW+Y4wBk9x9V9d2/UL8g1XbOJN4WAntodOnrecQ2agl8WLYH7tFyw5olj10iR3EJ+gPCxDFluj0YS6EAqKR8mi9M3Td1ifLxWShcU=)

[Try it in the Playground](https://play.vuejs.org/#eNp1UEEOwiAQ/MrKxYu1d4Mm+gWvXChuk0YKpCyNxvh3lxIb28SEA8zuDDPzEucQ9mNCcRAymqELdFKu64MfCK6p6Tu6JCLvoB18D9t9/Qtm4lY5AOXwMVFu2OpkCV4ZNZ51HDqKhwLAQjIjb+X4yHr+mh+EfbCakF8AclNVkCJCq61ttLkD4YOgqsp0YbGesJkVBj92NwSTIrH3v7zTVY8oF8F4SdazD7ET69S5rqXPpnigZ8CjEnHaVyInIp5G63O6XIGiIlZMzrGMd8RVfR0q4lIKKV+L+srW+wNTTZq3)

## Named Slots [​](#named-slots)

There are times when it's useful to have multiple slot outlets in a single component. For example, in a `` component with the following template:

template\`\`\`
\
 \
 \
 \
 \
 \
 \
 \
 \
 \
\
\`\`\`For these cases, the `` element has a special attribute, `name`, which can be used to assign a unique ID to different slots so you can determine where content should be rendered:

template\`\`\`
\
 \
 \\
 \
 \
 \\
 \
 \
 \\
 \
\
\`\`\`A `` outlet without `name` implicitly has the name "default".

In a parent component using ``, we need a way to pass multiple slot content fragments, each targeting a different slot outlet. This is where **named slots** come in.

To pass a named slot, we need to use a `` element with the `v-slot` directive, and then pass the name of the slot as an argument to `v-slot`:

template\`\`\`
\
 \
 \
 \
\
\`\`\``v-slot` has a dedicated shorthand `#`, so `` can be shortened to just ``. Think of it as "render this template fragment in the child component's 'header' slot".



Here's the code passing content for all three slots to `` using the shorthand syntax:

template\`\`\`
\
 \
 \Here might be a page title\
 \

 \
 \A paragraph for the main content.\
 \And another one.\
 \

 \
 \Here's some contact info\
 \
\
\`\`\`When a component accepts both a default slot and named slots, all top\-level non\-`` nodes are implicitly treated as content for the default slot. So the above can also be written as:

template\`\`\`
\
 \
 \Here might be a page title\
 \

 \
 \A paragraph for the main content.\
 \And another one.\

 \
 \Here's some contact info\
 \
\
\`\`\`Now everything inside the `` elements will be passed to the corresponding slots. The final rendered HTML will be:

html\`\`\`
\
 \
 \Here might be a page title\
 \
 \
 \A paragraph for the main content.\
 \And another one.\
 \
 \
 \Here's some contact info\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9UsFuwjAM/RWrHLgMOi5o6jIkdtphn9BLSF0aKU2ixEVjiH+fm8JoQdvRfu/5xS8+ZVvvl4cOsyITUQXtCSJS5zel1a13geBdRvyUR9cR1MG1MF/mt1YvnZdW5IOWVVwQtt5IQq4AxI2cau5ccZg1KCsMlz4jzWrzgQGh1fuGYIcgwcs9AmkyKHKGLyPykcfD1Apr2ZmrHUN+s+U5Qe6D9A3ULgA1bCK1BeUsoaWlyPuVb3xbgbSOaQGcxRH8v3XtHI0X8mmfeYToWkxmUhFoW7s/JvblJLERmj1l0+T7T5tqK30AZWSMb2WW3LTFUGZXp/u8o3EEVrbI9AFjLn8mt38fN9GIPrSp/p4/Yoj7OMZ+A/boN9KInPeZZpAOLNLRDAsPZDgN4p0L/NQFOV/Ayn9x6EZXMFNKvQ4E5YwLBczW6/WlU3NIi6i/sYDn5Qu2qX1OF51MsvMPkrIEHg==)

[Try it in the Playground](https://play.vuejs.org/#eNp9UkFuwjAQ/MoqHLiUpFxQlaZI9NRDn5CLSTbEkmNb9oKgiL934wRwQK3ky87O7njGPicba9PDHpM8KXzlpKV1qWVnjSP4FB6/xcnsCRpnOpin2R3qh+alBig1HgO9xkbsFcG5RyvDOzRq8vkAQLSury+l5lNkN1EuCDurBCFXAMWdH2pGrn2YtShqdCPOnXa5/kKH0MldS7BFEGDFDoEkKSwybo8rskjjaevo4L7Wrje8x4mdE7aFxjiglkWE1GxQE9tLi8xO+LoGoQ3THLD/qP2/dGMMxYZs8DP34E2HQUxUBFI35o+NfTlJLOomL8n04frXns7W8gCVEt5/lElQkxpdmVyVHvP2yhBo0SHThx5z+TEZvl1uMlP0oU3nH/kRo3iMI9Ybes960UyRsZ9pBuGDeTqpwfBAvn7NrXF81QUZm8PSHjl0JWuYVVX1PhAqo4zLYbZarUak4ZAWXv5gDq/pG3YBHn50EEkuv5irGBk=)

Again, it may help you understand named slots better using the JavaScript function analogy:

js\`\`\`
// passing multiple slot fragments with different names
BaseLayout({
 header: \`...\`,
 default: \`...\`,
 footer: \`...\`
})

// \ renders them in different places
function BaseLayout(slots) {
 return \`\
 \${slots.header}\
 \${slots.default}\
 \${slots.footer}\
 \\`
}
\`\`\`## Conditional Slots [​](#conditional-slots)

Sometimes you want to render something based on whether or not content has been passed to a slot.

You can use the [$slots](/api/component-instance#slots) property in combination with a [v\-if](/guide/essentials/conditional#v-if) to achieve this.

In the example below we define a Card component with three conditional slots: `header`, `footer` and the `default` one. When content for the header / footer / default is present, we want to wrap it to provide additional styling:

template\`\`\`
\
 \
 \
 \
 \

 \
 \
 \

 \
 \
 \
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqVVMtu2zAQ/BWCLZBLIjVoTq4aoA1yaA9t0eaoCy2tJcYUSZCUKyPwv2dJioplOw4C+EDuzM4+ONYT/aZ1tumBLmhhK8O1IxZcr29LyTutjCN3zNRkZVRHLrLcXzz9opRFHvnIxIuDTgvmAG+EFJ4WTnhOCPnQAqvBjHFE2uvbh5Zbgj/XAolwkWN4TM33VI/UalixXvjyo5yeqVVKOpCuyP0ob6utlHL7vUE3U4twkWP4hJq/jiPP4vSSOouNrHiTPVolcclPnl3SSnWaCzC/teNK2pIuSEA8xoRQ/3+GmDM9XKZ41UK1PhF/tIOPlfSPAQtmAyWdMMdMAy7C9/9+wYDnCexU3QtknwH/glWi9z1G2vde1tj2Hi90+yNYhcvmwd4PuHabhvKNeuYu8EuK1rk7M/pLu5+zm5BXyh1uMdnOu3S+95pvSCWYtV9xQcgqaXogj2yu+AqBj1YoZ7NosJLOEq5S9OXtPZtI1gFSppx8engUHs+vVhq9eVhq9ORRrXdpRyseSqfo6SmmnONK6XTw9yis24q448wXSG+0VAb3sSDXeiBoDV6TpWDV+ktENatrdMGCfAoBfL1JYNzzpINJjVFoJ9yKUKho19ul6OFQ6UYPx1rjIpPYeXIc/vXCgjetawzbni0dPnhhJ3T3DMVSruI=)

## Dynamic Slot Names [​](#dynamic-slot-names)

[Dynamic directive arguments](/guide/essentials/template-syntax#dynamic-arguments) also work on `v-slot`, allowing the definition of dynamic slot names:

template\`\`\`
\
 \
 ...
 \

 \
 \
 ...
 \
\
\`\`\`Do note the expression is subject to the [syntax constraints](/guide/essentials/template-syntax#dynamic-argument-syntax-constraints) of dynamic directive arguments.

## Scoped Slots [​](#scoped-slots)

As discussed in [Render Scope](#render-scope), slot content does not have access to state in the child component.

However, there are cases where it could be useful if a slot's content can make use of data from both the parent scope and the child scope. To achieve that, we need a way for the child to pass data to a slot when rendering it.

In fact, we can do exactly that \- we can pass attributes to a slot outlet just like passing props to a component:

template\`\`\`
\ template \-\-\>
\
 \\
\
\`\`\`Receiving the slot props is a bit different when using a single default slot vs. using named slots. We are going to show how to receive props using a single default slot first, by using `v-slot` directly on the child component tag:

template\`\`\`
\
 {{ slotProps.text }} {{ slotProps.count }}
\
\`\`\`

[Try it in the Playground](https://play.vuejs.org/#eNp9kMEKgzAMhl8l9OJlU3aVOhg7C3uAXsRlTtC2tFE2pO++dA5xMnZqk+b/8/2dxMnadBxQ5EL62rWWwCMN9qh021vjCMrn2fBNoya4OdNDkmarXhQnSstsVrOOC8LedhVhrEiuHca97wwVSsTj4oz1SvAUgKJpgqWZEj4IQoCvZm0Gtgghzss1BDvIbFkqdmID+CNdbbQnaBwitbop0fuqQSgguWPXmX+JePe1HT/QMtJBHnE51MZOCcjfzPx04JxsydPzp2Szxxo7vABY1I/p)

[Try it in the Playground](https://play.vuejs.org/#eNqFkNFqxCAQRX9l8CUttAl9DbZQ+rzQD/AlJLNpwKjoJGwJ/nvHpAnusrAg6FzHO567iE/nynlCUQsZWj84+lBmGJ31BKffL8sng4bg7O0IRVllWnpWKAOgDF7WBx2em0kTLElt975QbwLkhkmIyvCS1TGXC8LR6YYwVSTzH8yvQVt6VyJt3966oAR38XhaFjjEkvBCECNcia2d2CLyOACZQ7CDrI6h4kXcAF7lcg+za6h5et4JPdLkzV4B9B6RBtOfMISmxxqKH9TarrGtATxMgf/bDfM/qExEUCdEDuLGXAmoV06+euNs2JK7tyCrzSNHjX9aurQf)

The props passed to the slot by the child are available as the value of the corresponding `v-slot` directive, which can be accessed by expressions inside the slot.

You can think of a scoped slot as a function being passed into the child component. The child component then calls it, passing props as arguments:

js\`\`\`
MyComponent({
 // passing the default slot, but as a function
 default: (slotProps) =\> {
 return \`${slotProps.text} ${slotProps.count}\`
 }
})

function MyComponent(slots) {
 const greetingMessage = 'hello'
 return \`\${
 // call the slot function with props!
 slots.default({ text: greetingMessage, count: 1 })
 }\\`
}
\`\`\`In fact, this is very close to how scoped slots are compiled, and how you would use scoped slots in manual [render functions](/guide/extras/render-function).

Notice how `v-slot="slotProps"` matches the slot function signature. Just like with function arguments, we can use destructuring in `v-slot`:

template\`\`\`
\
 {{ text }} {{ count }}
\
\`\`\`### Named Scoped Slots [​](#named-scoped-slots)

Named scoped slots work similarly \- slot props are accessible as the value of the `v-slot` directive: `v-slot:name="slotProps"`. When using the shorthand, it looks like this:

template\`\`\`
\
 \
 {{ headerProps }}
 \

 \
 {{ defaultProps }}
 \

 \
 {{ footerProps }}
 \
\
\`\`\`Passing props to a named slot:

template\`\`\`
\\
\`\`\`Note the `name` of a slot won't be included in the props because it is reserved \- so the resulting `headerProps` would be `{ message: 'hello' }`.

If you are mixing named slots with the default scoped slot, you need to use an explicit `` tag for the default slot. Attempting to place the `v-slot` directive directly on the component will result in a compilation error. This is to avoid any ambiguity about the scope of the props of the default slot. For example:

template\`\`\`
\ template \-\-\>
\
 \\
 \
\
\`\`\`template\`\`\`
\
\
 \{{ message }}\
 \
 \
 \{{ message }}\
 \
\
\`\`\`Using an explicit `` tag for the default slot helps to make it clear that the `message` prop is not available inside the other slot:

template\`\`\`
\
 \
 \
 \{{ message }}\
 \

 \
 \Here's some contact info\
 \
\
\`\`\`### Fancy List Example [​](#fancy-list-example)

You may be wondering what would be a good use case for scoped slots. Here's an example: imagine a `` component that renders a list of items \- it may encapsulate the logic for loading remote data, using the data to display a list, or even advanced features like pagination or infinite scrolling. However, we want it to be flexible with how each item looks and leave the styling of each item to the parent component consuming it. So the desired usage may look like this:

template\`\`\`
\
 \
 \
 \{{ body }}\
 \by {{ username }} \| {{ likes }} likes\
 \
 \
\
\`\`\`Inside ``, we can render the same `` multiple times with different item data (notice we are using `v-bind` to pass an object as slot props):

template\`\`\`
\
 \
 \\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFU2Fv0zAQ/StHJtROapNuZTBCNwnQQKBpTGxCQss+uMml8+bYlu2UlZL/zjlp0lQa40sU3/nd3Xv3vA7eax0uSwziYGZTw7UDi67Up4nkhVbGwScm09U5tw5yowoYhFEX8cBBImdRgyQMHRwWWjCHdAKYbdFM83FpxEkS0DcJINZoxpotkCIHkySo7xOixcMep19KrmGustUISotGsgJHIPgDWqg6DKEyvoRUMGsJ4HG9HGX16bqpAlU1izy5baqDFegYweYroMttMwLAHx/Y9Kyan36RWUTN2+mjXfpbrei8k6SjdSuBYFOlMaNI6AeAtcflSrqx5b8xhkl4jMU7H0yVUCaGvVeH8+PjKYWqWnpf5DQYBTtb+fc612Awh2qzzGaBiUyVpBVpo7SFE8gw5xIv/Wl4M9gsbjCCQbuywe3+FuXl9iiqO7xpElEEhUofKFQo2mTGiFiOLr3jcpFImuiaF6hKNxzuw8lpw7kuEy6ZKJGK3TR6NluLYXBVqwRXQjkLn0ueIc3TLonyZ0sm4acqKVovKIbDCVQjGsb1qvyg2telU4Yzz6eHv6ARBWdwjVqUNCbbFjqgQn6aW1J8RKfJhDg+5/lStG4QHJZjnpO5XjT0BMqFu+uZ81yxjEQJw7A1kOA76FyZjaWBy0akvu8tCQKeQ+d7wsy5zLpz1FlzU3kW1QP+x40ApWgWAySEJTv6/NitNMkllcTakwCaZZ5ADEf6cROas/RhYVQps5igEpkZLwzRROmG04OjDBcj7+Js+vYQDo9e0uH1qzeY5/s1vtaaqG969+vTTrsmBTMLLv12nuy7l+d5W673SBzxkzlfhPdWSXokdZMkSFWhuUDzTTtOnk6CuG2fBEwI9etrHXOmRLJUE0/vMH14In5vH30sCS4Nkr+WmARdztHQ6Jr02dUFPtJ/lyxUVgq6/UzyO1olSj9jc+0DcaWxe/fqab/UT51Uu7Znjw6lbUn5QWtR6vtJQM//4zPUt+NOw+lGzCqo/gLm1QS8)

[Try it in the Playground](https://play.vuejs.org/#eNqNVNtq20AQ/ZWpQnECujhO0qaqY+hD25fQl4RCifKwllbKktXushcT1/W/d1bSSnYJNCCEZmbPmcuZ1S76olS6cTTKo6UpNVN2VQjWKqktfCOi3N4yY6HWsoVZmo0eD5kVAqAQ9KU7XNGaOG5h572lRAZBhTV574CJzJv7QuCzzMaMaFjaKk4sRQtgOeUmiiVO85siwncRQa6oThRpKHrO50XUnUdEwMMJw08M7mAtq20MzlAtSEtj4OyZGkweMIiq2AZKToxBgMcdxDCqVrueBfb7ZaaOQiOspZYgbL0FPBySIQD+eMeQc99/HJIsM0weqs+O258mjfZREE1jt5yCKaWiFXpSX0A/5loKmxj2m+YwT69p+7kXg0udw8nlYn19fYGufvSeZBXF0ZGmR2vwmrJKS4WiPswGWWYxzIIgs8fYH6mIJadnQXdNrdMiWAB+yJ7gsXdgLfjqcK10wtJqgmYZ+spnpGgl6up5oaa2fGKi6U8Yau9ZS6Wzpwi7WU1p7BMzaZcLbuBh0q2XM4fZXTc+uOPSGvjuWEWxlaAexr9uiIBf0qG3Uy6HxXwo9B+mn47CvbNSM+LHccDxAyvmjMA9Vdxh1WQiO0eywBVGEaN3Pj972wVxPKwOZ7BJWI2b+K5rOOVUNPbpYJNvJalwZmmahm3j7AhdSz3sPzDRS3R4SQwOCXxP4yVBzJqJarSzcY8H5mXWFfif1QVwPGjGcQWTLp7YrcLxCfyDdAuMW0cq30AOV+plcK1J+dxoXJkqR6igRCeNxjbxp3N6cX5V0Sb2K19dfFrA4uo9Gh8uP9K6Puvw3eyx9SH3IT/qPCZpiW6Y8Gq9mvekrutAN96o/V99ALPj)

### Renderless Components [​](#renderless-components)

The `` use case we discussed above encapsulates both reusable logic (data fetching, pagination etc.) and visual output, while delegating part of the visual output to the consumer component via scoped slots.

If we push this concept a bit further, we can come up with components that only encapsulate logic and do not render anything by themselves \- visual output is fully delegated to the consumer component with scoped slots. We call this type of component a **Renderless Component**.

An example renderless component could be one that encapsulates the logic of tracking the current mouse position:

template\`\`\`
\
 Mouse is at: {{ x }}, {{ y }}
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqNUcFqhDAQ/ZUhF12w2rO4Cz301t5aaCEX0dki1SQko6uI/96J7i4qLPQQmHmZ9+Y9ZhQvxsRdiyIVmStsZQgcUmtOUlWN0ZbgXbcOP2xe/KKFs9UNBHGyBj09kCpLFj4zuSFsTJ0T+o6yjUb35GpNRylG6CMYYJKCpwAkzWNQOcgphZG/YZoiX/DQNAttFjMrS+6LRCT2rh6HGsHiOQKtmKIIS19+qmZpYLrmXIKxM1Vo5Yj9HD0vfD7ckGGF3LDWlOyHP/idYPQCfdzldTtjscl/8MuDww78lsqHVHdTYXjwCpdKlfoS52X52qGit8oRKrRhwHYdNrrDILouPbCNVZCtgJ1n/6Xx8JYAmT8epD3fr5cC0oGLQYpkd4zpD27R0vA=)

[Try it in the Playground](https://play.vuejs.org/#eNqVUU1rwzAM/SvCl7SQJTuHdLDDbttthw18MbW6hjW2seU0oeS/T0lounQfUDBGepaenvxO4tG5rIkoClGGra8cPUhT1c56ghcbA756tf1EDztva0iy/Ds4NCbSAEiD7diicafigeA0oFvLPAYNhWICYEE5IL00fMp8Hs0JYe0OinDIqFyIaO7CwdJGihO0KXTcLriK59NYBlUARTyMn6Hv0yHgIp7ARAvl3FXm8yCRiuu1Fv/x23JakVqtz3t5pOjNOQNoC7hPz0nHyRSzEr7Ghxppb/XlZ6JjRlzhTAlA+ypkLWwAM6c+8G2BdzP+/pPbRkOoL/KOldH2mCmtnxr247kKhAb9KuHKgLVtMEkn2knG+sIVzV9sfmy8hfB/swHKwV0oWja4lQKKjoNOivzKrf4L/JPqaQ==)

While an interesting pattern, most of what can be achieved with Renderless Components can be achieved in a more efficient fashion with Composition API, without incurring the overhead of extra component nesting. Later, we will see how we can implement the same mouse tracking functionality as a [Composable](/guide/reusability/composables).

That said, scoped slots are still useful in cases where we need to both encapsulate logic **and** compose visual output, like in the `` example.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/slots.md)



## Async Components | Vue.js

[Read the full article](https://vuejs.org/guide/components/async)

# Async Components [​](#async-components)

## Basic Usage [​](#basic-usage)

In large applications, we may need to divide the app into smaller chunks and only load a component from the server when it's needed. To make that possible, Vue has a [`defineAsyncComponent`](/api/general#defineasynccomponent) function:

js\`\`\`
import { defineAsyncComponent } from 'vue'

const AsyncComp = defineAsyncComponent(() =\> {
 return new Promise((resolve, reject) =\> {
 // ...load component from server
 resolve(/\* loaded component \*/)
 })
})
// ... use \`AsyncComp\` like a normal component
\`\`\`As you can see, `defineAsyncComponent` accepts a loader function that returns a Promise. The Promise's `resolve` callback should be called when you have retrieved your component definition from the server. You can also call `reject(reason)` to indicate the load has failed.

[ES module dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import) also returns a Promise, so most of the time we will use it in combination with `defineAsyncComponent`. Bundlers like Vite and webpack also support the syntax (and will use it as bundle split points), so we can use it to import Vue SFCs:

js\`\`\`
import { defineAsyncComponent } from 'vue'

const AsyncComp = defineAsyncComponent(() =\>
 import('./components/MyComponent.vue')
)
\`\`\`The resulting `AsyncComp` is a wrapper component that only calls the loader function when it is actually rendered on the page. In addition, it will pass along any props and slots to the inner component, so you can use the async wrapper to seamlessly replace the original component while achieving lazy loading.

As with normal components, async components can be [registered globally](/guide/components/registration#global-registration) using `app.component()`:

js\`\`\`
app.component('MyComponent', defineAsyncComponent(() =\>
 import('./components/MyComponent.vue')
))
\`\`\`You can also use `defineAsyncComponent` when [registering a component locally](/guide/components/registration#local-registration):

vue\`\`\`
\
import { defineAsyncComponent } from 'vue'

export default {
 components: {
 AdminPage: defineAsyncComponent(() =\>
 import('./components/AdminPageComponent.vue')
 )
 }
}
\

\
 \
\
\`\`\`They can also be defined directly inside their parent component:

vue\`\`\`
\
import { defineAsyncComponent } from 'vue'

const AdminPage = defineAsyncComponent(() =\>
 import('./components/AdminPageComponent.vue')
)
\

\
 \
\
\`\`\`## Loading and Error States [​](#loading-and-error-states)

Asynchronous operations inevitably involve loading and error states \- `defineAsyncComponent()` supports handling these states via advanced options:

js\`\`\`
const AsyncComp = defineAsyncComponent({
 // the loader function
 loader: () =\> import('./Foo.vue'),

 // A component to use while the async component is loading
 loadingComponent: LoadingComponent,
 // Delay before showing the loading component. Default: 200ms.
 delay: 200,

 // A component to use if the load fails
 errorComponent: ErrorComponent,
 // The error component will be displayed if a timeout is
 // provided and exceeded. Default: Infinity.
 timeout: 3000
})
\`\`\`If a loading component is provided, it will be displayed first while the inner component is being loaded. There is a default 200ms delay before the loading component is shown \- this is because on fast networks, an instant loading state may get replaced too fast and end up looking like a flicker.

If an error component is provided, it will be displayed when the Promise returned by the loader function is rejected. You can also specify a timeout to show the error component when the request is taking too long.

## Lazy Hydration  [​](#lazy-hydration)

> This section only applies if you are using [Server\-Side Rendering](/guide/scaling-up/ssr).

In Vue 3\.5\+, async components can control when they are hydrated by providing a hydration strategy.

* Vue provides a number of built\-in hydration strategies. These built\-in strategies need to be individually imported so they can be tree\-shaken if not used.
* The design is intentionally low\-level for flexibility. Compiler syntax sugar can potentially be built on top of this in the future either in core or in higher level solutions (e.g. Nuxt).

### Hydrate on Idle [​](#hydrate-on-idle)

Hydrates via `requestIdleCallback`:

js\`\`\`
import { defineAsyncComponent, hydrateOnIdle } from 'vue'

const AsyncComp = defineAsyncComponent({
 loader: () =\> import('./Comp.vue'),
 hydrate: hydrateOnIdle(/\* optionally pass a max timeout \*/)
})
\`\`\`### Hydrate on Visible [​](#hydrate-on-visible)

Hydrate when element(s) become visible via `IntersectionObserver`.

js\`\`\`
import { defineAsyncComponent, hydrateOnVisible } from 'vue'

const AsyncComp = defineAsyncComponent({
 loader: () =\> import('./Comp.vue'),
 hydrate: hydrateOnVisible()
})
\`\`\`Can optionally pass in an options object value for the observer:

js\`\`\`
hydrateOnVisible({ rootMargin: '100px' })
\`\`\`### Hydrate on Media Query [​](#hydrate-on-media-query)

Hydrates when the specified media query matches.

js\`\`\`
import { defineAsyncComponent, hydrateOnMediaQuery } from 'vue'

const AsyncComp = defineAsyncComponent({
 loader: () =\> import('./Comp.vue'),
 hydrate: hydrateOnMediaQuery('(max\-width:500px)')
})
\`\`\`### Hydrate on Interaction [​](#hydrate-on-interaction)

Hydrates when specified event(s) are triggered on the component element(s). The event that triggered the hydration will also be replayed once hydration is complete.

js\`\`\`
import { defineAsyncComponent, hydrateOnInteraction } from 'vue'

const AsyncComp = defineAsyncComponent({
 loader: () =\> import('./Comp.vue'),
 hydrate: hydrateOnInteraction('click')
})
\`\`\`Can also be a list of multiple event types:

js\`\`\`
hydrateOnInteraction(\['wheel', 'mouseover'])
\`\`\`### Custom Strategy [​](#custom-strategy)

ts\`\`\`
import { defineAsyncComponent, type HydrationStrategy } from 'vue'

const myStrategy: HydrationStrategy = (hydrate, forEachElement) =\> {
 // forEachElement is a helper to iterate through all the root elements
 // in the component's non\-hydrated DOM, since the root can be a fragment
 // instead of a single element
 forEachElement(el =\> {
 // ...
 })
 // call \`hydrate\` when ready
 hydrate()
 return () =\> {
 // return a teardown function if needed
 }
}

const AsyncComp = defineAsyncComponent({
 loader: () =\> import('./Comp.vue'),
 hydrate: myStrategy
})
\`\`\`## Using with Suspense [​](#using-with-suspense)

Async components can be used with the `` built\-in component. The interaction between `` and async components is documented in the [dedicated chapter for ``](/guide/built-ins/suspense).

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/async.md)



## Security | Vue.js

[Read the full article](https://vuejs.org/guide/best-practices/security)

# Security [​](#security)

## Reporting Vulnerabilities [​](#reporting-vulnerabilities)

When a vulnerability is reported, it immediately becomes our top concern, with a full\-time contributor dropping everything to work on it. To report a vulnerability, please email [security@vuejs.org](mailto:security@vuejs.org).

While the discovery of new vulnerabilities is rare, we also recommend always using the latest versions of Vue and its official companion libraries to ensure your application remains as secure as possible.

## Rule No.1: Never Use Non\-trusted Templates [​](#rule-no-1-never-use-non-trusted-templates)

The most fundamental security rule when using Vue is **never use non\-trusted content as your component template**. Doing so is equivalent to allowing arbitrary JavaScript execution in your application \- and worse, could lead to server breaches if the code is executed during server\-side rendering. An example of such usage:

js\`\`\`
Vue.createApp({
 template: \`\\` \+ userProvidedString \+ \`\\` // NEVER DO THIS
}).mount('\#app')
\`\`\`Vue templates are compiled into JavaScript, and expressions inside templates will be executed as part of the rendering process. Although the expressions are evaluated against a specific rendering context, due to the complexity of potential global execution environments, it is impractical for a framework like Vue to completely shield you from potential malicious code execution without incurring unrealistic performance overhead. The most straightforward way to avoid this category of problems altogether is to make sure the contents of your Vue templates are always trusted and entirely controlled by you.

## What Vue Does to Protect You [​](#what-vue-does-to-protect-you)

### HTML content [​](#html-content)

Whether using templates or render functions, content is automatically escaped. That means in this template:

template\`\`\`
\{{ userProvidedString }}\
\`\`\`if `userProvidedString` contained:

js\`\`\`
'\alert("hi")\'
\`\`\`then it would be escaped to the following HTML:

template\`\`\`
\<script\>alert(\&quot;hi\&quot;)\</script\>
\`\`\`thus preventing the script injection. This escaping is done using native browser APIs, like `textContent`, so a vulnerability can only exist if the browser itself is vulnerable.

### Attribute bindings [​](#attribute-bindings)

Similarly, dynamic attribute bindings are also automatically escaped. That means in this template:

template\`\`\`
\
 hello
\
\`\`\`if `userProvidedString` contained:

js\`\`\`
'" onclick="alert(\\'hi\\')'
\`\`\`then it would be escaped to the following HTML:

template\`\`\`
\&quot; onclick=\&quot;alert('hi')
\`\`\`thus preventing the close of the `title` attribute to inject new, arbitrary HTML. This escaping is done using native browser APIs, like `setAttribute`, so a vulnerability can only exist if the browser itself is vulnerable.

## Potential Dangers [​](#potential-dangers)

In any web application, allowing unsanitized, user\-provided content to be executed as HTML, CSS, or JavaScript is potentially dangerous, so it should be avoided wherever possible. There are times when some risk may be acceptable, though.

For example, services like CodePen and JSFiddle allow user\-provided content to be executed, but it's in a context where this is expected and sandboxed to some extent inside iframes. In the cases when an important feature inherently requires some level of vulnerability, it's up to your team to weigh the importance of the feature against the worst\-case scenarios the vulnerability enables.

### HTML Injection [​](#html-injection)

As you learned earlier, Vue automatically escapes HTML content, preventing you from accidentally injecting executable HTML into your application. However, **in cases where you know the HTML is safe**, you can explicitly render HTML content:

* Using a template:

template\`\`\`
\\
\`\`\`
* Using a render function:

js\`\`\`
h('div', {
 innerHTML: this.userProvidedHtml
})
\`\`\`
* Using a render function with JSX:

jsx\`\`\`
\\
\`\`\`

WARNING

User\-provided HTML can never be considered 100% safe unless it's in a sandboxed iframe or in a part of the app where only the user who wrote that HTML can ever be exposed to it. Additionally, allowing users to write their own Vue templates brings similar dangers.

### URL Injection [​](#url-injection)

In a URL like this:

template\`\`\`
\
 click me
\
\`\`\`There's a potential security issue if the URL has not been "sanitized" to prevent JavaScript execution using `javascript:`. There are libraries such as [sanitize\-url](https://www.npmjs.com/package/@braintree/sanitize-url) to help with this, but note: if you're ever doing URL sanitization on the frontend, you already have a security issue. **User\-provided URLs should always be sanitized by your backend before even being saved to a database.** Then the problem is avoided for *every* client connecting to your API, including native mobile apps. Also note that even with sanitized URLs, Vue cannot help you guarantee that they lead to safe destinations.

### Style Injection [​](#style-injection)

Looking at this example:

template\`\`\`
\
 click me
\
\`\`\`Let's assume that `sanitizedUrl` has been sanitized, so that it's definitely a real URL and not JavaScript. With the `userProvidedStyles`, malicious users could still provide CSS to "click jack", e.g. styling the link into a transparent box over the "Log in" button. Then if `https://user-controlled-website.com/` is built to resemble the login page of your application, they might have just captured a user's real login information.

You may be able to imagine how allowing user\-provided content for a `` element would create an even greater vulnerability, giving that user full control over how to style the entire page. That's why Vue prevents rendering of style tags inside templates, such as:

template\`\`\`
\{{ userProvidedStyles }}\
\`\`\`To keep your users fully safe from clickjacking, we recommend only allowing full control over CSS inside a sandboxed iframe. Alternatively, when providing user control through a style binding, we recommend using its [object syntax](/guide/essentials/class-and-style#binding-to-objects-1) and only allowing users to provide values for specific properties it's safe for them to control, like this:

template\`\`\`
\
 click me
\
\`\`\`### JavaScript Injection [​](#javascript-injection)

We strongly discourage ever rendering a `` element with Vue, since templates and render functions should never have side effects. However, this isn't the only way to include strings that would be evaluated as JavaScript at runtime.

Every HTML element has attributes with values accepting strings of JavaScript, such as `onclick`, `onfocus`, and `onmouseenter`. Binding user\-provided JavaScript to any of these event attributes is a potential security risk, so it should be avoided.

WARNING

User\-provided JavaScript can never be considered 100% safe unless it's in a sandboxed iframe or in a part of the app where only the user who wrote that JavaScript can ever be exposed to it.

Sometimes we receive vulnerability reports on how it's possible to do cross\-site scripting (XSS) in Vue templates. In general, we do not consider such cases to be actual vulnerabilities because there's no practical way to protect developers from the two scenarios that would allow XSS:

1. The developer is explicitly asking Vue to render user\-provided, unsanitized content as Vue templates. This is inherently unsafe, and there's no way for Vue to know the origin.
2. The developer is mounting Vue to an entire HTML page which happens to contain server\-rendered and user\-provided content. This is fundamentally the same problem as \#1, but sometimes devs may do it without realizing it. This can lead to possible vulnerabilities where the attacker provides HTML which is safe as plain HTML but unsafe as a Vue template. The best practice is to **never mount Vue on nodes that may contain server\-rendered and user\-provided content**.

## Best Practices [​](#best-practices)

The general rule is that if you allow unsanitized, user\-provided content to be executed (as either HTML, JavaScript, or even CSS), you might open yourself up to attacks. This advice actually holds true whether using Vue, another framework, or even no framework.

Beyond the recommendations made above for [Potential Dangers](#potential-dangers), we also recommend familiarizing yourself with these resources:

* [HTML5 Security Cheat Sheet](https://html5sec.org/)
* [OWASP's Cross Site Scripting (XSS) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

Then use what you learn to also review the source code of your dependencies for potentially dangerous patterns, if any of them include 3rd\-party components or otherwise influence what's rendered to the DOM.

## Backend Coordination [​](#backend-coordination)

HTTP security vulnerabilities, such as cross\-site request forgery (CSRF/XSRF) and cross\-site script inclusion (XSSI), are primarily addressed on the backend, so they aren't a concern of Vue's. However, it's still a good idea to communicate with your backend team to learn how to best interact with their API, e.g., by submitting CSRF tokens with form submissions.

## Server\-Side Rendering (SSR) [​](#server-side-rendering-ssr)

There are some additional security concerns when using SSR, so make sure to follow the best practices outlined throughout [our SSR documentation](/guide/scaling-up/ssr) to avoid vulnerabilities.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/best-practices/security.md)



## Built-in Special Elements | Vue.js

[Read the full article](https://vuejs.org/api/built-in-special-elements)

# Built\-in Special Elements [​](#built-in-special-elements)

Not Components

``, `` and `` are component\-like features and part of the template syntax. They are not true components and are compiled away during template compilation. As such, they are conventionally written with lowercase in templates.

## `` [​](#component)

A "meta component" for rendering dynamic components or elements.

* **Props**

ts\`\`\`
interface DynamicComponentProps {
 is: string \| Component
}
\`\`\`
* **Details**

The actual component to render is determined by the `is` prop.

	+ When `is` is a string, it could be either an HTML tag name or a component's registered name.
	+ Alternatively, `is` can also be directly bound to the definition of a component.
* **Example**

Rendering components by registered name (Options API):

vue\`\`\`
\
import Foo from './Foo.vue'
import Bar from './Bar.vue'

export default {
 components: { Foo, Bar },
 data() {
 return {
 view: 'Foo'
 }
 }
}
\

\
 \
\
\`\`\`Rendering components by definition (Composition API with ``):

vue\`\`\`
\
import Foo from './Foo.vue'
import Bar from './Bar.vue'
\

\
 \ 0\.5 ? Foo : Bar" /\>
\
\`\`\`Rendering HTML elements:

template\`\`\`
\\
\`\`\`The [built\-in components](/api/built-in-components) can all be passed to `is`, but you must register them if you want to pass them by name. For example:

vue\`\`\`
\
import { Transition, TransitionGroup } from 'vue'

export default {
 components: {
 Transition,
 TransitionGroup
 }
}
\

\
 \
 ...
 \
\
\`\`\`Registration is not required if you pass the component itself to `is` rather than its name, e.g. in ``.

If `v-model` is used on a `` tag, the template compiler will expand it to a `modelValue` prop and `update:modelValue` event listener, much like it would for any other component. However, this won't be compatible with native HTML elements, such as `` or ``. As a result, using `v-model` with a dynamically created native element won't work:

vue\`\`\`
\
import { ref } from 'vue'

const tag = ref('input')
const username = ref('')
\

\
 \
 \
\
\`\`\`In practice, this edge case isn't common as native form fields are typically wrapped in components in real applications. If you do need to use a native element directly then you can split the `v-model` into an attribute and event manually.
* **See also** [Dynamic Components](/guide/essentials/component-basics#dynamic-components)

## `` [​](#slot)

Denotes slot content outlets in templates.

* **Props**

ts\`\`\`
interface SlotProps {
 /\*\*
 \* Any props passed to \ to passed as arguments
 \* for scoped slots
 \*/
 \[key: string]: any
 /\*\*
 \* Reserved for specifying slot name.
 \*/
 name?: string
}
\`\`\`
* **Details**

The `` element can use the `name` attribute to specify a slot name. When no `name` is specified, it will render the default slot. Additional attributes passed to the slot element will be passed as slot props to the scoped slot defined in the parent.

The element itself will be replaced by its matched slot content.

`` elements in Vue templates are compiled into JavaScript, so they are not to be confused with [native `` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot).
* **See also** [Component \- Slots](/guide/components/slots)

## `` [​](#template)

The `` tag is used as a placeholder when we want to use a built\-in directive without rendering an element in the DOM.

* **Details**

The special handling for `` is only triggered if it is used with one of these directives:

	+ `v-if`, `v-else-if`, or `v-else`
	+ `v-for`
	+ `v-slot`If none of those directives are present then it will be rendered as a [native `` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) instead.

A `` with a `v-for` can also have a [`key` attribute](/api/built-in-special-attributes#key). All other attributes and directives will be discarded, as they aren't meaningful without a corresponding element.

Single\-file components use a [top\-level `` tag](/api/sfc-spec#language-blocks) to wrap the entire template. That usage is separate from the use of `` described above. That top\-level tag is not part of the template itself and doesn't support template syntax, such as directives.
* **See also**

	+ [Guide \- `v-if` on ``](/guide/essentials/conditional#v-if-on-template)
	+ [Guide \- `v-for` on ``](/guide/essentials/list#v-for-on-template)
	+ [Guide \- Named slots](/guide/components/slots#named-slots)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/built-in-special-elements.md)



## TypeScript with Options API | Vue.js

[Read the full article](https://vuejs.org/guide/typescript/options-api)

# TypeScript with Options API [​](#typescript-with-options-api)

> This page assumes you've already read the overview on [Using Vue with TypeScript](/guide/typescript/overview).

TIP

While Vue does support TypeScript usage with Options API, it is recommended to use Vue with TypeScript via Composition API as it offers simpler, more efficient and more robust type inference.

## Typing Component Props [​](#typing-component-props)

Type inference for props in Options API requires wrapping the component with `defineComponent()`. With it, Vue is able to infer the types for the props based on the `props` option, taking additional options such as `required: true` and `default` into account:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 // type inference enabled
 props: {
 name: String,
 id: \[Number, String],
 msg: { type: String, required: true },
 metadata: null
 },
 mounted() {
 this.name // type: string \| undefined
 this.id // type: number \| string \| undefined
 this.msg // type: string
 this.metadata // type: any
 }
})
\`\`\`However, the runtime `props` options only support using constructor functions as a prop's type \- there is no way to specify complex types such as objects with nested properties or function call signatures.

To annotate complex props types, we can use the `PropType` utility type:

ts\`\`\`
import { defineComponent } from 'vue'
import type { PropType } from 'vue'

interface Book {
 title: string
 author: string
 year: number
}

export default defineComponent({
 props: {
 book: {
 // provide more specific type to \`Object\`
 type: Object as PropType\,
 required: true
 },
 // can also annotate functions
 callback: Function as PropType\ void\>
 },
 mounted() {
 this.book.title // string
 this.book.year // number

 // TS Error: argument of type 'string' is not
 // assignable to parameter of type 'number'
 this.callback?.('123')
 }
})
\`\`\`### Caveats [​](#caveats)

If your TypeScript version is less than `4.7`, you have to be careful when using function values for `validator` and `default` prop options \- make sure to use arrow functions:

ts\`\`\`
import { defineComponent } from 'vue'
import type { PropType } from 'vue'

interface Book {
 title: string
 year?: number
}

export default defineComponent({
 props: {
 bookA: {
 type: Object as PropType\,
 // Make sure to use arrow functions if your TypeScript version is less than 4\.7
 default: () =\> ({
 title: 'Arrow Function Expression'
 }),
 validator: (book: Book) =\> !!book.title
 }
 }
})
\`\`\`This prevents TypeScript from having to infer the type of `this` inside these functions, which, unfortunately, can cause the type inference to fail. It was a previous [design limitation](https://github.com/microsoft/TypeScript/issues/38845), and now has been improved in [TypeScript 4\.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-7.html#improved-function-inference-in-objects-and-methods).

## Typing Component Emits [​](#typing-component-emits)

We can declare the expected payload type for an emitted event using the object syntax of the `emits` option. Also, all non\-declared emitted events will throw a type error when called:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 emits: {
 addBook(payload: { bookName: string }) {
 // perform runtime validation
 return payload.bookName.length \> 0
 }
 },
 methods: {
 onSubmit() {
 this.$emit('addBook', {
 bookName: 123 // Type error!
 })

 this.$emit('non\-declared\-event') // Type error!
 }
 }
})
\`\`\`## Typing Computed Properties [​](#typing-computed-properties)

A computed property infers its type based on its return value:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 data() {
 return {
 message: 'Hello!'
 }
 },
 computed: {
 greeting() {
 return this.message \+ '!'
 }
 },
 mounted() {
 this.greeting // type: string
 }
})
\`\`\`In some cases, you may want to explicitly annotate the type of a computed property to ensure its implementation is correct:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 data() {
 return {
 message: 'Hello!'
 }
 },
 computed: {
 // explicitly annotate return type
 greeting(): string {
 return this.message \+ '!'
 },

 // annotating a writable computed property
 greetingUppercased: {
 get(): string {
 return this.greeting.toUpperCase()
 },
 set(newValue: string) {
 this.message = newValue.toUpperCase()
 }
 }
 }
})
\`\`\`Explicit annotations may also be required in some edge cases where TypeScript fails to infer the type of a computed property due to circular inference loops.

## Typing Event Handlers [​](#typing-event-handlers)

When dealing with native DOM events, it might be useful to type the argument we pass to the handler correctly. Let's take a look at this example:

vue\`\`\`
\
import { defineComponent } from 'vue'

export default defineComponent({
 methods: {
 handleChange(event) {
 // \`event\` implicitly has \`any\` type
 console.log(event.target.value)
 }
 }
})
\

\
 \
\
\`\`\`Without type annotation, the `event` argument will implicitly have a type of `any`. This will also result in a TS error if `"strict": true` or `"noImplicitAny": true` are used in `tsconfig.json`. It is therefore recommended to explicitly annotate the argument of event handlers. In addition, you may need to use type assertions when accessing the properties of `event`:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 methods: {
 handleChange(event: Event) {
 console.log((event.target as HTMLInputElement).value)
 }
 }
})
\`\`\`## Augmenting Global Properties [​](#augmenting-global-properties)

Some plugins install globally available properties to all component instances via [`app.config.globalProperties`](/api/application#app-config-globalproperties). For example, we may install `this.$http` for data\-fetching or `this.$translate` for internationalization. To make this play well with TypeScript, Vue exposes a `ComponentCustomProperties` interface designed to be augmented via [TypeScript module augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation):

ts\`\`\`
import axios from 'axios'

declare module 'vue' {
 interface ComponentCustomProperties {
 $http: typeof axios
 $translate: (key: string) =\> string
 }
}
\`\`\`See also:

* [TypeScript unit tests for component type extensions](https://github.com/vuejs/core/blob/main/packages-private/dts-test/componentTypeExtensions.test-d.tsx)

### Type Augmentation Placement [​](#type-augmentation-placement)

We can put this type augmentation in a `.ts` file, or in a project\-wide `*.d.ts` file. Either way, make sure it is included in `tsconfig.json`. For library / plugin authors, this file should be specified in the `types` property in `package.json`.

In order to take advantage of module augmentation, you will need to ensure the augmentation is placed in a [TypeScript module](https://www.typescriptlang.org/docs/handbook/modules.html). That is to say, the file needs to contain at least one top\-level `import` or `export`, even if it is just `export {}`. If the augmentation is placed outside of a module, it will overwrite the original types rather than augmenting them!

ts\`\`\`
// Does not work, overwrites the original types.
declare module 'vue' {
 interface ComponentCustomProperties {
 $translate: (key: string) =\> string
 }
}
\`\`\`ts\`\`\`
// Works correctly
export {}

declare module 'vue' {
 interface ComponentCustomProperties {
 $translate: (key: string) =\> string
 }
}
\`\`\`## Augmenting Custom Options [​](#augmenting-custom-options)

Some plugins, for example `vue-router`, provide support for custom component options such as `beforeRouteEnter`:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 beforeRouteEnter(to, from, next) {
 // ...
 }
})
\`\`\`Without proper type augmentation, the arguments of this hook will implicitly have `any` type. We can augment the `ComponentCustomOptions` interface to support these custom options:

ts\`\`\`
import { Route } from 'vue\-router'

declare module 'vue' {
 interface ComponentCustomOptions {
 beforeRouteEnter?(to: Route, from: Route, next: () =\> void): void
 }
}
\`\`\`Now the `beforeRouteEnter` option will be properly typed. Note this is just an example \- well\-typed libraries like `vue-router` should automatically perform these augmentations in their own type definitions.

The placement of this augmentation is subject to the [same restrictions](#type-augmentation-placement) as global property augmentations.

See also:

* [TypeScript unit tests for component type extensions](https://github.com/vuejs/core/blob/main/packages-private/dts-test/componentTypeExtensions.test-d.tsx)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/typescript/options-api.md)



## Lifecycle Hooks | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/lifecycle)

# Lifecycle Hooks [​](#lifecycle-hooks)

Each Vue component instance goes through a series of initialization steps when it's created \- for example, it needs to set up data observation, compile the template, mount the instance to the DOM, and update the DOM when data changes. Along the way, it also runs functions called lifecycle hooks, giving users the opportunity to add their own code at specific stages.

## Registering Lifecycle Hooks [​](#registering-lifecycle-hooks)

For example, the `onMounted``mounted` hook can be used to run code after the component has finished the initial rendering and created the DOM nodes:

vue\`\`\`
\
import { onMounted } from 'vue'

onMounted(() =\> {
 console.log(\`the component is now mounted.\`)
})
\
\`\`\`js\`\`\`
export default {
 mounted() {
 console.log(\`the component is now mounted.\`)
 }
}
\`\`\`There are also other hooks which will be called at different stages of the instance's lifecycle, with the most commonly used being [`onMounted`](/api/composition-api-lifecycle#onmounted), [`onUpdated`](/api/composition-api-lifecycle#onupdated), and [`onUnmounted`](/api/composition-api-lifecycle#onunmounted).[`mounted`](/api/options-lifecycle#mounted), [`updated`](/api/options-lifecycle#updated), and [`unmounted`](/api/options-lifecycle#unmounted).

All lifecycle hooks are called with their `this` context pointing to the current active instance invoking it. Note this means you should avoid using arrow functions when declaring lifecycle hooks, as you won't be able to access the component instance via `this` if you do so.

When calling `onMounted`, Vue automatically associates the registered callback function with the current active component instance. This requires these hooks to be registered **synchronously** during component setup. For example, do not do this:

js\`\`\`
setTimeout(() =\> {
 onMounted(() =\> {
 // this won't work.
 })
}, 100\)
\`\`\`Do note this doesn't mean that the call must be placed lexically inside `setup()` or ``. `onMounted()` can be called in an external function as long as the call stack is synchronous and originates from within `setup()`.

## Lifecycle Diagram [​](#lifecycle-diagram)

Below is a diagram for the instance lifecycle. You don't need to fully understand everything going on right now, but as you learn and build more, it will be a useful reference.



Consult the [Lifecycle Hooks API reference](/api/composition-api-lifecycle)[Lifecycle Hooks API reference](/api/options-lifecycle) for details on all lifecycle hooks and their respective use cases.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/lifecycle.md)



## Conditional Rendering | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/conditional)

# Conditional Rendering [​](#conditional-rendering)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/conditional-rendering-in-vue-3?friend=vuejs "Free Vue.js Conditional Rendering Lesson")[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-fundamentals-capi-conditionals-in-vue?friend=vuejs "Free Vue.js Conditional Rendering Lesson")## `v-if` [​](#v-if)

The directive `v-if` is used to conditionally render a block. The block will only be rendered if the directive's expression returns a truthy value.

template\`\`\`
\Vue is awesome!\
\`\`\`## `v-else` [​](#v-else)

You can use the `v-else` directive to indicate an "else block" for `v-if`:

template\`\`\`
\Toggle\

\Vue is awesome!\
\Oh no 😢\
\`\`\`Toggle# Vue is awesome!

[Try it in the Playground](https://play.vuejs.org/#eNpFjkEOgjAQRa8ydIMulLA1hegJ3LnqBskAjdA27RQXhHu4M/GEHsEiKLv5mfdf/sBOxux7j+zAuCutNAQOyZtcKNkZbQkGsFjBCJXVHcQBjYUSqtTKERR3dLpDyCZmQ9bjViiezKKgCIGwM21BGBIAv3oireBYtrK8ZYKtgmg5BctJ13WLPJnhr0YQb1Lod7JaS4G8eATpfjMinjTphC8wtg7zcwNKw/v5eC1fnvwnsfEDwaha7w==)

[Try it in the Playground](https://play.vuejs.org/#eNpFjj0OwjAMha9iMsEAFWuVVnACNqYsoXV/RJpEqVOQqt6DDYkTcgRSWoplWX7y56fXs6O1u84jixlvM1dbSoXGuzWOIMdCekXQCw2QS5LrzbQLckje6VEJglDyhq1pMAZyHidkGG9hhObRYh0EYWOVJAwKgF88kdFwyFSdXRPBZidIYDWvgqVkylIhjyb4ayOIV3votnXxfwrk2SPU7S/PikfVfsRnGFWL6akCbeD9fLzmK4+WSGz4AA5dYQY=)

A `v-else` element must immediately follow a `v-if` or a `v-else-if` element \- otherwise it will not be recognized.

## `v-else-if` [​](#v-else-if)

The `v-else-if`, as the name suggests, serves as an "else if block" for `v-if`. It can also be chained multiple times:

template\`\`\`
\
 A
\
\
 B
\
\
 C
\
\
 Not A/B/C
\
\`\`\`Similar to `v-else`, a `v-else-if` element must immediately follow a `v-if` or a `v-else-if` element.

## `v-if` on `` [​](#v-if-on-template)

Because `v-if` is a directive, it has to be attached to a single element. But what if we want to toggle more than one element? In this case we can use `v-if` on a `` element, which serves as an invisible wrapper. The final rendered result will not include the `` element.

template\`\`\`
\
 \Title\
 \Paragraph 1\
 \Paragraph 2\
\
\`\`\``v-else` and `v-else-if` can also be used on ``.

## `v-show` [​](#v-show)

Another option for conditionally displaying an element is the `v-show` directive. The usage is largely the same:

template\`\`\`
\Hello!\
\`\`\`The difference is that an element with `v-show` will always be rendered and remain in the DOM; `v-show` only toggles the `display` CSS property of the element.

`v-show` doesn't support the `` element, nor does it work with `v-else`.

## `v-if` vs. `v-show` [​](#v-if-vs-v-show)

`v-if` is "real" conditional rendering because it ensures that event listeners and child components inside the conditional block are properly destroyed and re\-created during toggles.

`v-if` is also **lazy**: if the condition is false on initial render, it will not do anything \- the conditional block won't be rendered until the condition becomes true for the first time.

In comparison, `v-show` is much simpler \- the element is always rendered regardless of initial condition, with CSS\-based toggling.

Generally speaking, `v-if` has higher toggle costs while `v-show` has higher initial render costs. So prefer `v-show` if you need to toggle something very often, and prefer `v-if` if the condition is unlikely to change at runtime.

## `v-if` with `v-for` [​](#v-if-with-v-for)

When `v-if` and `v-for` are both used on the same element, `v-if` will be evaluated first. See the [list rendering guide](/guide/essentials/list#v-for-with-v-if) for details.

Note

It's **not** recommended to use `v-if` and `v-for` on the same element due to implicit precedence. Refer to [list rendering guide](/guide/essentials/list#v-for-with-v-if) for details.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/conditional.md)



## Component Registration | Vue.js

[Read the full article](https://vuejs.org/guide/components/registration)

# Component Registration [​](#component-registration)

> This page assumes you've already read the [Components Basics](/guide/essentials/component-basics). Read that first if you are new to components.

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-3-global-vs-local-vue-components?friend=vuejs "Free Vue.js Component Registration Lesson")A Vue component needs to be "registered" so that Vue knows where to locate its implementation when it is encountered in a template. There are two ways to register components: global and local.

## Global Registration [​](#global-registration)

We can make components available globally in the current [Vue application](/guide/essentials/application) using the `.component()` method:

js\`\`\`
import { createApp } from 'vue'

const app = createApp({})

app.component(
 // the registered name
 'MyComponent',
 // the implementation
 {
 /\* ... \*/
 }
)
\`\`\`If using SFCs, you will be registering the imported `.vue` files:

js\`\`\`
import MyComponent from './App.vue'

app.component('MyComponent', MyComponent)
\`\`\`The `.component()` method can be chained:

js\`\`\`
app
 .component('ComponentA', ComponentA)
 .component('ComponentB', ComponentB)
 .component('ComponentC', ComponentC)
\`\`\`Globally registered components can be used in the template of any component within this application:

template\`\`\`
\
\
\
\
\`\`\`This even applies to all subcomponents, meaning all three of these components will also be available *inside each other*.

## Local Registration [​](#local-registration)

While convenient, global registration has a few drawbacks:

1. Global registration prevents build systems from removing unused components (a.k.a "tree\-shaking"). If you globally register a component but end up not using it anywhere in your app, it will still be included in the final bundle.
2. Global registration makes dependency relationships less explicit in large applications. It makes it difficult to locate a child component's implementation from a parent component using it. This can affect long\-term maintainability similar to using too many global variables.

Local registration scopes the availability of the registered components to the current component only. It makes the dependency relationship more explicit, and is more tree\-shaking friendly.

When using SFC with ``, imported components can be locally used without registration:

vue\`\`\`
\
import ComponentA from './ComponentA.vue'
\

\
 \
\
\`\`\`In non\-``, you will need to use the `components` option:

js\`\`\`
import ComponentA from './ComponentA.js'

export default {
 components: {
 ComponentA
 },
 setup() {
 // ...
 }
}
\`\`\`Local registration is done using the `components` option:

vue\`\`\`
\
import ComponentA from './ComponentA.vue'

export default {
 components: {
 ComponentA
 }
}
\

\
 \
\
\`\`\`For each property in the `components` object, the key will be the registered name of the component, while the value will contain the implementation of the component. The above example is using the ES2015 property shorthand and is equivalent to:

js\`\`\`
export default {
 components: {
 ComponentA: ComponentA
 }
 // ...
}
\`\`\`Note that **locally registered components are *not* also available in descendant components**. In this case, `ComponentA` will be made available to the current component only, not any of its child or descendant components.

## Component Name Casing [​](#component-name-casing)

Throughout the guide, we are using PascalCase names when registering components. This is because:

1. PascalCase names are valid JavaScript identifiers. This makes it easier to import and register components in JavaScript. It also helps IDEs with auto\-completion.
2. `` makes it more obvious that this is a Vue component instead of a native HTML element in templates. It also differentiates Vue components from custom elements (web components).

This is the recommended style when working with SFC or string templates. However, as discussed in [in\-DOM Template Parsing Caveats](/guide/essentials/component-basics#in-dom-template-parsing-caveats), PascalCase tags are not usable in in\-DOM templates.

Luckily, Vue supports resolving kebab\-case tags to components registered using PascalCase. This means a component registered as `MyComponent` can be referenced inside a Vue template (or inside an HTML element rendered by Vue) via both `` and ``. This allows us to use the same JavaScript component registration code regardless of template source.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/registration.md)



## Custom Directives | Vue.js

[Read the full article](https://vuejs.org/guide/reusability/custom-directives)

# Custom Directives [​](#custom-directives)

## Introduction [​](#introduction)

In addition to the default set of directives shipped in core (like `v-model` or `v-show`), Vue also allows you to register your own custom directives.

We have introduced two forms of code reuse in Vue: [components](/guide/essentials/component-basics) and [composables](/guide/reusability/composables). Components are the main building blocks, while composables are focused on reusing stateful logic. Custom directives, on the other hand, are mainly intended for reusing logic that involves low\-level DOM access on plain elements.

A custom directive is defined as an object containing lifecycle hooks similar to those of a component. The hooks receive the element the directive is bound to. Here is an example of a directive that adds a class to an element when it is inserted into the DOM by Vue:

vue\`\`\`
\
// enables v\-highlight in templates
const vHighlight = {
 mounted: (el) =\> {
 el.classList.add('is\-highlight')
 }
}
\

\
 \This sentence is important!\
\
\`\`\`js\`\`\`
const highlight = {
 mounted: (el) =\> el.classList.add('is\-highlight')
}

export default {
 directives: {
 // enables v\-highlight in template
 highlight
 }
}
\`\`\`template\`\`\`
\This sentence is important!\
\`\`\`This sentence is important!

In ``, any camelCase variable that starts with the `v` prefix can be used as a custom directive. In the example above, `vHighlight` can be used in the template as `v-highlight`.

If you are not using ``, custom directives can be registered using the `directives` option:

js\`\`\`
export default {
 setup() {
 /\*...\*/
 },
 directives: {
 // enables v\-highlight in template
 highlight: {
 /\* ... \*/
 }
 }
}
\`\`\`Similar to components, custom directives must be registered so that they can be used in templates. In the example above, we are using local registration via the `directives` option.

It is also common to globally register custom directives at the app level:

js\`\`\`
const app = createApp({})

// make v\-highlight usable in all components
app.directive('highlight', {
 /\* ... \*/
})
\`\`\`## When to use custom directives [​](#when-to-use)

Custom directives should only be used when the desired functionality can only be achieved via direct DOM manipulation.

A common example of this is a `v-focus` custom directive that brings an element into focus.

vue\`\`\`
\
// enables v\-focus in templates
const vFocus = {
 mounted: (el) =\> el.focus()
}
\

\
 \
\
\`\`\`js\`\`\`
const focus = {
 mounted: (el) =\> el.focus()
}

export default {
 directives: {
 // enables v\-focus in template
 focus
 }
}
\`\`\`template\`\`\`
\
\`\`\`This directive is more useful than the `autofocus` attribute because it works not just on page load \- it also works when the element is dynamically inserted by Vue!

Declarative templating with built\-in directives such as `v-bind` is recommended when possible because they are more efficient and server\-rendering friendly.

## Directive Hooks [​](#directive-hooks)

A directive definition object can provide several hook functions (all optional):

js\`\`\`
const myDirective = {
 // called before bound element's attributes
 // or event listeners are applied
 created(el, binding, vnode) {
 // see below for details on arguments
 },
 // called right before the element is inserted into the DOM.
 beforeMount(el, binding, vnode) {},
 // called when the bound element's parent component
 // and all its children are mounted.
 mounted(el, binding, vnode) {},
 // called before the parent component is updated
 beforeUpdate(el, binding, vnode, prevVnode) {},
 // called after the parent component and
 // all of its children have updated
 updated(el, binding, vnode, prevVnode) {},
 // called before the parent component is unmounted
 beforeUnmount(el, binding, vnode) {},
 // called when the parent component is unmounted
 unmounted(el, binding, vnode) {}
}
\`\`\`### Hook Arguments [​](#hook-arguments)

Directive hooks are passed these arguments:

* `el`: the element the directive is bound to. This can be used to directly manipulate the DOM.
* `binding`: an object containing the following properties.

	+ `value`: The value passed to the directive. For example in `v-my-directive="1 + 1"`, the value would be `2`.
	+ `oldValue`: The previous value, only available in `beforeUpdate` and `updated`. It is available whether or not the value has changed.
	+ `arg`: The argument passed to the directive, if any. For example in `v-my-directive:foo`, the arg would be `"foo"`.
	+ `modifiers`: An object containing modifiers, if any. For example in `v-my-directive.foo.bar`, the modifiers object would be `{ foo: true, bar: true }`.
	+ `instance`: The instance of the component where the directive is used.
	+ `dir`: the directive definition object.
* `vnode`: the underlying VNode representing the bound element.
* `prevVnode`: the VNode representing the bound element from the previous render. Only available in the `beforeUpdate` and `updated` hooks.

As an example, consider the following directive usage:

template\`\`\`
\
\`\`\`The `binding` argument would be an object in the shape of:

js\`\`\`
{
 arg: 'foo',
 modifiers: { bar: true },
 value: /\* value of \`baz\` \*/,
 oldValue: /\* value of \`baz\` from previous update \*/
}
\`\`\`Similar to built\-in directives, custom directive arguments can be dynamic. For example:

template\`\`\`
\\
\`\`\`Here the directive argument will be reactively updated based on `arg` property in our component state.

Note

Apart from `el`, you should treat these arguments as read\-only and never modify them. If you need to share information across hooks, it is recommended to do so through element's [dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset).

## Function Shorthand [​](#function-shorthand)

It's common for a custom directive to have the same behavior for `mounted` and `updated`, with no need for the other hooks. In such cases we can define the directive as a function:

template\`\`\`
\\
\`\`\`js\`\`\`
app.directive('color', (el, binding) =\> {
 // this will be called for both \`mounted\` and \`updated\`
 el.style.color = binding.value
})
\`\`\`## Object Literals [​](#object-literals)

If your directive needs multiple values, you can also pass in a JavaScript object literal. Remember, directives can take any valid JavaScript expression.

template\`\`\`
\\
\`\`\`js\`\`\`
app.directive('demo', (el, binding) =\> {
 console.log(binding.value.color) // =\> "white"
 console.log(binding.value.text) // =\> "hello!"
})
\`\`\`## Usage on Components [​](#usage-on-components)

Not recommended

Using custom directives on components is not recommended. Unexpected behaviour may occur when a component has multiple root nodes.

When used on components, custom directives will always apply to a component's root node, similar to [Fallthrough Attributes](/guide/components/attrs).

template\`\`\`
\
\`\`\`template\`\`\`
\

\ \
 \My component content\
\
\`\`\`Note that components can potentially have more than one root node. When applied to a multi\-root component, a directive will be ignored and a warning will be thrown. Unlike attributes, directives can't be passed to a different element with `v-bind="$attrs"`.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/reusability/custom-directives.md)



## Testing | Vue.js

[Read the full article](https://vuejs.org/guide/scaling-up/testing)

# Testing [​](#testing)

## Why Test? [​](#why-test)

Automated tests help you and your team build complex Vue applications quickly and confidently by preventing regressions and encouraging you to break apart your application into testable functions, modules, classes, and components. As with any application, your new Vue app can break in many ways, and it's important that you can catch these issues and fix them before releasing.

In this guide, we'll cover basic terminology and provide our recommendations on which tools to choose for your Vue 3 application.

There is one Vue\-specific section covering composables. See [Testing Composables](#testing-composables) below for more details.

## When to Test [​](#when-to-test)

Start testing early! We recommend you begin writing tests as soon as you can. The longer you wait to add tests to your application, the more dependencies your application will have, and the harder it will be to start.

## Testing Types [​](#testing-types)

When designing your Vue application's testing strategy, you should leverage the following testing types:

* **Unit**: Checks that inputs to a given function, class, or composable are producing the expected output or side effects.
* **Component**: Checks that your component mounts, renders, can be interacted with, and behaves as expected. These tests import more code than unit tests, are more complex, and require more time to execute.
* **End\-to\-end**: Checks features that span multiple pages and makes real network requests against your production\-built Vue application. These tests often involve standing up a database or other backend.

Each testing type plays a role in your application's testing strategy, and each will protect you against different types of issues.

## Overview [​](#overview)

We will briefly discuss what each of these are, how they can be implemented for Vue applications, and provide some general recommendations.

## Unit Testing [​](#unit-testing)

Unit tests are written to verify that small, isolated units of code are working as expected. A unit test usually covers a single function, class, composable, or module. Unit tests focus on logical correctness and only concern themselves with a small portion of the application's overall functionality. They may mock large parts of your application's environment (e.g. initial state, complex classes, 3rd party modules, and network requests).

In general, unit tests will catch issues with a function's business logic and logical correctness.

Take for example this `increment` function:

js\`\`\`
// helpers.js
export function increment(current, max = 10\) {
 if (current \ {
 test('increments the current number by 1', () =\> {
 expect(increment(0, 10\)).toBe(1\)
 })

 test('does not increment the current number over the max', () =\> {
 expect(increment(10, 10\)).toBe(10\)
 })

 test('has a default max of 10', () =\> {
 expect(increment(10\)).toBe(10\)
 })
})
\`\`\`As mentioned previously, unit testing is typically applied to self\-contained business logic, components, classes, modules, or functions that do not involve UI rendering, network requests, or other environmental concerns.

These are typically plain JavaScript / TypeScript modules unrelated to Vue. In general, writing unit tests for business logic in Vue applications does not differ significantly from applications using other frameworks.

There are two instances where you DO unit test Vue\-specific features:

1. Composables
2. Components

### Composables [​](#composables)

One category of functions specific to Vue applications is [Composables](/guide/reusability/composables), which may require special handling during tests. See [Testing Composables](#testing-composables) below for more details.

### Unit Testing Components [​](#unit-testing-components)

A component can be tested in two ways:

1. Whitebox: Unit Testing

Tests that are "Whitebox tests" are aware of the implementation details and dependencies of a component. They are focused on **isolating** the component under test. These tests will usually involve mocking some, if not all of your component's children, as well as setting up plugin state and dependencies (e.g. Pinia).
2. Blackbox: Component Testing

Tests that are "Blackbox tests" are unaware of the implementation details of a component. These tests mock as little as possible to test the integration of your component and the entire system. They usually render all child components and are considered more of an "integration test". See the [Component Testing recommendations](#component-testing) below.

### Recommendation [​](#recommendation)

* [Vitest](https://vitest.dev/)

Since the official setup created by `create-vue` is based on [Vite](https://vitejs.dev/), we recommend using a unit testing framework that can leverage the same configuration and transform pipeline directly from Vite. [Vitest](https://vitest.dev/) is a unit testing framework designed specifically for this purpose, created and maintained by Vue / Vite team members. It integrates with Vite\-based projects with minimal effort, and is blazing fast.

### Other Options [​](#other-options)

* [Jest](https://jestjs.io/) is a popular unit testing framework. However, we only recommend Jest if you have an existing Jest test suite that needs to be migrated over to a Vite\-based project, as Vitest offers a more seamless integration and better performance.

## Component Testing [​](#component-testing)

In Vue applications, components are the main building blocks of the UI. Components are therefore the natural unit of isolation when it comes to validating your application's behavior. From a granularity perspective, component testing sits somewhere above unit testing and can be considered a form of integration testing. Much of your Vue Application should be covered by a component test and we recommend that each Vue component has its own spec file.

Component tests should catch issues relating to your component's props, events, slots that it provides, styles, classes, lifecycle hooks, and more.

Component tests should not mock child components, but instead test the interactions between your component and its children by interacting with the components as a user would. For example, a component test should click on an element like a user would instead of programmatically interacting with the component.

Component tests should focus on the component's public interfaces rather than internal implementation details. For most components, the public interface is limited to: events emitted, props, and slots. When testing, remember to **test what a component does, not how it does it**.

**DO**

* For **Visual** logic: assert correct render output based on inputted props and slots.
* For **Behavioral** logic: assert correct render updates or emitted events in response to user input events.

In the below example, we demonstrate a Stepper component that has a DOM element labeled "increment" and can be clicked. We pass a prop called `max` that prevents the Stepper from being incremented past `2`, so if we click the button 3 times, the UI should still say `2`.

We know nothing about the implementation of Stepper, only that the "input" is the `max` prop and the "output" is the state of the DOM as the user will see it.

Vue Test UtilsCypressTesting Libraryjs\`\`\`
const valueSelector = '\[data\-testid=stepper\-value]'
const buttonSelector = '\[data\-testid=increment]'

const wrapper = mount(Stepper, {
 props: {
 max: 1
 }
})

expect(wrapper.find(valueSelector).text()).toContain('0')

await wrapper.find(buttonSelector).trigger('click')

expect(wrapper.find(valueSelector).text()).toContain('1')
\`\`\`js\`\`\`
const valueSelector = '\[data\-testid=stepper\-value]'
const buttonSelector = '\[data\-testid=increment]'

mount(Stepper, {
 props: {
 max: 1
 }
})

cy.get(valueSelector)
 .should('be.visible')
 .and('contain.text', '0')
 .get(buttonSelector)
 .click()
 .get(valueSelector)
 .should('contain.text', '1')
\`\`\`js\`\`\`
const { getByText } = render(Stepper, {
 props: {
 max: 1
 }
})

getByText('0') // Implicit assertion that "0" is within the component

const button = getByRole('button', { name: /increment/i })

// Dispatch a click event to our increment button.
await fireEvent.click(button)

getByText('1')

await fireEvent.click(button)
\`\`\`**DON'T**

* Don't assert the private state of a component instance or test the private methods of a component. Testing implementation details makes the tests brittle, as they are more likely to break and require updates when the implementation changes.

The component's ultimate job is rendering the correct DOM output, so tests focusing on the DOM output provide the same level of correctness assurance (if not more) while being more robust and resilient to change.

Don't rely exclusively on snapshot tests. Asserting HTML strings does not describe correctness. Write tests with intentionality.

If a method needs to be tested thoroughly, consider extracting it into a standalone utility function and write a dedicated unit test for it. If it cannot be extracted cleanly, it may be tested as a part of a component, integration, or end\-to\-end test that covers it.

### Recommendation [​](#recommendation-1)

* [Vitest](https://vitest.dev/) for components or composables that render headlessly (e.g. the [`useFavicon`](https://vueuse.org/core/useFavicon/#usefavicon) function in VueUse). Components and DOM can be tested using [`@vue/test-utils`](https://github.com/vuejs/test-utils).
* [Cypress Component Testing](https://on.cypress.io/component) for components whose expected behavior depends on properly rendering styles or triggering native DOM events. It can be used with Testing Library via [@testing\-library/cypress](https://testing-library.com/docs/cypress-testing-library/intro).

The main differences between Vitest and browser\-based runners are speed and execution context. In short, browser\-based runners, like Cypress, can catch issues that node\-based runners, like Vitest, cannot (e.g. style issues, real native DOM events, cookies, local storage, and network failures), but browser\-based runners are *orders of magnitude slower than Vitest* because they do open a browser, compile your stylesheets, and more. Cypress is a browser\-based runner that supports component testing. Please read [Vitest's comparison page](https://vitest.dev/guide/comparisons.html#cypress) for the latest information comparing Vitest and Cypress.

### Mounting Libraries [​](#mounting-libraries)

Component testing often involves mounting the component being tested in isolation, triggering simulated user input events, and asserting on the rendered DOM output. There are dedicated utility libraries that make these tasks simpler.

* [`@vue/test-utils`](https://github.com/vuejs/test-utils) is the official low\-level component testing library that was written to provide users access to Vue specific APIs. It's also the lower\-level library `@testing-library/vue` is built on top of.
* [`@testing-library/vue`](https://github.com/testing-library/vue-testing-library) is a Vue testing library focused on testing components without relying on implementation details. Its guiding principle is that the more tests resemble the way software is used, the more confidence they can provide.

We recommend using `@vue/test-utils` for testing components in applications. `@testing-library/vue` has issues with testing asynchronous component with Suspense, so it should be used with caution.

### Other Options [​](#other-options-1)

* [Nightwatch](https://nightwatchjs.org/) is an E2E test runner with Vue Component Testing support. ([Example Project](https://github.com/nightwatchjs-community/todo-vue))
* [WebdriverIO](https://webdriver.io/docs/component-testing/vue) for cross\-browser component testing that relies on native user interaction based on standardized automation. It can also be used with Testing Library.

## E2E Testing [​](#e2e-testing)

While unit tests provide developers with some degree of confidence, unit and component tests are limited in their abilities to provide holistic coverage of an application when deployed to production. As a result, end\-to\-end (E2E) tests provide coverage on what is arguably the most important aspect of an application: what happens when users actually use your applications.

End\-to\-end tests focus on multi\-page application behavior that makes network requests against your production\-built Vue application. They often involve standing up a database or other backend and may even be run against a live staging environment.

End\-to\-end tests will often catch issues with your router, state management library, top\-level components (e.g. an App or Layout), public assets, or any request handling. As stated above, they catch critical issues that may be impossible to catch with unit tests or component tests.

End\-to\-end tests do not import any of your Vue application's code but instead rely completely on testing your application by navigating through entire pages in a real browser.

End\-to\-end tests validate many of the layers in your application. They can either target your locally built application or even a live Staging environment. Testing against your Staging environment not only includes your frontend code and static server but all associated backend services and infrastructure.

> The more your tests resemble how your software is used, the more confidence they can give you. \- [Kent C. Dodds](https://twitter.com/kentcdodds/status/977018512689455106) \- Author of the Testing Library

By testing how user actions impact your application, E2E tests are often the key to higher confidence in whether an application is functioning properly or not.

### Choosing an E2E Testing Solution [​](#choosing-an-e2e-testing-solution)

While end\-to\-end (E2E) testing on the web has gained a negative reputation for unreliable (flaky) tests and slowing down development processes, modern E2E tools have made strides forward to create more reliable, interactive, and useful tests. When choosing an E2E testing framework, the following sections provide some guidance on things to keep in mind when choosing a testing framework for your application.

#### Cross\-browser testing [​](#cross-browser-testing)

One of the primary benefits that end\-to\-end (E2E) testing is known for is its ability to test your application across multiple browsers. While it may seem desirable to have 100% cross\-browser coverage, it is important to note that cross browser testing has diminishing returns on a team's resources due to the additional time and machine power required to run them consistently. As a result, it is important to be mindful of this trade\-off when choosing the amount of cross\-browser testing your application needs.

#### Faster feedback loops [​](#faster-feedback-loops)

One of the primary problems with end\-to\-end (E2E) tests and development is that running the entire suite takes a long time. Typically, this is only done in continuous integration and deployment (CI/CD) pipelines. Modern E2E testing frameworks have helped to solve this by adding features like parallelization, which allows for CI/CD pipelines to often run magnitudes faster than before. In addition, when developing locally, the ability to selectively run a single test for the page you are working on while also providing hot reloading of tests can help boost a developer's workflow and productivity.

#### First\-class debugging experience [​](#first-class-debugging-experience)

While developers have traditionally relied on scanning logs in a terminal window to help determine what went wrong in a test, modern end\-to\-end (E2E) test frameworks allow developers to leverage tools they are already familiar with, e.g. browser developer tools.

#### Visibility in headless mode [​](#visibility-in-headless-mode)

When end\-to\-end (E2E) tests are run in continuous integration/deployment pipelines, they are often run in headless browsers (i.e., no visible browser is opened for the user to watch). A critical feature of modern E2E testing frameworks is the ability to see snapshots and/or videos of the application during testing, providing some insight into why errors are happening. Historically, it was tedious to maintain these integrations.

### Recommendation [​](#recommendation-2)

* [Playwright](https://playwright.dev/) is a great E2E testing solution that supports Chromium, WebKit, and Firefox. Test on Windows, Linux, and macOS, locally or on CI, headless or headed with native mobile emulation of Google Chrome for Android and Mobile Safari. It has an informative UI, excellent debuggability, built\-in assertions, parallelization, traces and is designed to eliminate flaky tests. Support for [Component Testing](https://playwright.dev/docs/test-components) is available, but marked experimental. Playwright is open source and maintained by Microsoft.
* [Cypress](https://www.cypress.io/) has an informative graphical interface, excellent debuggability, built\-in assertions, stubs, flake\-resistance, and snapshots. As mentioned above, it provides stable support for [Component Testing](https://docs.cypress.io/guides/component-testing/introduction). Cypress supports Chromium\-based browsers, Firefox, and Electron. WebKit support is available, but marked experimental. Cypress is MIT\-licensed, but some features like parallelization require a subscription to Cypress Cloud.

[Testing SponsorLambdatest is a cloud platform for running E2E, accessibility, and visual regression tests across all major browsers and real devices, with AI assisted test generation!](https://lambdatest.com)### Other Options [​](#other-options-2)

* [Nightwatch](https://nightwatchjs.org/) is an E2E testing solution based on [Selenium WebDriver](https://www.npmjs.com/package/selenium-webdriver). This gives it the widest browser support range, including native mobile testing. Selenium\-based solutions will be slower than Playwright or Cypress.
* [WebdriverIO](https://webdriver.io/) is a test automation framework for web and mobile testing based on the WebDriver protocol.

## Recipes [​](#recipes)

### Adding Vitest to a Project [​](#adding-vitest-to-a-project)

In a Vite\-based Vue project, run:

sh\`\`\`
\> npm install \-D vitest happy\-dom @testing\-library/vue
\`\`\`Next, update the Vite configuration to add the `test` option block:

js\`\`\`
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
 // ...
 test: {
 // enable jest\-like global test APIs
 globals: true,
 // simulate DOM with happy\-dom
 // (requires installing happy\-dom as a peer dependency)
 environment: 'happy\-dom'
 }
})
\`\`\`TIP

If you use TypeScript, add `vitest/globals` to the `types` field in your `tsconfig.json`.

json\`\`\`
// tsconfig.json

{
 "compilerOptions": {
 "types": \["vitest/globals"]
 }
}
\`\`\`Then, create a file ending in `*.test.js` in your project. You can place all test files in a test directory in the project root or in test directories next to your source files. Vitest will automatically search for them using the naming convention.

js\`\`\`
// MyComponent.test.js
import { render } from '@testing\-library/vue'
import MyComponent from './MyComponent.vue'

test('it should work', () =\> {
 const { getByText } = render(MyComponent, {
 props: {
 /\* ... \*/
 }
 })

 // assert output
 getByText('...')
})
\`\`\`Finally, update `package.json` to add the test script and run it:

json\`\`\`
{
 // ...
 "scripts": {
 "test": "vitest"
 }
}
\`\`\`sh\`\`\`
\> npm test
\`\`\`### Testing Composables [​](#testing-composables)

> This section assumes you have read the [Composables](/guide/reusability/composables) section.

When it comes to testing composables, we can divide them into two categories: composables that do not rely on a host component instance, and composables that do.

A composable depends on a host component instance when it uses the following APIs:

* Lifecycle hooks
* Provide / Inject

If a composable only uses Reactivity APIs, then it can be tested by directly invoking it and asserting its returned state/methods:

js\`\`\`
// counter.js
import { ref } from 'vue'

export function useCounter() {
 const count = ref(0\)
 const increment = () =\> count.value\+\+

 return {
 count,
 increment
 }
}
\`\`\`js\`\`\`
// counter.test.js
import { useCounter } from './counter.js'

test('useCounter', () =\> {
 const { count, increment } = useCounter()
 expect(count.value).toBe(0\)

 increment()
 expect(count.value).toBe(1\)
})
\`\`\`A composable that relies on lifecycle hooks or Provide / Inject needs to be wrapped in a host component to be tested. We can create a helper like the following:

js\`\`\`
// test\-utils.js
import { createApp } from 'vue'

export function withSetup(composable) {
 let result
 const app = createApp({
 setup() {
 result = composable()
 // suppress missing template warning
 return () =\> {}
 }
 })
 app.mount(document.createElement('div'))
 // return the result and the app instance
 // for testing provide/unmount
 return \[result, app]
}
\`\`\`js\`\`\`
import { withSetup } from './test\-utils'
import { useFoo } from './foo'

test('useFoo', () =\> {
 const \[result, app] = withSetup(() =\> useFoo(123\))
 // mock provide for testing injections
 app.provide(...)
 // run assertions
 expect(result.foo.value).toBe(1\)
 // trigger onUnmounted hook if needed
 app.unmount()
})
\`\`\`For more complex composables, it could also be easier to test it by writing tests against the wrapper component using [Component Testing](#component-testing) techniques.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/scaling-up/testing.md)



## Composition API: Dependency Injection | Vue.js

[Read the full article](https://vuejs.org/api/composition-api-dependency-injection)

# Composition API: Dependency Injection [​](#composition-api-dependency-injection)

## provide() [​](#provide)

Provides a value that can be injected by descendant components.

* **Type**

ts\`\`\`
function provide\(key: InjectionKey\ \| string, value: T): void
\`\`\`
* **Details**

`provide()` takes two arguments: the key, which can be a string or a symbol, and the value to be injected.

When using TypeScript, the key can be a symbol casted as `InjectionKey` \- a Vue provided utility type that extends `Symbol`, which can be used to sync the value type between `provide()` and `inject()`.

Similar to lifecycle hook registration APIs, `provide()` must be called synchronously during a component's `setup()` phase.
* **Example**

vue\`\`\`
\
import { ref, provide } from 'vue'
import { countSymbol } from './injectionSymbols'

// provide static value
provide('path', '/project/')

// provide reactive value
const count = ref(0\)
provide('count', count)

// provide with Symbol keys
provide(countSymbol, count)
\
\`\`\`
* **See also**

	+ [Guide \- Provide / Inject](/guide/components/provide-inject)
	+ [Guide \- Typing Provide / Inject](/guide/typescript/composition-api#typing-provide-inject)

## inject() [​](#inject)

Injects a value provided by an ancestor component or the application (via `app.provide()`).

* **Type**

ts\`\`\`
// without default value
function inject\(key: InjectionKey\ \| string): T \| undefined

// with default value
function inject\(key: InjectionKey\ \| string, defaultValue: T): T

// with factory
function inject\(
 key: InjectionKey\ \| string,
 defaultValue: () =\> T,
 treatDefaultAsFactory: true
): T
\`\`\`
* **Details**

The first argument is the injection key. Vue will walk up the parent chain to locate a provided value with a matching key. If multiple components in the parent chain provides the same key, the one closest to the injecting component will "shadow" those higher up the chain. If no value with matching key was found, `inject()` returns `undefined` unless a default value is provided.

The second argument is optional and is the default value to be used when no matching value was found.

The second argument can also be a factory function that returns values that are expensive to create. In this case, `true` must be passed as the third argument to indicate that the function should be used as a factory instead of the value itself.

Similar to lifecycle hook registration APIs, `inject()` must be called synchronously during a component's `setup()` phase.

When using TypeScript, the key can be of type of `InjectionKey` \- a Vue\-provided utility type that extends `Symbol`, which can be used to sync the value type between `provide()` and `inject()`.
* **Example**

Assuming a parent component has provided values as shown in the previous `provide()` example:

vue\`\`\`
\
import { inject } from 'vue'
import { countSymbol } from './injectionSymbols'

// inject static value without default
const path = inject('path')

// inject reactive value
const count = inject('count')

// inject with Symbol keys
const count2 = inject(countSymbol)

// inject with default value
const bar = inject('path', '/default\-path')

// inject with function default value
const fn = inject('function', () =\> {})

// inject with default value factory
const baz = inject('factory', () =\> new ExpensiveObject(), true)
\
\`\`\`
* **See also**

	+ [Guide \- Provide / Inject](/guide/components/provide-inject)
	+ [Guide \- Typing Provide / Inject](/guide/typescript/composition-api#typing-provide-inject)

## hasInjectionContext() [​](#has-injection-context)

* Only supported in 3\.3\+

Returns true if [inject()](#inject) can be used without warning about being called in the wrong place (e.g. outside of `setup()`). This method is designed to be used by libraries that want to use `inject()` internally without triggering a warning to the end user.

* **Type**

ts\`\`\`
function hasInjectionContext(): boolean
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/composition-api-dependency-injection.md)



## Reactivity Fundamentals | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/reactivity-fundamentals)

# Reactivity Fundamentals [​](#reactivity-fundamentals)

API Preference

This page and many other chapters later in the guide contain different content for the Options API and the Composition API. Your current preference is Options APIComposition API. You can toggle between the API styles using the "API Preference" switches at the top of the left sidebar.

## Declaring Reactive State [​](#declaring-reactive-state)

With the Options API, we use the `data` option to declare reactive state of a component. The option value should be a function that returns an object. Vue will call the function when creating a new component instance, and wrap the returned object in its reactivity system. Any top\-level properties of this object are proxied on the component instance (`this` in methods and lifecycle hooks):

js\`\`\`
export default {
 data() {
 return {
 count: 1
 }
 },

 // \`mounted\` is a lifecycle hook which we will explain later
 mounted() {
 // \`this\` refers to the component instance.
 console.log(this.count) // =\> 1

 // data can be mutated as well
 this.count = 2
 }
}
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNpFUNFqhDAQ/JXBpzsoHu2j3B2U/oYPpnGtoetGkrW2iP/eRFsPApthd2Zndilex7H8mqioimu0wY16r4W+Rx8ULXVmYsVSC9AaNafz/gcC6RTkHwHWT6IVnne85rI+1ZLr5YJmyG1qG7gIA3Yd2R/LhN77T8y9sz1mwuyYkXazcQI2SiHz/7iP3VlQexeb5KKjEKEe2lPyMIxeSBROohqxVO4E6yV6ppL9xykTy83tOQvd7tnzoZtDwhrBO2GYNFloYWLyxrzPPOi44WWLWUt618txvASUhhRCKSHgbZt2scKy7HfCujGOqWL9BVfOgyI=)

These instance properties are only added when the instance is first created, so you need to ensure they are all present in the object returned by the `data` function. Where necessary, use `null`, `undefined` or some other placeholder value for properties where the desired value isn't yet available.

It is possible to add a new property directly to `this` without including it in `data`. However, properties added this way will not be able to trigger reactive updates.

Vue uses a `$` prefix when exposing its own built\-in APIs via the component instance. It also reserves the prefix `_` for internal properties. You should avoid using names for top\-level `data` properties that start with either of these characters.

### Reactive Proxy vs. Original [​](#reactive-proxy-vs-original)

In Vue 3, data is made reactive by leveraging [JavaScript Proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy). Users coming from Vue 2 should be aware of the following edge case:

js\`\`\`
export default {
 data() {
 return {
 someObject: {}
 }
 },
 mounted() {
 const newObject = {}
 this.someObject = newObject

 console.log(newObject === this.someObject) // false
 }
}
\`\`\`When you access `this.someObject` after assigning it, the value is a reactive proxy of the original `newObject`. **Unlike in Vue 2, the original `newObject` is left intact and will not be made reactive: make sure to always access reactive state as a property of `this`.**

## Declaring Reactive State [​](#declaring-reactive-state-1)

### `ref()` [​](#ref)

In Composition API, the recommended way to declare reactive state is using the [`ref()`](/api/reactivity-core#ref) function:

js\`\`\`
import { ref } from 'vue'

const count = ref(0\)
\`\`\``ref()` takes the argument and returns it wrapped within a ref object with a `.value` property:

js\`\`\`
const count = ref(0\)

console.log(count) // { value: 0 }
console.log(count.value) // 0

count.value\+\+
console.log(count.value) // 1
\`\`\`
> See also: [Typing Refs](/guide/typescript/composition-api#typing-ref)

To access refs in a component's template, declare and return them from a component's `setup()` function:

js\`\`\`
import { ref } from 'vue'

export default {
 // \`setup\` is a special hook dedicated for the Composition API.
 setup() {
 const count = ref(0\)

 // expose the ref to the template
 return {
 count
 }
 }
}
\`\`\`template\`\`\`
\{{ count }}\
\`\`\`Notice that we did **not** need to append `.value` when using the ref in the template. For convenience, refs are automatically unwrapped when used inside templates (with a few [caveats](#caveat-when-unwrapping-in-templates)).

You can also mutate a ref directly in event handlers:

template\`\`\`
\
 {{ count }}
\
\`\`\`For more complex logic, we can declare functions that mutate refs in the same scope and expose them as methods alongside the state:

js\`\`\`
import { ref } from 'vue'

export default {
 setup() {
 const count = ref(0\)

 function increment() {
 // .value is needed in JavaScript
 count.value\+\+
 }

 // don't forget to expose the function as well.
 return {
 count,
 increment
 }
 }
}
\`\`\`Exposed methods can then be used as event handlers:

template\`\`\`
\
 {{ count }}
\
\`\`\`Here's the example live on [Codepen](https://codepen.io/vuejs-examples/pen/WNYbaqo), without using any build tools.

### `` [​](#script-setup)

Manually exposing state and methods via `setup()` can be verbose. Luckily, it can be avoided when using [Single\-File Components (SFCs)](/guide/scaling-up/sfc). We can simplify the usage with ``:

vue\`\`\`
\
import { ref } from 'vue'

const count = ref(0\)

function increment() {
 count.value\+\+
}
\

\
 \
 {{ count }}
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNo9jUEKgzAQRa8yZKMiaNcllvYe2dgwQqiZhDhxE3L3jrW4/DPvv1/UK8Zhz6juSm82uciwIef4MOR8DImhQMIFKiwpeGgEbQwZsoE2BhsyMUwH0d66475ksuwCgSOb0CNx20ExBCc77POase8NVUN6PBdlSwKjj+vMKAlAvzOzWJ52dfYzGXXpjPoBAKX856uopDGeFfnq8XKp+gWq4FAi)

Top\-level imports, variables and functions declared in `` are automatically usable in the template of the same component. Think of the template as a JavaScript function declared in the same scope \- it naturally has access to everything declared alongside it.

TIP

For the rest of the guide, we will be primarily using SFC \+ `` syntax for the Composition API code examples, as that is the most common usage for Vue developers.

If you are not using SFC, you can still use Composition API with the [`setup()`](/api/composition-api-setup) option.

### Why Refs? [​](#why-refs)

You might be wondering why we need refs with the `.value` instead of plain variables. To explain that, we will need to briefly discuss how Vue's reactivity system works.

When you use a ref in a template, and change the ref's value later, Vue automatically detects the change and updates the DOM accordingly. This is made possible with a dependency\-tracking based reactivity system. When a component is rendered for the first time, Vue **tracks** every ref that was used during the render. Later on, when a ref is mutated, it will **trigger** a re\-render for components that are tracking it.

In standard JavaScript, there is no way to detect the access or mutation of plain variables. However, we can intercept the get and set operations of an object's properties using getter and setter methods.

The `.value` property gives Vue the opportunity to detect when a ref has been accessed or mutated. Under the hood, Vue performs the tracking in its getter, and performs triggering in its setter. Conceptually, you can think of a ref as an object that looks like this:

js\`\`\`
// pseudo code, not actual implementation
const myRef = {
 \_value: 0,
 get value() {
 track()
 return this.\_value
 },
 set value(newValue) {
 this.\_value = newValue
 trigger()
 }
}
\`\`\`Another nice trait of refs is that unlike plain variables, you can pass refs into functions while retaining access to the latest value and the reactivity connection. This is particularly useful when refactoring complex logic into reusable code.

The reactivity system is discussed in more details in the [Reactivity in Depth](/guide/extras/reactivity-in-depth) section.

## Declaring Methods [​](#declaring-methods)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/methods-in-vue-3?friend=vuejs "Free Vue.js Methods Lesson")To add methods to a component instance we use the `methods` option. This should be an object containing the desired methods:

js\`\`\`
export default {
 data() {
 return {
 count: 0
 }
 },
 methods: {
 increment() {
 this.count\+\+
 }
 },
 mounted() {
 // methods can be called in lifecycle hooks, or other methods!
 this.increment()
 }
}
\`\`\`Vue automatically binds the `this` value for `methods` so that it always refers to the component instance. This ensures that a method retains the correct `this` value if it's used as an event listener or callback. You should avoid using arrow functions when defining `methods`, as that prevents Vue from binding the appropriate `this` value:

js\`\`\`
export default {
 methods: {
 increment: () =\> {
 // BAD: no \`this\` access here!
 }
 }
}
\`\`\`Just like all other properties of the component instance, the `methods` are accessible from within the component's template. Inside a template they are most commonly used as event listeners:

template\`\`\`
\{{ count }}\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNplj9EKwyAMRX8l+LSx0e65uLL9hy+dZlTWqtg4BuK/z1baDgZicsPJgUR2d656B2QN45P02lErDH6c9QQKn10YCKIwAKqj7nAsPYBHCt6sCUDaYKiBS8lpLuk8/yNSb9XUrKg20uOIhnYXAPV6qhbF6fRvmOeodn6hfzwLKkx+vN5OyIFwdENHmBMAfwQia+AmBy1fV8E2gWBtjOUASInXBcxLvN4MLH0BCe1i4Q==)

In the example above, the method `increment` will be called when the `` is clicked.

### Deep Reactivity [​](#deep-reactivity)

In Vue, state is deeply reactive by default. This means you can expect changes to be detected even when you mutate nested objects or arrays:

js\`\`\`
export default {
 data() {
 return {
 obj: {
 nested: { count: 0 },
 arr: \['foo', 'bar']
 }
 }
 },
 methods: {
 mutateDeeply() {
 // these will work as expected.
 this.obj.nested.count\+\+
 this.obj.arr.push('baz')
 }
 }
}
\`\`\`Refs can hold any value type, including deeply nested objects, arrays, or JavaScript built\-in data structures like `Map`.

A ref will make its value deeply reactive. This means you can expect changes to be detected even when you mutate nested objects or arrays:

js\`\`\`
import { ref } from 'vue'

const obj = ref({
 nested: { count: 0 },
 arr: \['foo', 'bar']
})

function mutateDeeply() {
 // these will work as expected.
 obj.value.nested.count\+\+
 obj.value.arr.push('baz')
}
\`\`\`Non\-primitive values are turned into reactive proxies via [`reactive()`](#reactive), which is discussed below.

It is also possible to opt\-out of deep reactivity with [shallow refs](/api/reactivity-advanced#shallowref). For shallow refs, only `.value` access is tracked for reactivity. Shallow refs can be used for optimizing performance by avoiding the observation cost of large objects, or in cases where the inner state is managed by an external library.

Further reading:

* [Reduce Reactivity Overhead for Large Immutable Structures](/guide/best-practices/performance#reduce-reactivity-overhead-for-large-immutable-structures)
* [Integration with External State Systems](/guide/extras/reactivity-in-depth#integration-with-external-state-systems)
### DOM Update Timing [​](#dom-update-timing)

When you mutate reactive state, the DOM is updated automatically. However, it should be noted that the DOM updates are not applied synchronously. Instead, Vue buffers them until the "next tick" in the update cycle to ensure that each component updates only once no matter how many state changes you have made.

To wait for the DOM update to complete after a state change, you can use the [nextTick()](/api/general#nexttick) global API:

js\`\`\`
import { nextTick } from 'vue'

async function increment() {
 count.value\+\+
 await nextTick()
 // Now the DOM is updated
}
\`\`\`js\`\`\`
import { nextTick } from 'vue'

export default {
 methods: {
 async increment() {
 this.count\+\+
 await nextTick()
 // Now the DOM is updated
 }
 }
}
\`\`\`## `reactive()` [​](#reactive)

There is another way to declare reactive state, with the `reactive()` API. Unlike a ref which wraps the inner value in a special object, `reactive()` makes an object itself reactive:

js\`\`\`
import { reactive } from 'vue'

const state = reactive({ count: 0 })
\`\`\`
> See also: [Typing Reactive](/guide/typescript/composition-api#typing-reactive)

Usage in template:

template\`\`\`
\
 {{ state.count }}
\
\`\`\`Reactive objects are [JavaScript Proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) and behave just like normal objects. The difference is that Vue is able to intercept the access and mutation of all properties of a reactive object for reactivity tracking and triggering.

`reactive()` converts the object deeply: nested objects are also wrapped with `reactive()` when accessed. It is also called by `ref()` internally when the ref value is an object. Similar to shallow refs, there is also the [`shallowReactive()`](/api/reactivity-advanced#shallowreactive) API for opting\-out of deep reactivity.

### Reactive Proxy vs. Original [​](#reactive-proxy-vs-original-1)

It is important to note that the returned value from `reactive()` is a [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) of the original object, which is not equal to the original object:

js\`\`\`
const raw = {}
const proxy = reactive(raw)

// proxy is NOT equal to the original.
console.log(proxy === raw) // false
\`\`\`Only the proxy is reactive \- mutating the original object will not trigger updates. Therefore, the best practice when working with Vue's reactivity system is to **exclusively use the proxied versions of your state**.

To ensure consistent access to the proxy, calling `reactive()` on the same object always returns the same proxy, and calling `reactive()` on an existing proxy also returns that same proxy:

js\`\`\`
// calling reactive() on the same object returns the same proxy
console.log(reactive(raw) === proxy) // true

// calling reactive() on a proxy returns itself
console.log(reactive(proxy) === proxy) // true
\`\`\`This rule applies to nested objects as well. Due to deep reactivity, nested objects inside a reactive object are also proxies:

js\`\`\`
const proxy = reactive({})

const raw = {}
proxy.nested = raw

console.log(proxy.nested === raw) // false
\`\`\`### Limitations of `reactive()` [​](#limitations-of-reactive)

The `reactive()` API has a few limitations:

1. **Limited value types:** it only works for object types (objects, arrays, and [collection types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#keyed_collections) such as `Map` and `Set`). It cannot hold [primitive types](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) such as `string`, `number` or `boolean`.
2. **Cannot replace entire object:** since Vue's reactivity tracking works over property access, we must always keep the same reference to the reactive object. This means we can't easily "replace" a reactive object because the reactivity connection to the first reference is lost:

js\`\`\`
let state = reactive({ count: 0 })

// the above reference ({ count: 0 }) is no longer being tracked
// (reactivity connection is lost!)
state = reactive({ count: 1 })
\`\`\`
3. **Not destructure\-friendly:** when we destructure a reactive object's primitive type property into local variables, or when we pass that property into a function, we will lose the reactivity connection:

js\`\`\`
const state = reactive({ count: 0 })

// count is disconnected from state.count when destructured.
let { count } = state
// does not affect original state
count\+\+

// the function receives a plain number and
// won't be able to track changes to state.count
// we have to pass the entire object in to retain reactivity
callSomeFunction(state.count)
\`\`\`

Due to these limitations, we recommend using `ref()` as the primary API for declaring reactive state.

## Additional Ref Unwrapping Details [​](#additional-ref-unwrapping-details)

### As Reactive Object Property [​](#ref-unwrapping-as-reactive-object-property)

A ref is automatically unwrapped when accessed or mutated as a property of a reactive object. In other words, it behaves like a normal property:

js\`\`\`
const count = ref(0\)
const state = reactive({
 count
})

console.log(state.count) // 0

state.count = 1
console.log(count.value) // 1
\`\`\`If a new ref is assigned to a property linked to an existing ref, it will replace the old ref:

js\`\`\`
const otherCount = ref(2\)

state.count = otherCount
console.log(state.count) // 2
// original ref is now disconnected from state.count
console.log(count.value) // 1
\`\`\`Ref unwrapping only happens when nested inside a deep reactive object. It does not apply when it is accessed as a property of a [shallow reactive object](/api/reactivity-advanced#shallowreactive).

### Caveat in Arrays and Collections [​](#caveat-in-arrays-and-collections)

Unlike reactive objects, there is **no** unwrapping performed when the ref is accessed as an element of a reactive array or a native collection type like `Map`:

js\`\`\`
const books = reactive(\[ref('Vue 3 Guide')])
// need .value here
console.log(books\[0].value)

const map = reactive(new Map(\[\['count', ref(0\)]]))
// need .value here
console.log(map.get('count').value)
\`\`\`### Caveat when Unwrapping in Templates [​](#caveat-when-unwrapping-in-templates)

Ref unwrapping in templates only applies if the ref is a top\-level property in the template render context.

In the example below, `count` and `object` are top\-level properties, but `object.id` is not:

js\`\`\`
const count = ref(0\)
const object = { id: ref(1\) }
\`\`\`Therefore, this expression works as expected:

template\`\`\`
{{ count \+ 1 }}
\`\`\`...while this one does **NOT**:

template\`\`\`
{{ object.id \+ 1 }}
\`\`\`The rendered result will be `[object Object]1` because `object.id` is not unwrapped when evaluating the expression and remains a ref object. To fix this, we can destructure `id` into a top\-level property:

js\`\`\`
const { id } = object
\`\`\`template\`\`\`
{{ id \+ 1 }}
\`\`\`Now the render result will be `2`.

Another thing to note is that a ref does get unwrapped if it is the final evaluated value of a text interpolation (i.e. a `{{ }}` tag), so the following will render `1`:

template\`\`\`
{{ object.id }}
\`\`\`This is just a convenience feature of text interpolation and is equivalent to `{{ object.id.value }}`.

### Stateful Methods [​](#stateful-methods)

In some cases, we may need to dynamically create a method function, for example creating a debounced event handler:

js\`\`\`
import { debounce } from 'lodash\-es'

export default {
 methods: {
 // Debouncing with Lodash
 click: debounce(function () {
 // ... respond to click ...
 }, 500\)
 }
}
\`\`\`However, this approach is problematic for components that are reused because a debounced function is **stateful**: it maintains some internal state on the elapsed time. If multiple component instances share the same debounced function, they will interfere with one another.

To keep each component instance's debounced function independent of the others, we can create the debounced version in the `created` lifecycle hook:

js\`\`\`
export default {
 created() {
 // each instance now has its own copy of debounced handler
 this.debouncedClick = \_.debounce(this.click, 500\)
 },
 unmounted() {
 // also a good idea to cancel the timer
 // when the component is removed
 this.debouncedClick.cancel()
 },
 methods: {
 click() {
 // ... respond to click ...
 }
 }
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/reactivity-fundamentals.md)



## Template Syntax | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/template-syntax)

# Template Syntax [​](#template-syntax)

Vue uses an HTML\-based template syntax that allows you to declaratively bind the rendered DOM to the underlying component instance's data. All Vue templates are syntactically valid HTML that can be parsed by spec\-compliant browsers and HTML parsers.

Under the hood, Vue compiles the templates into highly\-optimized JavaScript code. Combined with the reactivity system, Vue can intelligently figure out the minimal number of components to re\-render and apply the minimal amount of DOM manipulations when the app state changes.

If you are familiar with Virtual DOM concepts and prefer the raw power of JavaScript, you can also [directly write render functions](/guide/extras/render-function) instead of templates, with optional JSX support. However, do note that they do not enjoy the same level of compile\-time optimizations as templates.

## Text Interpolation [​](#text-interpolation)

The most basic form of data binding is text interpolation using the "Mustache" syntax (double curly braces):

template\`\`\`
\Message: {{ msg }}\
\`\`\`The mustache tag will be replaced with the value of the `msg` property [from the corresponding component instance](/guide/essentials/reactivity-fundamentals#declaring-reactive-state). It will also be updated whenever the `msg` property changes.

## Raw HTML [​](#raw-html)

The double mustaches interpret the data as plain text, not HTML. In order to output real HTML, you will need to use the [`v-html` directive](/api/built-in-directives#v-html):

template\`\`\`
\Using text interpolation: {{ rawHtml }}\
\Using v\-html directive: \\\
\`\`\`Using text interpolation: \This should be red.\

Using v\-html directive: This should be red.

Here we're encountering something new. The `v-html` attribute you're seeing is called a **directive**. Directives are prefixed with `v-` to indicate that they are special attributes provided by Vue, and as you may have guessed, they apply special reactive behavior to the rendered DOM. Here, we're basically saying "keep this element's inner HTML up\-to\-date with the `rawHtml` property on the current active instance."

The contents of the `span` will be replaced with the value of the `rawHtml` property, interpreted as plain HTML \- data bindings are ignored. Note that you cannot use `v-html` to compose template partials, because Vue is not a string\-based templating engine. Instead, components are preferred as the fundamental unit for UI reuse and composition.

Security Warning

Dynamically rendering arbitrary HTML on your website can be very dangerous because it can easily lead to [XSS vulnerabilities](https://en.wikipedia.org/wiki/Cross-site_scripting). Only use `v-html` on trusted content and **never** on user\-provided content.

## Attribute Bindings [​](#attribute-bindings)

Mustaches cannot be used inside HTML attributes. Instead, use a [`v-bind` directive](/api/built-in-directives#v-bind):

template\`\`\`
\\
\`\`\`The `v-bind` directive instructs Vue to keep the element's `id` attribute in sync with the component's `dynamicId` property. If the bound value is `null` or `undefined`, then the attribute will be removed from the rendered element.

### Shorthand [​](#shorthand)

Because `v-bind` is so commonly used, it has a dedicated shorthand syntax:

template\`\`\`
\\
\`\`\`Attributes that start with `:` may look a bit different from normal HTML, but it is in fact a valid character for attribute names and all Vue\-supported browsers can parse it correctly. In addition, they do not appear in the final rendered markup. The shorthand syntax is optional, but you will likely appreciate it when you learn more about its usage later.

> For the rest of the guide, we will be using the shorthand syntax in code examples, as that's the most common usage for Vue developers.

### Same\-name Shorthand [​](#same-name-shorthand)

* Only supported in 3\.4\+

If the attribute has the same name with the JavaScript value being bound, the syntax can be further shortened to omit the attribute value:

template\`\`\`
\
\\

\
\\
\`\`\`This is similar to the property shorthand syntax when declaring objects in JavaScript. Note this is a feature that is only available in Vue 3\.4 and above.

### Boolean Attributes [​](#boolean-attributes)

[Boolean attributes](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attributes) are attributes that can indicate true / false values by their presence on an element. For example, [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled) is one of the most commonly used boolean attributes.

`v-bind` works a bit differently in this case:

template\`\`\`
\Button\
\`\`\`The `disabled` attribute will be included if `isButtonDisabled` has a [truthy value](https://developer.mozilla.org/en-US/docs/Glossary/Truthy). It will also be included if the value is an empty string, maintaining consistency with ``. For other [falsy values](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) the attribute will be omitted.

### Dynamically Binding Multiple Attributes [​](#dynamically-binding-multiple-attributes)

If you have a JavaScript object representing multiple attributes that looks like this:

js\`\`\`
const objectOfAttrs = {
 id: 'container',
 class: 'wrapper',
 style: 'background\-color:green'
}
\`\`\`js\`\`\`
data() {
 return {
 objectOfAttrs: {
 id: 'container',
 class: 'wrapper'
 }
 }
}
\`\`\`You can bind them to a single element by using `v-bind` without an argument:

template\`\`\`
\\
\`\`\`## Using JavaScript Expressions [​](#using-javascript-expressions)

So far we've only been binding to simple property keys in our templates. But Vue actually supports the full power of JavaScript expressions inside all data bindings:

template\`\`\`
{{ number \+ 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

\\
\`\`\`These expressions will be evaluated as JavaScript in the data scope of the current component instance.

In Vue templates, JavaScript expressions can be used in the following positions:

* Inside text interpolations (mustaches)
* In the attribute value of any Vue directives (special attributes that start with `v-`)

### Expressions Only [​](#expressions-only)

Each binding can only contain **one single expression**. An expression is a piece of code that can be evaluated to a value. A simple check is whether it can be used after `return`.

Therefore, the following will **NOT** work:

template\`\`\`
\
{{ var a = 1 }}

\
{{ if (ok) { return message } }}
\`\`\`### Calling Functions [​](#calling-functions)

It is possible to call a component\-exposed method inside a binding expression:

template\`\`\`
\
 {{ formatDate(date) }}
\
\`\`\`TIP

Functions called inside binding expressions will be called every time the component updates, so they should **not** have any side effects, such as changing data or triggering asynchronous operations.

### Restricted Globals Access [​](#restricted-globals-access)

Template expressions are sandboxed and only have access to a [restricted list of globals](https://github.com/vuejs/core/blob/main/packages/shared/src/globalsAllowList.ts#L3). The list exposes commonly used built\-in globals such as `Math` and `Date`.

Globals not explicitly included in the list, for example user\-attached properties on `window`, will not be accessible in template expressions. You can, however, explicitly define additional globals for all Vue expressions by adding them to [`app.config.globalProperties`](/api/application#app-config-globalproperties).

## Directives [​](#directives)

Directives are special attributes with the `v-` prefix. Vue provides a number of [built\-in directives](/api/built-in-directives), including `v-html` and `v-bind` which we have introduced above.

Directive attribute values are expected to be single JavaScript expressions (with the exception of `v-for`, `v-on` and `v-slot`, which will be discussed in their respective sections later). A directive's job is to reactively apply updates to the DOM when the value of its expression changes. Take [`v-if`](/api/built-in-directives#v-if) as an example:

template\`\`\`
\Now you see me\
\`\`\`Here, the `v-if` directive would remove or insert the `` element based on the truthiness of the value of the expression `seen`.

### Arguments [​](#arguments)

Some directives can take an "argument", denoted by a colon after the directive name. For example, the `v-bind` directive is used to reactively update an HTML attribute:

template\`\`\`
\ ... \

\
\ ... \
\`\`\`Here, `href` is the argument, which tells the `v-bind` directive to bind the element's `href` attribute to the value of the expression `url`. In the shorthand, everything before the argument (i.e., `v-bind:`) is condensed into a single character, `:`.

Another example is the `v-on` directive, which listens to DOM events:

template\`\`\`
\ ... \

\
\ ... \
\`\`\`Here, the argument is the event name to listen to: `click`. `v-on` has a corresponding shorthand, namely the `@` character. We will talk about event handling in more detail too.

### Dynamic Arguments [​](#dynamic-arguments)

It is also possible to use a JavaScript expression in a directive argument by wrapping it with square brackets:

template\`\`\`
\
\ ... \

\
\ ... \
\`\`\`Here, `attributeName` will be dynamically evaluated as a JavaScript expression, and its evaluated value will be used as the final value for the argument. For example, if your component instance has a data property, `attributeName`, whose value is `"href"`, then this binding will be equivalent to `v-bind:href`.

Similarly, you can use dynamic arguments to bind a handler to a dynamic event name:

template\`\`\`
\ ... \

\
\ ... \
\`\`\`In this example, when `eventName`'s value is `"focus"`, `v-on:[eventName]` will be equivalent to `v-on:focus`.

#### Dynamic Argument Value Constraints [​](#dynamic-argument-value-constraints)

Dynamic arguments are expected to evaluate to a string, with the exception of `null`. The special value `null` can be used to explicitly remove the binding. Any other non\-string value will trigger a warning.

#### Dynamic Argument Syntax Constraints [​](#dynamic-argument-syntax-constraints)

Dynamic argument expressions have some syntax constraints because certain characters, such as spaces and quotes, are invalid inside HTML attribute names. For example, the following is invalid:

template\`\`\`
\
\ ... \
\`\`\`If you need to pass a complex dynamic argument, it's probably better to use a [computed property](/guide/essentials/computed), which we will cover shortly.

When using in\-DOM templates (templates directly written in an HTML file), you should also avoid naming keys with uppercase characters, as browsers will coerce attribute names into lowercase:

template\`\`\`
\ ... \
\`\`\`The above will be converted to `:[someattr]` in in\-DOM templates. If your component has a `someAttr` property instead of `someattr`, your code won't work. Templates inside Single\-File Components are **not** subject to this constraint.

### Modifiers [​](#modifiers)

Modifiers are special postfixes denoted by a dot, which indicate that a directive should be bound in some special way. For example, the `.prevent` modifier tells the `v-on` directive to call `event.preventDefault()` on the triggered event:

template\`\`\`
\...\
\`\`\`You'll see other examples of modifiers later, [for `v-on`](/guide/essentials/event-handling#event-modifiers) and [for `v-model`](/guide/essentials/forms#modifiers), when we explore those features.

And finally, here's the full directive syntax visualized:



[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/template-syntax.md)



## Single-File Components | Vue.js

[Read the full article](https://vuejs.org/guide/scaling-up/sfc)

# Single\-File Components [​](#single-file-components)

## Introduction [​](#introduction)

Vue Single\-File Components (a.k.a. `*.vue` files, abbreviated as **SFC**) is a special file format that allows us to encapsulate the template, logic, **and** styling of a Vue component in a single file. Here's an example SFC:

vue\`\`\`
\
export default {
 data() {
 return {
 greeting: 'Hello World!'
 }
 }
}
\

\
 \{{ greeting }}\
\

\
.greeting {
 color: red;
 font\-weight: bold;
}
\
\`\`\`vue\`\`\`
\
import { ref } from 'vue'
const greeting = ref('Hello World!')
\

\
 \{{ greeting }}\
\

\
.greeting {
 color: red;
 font\-weight: bold;
}
\
\`\`\`As we can see, Vue SFC is a natural extension of the classic trio of HTML, CSS and JavaScript. The ``, ``, and `` blocks encapsulate and colocate the view, logic and styling of a component in the same file. The full syntax is defined in the [SFC Syntax Specification](/api/sfc-spec).

## Why SFC [​](#why-sfc)

While SFCs require a build step, there are numerous benefits in return:

* Author modularized components using familiar HTML, CSS and JavaScript syntax
* [Colocation of inherently coupled concerns](#what-about-separation-of-concerns)
* Pre\-compiled templates without runtime compilation cost
* [Component\-scoped CSS](/api/sfc-css-features)
* [More ergonomic syntax when working with Composition API](/api/sfc-script-setup)
* More compile\-time optimizations by cross\-analyzing template and script
* [IDE support](/guide/scaling-up/tooling#ide-support) with auto\-completion and type\-checking for template expressions
* Out\-of\-the\-box Hot\-Module Replacement (HMR) support

SFC is a defining feature of Vue as a framework, and is the recommended approach for using Vue in the following scenarios:

* Single\-Page Applications (SPA)
* Static Site Generation (SSG)
* Any non\-trivial frontend where a build step can be justified for better development experience (DX).

That said, we do realize there are scenarios where SFCs can feel like overkill. This is why Vue can still be used via plain JavaScript without a build step. If you are just looking for enhancing largely static HTML with light interactions, you can also check out [petite\-vue](https://github.com/vuejs/petite-vue), a 6 kB subset of Vue optimized for progressive enhancement.

## How It Works [​](#how-it-works)

Vue SFC is a framework\-specific file format and must be pre\-compiled by [@vue/compiler\-sfc](https://github.com/vuejs/core/tree/main/packages/compiler-sfc) into standard JavaScript and CSS. A compiled SFC is a standard JavaScript (ES) module \- which means with proper build setup you can import an SFC like a module:

js\`\`\`
import MyComponent from './MyComponent.vue'

export default {
 components: {
 MyComponent
 }
}
\`\`\``` tags inside SFCs are typically injected as native `` tags during development to support hot updates. For production they can be extracted and merged into a single CSS file.

You can play with SFCs and explore how they are compiled in the [Vue SFC Playground](https://play.vuejs.org/).

In actual projects, we typically integrate the SFC compiler with a build tool such as [Vite](https://vitejs.dev/) or [Vue CLI](http://cli.vuejs.org/) (which is based on [webpack](https://webpack.js.org/)), and Vue provides official scaffolding tools to get you started with SFCs as fast as possible. Check out more details in the [SFC Tooling](/guide/scaling-up/tooling) section.

## What About Separation of Concerns? [​](#what-about-separation-of-concerns)

Some users coming from a traditional web development background may have the concern that SFCs are mixing different concerns in the same place \- which HTML/CSS/JS were supposed to separate!

To answer this question, it is important for us to agree that **separation of concerns is not equal to the separation of file types**. The ultimate goal of engineering principles is to improve the maintainability of codebases. Separation of concerns, when applied dogmatically as separation of file types, does not help us reach that goal in the context of increasingly complex frontend applications.

In modern UI development, we have found that instead of dividing the codebase into three huge layers that interweave with one another, it makes much more sense to divide them into loosely\-coupled components and compose them. Inside a component, its template, logic, and styles are inherently coupled, and colocating them actually makes the component more cohesive and maintainable.

Note even if you don't like the idea of Single\-File Components, you can still leverage its hot\-reloading and pre\-compilation features by separating your JavaScript and CSS into separate files using [Src Imports](/api/sfc-spec#src-imports).

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/scaling-up/sfc.md)



## TransitionGroup | Vue.js

[Read the full article](https://vuejs.org/guide/built-ins/transition-group)

# TransitionGroup [​](#transitiongroup)

`` is a built\-in component designed for animating the insertion, removal, and order change of elements or components that are rendered in a list.

## Differences from `` [​](#differences-from-transition)

`` supports the same props, CSS transition classes, and JavaScript hook listeners as ``, with the following differences:

* By default, it doesn't render a wrapper element. But you can specify an element to be rendered with the `tag` prop.
* [Transition modes](/guide/built-ins/transition#transition-modes) are not available, because we are no longer alternating between mutually exclusive elements.
* Elements inside are **always required** to have a unique `key` attribute.
* CSS transition classes will be applied to individual elements in the list, **not** to the group / container itself.

TIP

When used in [in\-DOM templates](/guide/essentials/component-basics#in-dom-template-parsing-caveats), it should be referenced as ``.

## Enter / Leave Transitions [​](#enter-leave-transitions)

Here is an example of applying enter / leave transitions to a `v-for` list using ``:

template\`\`\`
\
 \
 {{ item }}
 \
\
\`\`\`css\`\`\`
.list\-enter\-active,
.list\-leave\-active {
 transition: all 0\.5s ease;
}
.list\-enter\-from,
.list\-leave\-to {
 opacity: 0;
 transform: translateX(30px);
}
\`\`\`Add at random indexRemove at random index* 1
* 2
* 3
* 4
* 5
## Move Transitions [​](#move-transitions)

The above demo has some obvious flaws: when an item is inserted or removed, its surrounding items instantly "jump" into place instead of moving smoothly. We can fix this by adding a few additional CSS rules:

css\`\`\`
.list\-move, /\* apply transition to moving elements \*/
.list\-enter\-active,
.list\-leave\-active {
 transition: all 0\.5s ease;
}

.list\-enter\-from,
.list\-leave\-to {
 opacity: 0;
 transform: translateX(30px);
}

/\* ensure leaving items are taken out of layout flow so that moving
 animations can be calculated correctly. \*/
.list\-leave\-active {
 position: absolute;
}
\`\`\`Now it looks much better \- even animating smoothly when the whole list is shuffled:

AddRemoveShuffle* 1
* 2
* 3
* 4
* 5
[Full Example](/examples/#list-transition)

### Custom TransitionGroup classes [​](#custom-transitiongroup-classes)

You can also specify custom transition classes for the moving element by passing the `moveClass` prop to ``, just like [custom transition classes on ``](/guide/built-ins/transition#custom-transition-classes).

## Staggering List Transitions [​](#staggering-list-transitions)

By communicating with JavaScript transitions through data attributes, it's also possible to stagger transitions in a list. First, we render the index of an item as a data attribute on the DOM element:

template\`\`\`
\
 \
 {{ item.msg }}
 \
\
\`\`\`Then, in JavaScript hooks, we animate the element with a delay based on the data attribute. This example is using the [GSAP library](https://gsap.com/) to perform the animation:

js\`\`\`
function onEnter(el, done) {
 gsap.to(el, {
 opacity: 1,
 height: '1\.6em',
 delay: el.dataset.index \* 0\.15,
 onComplete: done
 })
}
\`\`\`* Bruce Lee
* Jackie Chan
* Chuck Norris
* Jet Li
* Kung Fury
[Full Example in the Playground](https://play.vuejs.org/#eNqlVMuu0zAQ/ZVRNklRm7QLWETtBW4FSFCxYkdYmGSSmjp28KNQVfl3xk7SFyvEponPGc+cOTPNOXrbdenRYZRHa1Nq3lkwaF33VEjedkpbOIPGeg6lajtnsYIeaq1aiOlSfAlqDOtG3L8SUchSSWNBcPrZwNdCAqVqTZND/KxdibBDjKGf3xIfWXngCNs9k4/Udu/KA3xWWnPz1zW0sOOP6CcnG3jv9ImIQn67SvrpUJ9IE/WVxPHsSkw97gbN0zFJZrB5grNPrskcLUNXac2FRZ0k3GIbIvxLSsVTq3bqF+otM5jMUi5L4So0SSicHplwOKOyfShdO1lariQo+Yy10vhO+qwoZkNFFKmxJ4Gp6ljJrRe+vMP3yJu910swNXqXcco1h0pJHDP6CZHEAAcAYMydwypYCDAkJRdX6Sts4xGtUDAKotIVs9Scpd4q/A0vYJmuXo5BSm7JOIEW81DVo77VR207ZEf8F23LB23T+X9VrbNh82nn6UAz7ASzSCeANZe0AnBctIqqbIoojLCIIBvoL5pJw31DH7Ry3VDKsoYinSii4ZyXxhBQM2Fwwt58D7NeoB8QkXfDvwRd2XtceOsCHkwc8KCINAk+vADJppQUFjZ0DsGVGT3uFn1KSjoPeKLoaYtvCO/rIlz3vH9O5FiU/nXny/pDT6YGKZngg0/Zg1GErrMbp6N5NHxJFi3N/4dRkj5IYf5ULxCmiPJpI4rIr4kHimhvbWfyLHOyOzQpNZZ57jXNy4nRGFLTR/0fWBqe7w==)

[Full Example in the Playground](https://play.vuejs.org/#eNqtVE2P0zAQ/SujXNqgNmkPcIjaBbYCJKg4cSMcTDJNTB07+KNsVfW/M3aabNpyQltViT1vPPP8Zian6H3bJgeHURatTKF5ax9yyZtWaQuVYS3stGpg4peTXOayUNJYEJwea/ieS4ATNKbKYPKoXYGwRZzAeTYGPrNizxE2NZO30KZ2xR6+Kq25uTuGFrb81vrFyQo+On0kIJc/PCV8CmxL3DEnLJy8e8ksm8bdGkCjdVr2O4DfDvWRgtGN/JYC0SOkKVTTOotl1jv3hi3d+DngENILkey4sKinU26xiWH9AH6REN/Eqq36g3rDDE7jhMtCuBLN1NbcJIFEHN9RaNDWqjQDAyUfcac0fpA+CYoRCRSJsUeBiWpZwe2RSrK4w2rkVe2rdYG6LD5uH3EGpZI4iuurTdwDNBjpRJclg+UlhP914UnMZfIGm8kIKVEwciYivhoGLQlQ4hO8gkWyfD1yVHJDKgu0mAUmPXLuxRkYb5Ed8H8YL/7BeGx7Oa6hkLmk/yodBoo21BKtYBZpB7DikroKDvNGUeZ1HoVmyCNIO/ibZtJwy5X8pJVru9CWVeTpRB51+6wwhgw7Jgz2tnc/Q6/M0ZeWwKvmGZye0Wu78PIGexC6swdGxEnw/q6HOYUkt9DwMwhKxfS6GpY+KPHc45G8+6EYAV7reTjucf/uwUtSmvvTME1wDuISlVTwTqf0RiiyrtKR0tEs6r5l84b645dRkr5zoT8oXwBMHg2Tlke+jbwhj2prW5OlqZPtvkroYqnH3lK9nLgI46scnf8Cn22kBA==)

---

**Related**

* [`` API reference](/api/built-in-components#transitiongroup)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/built-ins/transition-group.md)



## KeepAlive | Vue.js

[Read the full article](https://vuejs.org/guide/built-ins/keep-alive)

# KeepAlive [​](#keepalive)

`` is a built\-in component that allows us to conditionally cache component instances when dynamically switching between multiple components.

## Basic Usage [​](#basic-usage)

In the Component Basics chapter, we introduced the syntax for [Dynamic Components](/guide/essentials/component-basics#dynamic-components), using the `` special element:

template\`\`\`
\
\`\`\`By default, an active component instance will be unmounted when switching away from it. This will cause any changed state it holds to be lost. When this component is displayed again, a new instance will be created with only the initial state.

In the example below, we have two stateful components \- A contains a counter, while B contains a message synced with an input via `v-model`. Try updating the state of one of them, switch away, and then switch back to it:

 A BCurrent component: A

Count: 0\+You'll notice that when switched back, the previous changed state would have been reset.

Creating fresh component instance on switch is normally useful behavior, but in this case, we'd really like the two component instances to be preserved even when they are inactive. To solve this problem, we can wrap our dynamic component with the `` built\-in component:

template\`\`\`
\
\
 \
\
\`\`\`Now, the state will be persisted across component switches:

 A BCurrent component: A

Count: 0\+[Try it in the Playground](https://play.vuejs.org/#eNqtUsFOwzAM/RWrl4IGC+cqq2h3RFw495K12YhIk6hJi1DVf8dJSllBaAJxi+2XZz8/j0lhzHboeZIl1NadMA4sd73JKyVaozsHI9hnJqV+feJHmODY6RZS/JEuiL1uTTEXtiREnnINKFeAcgZUqtbKOqj7ruPKwe6s2VVguq4UJXEynAkDx1sjmeMYAdBGDFBLZu2uShre6ioJeaxIduAyp0KZ3oF7MxwRHWsEQmC4bXXDJWbmxpjLBiZ7DwptMUFyKCiJNP/BWUbO8gvnA+emkGKIgkKqRrRWfh+Z8MIWwpySpfbxn6wJKMGV4IuSs0UlN1HVJae7bxYvBuk+2IOIq7sLnph8P9u5DJv5VfpWWLaGqTzwZTCOM/M0IaMvBMihd04ruK+lqF/8Ajxms8EFbCiJxR8khsP6ncQosLWnWV6a/kUf2nqu75Fby04chA0iPftaYryhz6NBRLjdtajpHZTWPio=)

[Try it in the Playground](https://play.vuejs.org/#eNqtU8tugzAQ/JUVl7RKWveMXFTIseofcHHAiawasPxArRD/3rVNSEhbpVUrIWB3x7PM7jAkuVL3veNJmlBTaaFsVraiUZ22sO0alcNedw2s7kmIPHS1ABQLQDEBAMqWvwVQzffMSQuDz1aI6VreWpPCEBtsJppx4wE1s+zmNoIBNLdOt8cIjzut8XAKq3A0NAIY/QNveFEyi8DA8kZJZjlGALQWPVSSGfNYJjVvujIJeaxItuMyo6JVzoJ9VxwRmtUCIdDfNV3NJWam5j7HpPOY8BEYkwxySiLLP1AWkbK4oHzmXOVS9FFOSM3jhFR4WTNfRslcO54nSwJKcCD4RsnZmJJNFPXJEl8t88quOuc39fCrHalsGyWcnJL62apYNoq12UQ8DLEFjCMy+kKA7Jy1XQtPlRTVqx+Jx6zXOJI1JbH4jejg3T+KbswBzXnFlz9Tjes/V/3CjWEHDsL/OYNvdCE8Wu3kLUQEhy+ljh+brFFu)

TIP

When used in [in\-DOM templates](/guide/essentials/component-basics#in-dom-template-parsing-caveats), it should be referenced as ``.

## Include / Exclude [​](#include-exclude)

By default, `` will cache any component instance inside. We can customize this behavior via the `include` and `exclude` props. Both props can be a comma\-delimited string, a `RegExp`, or an array containing either types:

template\`\`\`
\
\
 \
\

\
\
 \
\

\
\
 \
\
\`\`\`The match is checked against the component's [`name`](/api/options-misc#name) option, so components that need to be conditionally cached by `KeepAlive` must explicitly declare a `name` option.

TIP

Since version 3\.2\.34, a single\-file component using `` will automatically infer its `name` option based on the filename, removing the need to manually declare the name.

## Max Cached Instances [​](#max-cached-instances)

We can limit the maximum number of component instances that can be cached via the `max` prop. When `max` is specified, `` behaves like an [LRU cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)): if the number of cached instances is about to exceed the specified max count, the least recently accessed cached instance will be destroyed to make room for the new one.

template\`\`\`
\
 \
\
\`\`\`## Lifecycle of Cached Instance [​](#lifecycle-of-cached-instance)

When a component instance is removed from the DOM but is part of a component tree cached by ``, it goes into a **deactivated** state instead of being unmounted. When a component instance is inserted into the DOM as part of a cached tree, it is **activated**.

A kept\-alive component can register lifecycle hooks for these two states using [`onActivated()`](/api/composition-api-lifecycle#onactivated) and [`onDeactivated()`](/api/composition-api-lifecycle#ondeactivated):

vue\`\`\`
\
import { onActivated, onDeactivated } from 'vue'

onActivated(() =\> {
 // called on initial mount
 // and every time it is re\-inserted from the cache
})

onDeactivated(() =\> {
 // called when removed from the DOM into the cache
 // and also when unmounted
})
\
\`\`\`A kept\-alive component can register lifecycle hooks for these two states using [`activated`](/api/options-lifecycle#activated) and [`deactivated`](/api/options-lifecycle#deactivated) hooks:

js\`\`\`
export default {
 activated() {
 // called on initial mount
 // and every time it is re\-inserted from the cache
 },
 deactivated() {
 // called when removed from the DOM into the cache
 // and also when unmounted
 }
}
\`\`\`Note that:

* `onActivated``activated` is also called on mount, and `onDeactivated``deactivated` on unmount.
* Both hooks work for not only the root component cached by ``, but also the descendant components in the cached tree.

---

**Related**

* [`` API reference](/api/built-in-components#keepalive)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/built-ins/keep-alive.md)



## Fallthrough Attributes | Vue.js

[Read the full article](https://vuejs.org/guide/components/attrs)

# Fallthrough Attributes [​](#fallthrough-attributes)

> This page assumes you've already read the [Components Basics](/guide/essentials/component-basics). Read that first if you are new to components.

## Attribute Inheritance [​](#attribute-inheritance)

A "fallthrough attribute" is an attribute or `v-on` event listener that is passed to a component, but is not explicitly declared in the receiving component's [props](/guide/components/props) or [emits](/guide/components/events#declaring-emitted-events). Common examples of this include `class`, `style`, and `id` attributes.

When a component renders a single root element, fallthrough attributes will be automatically added to the root element's attributes. For example, given a `` component with the following template:

template\`\`\`
\ \-\-\>
\Click Me\
\`\`\`And a parent using this component with:

template\`\`\`
\
\`\`\`The final rendered DOM would be:

html\`\`\`
\Click Me\
\`\`\`Here, `` did not declare `class` as an accepted prop. Therefore, `class` is treated as a fallthrough attribute and automatically added to ``'s root element.

### `class` and `style` Merging [​](#class-and-style-merging)

If the child component's root element already has existing `class` or `style` attributes, it will be merged with the `class` and `style` values that are inherited from the parent. Suppose we change the template of `` in the previous example to:

template\`\`\`
\ \-\-\>
\Click Me\
\`\`\`Then the final rendered DOM would now become:

html\`\`\`
\Click Me\
\`\`\`### `v-on` Listener Inheritance [​](#v-on-listener-inheritance)

The same rule applies to `v-on` event listeners:

template\`\`\`
\
\`\`\`The `click` listener will be added to the root element of ``, i.e. the native `` element. When the native `` is clicked, it will trigger the `onClick` method of the parent component. If the native `` already has a `click` listener bound with `v-on`, then both listeners will trigger.

### Nested Component Inheritance [​](#nested-component-inheritance)

If a component renders another component as its root node, for example, we refactored `` to render a `` as its root:

template\`\`\`
\ that simply renders another component \-\-\>
\
\`\`\`Then the fallthrough attributes received by `` will be automatically forwarded to ``.

Note that:

1. Forwarded attributes do not include any attributes that are declared as props, or `v-on` listeners of declared events by `` \- in other words, the declared props and listeners have been "consumed" by ``.
2. Forwarded attributes may be accepted as props by ``, if declared by it.

## Disabling Attribute Inheritance [​](#disabling-attribute-inheritance)

If you do **not** want a component to automatically inherit attributes, you can set `inheritAttrs: false` in the component's options.

Since 3\.3 you can also use [`defineOptions`](/api/sfc-script-setup#defineoptions) directly in ``:

vue\`\`\`
\
defineOptions({
 inheritAttrs: false
})
// ...setup logic
\
\`\`\`The common scenario for disabling attribute inheritance is when attributes need to be applied to other elements besides the root node. By setting the `inheritAttrs` option to `false`, you can take full control over where the fallthrough attributes should be applied.

These fallthrough attributes can be accessed directly in template expressions as `$attrs`:

template\`\`\`
\Fallthrough attributes: {{ $attrs }}\
\`\`\`The `$attrs` object includes all attributes that are not declared by the component's `props` or `emits` options (e.g., `class`, `style`, `v-on` listeners, etc.).

Some notes:

* Unlike props, fallthrough attributes preserve their original casing in JavaScript, so an attribute like `foo-bar` needs to be accessed as `$attrs['foo-bar']`.
* A `v-on` event listener like `@click` will be exposed on the object as a function under `$attrs.onClick`.

Using our `` component example from the [previous section](#attribute-inheritance) \- sometimes we may need to wrap the actual `` element with an extra `` for styling purposes:

template\`\`\`
\
 \Click Me\
\
\`\`\`We want all fallthrough attributes like `class` and `v-on` listeners to be applied to the inner ``, not the outer ``. We can achieve this with `inheritAttrs: false` and `v-bind="$attrs"`:

template\`\`\`
\
 \Click Me\
\
\`\`\`Remember that [`v-bind` without an argument](/guide/essentials/template-syntax#dynamically-binding-multiple-attributes) binds all the properties of an object as attributes of the target element.

## Attribute Inheritance on Multiple Root Nodes [​](#attribute-inheritance-on-multiple-root-nodes)

Unlike components with a single root node, components with multiple root nodes do not have an automatic attribute fallthrough behavior. If `$attrs` are not bound explicitly, a runtime warning will be issued.

template\`\`\`
\
\`\`\`If `` has the following multi\-root template, there will be a warning because Vue cannot be sure where to apply the fallthrough attributes:

template\`\`\`
\...\
\...\
\...\
\`\`\`The warning will be suppressed if `$attrs` is explicitly bound:

template\`\`\`
\...\
\...\
\...\
\`\`\`## Accessing Fallthrough Attributes in JavaScript [​](#accessing-fallthrough-attributes-in-javascript)

If needed, you can access a component's fallthrough attributes in `` using the `useAttrs()` API:

vue\`\`\`
\
import { useAttrs } from 'vue'

const attrs = useAttrs()
\
\`\`\`If not using ``, `attrs` will be exposed as a property of the `setup()` context:

js\`\`\`
export default {
 setup(props, ctx) {
 // fallthrough attributes are exposed as ctx.attrs
 console.log(ctx.attrs)
 }
}
\`\`\`Note that although the `attrs` object here always reflects the latest fallthrough attributes, it isn't reactive (for performance reasons). You cannot use watchers to observe its changes. If you need reactivity, use a prop. Alternatively, you can use `onUpdated()` to perform side effects with the latest `attrs` on each update.

If needed, you can access a component's fallthrough attributes via the `$attrs` instance property:

js\`\`\`
export default {
 created() {
 console.log(this.$attrs)
 }
}
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/attrs.md)



## Options: State | Vue.js

[Read the full article](https://vuejs.org/api/options-state)

# Options: State [​](#options-state)

## data [​](#data)

A function that returns the initial reactive state for the component instance.

* **Type**

ts\`\`\`
interface ComponentOptions {
 data?(
 this: ComponentPublicInstance,
 vm: ComponentPublicInstance
 ): object
}
\`\`\`
* **Details**

The function is expected to return a plain JavaScript object, which will be made reactive by Vue. After the instance is created, the reactive data object can be accessed as `this.$data`. The component instance also proxies all the properties found on the data object, so `this.a` will be equivalent to `this.$data.a`.

All top\-level data properties must be included in the returned data object. Adding new properties to `this.$data` is possible, but it is **not** recommended. If the desired value of a property is not yet available then an empty value such as `undefined` or `null` should be included as a placeholder to ensure that Vue knows that the property exists.

Properties that start with `_` or `$` will **not** be proxied on the component instance because they may conflict with Vue's internal properties and API methods. You will have to access them as `this.$data._property`.

It is **not** recommended to return objects with their own stateful behavior like browser API objects and prototype properties. The returned object should ideally be a plain object that only represents the state of the component.
* **Example**

js\`\`\`
export default {
 data() {
 return { a: 1 }
 },
 created() {
 console.log(this.a) // 1
 console.log(this.$data) // { a: 1 }
 }
}
\`\`\`Note that if you use an arrow function with the `data` property, `this` won't be the component's instance, but you can still access the instance as the function's first argument:

js\`\`\`
data: (vm) =\> ({ a: vm.myProp })
\`\`\`
* **See also** [Reactivity in Depth](/guide/extras/reactivity-in-depth)

## props [​](#props)

Declare the props of a component.

* **Type**

ts\`\`\`
interface ComponentOptions {
 props?: ArrayPropsOptions \| ObjectPropsOptions
}

type ArrayPropsOptions = string\[]

type ObjectPropsOptions = { \[key: string]: Prop }

type Prop\ = PropOptions\ \| PropType\ \| null

interface PropOptions\ {
 type?: PropType\
 required?: boolean
 default?: T \| ((rawProps: object) =\> T)
 validator?: (value: unknown, rawProps: object) =\> boolean
}

type PropType\ = { new (): T } \| { new (): T }\[]
\`\`\`
> Types are simplified for readability.
* **Details**

In Vue, all component props need to be explicitly declared. Component props can be declared in two forms:

	+ Simple form using an array of strings
	+ Full form using an object where each property key is the name of the prop, and the value is the prop's type (a constructor function) or advanced options.With object\-based syntax, each prop can further define the following options:

	+ **`type`**: Can be one of the following native constructors: `String`, `Number`, `Boolean`, `Array`, `Object`, `Date`, `Function`, `Symbol`, any custom constructor function or an array of those. In development mode, Vue will check if a prop's value matches the declared type, and will throw a warning if it doesn't. See [Prop Validation](/guide/components/props#prop-validation) for more details.

	Also note that a prop with `Boolean` type affects its value casting behavior in both development and production. See [Boolean Casting](/guide/components/props#boolean-casting) for more details.
	+ **`default`**: Specifies a default value for the prop when it is not passed by the parent or has `undefined` value. Object or array defaults must be returned using a factory function. The factory function also receives the raw props object as the argument.
	+ **`required`**: Defines if the prop is required. In a non\-production environment, a console warning will be thrown if this value is truthy and the prop is not passed.
	+ **`validator`**: Custom validator function that takes the prop value as the sole argument. In development mode, a console warning will be thrown if this function returns a falsy value (i.e. the validation fails).
* **Example**

Simple declaration:

js\`\`\`
export default {
 props: \['size', 'myMessage']
}
\`\`\`Object declaration with validations:

js\`\`\`
export default {
 props: {
 // type check
 height: Number,
 // type check plus other validations
 age: {
 type: Number,
 default: 0,
 required: true,
 validator: (value) =\> {
 return value \>= 0
 }
 }
 }
}
\`\`\`
* **See also**

	+ [Guide \- Props](/guide/components/props)
	+ [Guide \- Typing Component Props](/guide/typescript/options-api#typing-component-props)

## computed [​](#computed)

Declare computed properties to be exposed on the component instance.

* **Type**

ts\`\`\`
interface ComponentOptions {
 computed?: {
 \[key: string]: ComputedGetter\ \| WritableComputedOptions\
 }
}

type ComputedGetter\ = (
 this: ComponentPublicInstance,
 vm: ComponentPublicInstance
) =\> T

type ComputedSetter\ = (
 this: ComponentPublicInstance,
 value: T
) =\> void

type WritableComputedOptions\ = {
 get: ComputedGetter\
 set: ComputedSetter\
}
\`\`\`
* **Details**

The option accepts an object where the key is the name of the computed property, and the value is either a computed getter, or an object with `get` and `set` methods (for writable computed properties).

All getters and setters have their `this` context automatically bound to the component instance.

Note that if you use an arrow function with a computed property, `this` won't point to the component's instance, but you can still access the instance as the function's first argument:

js\`\`\`
export default {
 computed: {
 aDouble: (vm) =\> vm.a \* 2
 }
}
\`\`\`
* **Example**

js\`\`\`
export default {
 data() {
 return { a: 1 }
 },
 computed: {
 // readonly
 aDouble() {
 return this.a \* 2
 },
 // writable
 aPlus: {
 get() {
 return this.a \+ 1
 },
 set(v) {
 this.a = v \- 1
 }
 }
 },
 created() {
 console.log(this.aDouble) // =\> 2
 console.log(this.aPlus) // =\> 2

 this.aPlus = 3
 console.log(this.a) // =\> 2
 console.log(this.aDouble) // =\> 4
 }
}
\`\`\`
* **See also**

	+ [Guide \- Computed Properties](/guide/essentials/computed)
	+ [Guide \- Typing Computed Properties](/guide/typescript/options-api#typing-computed-properties)

## methods [​](#methods)

Declare methods to be mixed into the component instance.

* **Type**

ts\`\`\`
interface ComponentOptions {
 methods?: {
 \[key: string]: (this: ComponentPublicInstance, ...args: any\[]) =\> any
 }
}
\`\`\`
* **Details**

Declared methods can be directly accessed on the component instance, or used in template expressions. All methods have their `this` context automatically bound to the component instance, even when passed around.

Avoid using arrow functions when declaring methods, as they will not have access to the component instance via `this`.
* **Example**

js\`\`\`
export default {
 data() {
 return { a: 1 }
 },
 methods: {
 plus() {
 this.a\+\+
 }
 },
 created() {
 this.plus()
 console.log(this.a) // =\> 2
 }
}
\`\`\`
* **See also** [Event Handling](/guide/essentials/event-handling)

## watch [​](#watch)

Declare watch callbacks to be invoked on data change.

* **Type**

ts\`\`\`
interface ComponentOptions {
 watch?: {
 \[key: string]: WatchOptionItem \| WatchOptionItem\[]
 }
}

type WatchOptionItem = string \| WatchCallback \| ObjectWatchOptionItem

type WatchCallback\ = (
 value: T,
 oldValue: T,
 onCleanup: (cleanupFn: () =\> void) =\> void
) =\> void

type ObjectWatchOptionItem = {
 handler: WatchCallback \| string
 immediate?: boolean // default: false
 deep?: boolean // default: false
 flush?: 'pre' \| 'post' \| 'sync' // default: 'pre'
 onTrack?: (event: DebuggerEvent) =\> void
 onTrigger?: (event: DebuggerEvent) =\> void
}
\`\`\`
> Types are simplified for readability.
* **Details**

The `watch` option expects an object where keys are the reactive component instance properties to watch (e.g. properties declared via `data` or `computed`) — and values are the corresponding callbacks. The callback receives the new value and the old value of the watched source.

In addition to a root\-level property, the key can also be a simple dot\-delimited path, e.g. `a.b.c`. Note that this usage does **not** support complex expressions \- only dot\-delimited paths are supported. If you need to watch complex data sources, use the imperative [`$watch()`](/api/component-instance#watch) API instead.

The value can also be a string of a method name (declared via `methods`), or an object that contains additional options. When using the object syntax, the callback should be declared under the `handler` field. Additional options include:

	+ **`immediate`**: trigger the callback immediately on watcher creation. Old value will be `undefined` on the first call.
	+ **`deep`**: force deep traversal of the source if it is an object or an array, so that the callback fires on deep mutations. See [Deep Watchers](/guide/essentials/watchers#deep-watchers).
	+ **`flush`**: adjust the callback's flush timing. See [Callback Flush Timing](/guide/essentials/watchers#callback-flush-timing) and [`watchEffect()`](/api/reactivity-core#watcheffect).
	+ **`onTrack / onTrigger`**: debug the watcher's dependencies. See [Watcher Debugging](/guide/extras/reactivity-in-depth#watcher-debugging).Avoid using arrow functions when declaring watch callbacks as they will not have access to the component instance via `this`.
* **Example**

js\`\`\`
export default {
 data() {
 return {
 a: 1,
 b: 2,
 c: {
 d: 4
 },
 e: 5,
 f: 6
 }
 },
 watch: {
 // watching top\-level property
 a(val, oldVal) {
 console.log(\`new: ${val}, old: ${oldVal}\`)
 },
 // string method name
 b: 'someMethod',
 // the callback will be called whenever any of the watched object properties change regardless of their nested depth
 c: {
 handler(val, oldVal) {
 console.log('c changed')
 },
 deep: true
 },
 // watching a single nested property:
 'c.d': function (val, oldVal) {
 // do something
 },
 // the callback will be called immediately after the start of the observation
 e: {
 handler(val, oldVal) {
 console.log('e changed')
 },
 immediate: true
 },
 // you can pass array of callbacks, they will be called one\-by\-one
 f: \[
 'handle1',
 function handle2(val, oldVal) {
 console.log('handle2 triggered')
 },
 {
 handler: function handle3(val, oldVal) {
 console.log('handle3 triggered')
 }
 /\* ... \*/
 }
 ]
 },
 methods: {
 someMethod() {
 console.log('b changed')
 },
 handle1() {
 console.log('handle 1 triggered')
 }
 },
 created() {
 this.a = 3 // =\> new: 3, old: 1
 }
}
\`\`\`
* **See also** [Watchers](/guide/essentials/watchers)

## emits [​](#emits)

Declare the custom events emitted by the component.

* **Type**

ts\`\`\`
interface ComponentOptions {
 emits?: ArrayEmitsOptions \| ObjectEmitsOptions
}

type ArrayEmitsOptions = string\[]

type ObjectEmitsOptions = { \[key: string]: EmitValidator \| null }

type EmitValidator = (...args: unknown\[]) =\> boolean
\`\`\`
* **Details**

Emitted events can be declared in two forms:

	+ Simple form using an array of strings
	+ Full form using an object where each property key is the name of the event, and the value is either `null` or a validator function.The validation function will receive the additional arguments passed to the component's `$emit` call. For example, if `this.$emit('foo', 1)` is called, the corresponding validator for `foo` will receive the argument `1`. The validator function should return a boolean to indicate whether the event arguments are valid.

Note that the `emits` option affects which event listeners are considered component event listeners, rather than native DOM event listeners. The listeners for declared events will be removed from the component's `$attrs` object, so they will not be passed through to the component's root element. See [Fallthrough Attributes](/guide/components/attrs) for more details.
* **Example**

Array syntax:

js\`\`\`
export default {
 emits: \['check'],
 created() {
 this.$emit('check')
 }
}
\`\`\`Object syntax:

js\`\`\`
export default {
 emits: {
 // no validation
 click: null,

 // with validation
 submit: (payload) =\> {
 if (payload.email \&\& payload.password) {
 return true
 } else {
 console.warn(\`Invalid submit event payload!\`)
 return false
 }
 }
 }
}
\`\`\`
* **See also**

	+ [Guide \- Fallthrough Attributes](/guide/components/attrs)
	+ [Guide \- Typing Component Emits](/guide/typescript/options-api#typing-component-emits)

## expose [​](#expose)

Declare exposed public properties when the component instance is accessed by a parent via template refs.

* **Type**

ts\`\`\`
interface ComponentOptions {
 expose?: string\[]
}
\`\`\`
* **Details**

By default, a component instance exposes all instance properties to the parent when accessed via `$parent`, `$root`, or template refs. This can be undesirable, since a component most likely has internal state or methods that should be kept private to avoid tight coupling.

The `expose` option expects a list of property name strings. When `expose` is used, only the properties explicitly listed will be exposed on the component's public instance.

`expose` only affects user\-defined properties \- it does not filter out built\-in component instance properties.
* **Example**

js\`\`\`
export default {
 // only \`publicMethod\` will be available on the public instance
 expose: \['publicMethod'],
 methods: {
 publicMethod() {
 // ...
 },
 privateMethod() {
 // ...
 }
 }
}
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/options-state.md)



## Using Vue with TypeScript | Vue.js

[Read the full article](https://vuejs.org/guide/typescript/overview)

# Using Vue with TypeScript [​](#using-vue-with-typescript)

A type system like TypeScript can detect many common errors via static analysis at build time. This reduces the chance of runtime errors in production, and also allows us to more confidently refactor code in large\-scale applications. TypeScript also improves developer ergonomics via type\-based auto\-completion in IDEs.

Vue is written in TypeScript itself and provides first\-class TypeScript support. All official Vue packages come with bundled type declarations that should work out\-of\-the\-box.

## Project Setup [​](#project-setup)

[`create-vue`](https://github.com/vuejs/create-vue), the official project scaffolding tool, offers the options to scaffold a [Vite](https://vitejs.dev/)\-powered, TypeScript\-ready Vue project.

### Overview [​](#overview)

With a Vite\-based setup, the dev server and the bundler are transpilation\-only and do not perform any type\-checking. This ensures the Vite dev server stays blazing fast even when using TypeScript.

* During development, we recommend relying on a good [IDE setup](#ide-support) for instant feedback on type errors.
* If using SFCs, use the [`vue-tsc`](https://github.com/vuejs/language-tools/tree/master/packages/tsc) utility for command line type checking and type declaration generation. `vue-tsc` is a wrapper around `tsc`, TypeScript's own command line interface. It works largely the same as `tsc` except that it supports Vue SFCs in addition to TypeScript files. You can run `vue-tsc` in watch mode in parallel to the Vite dev server, or use a Vite plugin like [vite\-plugin\-checker](https://vite-plugin-checker.netlify.app/) which runs the checks in a separate worker thread.
* Vue CLI also provides TypeScript support, but is no longer recommended. See [notes below](#note-on-vue-cli-and-ts-loader).

### IDE Support [​](#ide-support)

* [Visual Studio Code](https://code.visualstudio.com/) (VS Code) is strongly recommended for its great out\-of\-the\-box support for TypeScript.

	+ [Vue \- Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (previously Volar) is the official VS Code extension that provides TypeScript support inside Vue SFCs, along with many other great features.

	TIP

	Vue \- Official extension replaces [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur), our previous official VS Code extension for Vue 2\. If you have Vetur currently installed, make sure to disable it in Vue 3 projects.
* [WebStorm](https://www.jetbrains.com/webstorm/) also provides out\-of\-the\-box support for both TypeScript and Vue. Other JetBrains IDEs support them too, either out of the box or via [a free plugin](https://plugins.jetbrains.com/plugin/9442-vue-js). As of version 2023\.2, WebStorm and the Vue Plugin come with built\-in support for the Vue Language Server. You can set the Vue service to use Volar integration on all TypeScript versions, under Settings \> Languages \& Frameworks \> TypeScript \> Vue. By default, Volar will be used for TypeScript versions 5\.0 and higher.

### Configuring `tsconfig.json` [​](#configuring-tsconfig-json)

Projects scaffolded via `create-vue` include pre\-configured `tsconfig.json`. The base config is abstracted in the [`@vue/tsconfig`](https://github.com/vuejs/tsconfig) package. Inside the project, we use [Project References](https://www.typescriptlang.org/docs/handbook/project-references.html) to ensure correct types for code running in different environments (e.g. app code and test code should have different global variables).

When configuring `tsconfig.json` manually, some notable options include:

* [`compilerOptions.isolatedModules`](https://www.typescriptlang.org/tsconfig#isolatedModules) is set to `true` because Vite uses [esbuild](https://esbuild.github.io/) for transpiling TypeScript and is subject to single\-file transpile limitations. [`compilerOptions.verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig#verbatimModuleSyntax) is [a superset of `isolatedModules`](https://github.com/microsoft/TypeScript/issues/53601) and is a good choice, too \- it's what [`@vue/tsconfig`](https://github.com/vuejs/tsconfig) uses.
* If you're using Options API, you need to set [`compilerOptions.strict`](https://www.typescriptlang.org/tsconfig#strict) to `true` (or at least enable [`compilerOptions.noImplicitThis`](https://www.typescriptlang.org/tsconfig#noImplicitThis), which is a part of the `strict` flag) to leverage type checking of `this` in component options. Otherwise `this` will be treated as `any`.
* If you have configured resolver aliases in your build tool, for example the `@/*` alias configured by default in a `create-vue` project, you need to also configure it for TypeScript via [`compilerOptions.paths`](https://www.typescriptlang.org/tsconfig#paths).
* If you intend to use TSX with Vue, set [`compilerOptions.jsx`](https://www.typescriptlang.org/tsconfig#jsx) to `"preserve"`, and set [`compilerOptions.jsxImportSource`](https://www.typescriptlang.org/tsconfig#jsxImportSource) to `"vue"`.

See also:

* [Official TypeScript compiler options docs](https://www.typescriptlang.org/docs/handbook/compiler-options.html)
* [esbuild TypeScript compilation caveats](https://esbuild.github.io/content-types/#typescript-caveats)

### Note on Vue CLI and `ts-loader` [​](#note-on-vue-cli-and-ts-loader)

In webpack\-based setups such as Vue CLI, it is common to perform type checking as part of the module transform pipeline, for example with `ts-loader`. This, however, isn't a clean solution because the type system needs knowledge of the entire module graph to perform type checks. Individual module's transform step simply is not the right place for the task. It leads to the following problems:

* `ts-loader` can only type check post\-transform code. This doesn't align with the errors we see in IDEs or from `vue-tsc`, which map directly back to the source code.
* Type checking can be slow. When it is performed in the same thread / process with code transformations, it significantly affects the build speed of the entire application.
* We already have type checking running right in our IDE in a separate process, so the cost of dev experience slow down simply isn't a good trade\-off.

If you are currently using Vue 3 \+ TypeScript via Vue CLI, we strongly recommend migrating over to Vite. We are also working on CLI options to enable transpile\-only TS support, so that you can switch to `vue-tsc` for type checking.

## General Usage Notes [​](#general-usage-notes)

### `defineComponent()` [​](#definecomponent)

To let TypeScript properly infer types inside component options, we need to define components with [`defineComponent()`](/api/general#definecomponent):

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 // type inference enabled
 props: {
 name: String,
 msg: { type: String, required: true }
 },
 data() {
 return {
 count: 1
 }
 },
 mounted() {
 this.name // type: string \| undefined
 this.msg // type: string
 this.count // type: number
 }
})
\`\`\``defineComponent()` also supports inferring the props passed to `setup()` when using Composition API without ``:

ts\`\`\`
import { defineComponent } from 'vue'

export default defineComponent({
 // type inference enabled
 props: {
 message: String
 },
 setup(props) {
 props.message // type: string \| undefined
 }
})
\`\`\`See also:

* [Note on webpack Treeshaking](/api/general#note-on-webpack-treeshaking)
* [type tests for `defineComponent`](https://github.com/vuejs/core/blob/main/packages-private/dts-test/defineComponent.test-d.tsx)

TIP

`defineComponent()` also enables type inference for components defined in plain JavaScript.

### Usage in Single\-File Components [​](#usage-in-single-file-components)

To use TypeScript in SFCs, add the `lang="ts"` attribute to `` tags. When `lang="ts"` is present, all template expressions also enjoy stricter type checking.

vue\`\`\`
\
import { defineComponent } from 'vue'

export default defineComponent({
 data() {
 return {
 count: 1
 }
 }
})
\

\
 \
 {{ count.toFixed(2\) }}
\
\`\`\``lang="ts"` can also be used with ``:

vue\`\`\`
\
// TypeScript enabled
import { ref } from 'vue'

const count = ref(1\)
\

\
 \
 {{ count.toFixed(2\) }}
\
\`\`\`### TypeScript in Templates [​](#typescript-in-templates)

The `` also supports TypeScript in binding expressions when `` or `` is used. This is useful in cases where you need to perform type casting in template expressions.

Here's a contrived example:

vue\`\`\`
\
let x: string \| number = 1
\

\
 \
 {{ x.toFixed(2\) }}
\
\`\`\`This can be worked around with an inline type cast:

vue\`\`\`
\
let x: string \| number = 1
\

\
 {{ (x as number).toFixed(2\) }}
\
\`\`\`TIP

If using Vue CLI or a webpack\-based setup, TypeScript in template expressions requires `vue-loader@^16.8.0`.

### Usage with TSX [​](#usage-with-tsx)

Vue also supports authoring components with JSX / TSX. Details are covered in the [Render Function \& JSX](/guide/extras/render-function#jsx-tsx) guide.

## Generic Components [​](#generic-components)

Generic components are supported in two cases:

* In SFCs: [`` with the `generic` attribute](/api/sfc-script-setup#generics)
* Render function / JSX components: [`defineComponent()`'s function signature](/api/general#function-signature)

## API\-Specific Recipes [​](#api-specific-recipes)

* [TS with Composition API](/guide/typescript/composition-api)
* [TS with Options API](/guide/typescript/options-api)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/typescript/overview.md)



## Built-in Components | Vue.js

[Read the full article](https://vuejs.org/api/built-in-components)

# Built\-in Components [​](#built-in-components)

Registration and Usage

Built\-in components can be used directly in templates without needing to be registered. They are also tree\-shakeable: they are only included in the build when they are used.

When using them in [render functions](/guide/extras/render-function), they need to be imported explicitly. For example:

js\`\`\`
import { h, Transition } from 'vue'

h(Transition, {
 /\* props \*/
})
\`\`\`## `` [​](#transition)

Provides animated transition effects to a **single** element or component.

* **Props**

ts\`\`\`
interface TransitionProps {
 /\*\*
 \* Used to automatically generate transition CSS class names.
 \* e.g. \`name: 'fade'\` will auto expand to \`.fade\-enter\`,
 \* \`.fade\-enter\-active\`, etc.
 \*/
 name?: string
 /\*\*
 \* Whether to apply CSS transition classes.
 \* Default: true
 \*/
 css?: boolean
 /\*\*
 \* Specifies the type of transition events to wait for to
 \* determine transition end timing.
 \* Default behavior is auto detecting the type that has
 \* longer duration.
 \*/
 type?: 'transition' \| 'animation'
 /\*\*
 \* Specifies explicit durations of the transition.
 \* Default behavior is wait for the first \`transitionend\`
 \* or \`animationend\` event on the root transition element.
 \*/
 duration?: number \| { enter: number; leave: number }
 /\*\*
 \* Controls the timing sequence of leaving/entering transitions.
 \* Default behavior is simultaneous.
 \*/
 mode?: 'in\-out' \| 'out\-in' \| 'default'
 /\*\*
 \* Whether to apply transition on initial render.
 \* Default: false
 \*/
 appear?: boolean

 /\*\*
 \* Props for customizing transition classes.
 \* Use kebab\-case in templates, e.g. enter\-from\-class="xxx"
 \*/
 enterFromClass?: string
 enterActiveClass?: string
 enterToClass?: string
 appearFromClass?: string
 appearActiveClass?: string
 appearToClass?: string
 leaveFromClass?: string
 leaveActiveClass?: string
 leaveToClass?: string
}
\`\`\`
* **Events**

	+ `@before-enter`
	+ `@before-leave`
	+ `@enter`
	+ `@leave`
	+ `@appear`
	+ `@after-enter`
	+ `@after-leave`
	+ `@after-appear`
	+ `@enter-cancelled`
	+ `@leave-cancelled` (`v-show` only)
	+ `@appear-cancelled`
* **Example**

Simple element:

template\`\`\`
\
 \toggled content\
\
\`\`\`Forcing a transition by changing the `key` attribute:

template\`\`\`
\
 \{{ text }}\
\
\`\`\`Dynamic component, with transition mode \+ animate on appear:

template\`\`\`
\
 \\
\
\`\`\`Listening to transition events:

template\`\`\`
\
 \toggled content\
\
\`\`\`
* **See also** [Guide \- Transition](/guide/built-ins/transition)

## `` [​](#transitiongroup)

Provides transition effects for **multiple** elements or components in a list.

* **Props**

`` accepts the same props as `` except `mode`, plus two additional props:

ts\`\`\`
interface TransitionGroupProps extends Omit\ {
 /\*\*
 \* If not defined, renders as a fragment.
 \*/
 tag?: string
 /\*\*
 \* For customizing the CSS class applied during move transitions.
 \* Use kebab\-case in templates, e.g. move\-class="xxx"
 \*/
 moveClass?: string
}
\`\`\`
* **Events**

`` emits the same events as ``.
* **Details**

By default, `` doesn't render a wrapper DOM element, but one can be defined via the `tag` prop.

Note that every child in a `` must be [**uniquely keyed**](/guide/essentials/list#maintaining-state-with-key) for the animations to work properly.

`` supports moving transitions via CSS transform. When a child's position on screen has changed after an update, it will get applied a moving CSS class (auto generated from the `name` attribute or configured with the `move-class` prop). If the CSS `transform` property is "transition\-able" when the moving class is applied, the element will be smoothly animated to its destination using the [FLIP technique](https://aerotwist.com/blog/flip-your-animations/).
* **Example**

template\`\`\`
\
 \
 {{ item.text }}
 \
\
\`\`\`
* **See also** [Guide \- TransitionGroup](/guide/built-ins/transition-group)

## `` [​](#keepalive)

Caches dynamically toggled components wrapped inside.

* **Props**

ts\`\`\`
interface KeepAliveProps {
 /\*\*
 \* If specified, only components with names matched by
 \* \`include\` will be cached.
 \*/
 include?: MatchPattern
 /\*\*
 \* Any component with a name matched by \`exclude\` will
 \* not be cached.
 \*/
 exclude?: MatchPattern
 /\*\*
 \* The maximum number of component instances to cache.
 \*/
 max?: number \| string
}

type MatchPattern = string \| RegExp \| (string \| RegExp)\[]
\`\`\`
* **Details**

When wrapped around a dynamic component, `` caches the inactive component instances without destroying them.

There can only be one active component instance as the direct child of `` at any time.

When a component is toggled inside ``, its `activated` and `deactivated` lifecycle hooks will be invoked accordingly, providing an alternative to `mounted` and `unmounted`, which are not called. This applies to the direct child of `` as well as to all of its descendants.
* **Example**

Basic usage:

template\`\`\`
\
 \\
\
\`\`\`When used with `v-if` / `v-else` branches, there must be only one component rendered at a time:

template\`\`\`
\
 \ 1"\>\
 \\
\
\`\`\`Used together with ``:

template\`\`\`
\
 \
 \\
 \
\
\`\`\`Using `include` / `exclude`:

template\`\`\`
\
\
 \\
\

\
\
 \\
\

\
\
 \\
\
\`\`\`Usage with `max`:

template\`\`\`
\
 \\
\
\`\`\`
* **See also** [Guide \- KeepAlive](/guide/built-ins/keep-alive)

## `` [​](#teleport)

Renders its slot content to another part of the DOM.

* **Props**

ts\`\`\`
interface TeleportProps {
 /\*\*
 \* Required. Specify target container.
 \* Can either be a selector or an actual element.
 \*/
 to: string \| HTMLElement
 /\*\*
 \* When \`true\`, the content will remain in its original
 \* location instead of moved into the target container.
 \* Can be changed dynamically.
 \*/
 disabled?: boolean
 /\*\*
 \* When \`true\`, the Teleport will defer until other
 \* parts of the application have been mounted before
 \* resolving its target. (3\.5\+)
 \*/
 defer?: boolean
}
\`\`\`
* **Example**

Specifying target container:

template\`\`\`
\
\
\
\`\`\`Conditionally disabling:

template\`\`\`
\
 \
\
\`\`\`Defer target resolution :

template\`\`\`
\...\

\
\\
\`\`\`
* **See also** [Guide \- Teleport](/guide/built-ins/teleport)

## ``  [​](#suspense)

Used for orchestrating nested async dependencies in a component tree.

* **Props**

ts\`\`\`
interface SuspenseProps {
 timeout?: string \| number
 suspensible?: boolean
}
\`\`\`
* **Events**

	+ `@resolve`
	+ `@pending`
	+ `@fallback`
* **Details**

`` accepts two slots: the `#default` slot and the `#fallback` slot. It will display the content of the fallback slot while rendering the default slot in memory.

If it encounters async dependencies ([Async Components](/guide/components/async) and components with [`async setup()`](/guide/built-ins/suspense#async-setup)) while rendering the default slot, it will wait until all of them are resolved before displaying the default slot.

By setting the Suspense as `suspensible`, all the async dependency handling will be handled by the parent Suspense. See [implementation details](https://github.com/vuejs/core/pull/6736)
* **See also** [Guide \- Suspense](/guide/built-ins/suspense)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/built-in-components.md)



## Reactivity API: Utilities | Vue.js

[Read the full article](https://vuejs.org/api/reactivity-utilities)

# Reactivity API: Utilities [​](#reactivity-api-utilities)

## isRef() [​](#isref)

Checks if a value is a ref object.

* **Type**

ts\`\`\`
function isRef\(r: Ref\ \| unknown): r is Ref\
\`\`\`Note the return type is a [type predicate](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates), which means `isRef` can be used as a type guard:

ts\`\`\`
let foo: unknown
if (isRef(foo)) {
 // foo's type is narrowed to Ref\
 foo.value
}
\`\`\`

## unref() [​](#unref)

Returns the inner value if the argument is a ref, otherwise return the argument itself. This is a sugar function for `val = isRef(val) ? val.value : val`.

* **Type**

ts\`\`\`
function unref\(ref: T \| Ref\): T
\`\`\`
* **Example**

ts\`\`\`
function useFoo(x: number \| Ref\) {
 const unwrapped = unref(x)
 // unwrapped is guaranteed to be number now
}
\`\`\`

## toRef() [​](#toref)

Can be used to normalize values / refs / getters into refs (3\.3\+).

Can also be used to create a ref for a property on a source reactive object. The created ref is synced with its source property: mutating the source property will update the ref, and vice\-versa.

* **Type**

ts\`\`\`
// normalization signature (3\.3\+)
function toRef\(
 value: T
): T extends () =\> infer R
 ? Readonly\\>
 : T extends Ref
 ? T
 : Ref\\>

// object property signature
function toRef\(
 object: T,
 key: K,
 defaultValue?: T\[K]
): ToRef\

type ToRef\ = T extends Ref ? T : Ref\
\`\`\`
* **Example**

Normalization signature (3\.3\+):

js\`\`\`
// returns existing refs as\-is
toRef(existingRef)

// creates a readonly ref that calls the getter on .value access
toRef(() =\> props.foo)

// creates normal refs from non\-function values
// equivalent to ref(1\)
toRef(1\)
\`\`\`Object property signature:

js\`\`\`
const state = reactive({
 foo: 1,
 bar: 2
})

// a two\-way ref that syncs with the original property
const fooRef = toRef(state, 'foo')

// mutating the ref updates the original
fooRef.value\+\+
console.log(state.foo) // 2

// mutating the original also updates the ref
state.foo\+\+
console.log(fooRef.value) // 3
\`\`\`Note this is different from:

js\`\`\`
const fooRef = ref(state.foo)
\`\`\`The above ref is **not** synced with `state.foo`, because the `ref()` receives a plain number value.

`toRef()` is useful when you want to pass the ref of a prop to a composable function:

vue\`\`\`
\
import { toRef } from 'vue'

const props = defineProps(/\* ... \*/)

// convert \`props.foo\` into a ref, then pass into
// a composable
useSomeFeature(toRef(props, 'foo'))

// getter syntax \- recommended in 3\.3\+
useSomeFeature(toRef(() =\> props.foo))
\
\`\`\`When `toRef` is used with component props, the usual restrictions around mutating the props still apply. Attempting to assign a new value to the ref is equivalent to trying to modify the prop directly and is not allowed. In that scenario you may want to consider using [`computed`](/api/reactivity-core#computed) with `get` and `set` instead. See the guide to [using `v-model` with components](/guide/components/v-model) for more information.

When using the object property signature, `toRef()` will return a usable ref even if the source property doesn't currently exist. This makes it possible to work with optional properties, which wouldn't be picked up by [`toRefs`](#torefs).

## toValue() [​](#tovalue)

* Only supported in 3\.3\+

Normalizes values / refs / getters to values. This is similar to [unref()](#unref), except that it also normalizes getters. If the argument is a getter, it will be invoked and its return value will be returned.

This can be used in [Composables](/guide/reusability/composables) to normalize an argument that can be either a value, a ref, or a getter.

* **Type**

ts\`\`\`
function toValue\(source: T \| Ref\ \| (() =\> T)): T
\`\`\`
* **Example**

js\`\`\`
toValue(1\) // \-\-\> 1
toValue(ref(1\)) // \-\-\> 1
toValue(() =\> 1\) // \-\-\> 1
\`\`\`Normalizing arguments in composables:

ts\`\`\`
import type { MaybeRefOrGetter } from 'vue'

function useFeature(id: MaybeRefOrGetter\) {
 watch(() =\> toValue(id), id =\> {
 // react to id changes
 })
}

// this composable supports any of the following:
useFeature(1\)
useFeature(ref(1\))
useFeature(() =\> 1\)
\`\`\`

## toRefs() [​](#torefs)

Converts a reactive object to a plain object where each property of the resulting object is a ref pointing to the corresponding property of the original object. Each individual ref is created using [`toRef()`](#toref).

* **Type**

ts\`\`\`
function toRefs\(
 object: T
): {
 \[K in keyof T]: ToRef\
}

type ToRef = T extends Ref ? T : Ref\
\`\`\`
* **Example**

js\`\`\`
const state = reactive({
 foo: 1,
 bar: 2
})

const stateAsRefs = toRefs(state)
/\*
Type of stateAsRefs: {
 foo: Ref\,
 bar: Ref\
}
\*/

// The ref and the original property is "linked"
state.foo\+\+
console.log(stateAsRefs.foo.value) // 2

stateAsRefs.foo.value\+\+
console.log(state.foo) // 3
\`\`\``toRefs` is useful when returning a reactive object from a composable function so that the consuming component can destructure/spread the returned object without losing reactivity:

js\`\`\`
function useFeatureX() {
 const state = reactive({
 foo: 1,
 bar: 2
 })

 // ...logic operating on state

 // convert to refs when returning
 return toRefs(state)
}

// can destructure without losing reactivity
const { foo, bar } = useFeatureX()
\`\`\``toRefs` will only generate refs for properties that are enumerable on the source object at call time. To create a ref for a property that may not exist yet, use [`toRef`](#toref) instead.

## isProxy() [​](#isproxy)

Checks if an object is a proxy created by [`reactive()`](/api/reactivity-core#reactive), [`readonly()`](/api/reactivity-core#readonly), [`shallowReactive()`](/api/reactivity-advanced#shallowreactive) or [`shallowReadonly()`](/api/reactivity-advanced#shallowreadonly).

* **Type**

ts\`\`\`
function isProxy(value: any): boolean
\`\`\`

## isReactive() [​](#isreactive)

Checks if an object is a proxy created by [`reactive()`](/api/reactivity-core#reactive) or [`shallowReactive()`](/api/reactivity-advanced#shallowreactive).

* **Type**

ts\`\`\`
function isReactive(value: unknown): boolean
\`\`\`

## isReadonly() [​](#isreadonly)

Checks whether the passed value is a readonly object. The properties of a readonly object can change, but they can't be assigned directly via the passed object.

The proxies created by [`readonly()`](/api/reactivity-core#readonly) and [`shallowReadonly()`](/api/reactivity-advanced#shallowreadonly) are both considered readonly, as is a [`computed()`](/api/reactivity-core#computed) ref without a `set` function.

* **Type**

ts\`\`\`
function isReadonly(value: unknown): boolean
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/reactivity-utilities.md)



## Composition API: Lifecycle Hooks | Vue.js

[Read the full article](https://vuejs.org/api/composition-api-lifecycle)

# Composition API: Lifecycle Hooks [​](#composition-api-lifecycle-hooks)

Usage Note

All APIs listed on this page must be called synchronously during the `setup()` phase of a component. See [Guide \- Lifecycle Hooks](/guide/essentials/lifecycle) for more details.

## onMounted() [​](#onmounted)

Registers a callback to be called after the component has been mounted.

* **Type**

ts\`\`\`
function onMounted(callback: () =\> void): void
\`\`\`
* **Details**

A component is considered mounted after:

	+ All of its synchronous child components have been mounted (does not include async components or components inside `` trees).
	+ Its own DOM tree has been created and inserted into the parent container. Note it only guarantees that the component's DOM tree is in\-document if the application's root container is also in\-document.This hook is typically used for performing side effects that need access to the component's rendered DOM, or for limiting DOM\-related code to the client in a [server\-rendered application](/guide/scaling-up/ssr).

**This hook is not called during server\-side rendering.**
* **Example**

Accessing an element via template ref:

vue\`\`\`
\
import { ref, onMounted } from 'vue'

const el = ref()

onMounted(() =\> {
 el.value // \
})
\

\
 \\
\
\`\`\`

## onUpdated() [​](#onupdated)

Registers a callback to be called after the component has updated its DOM tree due to a reactive state change.

* **Type**

ts\`\`\`
function onUpdated(callback: () =\> void): void
\`\`\`
* **Details**

A parent component's updated hook is called after that of its child components.

This hook is called after any DOM update of the component, which can be caused by different state changes, because multiple state changes can be batched into a single render cycle for performance reasons. If you need to access the updated DOM after a specific state change, use [nextTick()](/api/general#nexttick) instead.

**This hook is not called during server\-side rendering.**

WARNING

Do not mutate component state in the updated hook \- this will likely lead to an infinite update loop!
* **Example**

Accessing updated DOM:

vue\`\`\`
\
import { ref, onUpdated } from 'vue'

const count = ref(0\)

onUpdated(() =\> {
 // text content should be the same as current \`count.value\`
 console.log(document.getElementById('count').textContent)
})
\

\
 \{{ count }}\
\
\`\`\`

## onUnmounted() [​](#onunmounted)

Registers a callback to be called after the component has been unmounted.

* **Type**

ts\`\`\`
function onUnmounted(callback: () =\> void): void
\`\`\`
* **Details**

A component is considered unmounted after:

	+ All of its child components have been unmounted.
	+ All of its associated reactive effects (render effect and computed / watchers created during `setup()`) have been stopped.Use this hook to clean up manually created side effects such as timers, DOM event listeners or server connections.

**This hook is not called during server\-side rendering.**
* **Example**

vue\`\`\`
\
import { onMounted, onUnmounted } from 'vue'

let intervalId
onMounted(() =\> {
 intervalId = setInterval(() =\> {
 // ...
 })
})

onUnmounted(() =\> clearInterval(intervalId))
\
\`\`\`

## onBeforeMount() [​](#onbeforemount)

Registers a hook to be called right before the component is to be mounted.

* **Type**

ts\`\`\`
function onBeforeMount(callback: () =\> void): void
\`\`\`
* **Details**

When this hook is called, the component has finished setting up its reactive state, but no DOM nodes have been created yet. It is about to execute its DOM render effect for the first time.

**This hook is not called during server\-side rendering.**

## onBeforeUpdate() [​](#onbeforeupdate)

Registers a hook to be called right before the component is about to update its DOM tree due to a reactive state change.

* **Type**

ts\`\`\`
function onBeforeUpdate(callback: () =\> void): void
\`\`\`
* **Details**

This hook can be used to access the DOM state before Vue updates the DOM. It is also safe to modify component state inside this hook.

**This hook is not called during server\-side rendering.**

## onBeforeUnmount() [​](#onbeforeunmount)

Registers a hook to be called right before a component instance is to be unmounted.

* **Type**

ts\`\`\`
function onBeforeUnmount(callback: () =\> void): void
\`\`\`
* **Details**

When this hook is called, the component instance is still fully functional.

**This hook is not called during server\-side rendering.**

## onErrorCaptured() [​](#onerrorcaptured)

Registers a hook to be called when an error propagating from a descendant component has been captured.

* **Type**

ts\`\`\`
function onErrorCaptured(callback: ErrorCapturedHook): void

type ErrorCapturedHook = (
 err: unknown,
 instance: ComponentPublicInstance \| null,
 info: string
) =\> boolean \| void
\`\`\`
* **Details**

Errors can be captured from the following sources:

	+ Component renders
	+ Event handlers
	+ Lifecycle hooks
	+ `setup()` function
	+ Watchers
	+ Custom directive hooks
	+ Transition hooksThe hook receives three arguments: the error, the component instance that triggered the error, and an information string specifying the error source type.

TIP

In production, the 3rd argument (`info`) will be a shortened code instead of the full information string. You can find the code to string mapping in the [Production Error Code Reference](/error-reference/#runtime-errors).

You can modify component state in `errorCaptured()` to display an error state to the user. However, it is important that the error state should not render the original content that caused the error; otherwise the component will be thrown into an infinite render loop.

The hook can return `false` to stop the error from propagating further. See error propagation details below.

**Error Propagation Rules**

	+ By default, all errors are still sent to the application\-level [`app.config.errorHandler`](/api/application#app-config-errorhandler) if it is defined, so that these errors can still be reported to an analytics service in a single place.
	+ If multiple `errorCaptured` hooks exist on a component's inheritance chain or parent chain, all of them will be invoked on the same error, in the order of bottom to top. This is similar to the bubbling mechanism of native DOM events.
	+ If the `errorCaptured` hook itself throws an error, both this error and the original captured error are sent to `app.config.errorHandler`.
	+ An `errorCaptured` hook can return `false` to prevent the error from propagating further. This is essentially saying "this error has been handled and should be ignored." It will prevent any additional `errorCaptured` hooks or `app.config.errorHandler` from being invoked for this error.

## onRenderTracked()  [​](#onrendertracked)

Registers a debug hook to be called when a reactive dependency has been tracked by the component's render effect.

**This hook is development\-mode\-only and not called during server\-side rendering.**

* **Type**

ts\`\`\`
function onRenderTracked(callback: DebuggerHook): void

type DebuggerHook = (e: DebuggerEvent) =\> void

type DebuggerEvent = {
 effect: ReactiveEffect
 target: object
 type: TrackOpTypes /\* 'get' \| 'has' \| 'iterate' \*/
 key: any
}
\`\`\`
* **See also** [Reactivity in Depth](/guide/extras/reactivity-in-depth)

## onRenderTriggered()  [​](#onrendertriggered)

Registers a debug hook to be called when a reactive dependency triggers the component's render effect to be re\-run.

**This hook is development\-mode\-only and not called during server\-side rendering.**

* **Type**

ts\`\`\`
function onRenderTriggered(callback: DebuggerHook): void

type DebuggerHook = (e: DebuggerEvent) =\> void

type DebuggerEvent = {
 effect: ReactiveEffect
 target: object
 type: TriggerOpTypes /\* 'set' \| 'add' \| 'delete' \| 'clear' \*/
 key: any
 newValue?: any
 oldValue?: any
 oldTarget?: Map\ \| Set\
}
\`\`\`
* **See also** [Reactivity in Depth](/guide/extras/reactivity-in-depth)

## onActivated() [​](#onactivated)

Registers a callback to be called after the component instance is inserted into the DOM as part of a tree cached by [``](/api/built-in-components#keepalive).

**This hook is not called during server\-side rendering.**

* **Type**

ts\`\`\`
function onActivated(callback: () =\> void): void
\`\`\`
* **See also** [Guide \- Lifecycle of Cached Instance](/guide/built-ins/keep-alive#lifecycle-of-cached-instance)

## onDeactivated() [​](#ondeactivated)

Registers a callback to be called after the component instance is removed from the DOM as part of a tree cached by [``](/api/built-in-components#keepalive).

**This hook is not called during server\-side rendering.**

* **Type**

ts\`\`\`
function onDeactivated(callback: () =\> void): void
\`\`\`
* **See also** [Guide \- Lifecycle of Cached Instance](/guide/built-ins/keep-alive#lifecycle-of-cached-instance)

## onServerPrefetch()  [​](#onserverprefetch)

Registers an async function to be resolved before the component instance is to be rendered on the server.

* **Type**

ts\`\`\`
function onServerPrefetch(callback: () =\> Promise\): void
\`\`\`
* **Details**

If the callback returns a Promise, the server renderer will wait until the Promise is resolved before rendering the component.

This hook is only called during server\-side rendering can be used to perform server\-only data fetching.
* **Example**

vue\`\`\`
\
import { ref, onServerPrefetch, onMounted } from 'vue'

const data = ref(null)

onServerPrefetch(async () =\> {
 // component is rendered as part of the initial request
 // pre\-fetch data on server as it is faster than on the client
 data.value = await fetchOnServer(/\* ... \*/)
})

onMounted(async () =\> {
 if (!data.value) {
 // if data is null on mount, it means the component
 // is dynamically rendered on the client. Perform a
 // client\-side fetch instead.
 data.value = await fetchOnClient(/\* ... \*/)
 }
})
\
\`\`\`
* **See also** [Server\-Side Rendering](/guide/scaling-up/ssr)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/composition-api-lifecycle.md)



## List Rendering | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/list)

# List Rendering [​](#list-rendering)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/list-rendering-in-vue-3?friend=vuejs "Free Vue.js List Rendering Lesson")[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-fundamentals-capi-list-rendering-in-vue?friend=vuejs "Free Vue.js List Rendering Lesson")## `v-for` [​](#v-for)

We can use the `v-for` directive to render a list of items based on an array. The `v-for` directive requires a special syntax in the form of `item in items`, where `items` is the source data array and `item` is an **alias** for the array element being iterated on:

js\`\`\`
const items = ref(\[{ message: 'Foo' }, { message: 'Bar' }])
\`\`\`js\`\`\`
data() {
 return {
 items: \[{ message: 'Foo' }, { message: 'Bar' }]
 }
}
\`\`\`template\`\`\`
\
 {{ item.message }}
\
\`\`\`Inside the `v-for` scope, template expressions have access to all parent scope properties. In addition, `v-for` also supports an optional second alias for the index of the current item:

js\`\`\`
const parentMessage = ref('Parent')
const items = ref(\[{ message: 'Foo' }, { message: 'Bar' }])
\`\`\`js\`\`\`
data() {
 return {
 parentMessage: 'Parent',
 items: \[{ message: 'Foo' }, { message: 'Bar' }]
 }
}
\`\`\`template\`\`\`
\
 {{ parentMessage }} \- {{ index }} \- {{ item.message }}
\
\`\`\`- Parent \- 0 \- Foo
- Parent \- 1 \- Bar
[Try it in the Playground](https://play.vuejs.org/#eNpdTsuqwjAQ/ZVDNlFQu5d64bpwJ7g3LopOJdAmIRlFCPl3p60PcDWcM+eV1X8Iq/uN1FrV6RxtYCTiW/gzzvbBR0ZGpBYFbfQ9tEi1ccadvUuM0ERyvKeUmithMyhn+jCSev4WWaY+vZ7HjH5Sr6F33muUhTR8uW0ThTuJua6mPbJEgGSErmEaENedxX3Z+rgxajbEL2DdhR5zOVOdUSIEDOf8M7IULCHsaPgiMa1eK4QcS6rOSkhdfapVeQLQEWnH)

[Try it in the Playground](https://play.vuejs.org/#eNpVTssKwjAQ/JUllyr0cS9V0IM3wbvxEOxWAm0a0m0phPy7m1aqhpDsDLMz48XJ2nwaUZSiGp5OWzpKg7PtHUGNjRpbAi8NQK1I7fbrLMkhjc5EJAn4WOXQ0BWHQb2whOS24CSN6qjXhN1Qwt1Dt2kufZ9ASOGXOyvH3GMNCdGdH75VsZVjwGa2VYQRUdVqmLKmdwcpdjEnBW1qnPf8wZIrBQujoff/RSEEyIDZZeGLeCn/dGJyCSlazSZVsUWL8AYme21i)

The variable scoping of `v-for` is similar to the following JavaScript:

js\`\`\`
const parentMessage = 'Parent'
const items = \[
 /\* ... \*/
]

items.forEach((item, index) =\> {
 // has access to outer scope \`parentMessage\`
 // but \`item\` and \`index\` are only available in here
 console.log(parentMessage, item.message, index)
})
\`\`\`Notice how the `v-for` value matches the function signature of the `forEach` callback. In fact, you can use destructuring on the `v-for` item alias similar to destructuring function arguments:

template\`\`\`
\
 {{ message }}
\

\
\
 {{ message }} {{ index }}
\
\`\`\`For nested `v-for`, scoping also works similar to nested functions. Each `v-for` scope has access to parent scopes:

template\`\`\`
\
 \
 {{ item.message }} {{ childItem }}
 \
\
\`\`\`You can also use `of` as the delimiter instead of `in`, so that it is closer to JavaScript's syntax for iterators:

template\`\`\`
\\
\`\`\`## `v-for` with an Object [​](#v-for-with-an-object)

You can also use `v-for` to iterate through the properties of an object. The iteration order will be based on the result of calling `Object.values()` on the object:

js\`\`\`
const myObject = reactive({
 title: 'How to do lists in Vue',
 author: 'Jane Doe',
 publishedAt: '2016\-04\-10'
})
\`\`\`js\`\`\`
data() {
 return {
 myObject: {
 title: 'How to do lists in Vue',
 author: 'Jane Doe',
 publishedAt: '2016\-04\-10'
 }
 }
}
\`\`\`template\`\`\`
\
 \
 {{ value }}
 \
\
\`\`\`You can also provide a second alias for the property's name (a.k.a. key):

template\`\`\`
\
 {{ key }}: {{ value }}
\
\`\`\`And another for the index:

template\`\`\`
\
 {{ index }}. {{ key }}: {{ value }}
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNo9jjFvgzAQhf/KE0sSCQKpqg7IqRSpQ9WlWycvBC6KW2NbcKaNEP+9B7Tx4nt33917Y3IKYT9ESspE9XVnAqMnjuFZO9MG3zFGdFTVbAbChEvnW2yE32inXe1dz2hv7+dPqhnHO7kdtQPYsKUSm1f/DfZoPKzpuYdx+JAL6cxUka++E+itcoQX/9cO8SzslZoTy+yhODxlxWN2KMR22mmn8jWrpBTB1AZbMc2KVbTyQ56yBkN28d1RJ9uhspFSfNEtFf+GfnZzjP/oOll2NQPjuM4xTftZyIaU5VwuN0SsqMqtWZxUvliq/J4jmX4BTCp08A==)

[Try it in the Playground](https://play.vuejs.org/#eNo9T8FqwzAM/RWRS1pImnSMHYI3KOwwdtltJ1/cRqXe3Ng4ctYS8u+TbVJjLD3rPelpLg7O7aaARVeI8eS1ozc54M1ZT9DjWQVDMMsBoFekNtucS/JIwQ8RSQI+1/vX8QdP1K2E+EmaDHZQftg/IAu9BaNHGkEP8B2wrFYxgAp0sZ6pn2pAeLepmEuSXDiy7oL9gduXT+3+pW6f631bZoqkJY/kkB6+onnswoDw6owijIhEMByjUBgNU322/lUWm0mZgBX84r1ifz3ettHmupYskjbanedch2XZRcAKTnnvGVIPBpkqGqPTJNGkkaJ5+CiWf4KkfBs=)

## `v-for` with a Range [​](#v-for-with-a-range)

`v-for` can also take an integer. In this case it will repeat the template that many times, based on a range of `1...n`.

template\`\`\`
\{{ n }}\
\`\`\`Note here `n` starts with an initial value of `1` instead of `0`.

## `v-for` on `` [​](#v-for-on-template)

Similar to template `v-if`, you can also use a `` tag with `v-for` to render a block of multiple elements. For example:

template\`\`\`
\
 \
 \{{ item.msg }}\
 \\
 \
\
\`\`\`## `v-for` with `v-if` [​](#v-for-with-v-if)

When they exist on the same node, `v-if` has a higher priority than `v-for`. That means the `v-if` condition will not have access to variables from the scope of the `v-for`:

template\`\`\`
\
\
 {{ todo.name }}
\
\`\`\`This can be fixed by moving `v-for` to a wrapping `` tag (which is also more explicit):

template\`\`\`
\
 \
 {{ todo.name }}
 \
\
\`\`\`Note

It's **not** recommended to use `v-if` and `v-for` on the same element due to implicit precedence.

There are two common cases where this can be tempting:

* To filter items in a list (e.g. `v-for="user in users" v-if="user.isActive"`). In these cases, replace `users` with a new computed property that returns your filtered list (e.g. `activeUsers`).
* To avoid rendering a list if it should be hidden (e.g. `v-for="user in users" v-if="shouldShowUsers"`). In these cases, move the `v-if` to a container element (e.g. `ul`, `ol`).
## Maintaining State with `key` [​](#maintaining-state-with-key)

When Vue is updating a list of elements rendered with `v-for`, by default it uses an "in\-place patch" strategy. If the order of the data items has changed, instead of moving the DOM elements to match the order of the items, Vue will patch each element in\-place and make sure it reflects what should be rendered at that particular index.

This default mode is efficient, but **only suitable when your list render output does not rely on child component state or temporary DOM state (e.g. form input values)**.

To give Vue a hint so that it can track each node's identity, and thus reuse and reorder existing elements, you need to provide a unique `key` attribute for each item:

template\`\`\`
\
 \
\
\`\`\`When using ``, the `key` should be placed on the `` container:

template\`\`\`
\
 \{{ todo.name }}\
\
\`\`\`Note

`key` here is a special attribute being bound with `v-bind`. It should not be confused with the property key variable when [using `v-for` with an object](#v-for-with-an-object).

It is recommended to provide a `key` attribute with `v-for` whenever possible, unless the iterated DOM content is simple (i.e. contains no components or stateful DOM elements), or you are intentionally relying on the default behavior for performance gains.

The `key` binding expects primitive values \- i.e. strings and numbers. Do not use objects as `v-for` keys. For detailed usage of the `key` attribute, please see the [`key` API documentation](/api/built-in-special-attributes#key).

## `v-for` with a Component [​](#v-for-with-a-component)

> This section assumes knowledge of [Components](/guide/essentials/component-basics). Feel free to skip it and come back later.

You can directly use `v-for` on a component, like any normal element (don't forget to provide a `key`):

template\`\`\`
\
\`\`\`However, this won't automatically pass any data to the component, because components have isolated scopes of their own. In order to pass the iterated data into the component, we should also use props:

template\`\`\`
\
\`\`\`The reason for not automatically injecting `item` into the component is because that makes the component tightly coupled to how `v-for` works. Being explicit about where its data comes from makes the component reusable in other situations.

Check out [this example of a simple todo list](https://play.vuejs.org/#eNp1U8Fu2zAM/RXCGGAHTWx02ylwgxZYB+ywYRhyq3dwLGYRYkuCJTsZjPz7KMmK3ay9JBQfH/meKA/Rk1Jp32G0jnJdtVwZ0Gg6tSkEb5RsDQzQ4h4usG9lAzGVxldoK5n8ZrAZsTQLCduRygAKUUmhDQg8WWyLZwMPtmESx4sAGkL0mH6xrMH+AHC2hvuljw03Na4h/iLBHBAY1wfUbsTFVcwoH28o2/KIIDuaQ0TTlvrwNu/TDe+7PDlKXZ6EZxTiN4kuRI3W0dk4u4yUf7bZfScqw6WAkrEf3m+y8AOcw7Qv6w5T1elDMhs7Nbq7e61gdmme60SQAvgfIhExiSSJeeb3SBukAy1D1aVBezL5XrYN9Csp1rrbNdykqsUehXkookl0EVGxlZHX5Q5rIBLhNHFlbRD6xBiUzlOeuZJQz4XqjI+BxjSSYe2pQWwRBZizV01DmsRWeJA1Qzv0Of2TwldE5hZRlVd+FkbuOmOksJLybIwtkmfWqg+7qz47asXpSiaN3lxikSVwwfC8oD+/sEnV+oh/qcxmU85mebepgLjDBD622Mg+oDrVquYVJm7IEu4XoXKTZ1dho3gnmdJhedEymn9ab3ysDPdc4M9WKp28xE5JbB+rzz/Trm3eK3LAu8/E7p2PNzYM/i3ChR7W7L7hsSIvR7L2Aal1EhqTp80vF95sw3WcG7r8A0XaeME=) to see how to render a list of components using `v-for`, passing different data to each instance.

Check out [this example of a simple todo list](https://play.vuejs.org/#eNqNVE2PmzAQ/SsjVIlEm4C27Qmx0a7UVuqhPVS5lT04eFKsgG2BSVJF+e8d2xhIu10tihR75s2bNx9wiZ60To49RlmUd2UrtNkUUjRatQa2iquvBhvYt6qBOEmDwQbEhQQoJJ4dlOOe9bWBi7WWiuIlStNlcJlYrivr5MywxdIDAVo0fSvDDUDiyeK3eDYZxLGLsI8hI7H9DHeYQuwjeAb3I9gFCFMjUXxSYCoELroKO6fZP17Mf6jev0i1ZQcE1RtHaFrWVW/l+/Ai3zd1clQ1O8k5Uzg+j1HUZePaSFwfvdGhfNIGTaW47bV3Mc6/+zZOfaaslegS18ZE9121mIm0Ep17ynN3N5M8CB4g44AC4Lq8yTFDwAPNcK63kPTL03HR6EKboWtm0N5MvldtA8e1klnX7xphEt3ikTbpoYimsoqIwJY0r9kOa6Ag8lPeta2PvE+cA3M7k6cOEvBC6n7UfVw3imPtQ8eiouAW/IY0mElsiZWqOdqkn5NfCXxB5G6SJRvj05By1xujpJWUp8PZevLUluqP/ajPploLasmk0Re3sJ4VCMnxvKQ//0JMqrID/iaYtSaCz+xudsHjLpPzscVGHYO3SzpdixIXLskK7pcBucnTUdgg3kkmcxhetIrmH4ebr8m/n4jC6FZp+z7HTlLsVx1p4M7odcXPr6+Lnb8YOne5+C2F6/D6DH2Hx5JqOlCJ7yz7IlBTbZsf7vjXVBzjvLDrH5T0lgo=) to see how to render a list of components using `v-for`, passing different data to each instance.

## Array Change Detection [​](#array-change-detection)

### Mutation Methods [​](#mutation-methods)

Vue is able to detect when a reactive array's mutation methods are called and trigger necessary updates. These mutation methods are:

* `push()`
* `pop()`
* `shift()`
* `unshift()`
* `splice()`
* `sort()`
* `reverse()`

### Replacing an Array [​](#replacing-an-array)

Mutation methods, as the name suggests, mutate the original array they are called on. In comparison, there are also non\-mutating methods, e.g. `filter()`, `concat()` and `slice()`, which do not mutate the original array but **always return a new array**. When working with non\-mutating methods, we should replace the old array with the new one:

js\`\`\`
// \`items\` is a ref with array value
items.value = items.value.filter((item) =\> item.message.match(/Foo/))
\`\`\`js\`\`\`
this.items = this.items.filter((item) =\> item.message.match(/Foo/))
\`\`\`You might think this will cause Vue to throw away the existing DOM and re\-render the entire list \- luckily, that is not the case. Vue implements some smart heuristics to maximize DOM element reuse, so replacing an array with another array containing overlapping objects is a very efficient operation.

## Displaying Filtered/Sorted Results [​](#displaying-filtered-sorted-results)

Sometimes we want to display a filtered or sorted version of an array without actually mutating or resetting the original data. In this case, you can create a computed property that returns the filtered or sorted array.

For example:

js\`\`\`
const numbers = ref(\[1, 2, 3, 4, 5])

const evenNumbers = computed(() =\> {
 return numbers.value.filter((n) =\> n % 2 === 0\)
})
\`\`\`js\`\`\`
data() {
 return {
 numbers: \[1, 2, 3, 4, 5]
 }
},
computed: {
 evenNumbers() {
 return this.numbers.filter(n =\> n % 2 === 0\)
 }
}
\`\`\`template\`\`\`
\{{ n }}\
\`\`\`In situations where computed properties are not feasible (e.g. inside nested `v-for` loops), you can use a method:

js\`\`\`
const sets = ref(\[
 \[1, 2, 3, 4, 5],
 \[6, 7, 8, 9, 10]
])

function even(numbers) {
 return numbers.filter((number) =\> number % 2 === 0\)
}
\`\`\`js\`\`\`
data() {
 return {
 sets: \[\[ 1, 2, 3, 4, 5 ], \[6, 7, 8, 9, 10]]
 }
},
methods: {
 even(numbers) {
 return numbers.filter(number =\> number % 2 === 0\)
 }
}
\`\`\`template\`\`\`
\
 \{{ n }}\
\
\`\`\`Be careful with `reverse()` and `sort()` in a computed property! These two methods will mutate the original array, which should be avoided in computed getters. Create a copy of the original array before calling these methods:

diff\`\`\`
\- return numbers.reverse()
\+ return \[...numbers].reverse()
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/list.md)



## Component Instance | Vue.js

[Read the full article](https://vuejs.org/api/component-instance)

# Component Instance [​](#component-instance)

INFO

This page documents the built\-in properties and methods exposed on the component public instance, i.e. `this`.

All properties listed on this page are readonly (except nested properties in `$data`).

## $data [​](#data)

The object returned from the [`data`](/api/options-state#data) option, made reactive by the component. The component instance proxies access to the properties on its data object.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $data: object
}
\`\`\`

## $props [​](#props)

An object representing the component's current, resolved props.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $props: object
}
\`\`\`
* **Details**

Only props declared via the [`props`](/api/options-state#props) option will be included. The component instance proxies access to the properties on its props object.

## $el [​](#el)

The root DOM node that the component instance is managing.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $el: Node \| undefined
}
\`\`\`
* **Details**

`$el` will be `undefined` until the component is [mounted](/api/options-lifecycle#mounted).

	+ For components with a single root element, `$el` will point to that element.
	+ For components with text root, `$el` will point to the text node.
	+ For components with multiple root nodes, `$el` will be the placeholder DOM node that Vue uses to keep track of the component's position in the DOM (a text node, or a comment node in SSR hydration mode).TIP

For consistency, it is recommended to use [template refs](/guide/essentials/template-refs) for direct access to elements instead of relying on `$el`.

## $options [​](#options)

The resolved component options used for instantiating the current component instance.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $options: ComponentOptions
}
\`\`\`
* **Details**

The `$options` object exposes the resolved options for the current component and is the merge result of these possible sources:

	+ Global mixins
	+ Component `extends` base
	+ Component mixinsIt is typically used to support custom component options:

js\`\`\`
const app = createApp({
 customOption: 'foo',
 created() {
 console.log(this.$options.customOption) // =\> 'foo'
 }
})
\`\`\`
* **See also** [`app.config.optionMergeStrategies`](/api/application#app-config-optionmergestrategies)

## $parent [​](#parent)

The parent instance, if the current instance has one. It will be `null` for the root instance itself.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $parent: ComponentPublicInstance \| null
}
\`\`\`

## $root [​](#root)

The root component instance of the current component tree. If the current instance has no parents this value will be itself.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $root: ComponentPublicInstance
}
\`\`\`

## $slots [​](#slots)

An object representing the [slots](/guide/components/slots) passed by the parent component.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $slots: { \[name: string]: Slot }
}

type Slot = (...args: any\[]) =\> VNode\[]
\`\`\`
* **Details**

Typically used when manually authoring [render functions](/guide/extras/render-function), but can also be used to detect whether a slot is present.

Each slot is exposed on `this.$slots` as a function that returns an array of vnodes under the key corresponding to that slot's name. The default slot is exposed as `this.$slots.default`.

If a slot is a [scoped slot](/guide/components/slots#scoped-slots), arguments passed to the slot functions are available to the slot as its slot props.
* **See also** [Render Functions \- Rendering Slots](/guide/extras/render-function#rendering-slots)

## $refs [​](#refs)

An object of DOM elements and component instances, registered via [template refs](/guide/essentials/template-refs).

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $refs: { \[name: string]: Element \| ComponentPublicInstance \| null }
}
\`\`\`
* **See also**

	+ [Template refs](/guide/essentials/template-refs)
	+ [Special Attributes \- ref](/api/built-in-special-attributes#ref)

## $attrs [​](#attrs)

An object that contains the component's fallthrough attributes.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $attrs: object
}
\`\`\`
* **Details**

[Fallthrough Attributes](/guide/components/attrs) are attributes and event handlers passed by the parent component, but not declared as a prop or an emitted event by the child.

By default, everything in `$attrs` will be automatically inherited on the component's root element if there is only a single root element. This behavior is disabled if the component has multiple root nodes, and can be explicitly disabled with the [`inheritAttrs`](/api/options-misc#inheritattrs) option.
* **See also**

	+ [Fallthrough Attributes](/guide/components/attrs)

## $watch() [​](#watch)

Imperative API for creating watchers.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $watch(
 source: string \| (() =\> any),
 callback: WatchCallback,
 options?: WatchOptions
 ): StopHandle
}

type WatchCallback\ = (
 value: T,
 oldValue: T,
 onCleanup: (cleanupFn: () =\> void) =\> void
) =\> void

interface WatchOptions {
 immediate?: boolean // default: false
 deep?: boolean // default: false
 flush?: 'pre' \| 'post' \| 'sync' // default: 'pre'
 onTrack?: (event: DebuggerEvent) =\> void
 onTrigger?: (event: DebuggerEvent) =\> void
}

type StopHandle = () =\> void
\`\`\`
* **Details**

The first argument is the watch source. It can be a component property name string, a simple dot\-delimited path string, or a [getter function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description).

The second argument is the callback function. The callback receives the new value and the old value of the watched source.

	+ **`immediate`**: trigger the callback immediately on watcher creation. Old value will be `undefined` on the first call.
	+ **`deep`**: force deep traversal of the source if it is an object, so that the callback fires on deep mutations. See [Deep Watchers](/guide/essentials/watchers#deep-watchers).
	+ **`flush`**: adjust the callback's flush timing. See [Callback Flush Timing](/guide/essentials/watchers#callback-flush-timing) and [`watchEffect()`](/api/reactivity-core#watcheffect).
	+ **`onTrack / onTrigger`**: debug the watcher's dependencies. See [Watcher Debugging](/guide/extras/reactivity-in-depth#watcher-debugging).
* **Example**

Watch a property name:

js\`\`\`
this.$watch('a', (newVal, oldVal) =\> {})
\`\`\`Watch a dot\-delimited path:

js\`\`\`
this.$watch('a.b', (newVal, oldVal) =\> {})
\`\`\`Using getter for more complex expressions:

js\`\`\`
this.$watch(
 // every time the expression \`this.a \+ this.b\` yields
 // a different result, the handler will be called.
 // It's as if we were watching a computed property
 // without defining the computed property itself.
 () =\> this.a \+ this.b,
 (newVal, oldVal) =\> {}
)
\`\`\`Stopping the watcher:

js\`\`\`
const unwatch = this.$watch('a', cb)

// later...
unwatch()
\`\`\`
* **See also**

	+ [Options \- `watch`](/api/options-state#watch)
	+ [Guide \- Watchers](/guide/essentials/watchers)

## $emit() [​](#emit)

Trigger a custom event on the current instance. Any additional arguments will be passed into the listener's callback function.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $emit(event: string, ...args: any\[]): void
}
\`\`\`
* **Example**

js\`\`\`
export default {
 created() {
 // only event
 this.$emit('foo')
 // with additional arguments
 this.$emit('bar', 1, 2, 3\)
 }
}
\`\`\`
* **See also**

	+ [Component \- Events](/guide/components/events)
	+ [`emits` option](/api/options-state#emits)

## $forceUpdate() [​](#forceupdate)

Force the component instance to re\-render.

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $forceUpdate(): void
}
\`\`\`
* **Details**

This should be rarely needed given Vue's fully automatic reactivity system. The only cases where you may need it is when you have explicitly created non\-reactive component state using advanced reactivity APIs.

## $nextTick() [​](#nexttick)

Instance\-bound version of the global [`nextTick()`](/api/general#nexttick).

* **Type**

ts\`\`\`
interface ComponentPublicInstance {
 $nextTick(callback?: (this: ComponentPublicInstance) =\> void): Promise\
}
\`\`\`
* **Details**

The only difference from the global version of `nextTick()` is that the callback passed to `this.$nextTick()` will have its `this` context bound to the current component instance.
* **See also** [`nextTick()`](/api/general#nexttick)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/component-instance.md)



## Component v-model | Vue.js

[Read the full article](https://vuejs.org/guide/components/v-model)

# Component v\-model [​](#component-v-model)

## Basic Usage [​](#basic-usage)

`v-model` can be used on a component to implement a two\-way binding.

Starting in Vue 3\.4, the recommended approach to achieve this is using the [`defineModel()`](/api/sfc-script-setup#definemodel) macro:

vue\`\`\`
\
\
const model = defineModel()

function update() {
 model.value\+\+
}
\

\
 \Parent bound v\-model is: {{ model }}\
 \Increment\
\
\`\`\`The parent can then bind a value with `v-model`:

template\`\`\`
\
\
\`\`\`The value returned by `defineModel()` is a ref. It can be accessed and mutated like any other ref, except that it acts as a two\-way binding between a parent value and a local one:

* Its `.value` is synced with the value bound by the parent `v-model`;
* When it is mutated by the child, it causes the parent bound value to be updated as well.

This means you can also bind this ref to a native input element with `v-model`, making it straightforward to wrap native input elements while providing the same `v-model` usage:

vue\`\`\`
\
const model = defineModel()
\

\
 \
\
\`\`\`[Try it in the playground](https://play.vuejs.org/#eNqFUtFKwzAU/ZWYl06YLbK30Q10DFSYigq+5KW0t11mmoQknZPSf/cm3eqEsT0l555zuefmpKV3WsfbBuiUpjY3XDtiwTV6ziSvtTKOLNZcFKQ0qiZRnATkG6JB0BIDJen2kp5iMlfSOlLbisw8P4oeQAhFPpURxVV0zWSa9PNwEgIHtRaZA0SEpOvbeduG5q5LE0Sh2jvZ3tSqADFjFHlGSYJkmhz10zF1FseXvIo3VklcrfX9jOaq1lyAedGOoz1GpyQwnsvQ3fdTqDnTwPhQz9eQf52ob+zO1xh9NWDBbIHRgXOZqcD19PL9GXZ4H0h03whUnyHfwCrReI+97L6RBdo+0gW3j+H9uaw+7HLnQNrDUt6oV3ZBzyhmsjiz+p/dSTwJfUx2+IpD1ic+xz5enwQGXEDJJaw8Gl2I1upMzlc/hEvdOBR6SNKAjqP1J6P/o6XdL11L5h4=)

### Under the Hood [​](#under-the-hood)

`defineModel` is a convenience macro. The compiler expands it to the following:

* A prop named `modelValue`, which the local ref's value is synced with;
* An event named `update:modelValue`, which is emitted when the local ref's value is mutated.

This is how you would implement the same child component shown above prior to 3\.4:

vue\`\`\`
\
\
const props = defineProps(\['modelValue'])
const emit = defineEmits(\['update:modelValue'])
\

\
 \
\
\`\`\`Then, `v-model="foo"` in the parent component will be compiled to:

template\`\`\`
\
\ (foo = $event)"
/\>
\`\`\`As you can see, it is quite a bit more verbose. However, it is helpful to understand what is happening under the hood.

Because `defineModel` declares a prop, you can therefore declare the underlying prop's options by passing it to `defineModel`:

js\`\`\`
// making the v\-model required
const model = defineModel({ required: true })

// providing a default value
const model = defineModel({ default: 0 })
\`\`\`WARNING

If you have a `default` value for `defineModel` prop and you don't provide any value for this prop from the parent component, it can cause a de\-synchronization between parent and child components. In the example below, the parent's `myRef` is undefined, but the child's `model` is 1:

**Child component:**

js\`\`\`
const model = defineModel({ default: 1 })
\`\`\`**Parent component:**

js\`\`\`
const myRef = ref()
\`\`\`html\`\`\`
\\
\`\`\`First let's revisit how `v-model` is used on a native element:

template\`\`\`
\
\`\`\`Under the hood, the template compiler expands `v-model` to the more verbose equivalent for us. So the above code does the same as the following:

template\`\`\`
\
\`\`\`When used on a component, `v-model` instead expands to this:

template\`\`\`
\ searchText = newValue"
/\>
\`\`\`For this to actually work though, the `` component must do two things:

1. Bind the `value` attribute of a native `` element to the `modelValue` prop
2. When a native `input` event is triggered, emit an `update:modelValue` custom event with the new value

Here's that in action:

vue\`\`\`
\
\
export default {
 props: \['modelValue'],
 emits: \['update:modelValue']
}
\

\
 \
\
\`\`\`Now `v-model` should work perfectly with this component:

template\`\`\`
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFkctqwzAQRX9lEAEn4Np744aWrvoD3URdiHiSGvRCHpmC8b93JDfGKYGCkJjXvTrSJF69r8aIohHtcA69p6O0vfEuELzFgZx5tz4SXIIzUFT1JpfGCmmlxe/c3uFFRU0wSQtwdqxh0dLQwHSnNJep3ilS+8PSCxCQYrC3CMDgMKgrNlB8odaOXVJ2TgdvvNp6vSwHhMZrRcgRQLs1G5+M61A/S/ErKQXUR5immwXMWW1VEKX4g3j3Mo9QfXCeKU9FtvpQmp/lM0Oi6RP/qYieebHZNvyL0acLLODNmGYSxCogxVJ6yW1c2iWz/QOnEnY48kdUpMIVGSllD8t8zVZb+PkHqPG4iw==)

Another way of implementing `v-model` within this component is to use a writable `computed` property with both a getter and a setter. The `get` method should return the `modelValue` property and the `set` method should emit the corresponding event:

vue\`\`\`
\
\
export default {
 props: \['modelValue'],
 emits: \['update:modelValue'],
 computed: {
 value: {
 get() {
 return this.modelValue
 },
 set(value) {
 this.$emit('update:modelValue', value)
 }
 }
 }
}
\

\
 \
\
\`\`\`## `v-model` arguments [​](#v-model-arguments)

`v-model` on a component can also accept an argument:

template\`\`\`
\
\`\`\`In the child component, we can support the corresponding argument by passing a string to `defineModel()` as its first argument:

vue\`\`\`
\
\
const title = defineModel('title')
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFklFPwjAUhf9K05dhgiyGNzJI1PCgCWqUx77McQeFrW3aOxxZ9t+9LTAXA/q2nnN6+t12Db83ZrSvgE944jIrDTIHWJmZULI02iJrmIWctSy3umQRRaPOWhweNX0pUHiyR3FP870UZkyoTCuH7FPr3VJiAWzqSwfR/rbUKyhYatdV6VugTktTQHQjVBIfeYiEFgikpwi0YizZ3M2aplfXtklMWvD6UKf+CfrUVPBuh+AspngSd718yH+hX7iS4xihjUZYQS4VLPwJgyiI/3FLZSrafzAeBqFG4jgxeuEqGTo6OZfr0dZpRVxNuFWeEa4swL4alEQm+IQFx3tpUeiv56ChrWB41rMNZLsL+tbVXhP8zYIDuyeQzkN6HyBWb88/XgJ3ZxJ95bH/MN/B6aLyjMfYQ6VWhN3LBdqn8FdJtV66eY2g3HkoD+qTbcgLTo/jX+ra6D+449E47BOq5e039mr+gA==)

If prop options are also needed, they should be passed after the model name:

js\`\`\`
const title = defineModel('title', { required: true })
\`\`\`Pre 3\.4 Usagevue\`\`\`
\
\
defineProps({
 title: {
 required: true
 }
})
defineEmits(\['update:title'])
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9kE1rwzAMhv+KMIW00DXsGtKyMXYc7D7vEBplM8QfOHJoCfnvk+1QsjJ2svVKevRKk3h27jAGFJWoh7NXjmBACu4kjdLOeoIJPHYwQ+ethoJLi1vq7fpi+WfQ0JI+lCstcrkYQJqzNQMBKeoRjhG4LcYHbVvsofFfQUcCXhrteix20tRl9sIuOCBkvSHkCKD+fjxN04Ka57rkOOlrMwu7SlVHKdIrBZRcWpc3ntiLO7t/nKHFThl899YN248ikYpP9pj1V60o6sG1TMwDU/q/FZRxgeIPgK4uGcQLSZGlamz6sHKd1afUxOoGeeT298A9bHCMKxBfE3mTSNjl1vud5x8qNa76)

In this case, instead of the default `modelValue` prop and `update:modelValue` event, the child component should expect a `title` prop and emit an `update:title` event to update the parent value:

vue\`\`\`
\
\
export default {
 props: \['title'],
 emits: \['update:title']
}
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFUNFqwzAM/BVhCm6ha9hryMrGnvcFdR9Mo26B2DGuHFJC/n2yvZakDAohtuTTne5G8eHcrg8oSlFdTr5xtFe2Ma7zBF/Xz45vFi3B2XcG5K6Y9eKYVFZZHBK8xrMOLcGoLMDphrqUMC6Ypm18rzXp9SZjATxS8PZWAVBDLZYg+xfT1diC9t/BxGEctHFtlI2wKR78468q7ttzQcgoTcgVQPXzuh/HzAnTVBVcp/58qz+lMqHelEinElAwtCrufGIrHhJYBPdfEs53jkM4yEQpj8k+miYmc5DBcRKYZeXxqZXGukDZPF1dWhQHUiK3yl63YbZ97r6nIe6uoup6KbmFFfbRCnHGyI4iwyaPPnqffgGMlsEM)

## Multiple `v-model` bindings [​](#multiple-v-model-bindings)

By leveraging the ability to target a particular prop and event as we learned before with [`v-model` arguments](#v-model-arguments), we can now create multiple `v-model` bindings on a single component instance.

Each `v-model` will sync to a different prop, without the need for extra options in the component:

template\`\`\`
\
\`\`\`vue\`\`\`
\
const firstName = defineModel('firstName')
const lastName = defineModel('lastName')
\

\
 \
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFkstuwjAQRX/F8iZUAqKKHQpIfbAoUmnVx86bKEzANLEt26FUkf+9Y4MDSAg2UWbu9fjckVv6oNRw2wAd08wUmitLDNhGTZngtZLakpZoKIkjpZY1SdCadNK3Ab3IazhowzQ2/ES0MVFIYSwpucbvxA/qJXO5FsldlKr8qDxL8EKW7kEQAQsLtapyC1gRkq3vp217mOccwf8wwLksRSlYIoMvCNkOarmEahyODAT2J4yGgtFzhx8UDf5/r6c4NEs7CNqnpxkvbO0kcVjNhCyh5AJe/SW9pBPOV3DJGvu3dsKFaiyxf8qTW9gheQwVs4Z90BDm5oF47cF/Ht4aZC75argxUmD61g9ktJC14hXoN2U5ZmJ0TILitbyq5O889KxuoB/7xRqKnwv9jdn5HqPvGnDVWwTpNJvrFSCul2efi4DeiRigqdB9RfwAI6vGM+5tj41YIvaJL9C+hOfNxerLzHYWhImhPKh3uuBnFJ/A05XoR9zRcBTOMeGo+wcs+yse)

Pre 3\.4 Usagevue\`\`\`
\
defineProps({
 firstName: String,
 lastName: String
})

defineEmits(\['update:firstName', 'update:lastName'])
\

\
 \
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqNUc1qwzAMfhVjCk6hTdg1pGWD7bLDGIydlh1Cq7SGxDaOEjaC332yU6cdFNpLsPRJ348y8idj0qEHnvOi21lpkHWAvdmWSrZGW2Qjs1Azx2qrWyZoVMzQZwf2rWrhhKVZbHhGGivVTqsOWS0tfTeeKBGv+qjEMkJNdUaeNXigyCYjZIEKhNY0FQJVjBXHh+04nvicY/QOBM4VGUFhJHrwBWPDutV7aPKwslbU35Q8FCX/P+GJ4oB/T3hGpEU2m+ArfpnxytX2UEsF71abLhk9QxDzCzn7QCvVYeW7XuGyWSpH0eP6SyuxS75Eb/akOpn302LFYi8SiO8bJ5PK9DhFxV/j0yH8zOnzoWr6+SbhbifkMSwSsgByk1zzsoABFKZY2QNgGpiW57Pdrx2z3JCeI99Svvxh7g8muf2x)

vue\`\`\`
\
export default {
 props: {
 firstName: String,
 lastName: String
 },
 emits: \['update:firstName', 'update:lastName']
}
\

\
 \
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqNkk1rg0AQhv/KIAETSJRexYYWeuqhl9JTt4clmSSC7i7rKCnif+/ObtYkELAiujPzztejQ/JqTNZ3mBRJ2e5sZWgrVNUYbQm+WrQfskE4WN1AmuXRwQmpUELh2Qv3eJBdTTAIBbDTLluhoraA4VpjXHNwL0kuV0EIYJE6q6IFcKhsSwWk7/qkUq/nq5be+aa5JztGfrmHu8t8GtoZhI2pJaGzAMrT03YYQk0YR3BnruSOZe5CXhKnC3X7TaP3WBc+ZaOc/1kk3hDJvYILRQGfQzx3Rct8GiJZJ7fA7gg/AmesNszMrUIXFpxbwCfZSh09D0Hc7tbN6sAWm4qZf6edcZgxrMHSdA3RF7PTn1l8lTIdhbXp1/CmhOeJRNHLupv4eIaXyItPdJEFD7R8NM0Ce/d/ZCTtESnzlVZXhP/vHbeZaT0tPdf59uONfx7mDVM=)

## Handling `v-model` modifiers [​](#handling-v-model-modifiers)

When we were learning about form input bindings, we saw that `v-model` has [built\-in modifiers](/guide/essentials/forms#modifiers) \- `.trim`, `.number` and `.lazy`. In some cases, you might also want the `v-model` on your custom input component to support custom modifiers.

Let's create an example custom modifier, `capitalize`, that capitalizes the first letter of the string provided by the `v-model` binding:

template\`\`\`
\
\`\`\`Modifiers added to a component `v-model` can be accessed in the child component by destructuring the `defineModel()` return value like this:

vue\`\`\`
\
const \[model, modifiers] = defineModel()

console.log(modifiers) // { capitalize: true }
\

\
 \
\
\`\`\`To conditionally adjust how the value should be read / written based on modifiers, we can pass `get` and `set` options to `defineModel()`. These two options receive the value on get / set of the model ref and should return a transformed value. This is how we can use the `set` option to implement the `capitalize` modifier:

vue\`\`\`
\
const \[model, modifiers] = defineModel({
 set(value) {
 if (modifiers.capitalize) {
 return value.charAt(0\).toUpperCase() \+ value.slice(1\)
 }
 return value
 }
})
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9UsFu2zAM/RVClzhY5mzoLUgHdEUPG9Bt2LLTtIPh0Ik6WRIkKksa5N9LybFrFG1OkvgeyccnHsWNc+UuoliIZai9cgQBKbpP0qjWWU9wBI8NnKDxtoUJUycDdH+4tXwzaOgMl/NRLNVlMoA0tTWBoD2scE9wnSoWk8lUmuW8a8rt+EHYOl0R8gtgtVUBlHGRoK6cokqrRwxAW4RGea6mkQg9HGwEboZ+kbKWY027961doy6f86+l6ERIAXNus5wPPcVMvNB+yZOaiZFw/cKYftI/ufEM+FCNQh/+8tRrbJTB+4QUxySWqxa7SkecQn4DqAaKIWekeyAAe0fRG8h5Zb2t/A0VH6Yl2d/Oob+tAhZTeHfGg1Y1Fh/Z6ZR66o5xhRTh8OnyXyy7f6CDSw5S59/Z3WRpOl91lAL70ahN+RCsYT/zFFIk95RG/92RYr+kWPTzSVFpbf9/zTHyEWd9vN5i/e+V+EPYp5gUPzwG9DuUYsCo8htkrQm++/Ut6x5AVh01sy+APzFYHZPGjvY5mjXLHvGy2i95K5TZrMLdntCEfqgkNDuc+VLwkqQNe2v0Z7lX5VX/M+L0BFEuPdc=)

Pre 3\.4 Usagevue\`\`\`
\
const props = defineProps({
 modelValue: String,
 modelModifiers: { default: () =\> ({}) }
})

const emit = defineEmits(\['update:modelValue'])

function emitValue(e) {
 let value = e.target.value
 if (props.modelModifiers.capitalize) {
 value = value.charAt(0\).toUpperCase() \+ value.slice(1\)
 }
 emit('update:modelValue', value)
}
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNp9Us1Og0AQfpUJF5ZYqV4JNTaNxyYmVi/igdCh3QR2N7tDIza8u7NLpdU0nmB+v5/ZY7Q0Jj10GGVR7iorDYFD6sxDoWRrtCU4gsUaBqitbiHm1ngqrfuV5j+Fik7ldH6R83u5GaBQlVaOoO03+Emw8BtFHCeFyucjKMNxQNiapiTkCGCzlw6kMh1BVRpJZSO/0AEe0Pa0l2oHve6AYdBmvj+/ZHO4bfUWm/Q8uSiiEb6IYM4A+XxCi2bRH9ZX3BgVGKuNYwFbrKXCZx+Jo0cPcG9l02EGL2SZ3mxKr/VW1hKty9hMniy7hjIQCSweQByHBIZCDWzGDwi20ps0Yjxx4MR73Jktc83OOPFHGKk7VZHUKkyFgsAEAqcG2Qif4WWYUml3yOp8wldlDSLISX+TvPDstAemLeGbVvvSLkncJSnpV2PQrkqHLOfmVHeNrFDcMz3w0iBQE1cUzMYBbuS2f55CPj4D6o0/I41HzMKsP+u0kLOPoZWzkx1X7j18A8s0DEY=)

Modifiers added to a component `v-model` will be provided to the component via the `modelModifiers` prop. In the below example, we have created a component that contains a `modelModifiers` prop that defaults to an empty object:

vue\`\`\`
\
export default {
 props: {
 modelValue: String,
 modelModifiers: {
 default: () =\> ({})
 }
 },
 emits: \['update:modelValue'],
 created() {
 console.log(this.modelModifiers) // { capitalize: true }
 }
}
\

\
 \
\
\`\`\`Notice the component's `modelModifiers` prop contains `capitalize` and its value is `true` \- due to it being set on the `v-model` binding `v-model.capitalize="myText"`.

Now that we have our prop set up, we can check the `modelModifiers` object keys and write a handler to change the emitted value. In the code below we will capitalize the string whenever the `` element fires an `input` event.

vue\`\`\`
\
export default {
 props: {
 modelValue: String,
 modelModifiers: {
 default: () =\> ({})
 }
 },
 emits: \['update:modelValue'],
 methods: {
 emitValue(e) {
 let value = e.target.value
 if (this.modelModifiers.capitalize) {
 value = value.charAt(0\).toUpperCase() \+ value.slice(1\)
 }
 this.$emit('update:modelValue', value)
 }
 }
}
\

\
 \
\
\`\`\`[Try it in the Playground](https://play.vuejs.org/#eNqFks1qg0AQgF9lkIKGpqa9iikNOefUtJfaw6KTZEHdZR1DbPDdO7saf0qgIq47//PNXL2N1uG5Ri/y4io1UtNrUspCK0Owa7aK/0osCQ5GFeCHq4nMuvlJCZCUeHEOGR5EnRNcrTS92VURXGex2qXVZ4JEsOhsAQxSbcrbDaBo9nihCHyXAaC1B3/4jVdDoXwhLHQuCPkGsD/JCmSpa4JUaEkilz9YAZ7RNHSS5REaVQPXgCay9vG0rPNToTLMw9FznXhdHYkHK04Qr4Zs3tL7g2JG8B4QbZS2LLqGXK5PkdcYwTsZrs1R6RU7lcmDRDPaM7AuWARMbf0KwbVdTNk4dyyk5f3l15r5YjRm8b+dQYF0UtkY1jo4fYDDLAByZBxWCmvAkIQ5IvdoBTcLeYCAiVbhvNwJvEk4GIK5M0xPwmwoeF6EpD60RrMVFXJXj72+ymWKwUvfXt+gfVzGB1tzcKfDZec+o/LfxsTdtlCj7bSpm3Xk4tjpD8FZ+uZMWTowu7MW7S+CWR77)

### Modifiers for `v-model` with arguments [​](#modifiers-for-v-model-with-arguments)

For `v-model` bindings with both argument and modifiers, the generated prop name will be `arg + "Modifiers"`. For example:

template\`\`\`
\
\`\`\`The corresponding declarations should be:

js\`\`\`
export default {
 props: \['title', 'titleModifiers'],
 emits: \['update:title'],
 created() {
 console.log(this.titleModifiers) // { capitalize: true }
 }
}
\`\`\`Here's another example of using modifiers with multiple `v-model` with different arguments:

template\`\`\`
\
\`\`\`vue\`\`\`
\
const \[firstName, firstNameModifiers] = defineModel('firstName')
const \[lastName, lastNameModifiers] = defineModel('lastName')

console.log(firstNameModifiers) // { capitalize: true }
console.log(lastNameModifiers) // { uppercase: true }
\
\`\`\`Pre 3\.4 Usagevue\`\`\`
\
const props = defineProps({
firstName: String,
lastName: String,
firstNameModifiers: { default: () =\> ({}) },
lastNameModifiers: { default: () =\> ({}) }
})
defineEmits(\['update:firstName', 'update:lastName'])

console.log(props.firstNameModifiers) // { capitalize: true }
console.log(props.lastNameModifiers) // { uppercase: true }
\
\`\`\`vue\`\`\`
\
export default {
 props: {
 firstName: String,
 lastName: String,
 firstNameModifiers: {
 default: () =\> ({})
 },
 lastNameModifiers: {
 default: () =\> ({})
 }
 },
 emits: \['update:firstName', 'update:lastName'],
 created() {
 console.log(this.firstNameModifiers) // { capitalize: true }
 console.log(this.lastNameModifiers) // { uppercase: true }
 }
}
\
\`\`\`[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/components/v-model.md)



## Suspense | Vue.js

[Read the full article](https://vuejs.org/guide/built-ins/suspense)

# Suspense [​](#suspense)

Experimental Feature

`` is an experimental feature. It is not guaranteed to reach stable status and the API may change before it does.

`` is a built\-in component for orchestrating async dependencies in a component tree. It can render a loading state while waiting for multiple nested async dependencies down the component tree to be resolved.

## Async Dependencies [​](#async-dependencies)

To explain the problem `` is trying to solve and how it interacts with these async dependencies, let's imagine a component hierarchy like the following:

\`\`\`
\
└─ \
 ├─ \
 │ └─ \ (component with async setup())
 └─ \
 ├─ \ (async component)
 └─ \ (async component)
\`\`\`In the component tree there are multiple nested components whose rendering depends on some async resource to be resolved first. Without ``, each of them will need to handle its own loading / error and loaded states. In the worst case scenario, we may see three loading spinners on the page, with content displayed at different times.

The `` component gives us the ability to display top\-level loading / error states while we wait on these nested async dependencies to be resolved.

There are two types of async dependencies that `` can wait on:

1. Components with an async `setup()` hook. This includes components using `` with top\-level `await` expressions.
2. [Async Components](/guide/components/async).

### `async setup()` [​](#async-setup)

A Composition API component's `setup()` hook can be async:

js\`\`\`
export default {
 async setup() {
 const res = await fetch(...)
 const posts = await res.json()
 return {
 posts
 }
 }
}
\`\`\`If using ``, the presence of top\-level `await` expressions automatically makes the component an async dependency:

vue\`\`\`
\
const res = await fetch(...)
const posts = await res.json()
\

\
 {{ posts }}
\
\`\`\`### Async Components [​](#async-components)

Async components are **"suspensible"** by default. This means that if it has a `` in the parent chain, it will be treated as an async dependency of that ``. In this case, the loading state will be controlled by the ``, and the component's own loading, error, delay and timeout options will be ignored.

The async component can opt\-out of `Suspense` control and let the component always control its own loading state by specifying `suspensible: false` in its options.

## Loading State [​](#loading-state)

The `` component has two slots: `#default` and `#fallback`. Both slots only allow for **one** immediate child node. The node in the default slot is shown if possible. If not, the node in the fallback slot will be shown instead.

template\`\`\`
\
 \
 \

 \
 \
 Loading...
 \
\
\`\`\`On initial render, `` will render its default slot content in memory. If any async dependencies are encountered during the process, it will enter a **pending** state. During the pending state, the fallback content will be displayed. When all encountered async dependencies have been resolved, `` enters a **resolved** state and the resolved default slot content is displayed.

If no async dependencies were encountered during the initial render, `` will directly go into a resolved state.

Once in a resolved state, `` will only revert to a pending state if the root node of the `#default` slot is replaced. New async dependencies nested deeper in the tree will **not** cause the `` to revert to a pending state.

When a revert happens, fallback content will not be immediately displayed. Instead, `` will display the previous `#default` content while waiting for the new content and its async dependencies to be resolved. This behavior can be configured with the `timeout` prop: `` will switch to fallback content if it takes longer than `timeout` to render the new default content. A `timeout` value of `0` will cause the fallback content to be displayed immediately when default content is replaced.

## Events [​](#events)

The `` component emits 3 events: `pending`, `resolve` and `fallback`. The `pending` event occurs when entering a pending state. The `resolve` event is emitted when new content has finished resolving in the `default` slot. The `fallback` event is fired when the contents of the `fallback` slot are shown.

The events could be used, for example, to show a loading indicator in front of the old DOM while new components are loading.

## Error Handling [​](#error-handling)

`` currently does not provide error handling via the component itself \- however, you can use the [`errorCaptured`](/api/options-lifecycle#errorcaptured) option or the [`onErrorCaptured()`](/api/composition-api-lifecycle#onerrorcaptured) hook to capture and handle async errors in the parent component of ``.

## Combining with Other Components [​](#combining-with-other-components)

It is common to want to use `` in combination with the [``](/guide/built-ins/transition) and [``](/guide/built-ins/keep-alive) components. The nesting order of these components is important to get them all working correctly.

In addition, these components are often used in conjunction with the `` component from [Vue Router](https://router.vuejs.org/).

The following example shows how to nest these components so that they all behave as expected. For simpler combinations you can remove the components that you don't need:

template\`\`\`
\
 \
 \
 \
 \
 \
 \\

 \
 \
 Loading...
 \
 \
 \
 \
 \
\
\`\`\`Vue Router has built\-in support for [lazily loading components](https://router.vuejs.org/guide/advanced/lazy-loading.html) using dynamic imports. These are distinct from async components and currently they will not trigger ``. However, they can still have async components as descendants and those can trigger `` in the usual way.

## Nested Suspense [​](#nested-suspense)

* Only supported in 3\.3\+

When we have multiple async components (common for nested or layout\-based routes) like this:

template\`\`\`
\
 \
 \
 \
\
\`\`\``` creates a boundary that will resolve all the async components down the tree, as expected. However, when we change `DynamicAsyncOuter`, `` awaits it correctly, but when we change `DynamicAsyncInner`, the nested `DynamicAsyncInner` renders an empty node until it has been resolved (instead of the previous one or fallback slot).

In order to solve that, we could have a nested suspense to handle the patch for the nested component, like:

template\`\`\`
\
 \
 \ \
 \
 \
 \
\
\`\`\`If you don't set the `suspensible` prop, the inner `` will be treated like a sync component by the parent ``. That means that it has its own fallback slot and if both `Dynamic` components change at the same time, there might be empty nodes and multiple patching cycles while the child `` is loading its own dependency tree, which might not be desirable. When it's set, all the async dependency handling is given to the parent `` (including the events emitted) and the inner `` serves solely as another boundary for the dependency resolution and patching.

---

**Related**

* [`` API reference](/api/built-in-components#suspense)
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/built-ins/suspense.md)



## Options: Rendering | Vue.js

[Read the full article](https://vuejs.org/api/options-rendering)

# Options: Rendering [​](#options-rendering)

## template [​](#template)

A string template for the component.

* **Type**

ts\`\`\`
interface ComponentOptions {
 template?: string
}
\`\`\`
* **Details**

A template provided via the `template` option will be compiled on\-the\-fly at runtime. It is only supported when using a build of Vue that includes the template compiler. The template compiler is **NOT** included in Vue builds that have the word `runtime` in their names, e.g. `vue.runtime.esm-bundler.js`. Consult the [dist file guide](https://github.com/vuejs/core/tree/main/packages/vue#which-dist-file-to-use) for more details about the different builds.

If the string starts with `#` it will be used as a `querySelector` and use the selected element's `innerHTML` as the template string. This allows the source template to be authored using native `` elements.

If the `render` option is also present in the same component, `template` will be ignored.

If the root component of your application doesn't have a `template` or `render` option specified, Vue will try to use the `innerHTML` of the mounted element as the template instead.

Security Note

Only use template sources that you can trust. Do not use user\-provided content as your template. See [Security Guide](/guide/best-practices/security#rule-no-1-never-use-non-trusted-templates) for more details.

## render [​](#render)

A function that programmatically returns the virtual DOM tree of the component.

* **Type**

ts\`\`\`
interface ComponentOptions {
 render?(this: ComponentPublicInstance) =\> VNodeChild
}

type VNodeChild = VNodeChildAtom \| VNodeArrayChildren

type VNodeChildAtom =
 \| VNode
 \| string
 \| number
 \| boolean
 \| null
 \| undefined
 \| void

type VNodeArrayChildren = (VNodeArrayChildren \| VNodeChildAtom)\[]
\`\`\`
* **Details**

`render` is an alternative to string templates that allows you to leverage the full programmatic power of JavaScript to declare the render output of the component.

Pre\-compiled templates, for example those in Single\-File Components, are compiled into the `render` option at build time. If both `render` and `template` are present in a component, `render` will take higher priority.
* **See also**

	+ [Rendering Mechanism](/guide/extras/rendering-mechanism)
	+ [Render Functions](/guide/extras/render-function)

## compilerOptions [​](#compileroptions)

Configure runtime compiler options for the component's template.

* **Type**

ts\`\`\`
interface ComponentOptions {
 compilerOptions?: {
 isCustomElement?: (tag: string) =\> boolean
 whitespace?: 'condense' \| 'preserve' // default: 'condense'
 delimiters?: \[string, string] // default: \['{{', '}}']
 comments?: boolean // default: false
 }
}
\`\`\`
* **Details**

This config option is only respected when using the full build (i.e. the standalone `vue.js` that can compile templates in the browser). It supports the same options as the app\-level [app.config.compilerOptions](/api/application#app-config-compileroptions), and has higher priority for the current component.
* **See also** [app.config.compilerOptions](/api/application#app-config-compileroptions)

## slots [​](#slots)

* Only supported in 3\.3\+

An option to assist with type inference when using slots programmatically in render functions.

* **Details**

This option's runtime value is not used. The actual types should be declared via type casting using the `SlotsType` type helper:

ts\`\`\`
import { SlotsType } from 'vue'

defineComponent({
 slots: Object as SlotsType\,
 setup(props, { slots }) {
 expectType\ any)
 \>(slots.default)
 expectType\ any)\>(
 slots.item
 )
 }
})
\`\`\`
[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/options-rendering.md)



## Composition API: setup() | Vue.js

[Read the full article](https://vuejs.org/api/composition-api-setup)

# Composition API: setup() [​](#composition-api-setup)

## Basic Usage [​](#basic-usage)

The `setup()` hook serves as the entry point for Composition API usage in components in the following cases:

1. Using Composition API without a build step;
2. Integrating with Composition\-API\-based code in an Options API component.

Note

If you are using Composition API with Single\-File Components, [``](/api/sfc-script-setup) is strongly recommended for a more succinct and ergonomic syntax.

We can declare reactive state using [Reactivity APIs](/api/reactivity-core) and expose them to the template by returning an object from `setup()`. The properties on the returned object will also be made available on the component instance (if other options are used):

vue\`\`\`
\
import { ref } from 'vue'

export default {
 setup() {
 const count = ref(0\)

 // expose to template and other options API hooks
 return {
 count
 }
 },

 mounted() {
 console.log(this.count) // 0
 }
}
\

\
 \{{ count }}\
\
\`\`\`[refs](/api/reactivity-core#ref) returned from `setup` are [automatically shallow unwrapped](/guide/essentials/reactivity-fundamentals#deep-reactivity) when accessed in the template so you do not need to use `.value` when accessing them. They are also unwrapped in the same way when accessed on `this`.

`setup()` itself does not have access to the component instance \- `this` will have a value of `undefined` inside `setup()`. You can access Composition\-API\-exposed values from Options API, but not the other way around.

`setup()` should return an object *synchronously*. The only case when `async setup()` can be used is when the component is a descendant of a [Suspense](/guide/built-ins/suspense) component.

## Accessing Props [​](#accessing-props)

The first argument in the `setup` function is the `props` argument. Just as you would expect in a standard component, `props` inside of a `setup` function are reactive and will be updated when new props are passed in.

js\`\`\`
export default {
 props: {
 title: String
 },
 setup(props) {
 console.log(props.title)
 }
}
\`\`\`Note that if you destructure the `props` object, the destructured variables will lose reactivity. It is therefore recommended to always access props in the form of `props.xxx`.

If you really need to destructure the props, or need to pass a prop into an external function while retaining reactivity, you can do so with the [toRefs()](/api/reactivity-utilities#torefs) and [toRef()](/api/reactivity-utilities#toref) utility APIs:

js\`\`\`
import { toRefs, toRef } from 'vue'

export default {
 setup(props) {
 // turn \`props\` into an object of refs, then destructure
 const { title } = toRefs(props)
 // \`title\` is a ref that tracks \`props.title\`
 console.log(title.value)

 // OR, turn a single property on \`props\` into a ref
 const title = toRef(props, 'title')
 }
}
\`\`\`## Setup Context [​](#setup-context)

The second argument passed to the `setup` function is a **Setup Context** object. The context object exposes other values that may be useful inside `setup`:

js\`\`\`
export default {
 setup(props, context) {
 // Attributes (Non\-reactive object, equivalent to $attrs)
 console.log(context.attrs)

 // Slots (Non\-reactive object, equivalent to $slots)
 console.log(context.slots)

 // Emit events (Function, equivalent to $emit)
 console.log(context.emit)

 // Expose public properties (Function)
 console.log(context.expose)
 }
}
\`\`\`The context object is not reactive and can be safely destructured:

js\`\`\`
export default {
 setup(props, { attrs, slots, emit, expose }) {
 ...
 }
}
\`\`\``attrs` and `slots` are stateful objects that are always updated when the component itself is updated. This means you should avoid destructuring them and always reference properties as `attrs.x` or `slots.x`. Also note that, unlike `props`, the properties of `attrs` and `slots` are **not** reactive. If you intend to apply side effects based on changes to `attrs` or `slots`, you should do so inside an `onBeforeUpdate` lifecycle hook.

### Exposing Public Properties [​](#exposing-public-properties)

`expose` is a function that can be used to explicitly limit the properties exposed when the component instance is accessed by a parent component via [template refs](/guide/essentials/template-refs#ref-on-component):

js\`\`\`
export default {
 setup(props, { expose }) {
 // make the instance "closed" \-
 // i.e. do not expose anything to the parent
 expose()

 const publicCount = ref(0\)
 const privateCount = ref(0\)
 // selectively expose local state
 expose({ count: publicCount })
 }
}
\`\`\`## Usage with Render Functions [​](#usage-with-render-functions)

`setup` can also return a [render function](/guide/extras/render-function) which can directly make use of the reactive state declared in the same scope:

js\`\`\`
import { h, ref } from 'vue'

export default {
 setup() {
 const count = ref(0\)
 return () =\> h('div', count.value)
 }
}
\`\`\`Returning a render function prevents us from returning anything else. Internally that shouldn't be a problem, but it can be problematic if we want to expose methods of this component to the parent component via template refs.

We can solve this problem by calling [`expose()`](#exposing-public-properties):

js\`\`\`
import { h, ref } from 'vue'

export default {
 setup(props, { expose }) {
 const count = ref(0\)
 const increment = () =\> \+\+count.value

 expose({
 increment
 })

 return () =\> h('div', count.value)
 }
}
\`\`\`The `increment` method would then be available in the parent component via a template ref.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/api/composition-api-setup.md)



## Class and Style Bindings | Vue.js

[Read the full article](https://vuejs.org/guide/essentials/class-and-style)

# Class and Style Bindings [​](#class-and-style-bindings)

A common need for data binding is manipulating an element's class list and inline styles. Since `class` and `style` are both attributes, we can use `v-bind` to assign them a string value dynamically, much like with other attributes. However, trying to generate those values using string concatenation can be annoying and error\-prone. For this reason, Vue provides special enhancements when `v-bind` is used with `class` and `style`. In addition to strings, the expressions can also evaluate to objects or arrays.

## Binding HTML Classes [​](#binding-html-classes)

[Watch a free video lesson on Vue School](https://vueschool.io/lessons/dynamic-css-classes-with-vue-3?friend=vuejs "Free Vue.js Dynamic CSS Classes Lesson")[Watch a free video lesson on Vue School](https://vueschool.io/lessons/vue-fundamentals-capi-dynamic-css-classes-with-vue?friend=vuejs "Free Vue.js Dynamic CSS Classes Lesson")### Binding to Objects [​](#binding-to-objects)

We can pass an object to `:class` (short for `v-bind:class`) to dynamically toggle classes:

template\`\`\`
\\
\`\`\`The above syntax means the presence of the `active` class will be determined by the [truthiness](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) of the data property `isActive`.

You can have multiple classes toggled by having more fields in the object. In addition, the `:class` directive can also co\-exist with the plain `class` attribute. So given the following state:

js\`\`\`
const isActive = ref(true)
const hasError = ref(false)
\`\`\`js\`\`\`
data() {
 return {
 isActive: true,
 hasError: false
 }
}
\`\`\`And the following template:

template\`\`\`
\\
\`\`\`It will render:

template\`\`\`
\\
\`\`\`When `isActive` or `hasError` changes, the class list will be updated accordingly. For example, if `hasError` becomes `true`, the class list will become `"static active text-danger"`.

The bound object doesn't have to be inline:

js\`\`\`
const classObject = reactive({
 active: true,
 'text\-danger': false
})
\`\`\`js\`\`\`
data() {
 return {
 classObject: {
 active: true,
 'text\-danger': false
 }
 }
}
\`\`\`template\`\`\`
\\
\`\`\`This will render:

template\`\`\`
\\
\`\`\`We can also bind to a [computed property](/guide/essentials/computed) that returns an object. This is a common and powerful pattern:

js\`\`\`
const isActive = ref(true)
const error = ref(null)

const classObject = computed(() =\> ({
 active: isActive.value \&\& !error.value,
 'text\-danger': error.value \&\& error.value.type === 'fatal'
}))
\`\`\`js\`\`\`
data() {
 return {
 isActive: true,
 error: null
 }
},
computed: {
 classObject() {
 return {
 active: this.isActive \&\& !this.error,
 'text\-danger': this.error \&\& this.error.type === 'fatal'
 }
 }
}
\`\`\`template\`\`\`
\\
\`\`\`### Binding to Arrays [​](#binding-to-arrays)

We can bind `:class` to an array to apply a list of classes:

js\`\`\`
const activeClass = ref('active')
const errorClass = ref('text\-danger')
\`\`\`js\`\`\`
data() {
 return {
 activeClass: 'active',
 errorClass: 'text\-danger'
 }
}
\`\`\`template\`\`\`
\\
\`\`\`Which will render:

template\`\`\`
\\
\`\`\`If you would like to also toggle a class in the list conditionally, you can do it with a ternary expression:

template\`\`\`
\\
\`\`\`This will always apply `errorClass`, but `activeClass` will only be applied when `isActive` is truthy.

However, this can be a bit verbose if you have multiple conditional classes. That's why it's also possible to use the object syntax inside the array syntax:

template\`\`\`
\\
\`\`\`### With Components [​](#with-components)

> This section assumes knowledge of [Components](/guide/essentials/component-basics). Feel free to skip it and come back later.

When you use the `class` attribute on a component with a single root element, those classes will be added to the component's root element and merged with any existing class already on it.

For example, if we have a component named `MyComponent` with the following template:

template\`\`\`
\
\Hi!\
\`\`\`Then add some classes when using it:

template\`\`\`
\
\
\`\`\`The rendered HTML will be:

template\`\`\`
\Hi!\
\`\`\`The same is true for class bindings:

template\`\`\`
\
\`\`\`When `isActive` is truthy, the rendered HTML will be:

template\`\`\`
\Hi!\
\`\`\`If your component has multiple root elements, you would need to define which element will receive this class. You can do this using the `$attrs` component property:

template\`\`\`
\
\Hi!\
\This is a child component\
\`\`\`template\`\`\`
\
\`\`\`Will render:

html\`\`\`
\Hi!\
\This is a child component\
\`\`\`You can learn more about component attribute inheritance in [Fallthrough Attributes](/guide/components/attrs) section.

## Binding Inline Styles [​](#binding-inline-styles)

### Binding to Objects [​](#binding-to-objects-1)

`:style` supports binding to JavaScript object values \- it corresponds to an [HTML element's `style` property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style):

js\`\`\`
const activeColor = ref('red')
const fontSize = ref(30\)
\`\`\`js\`\`\`
data() {
 return {
 activeColor: 'red',
 fontSize: 30
 }
}
\`\`\`template\`\`\`
\\
\`\`\`Although camelCase keys are recommended, `:style` also supports kebab\-cased CSS property keys (corresponds to how they are used in actual CSS) \- for example:

template\`\`\`
\\
\`\`\`It is often a good idea to bind to a style object directly so that the template is cleaner:

js\`\`\`
const styleObject = reactive({
 color: 'red',
 fontSize: '30px'
})
\`\`\`js\`\`\`
data() {
 return {
 styleObject: {
 color: 'red',
 fontSize: '13px'
 }
 }
}
\`\`\`template\`\`\`
\\
\`\`\`Again, object style binding is often used in conjunction with computed properties that return objects.

### Binding to Arrays [​](#binding-to-arrays-1)

We can bind `:style` to an array of multiple style objects. These objects will be merged and applied to the same element:

template\`\`\`
\\
\`\`\`### Auto\-prefixing [​](#auto-prefixing)

When you use a CSS property that requires a [vendor prefix](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix) in `:style`, Vue will automatically add the appropriate prefix. Vue does this by checking at runtime to see which style properties are supported in the current browser. If the browser doesn't support a particular property then various prefixed variants will be tested to try to find one that is supported.

### Multiple Values [​](#multiple-values)

You can provide an array of multiple (prefixed) values to a style property, for example:

template\`\`\`
\\
\`\`\`This will only render the last value in the array which the browser supports. In this example, it will render `display: flex` for browsers that support the unprefixed version of flexbox.

[Edit this page on GitHub](https://github.com/vuejs/docs/edit/main/src/guide/essentials/class-and-style.md)



