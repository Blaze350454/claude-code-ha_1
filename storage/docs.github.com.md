# GitHub REST API Documentation

Source: https://docs.github.com/en/rest



---

<!-- source: https://docs.github.com/en/rest/about-the-rest-api/about-the-openapi-description-for-the-rest-api -->

---
title: About the OpenAPI description for the REST API
shortTitle: OpenAPI description
intro: 'The {% data variables.product.github %} REST API is fully described in an OpenAPI compliant document.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/overview/openapi-description
  - /rest/overview/about-the-openapi-description-for-the-rest-api
category:
  - Learn about the REST API
---

## About OpenAPI

OpenAPI is a specification for describing REST API interfaces. It describes the API without requiring access to the source code or additional documentation. The specification is both human and machine readable. For more information, see [the OpenAPI specification documentation](https://spec.openapis.org/oas/v3.1.0).

## About {% data variables.product.company_short %}'s OpenAPI description

{% data variables.product.company_short %}'s OpenAPI description of the REST API is publicly available. You can find the description in the open source [github/rest-api-description](https://github.com/github/rest-api-description) repository.

{% data variables.product.company_short %} provides both 3.0 and 3.1 OpenAPI descriptions.

For each description, there is a version for each product: {% data variables.product.prodname_free_user %}/{% data variables.product.prodname_pro %}/{% data variables.product.prodname_team %} (`api.github.com`), {% data variables.product.prodname_ghe_cloud %} (`ghec`), and each version of {% data variables.product.prodname_ghe_server %} (`ghes-X.X`).

For each product, if date-based versioning is supported, there is also a description for each date-based version. For more information, see [AUTOTITLE](/rest/overview/api-versions).

Each description is available in a bundled or in a dereferenced format. The bundled format uses `$ref` to refer to OpenAPI components that are shared between endpoints. The dereferenced format includes the fully expanded description.

## Using the {% data variables.product.company_short %} OpenAPI description

Because the OpenAPI description is machine readable, you can use it to do things like:

* Generate libraries to facilitate using the REST API
* Validate and test an integration that uses the REST API
* Explore and interact with the REST API using third-party tools, such as Insomnia or Postman

For example, {% data variables.product.company_short %} uses the OpenAPI description to generate the Octokit SDKs. {% data variables.product.company_short %} also uses the OpenAPI description to generate the REST API reference documentation for each endpoint.


---

<!-- source: https://docs.github.com/en/rest/about-the-rest-api/about-the-rest-api -->

---
title: About the REST API
shortTitle: About the REST API
intro: 'Get oriented to the REST API documentation.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/overview/about-the-rest-api
category:
  - Learn about the REST API
---

You can use {% data variables.product.company_short %}'s API to build scripts and applications that automate processes, integrate with {% data variables.product.company_short %}, and extend {% data variables.product.company_short %}. For example, you could use the API to triage issues, build an analytics dashboard, or manage releases.

Each REST API endpoint is documented individually, and the endpoints are categorized by the resource that they primarily affect. For example, you can find endpoints relating to issues in [AUTOTITLE](/rest/issues).

## Getting started with the REST API

**If you are new to REST APIs**, you may find it helpful to refer to the Quickstart or Getting Started guide for an introduction. For more information, see:

* [AUTOTITLE](/rest/quickstart)
* [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api)

**If you are familiar with REST APIs** but new to {% data variables.product.company_short %}'s REST API, you may find it helpful to refer to the authentication documentation. For more information, see:

* [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api)

**If you are building scripts or applications** that use the REST API, you may find some of the following guides helpful. For examples of scripting with the REST API, see:

* [AUTOTITLE](/rest/guides/scripting-with-the-rest-api-and-javascript)
* [AUTOTITLE](/rest/guides/scripting-with-the-rest-api-and-ruby)
* [AUTOTITLE](/apps/creating-github-apps/writing-code-for-a-github-app/building-a-github-app-that-responds-to-webhook-events)
* [AUTOTITLE](/apps/creating-github-apps/writing-code-for-a-github-app/building-a-cli-with-a-github-app)
* [AUTOTITLE](/webhooks/using-webhooks/automatically-redelivering-failed-deliveries-for-a-repository-webhook)

For a list of libraries to facilitate scripting with the REST API, see [AUTOTITLE](/rest/overview/libraries-for-the-rest-api).

If you are building scripts or applications that use the REST API, you might also be interested in using webhooks to get notified about events or a {% data variables.product.prodname_github_app %} to access resources on behalf of a user or in an organization. For more information, see [AUTOTITLE](/webhooks/about-webhooks) and [AUTOTITLE](/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app).

## Further reading

* [AUTOTITLE](/rest/overview/comparing-githubs-rest-api-and-graphql-api)
* [AUTOTITLE](/rest/guides/best-practices-for-using-the-rest-api)
* [AUTOTITLE](/rest/overview/keeping-your-api-credentials-secure)
* [AUTOTITLE](/rest/overview/troubleshooting-the-rest-api)


---

<!-- source: https://docs.github.com/en/rest/about-the-rest-api/api-versions -->

---
title: API Versions
shortTitle: API Versions
intro: Learn how to specify which REST API version to use whenever you make a request to the REST API.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/overview/api-versions
category:
  - Learn about the REST API
---

## About API versioning

{% data reusables.rest-api.about-api-versions %}

{% ifversion ghes %}

## About {% data variables.product.prodname_ghe_server %} versioning and REST API versioning

{% data variables.product.prodname_ghe_server %} versions are decoupled from REST API versions. You can upgrade your {% data variables.product.prodname_ghe_server %} version but keep the same REST API version, as long as the API version is included in the {% data variables.product.prodname_ghe_server %} version. Similarly, you can upgrade your REST API version without updating your {% data variables.product.prodname_ghe_server %} version, as long as the new REST API version you choose is available for your {% data variables.product.prodname_ghe_server %} version.

The {% data variables.product.prodname_ghe_server %} release notes will state when a REST API version is no longer supported. For more information, see [AUTOTITLE](/admin/release-notes).

{% endif %}

## Specifying an API version

You should use the `X-GitHub-Api-Version` header to specify an API version. For example:

```shell
curl {% data reusables.rest-api.version-header %} https://api.github.com/zen
```

Requests without the `X-GitHub-Api-Version` header will default to use the `{{ defaultRestApiVersion }}` version.

If you specify an API version that is no longer supported, you will receive a `410 Gone` response.

## Upgrading to a new API version

Before upgrading to a new REST API version, you should read the changelog of breaking changes for the new API version to understand what breaking changes are included and to learn more about how to upgrade to that specific API version. For more information, see [AUTOTITLE](/rest/overview/breaking-changes).

When you update your integration to specify the new API version in the `X-GitHub-Api-Version` header, you'll also need to make any changes required for your integration to work with the new API version.

Once your integration is updated, test your integration to verify that it works with the new API version.

## API version {% data variables.release-phases.closing_down %}

API versions are supported for 24 months after a newer API version is released.

While a version is within its support window but approaching  {% data variables.release-phases.closing_down %}, {% data variables.product.github %} includes the following headers in API responses to help you prepare for migration:

* `Deprecation` — The date when the API version will be {% data variables.release-phases.closing_down %}, formatted as an HTTP date per [RFC 7231](https://tools.ietf.org/html/rfc7231#section-7.1.1.1). For example: `Wed, 27 Nov 2019 14:34:29 GMT`. <!-- markdownlint-disable-line GHD046 -->
* `Sunset` — The date when the API version will be completely removed ({% data variables.release-phases.retired %}), after which requests will return a `410 Gone` response. Follows [RFC 8594](https://tools.ietf.org/html/rfc8594). For example: `Fri, 27 Nov 2020 14:34:29 GMT`. <!-- markdownlint-disable-line GHD046 -->

After the support window ends:

* Requests that specify a {% data variables.release-phases.closing_down %} API version receive a `410 Gone` response.
* Requests that do not specify an API version default to the next oldest supported version, not the {% data variables.release-phases.closing_down %} version. If you rely on unversioned requests, you may observe behavioral changes as older versions are removed from support.

For more information on migrating to a newer API version, see [AUTOTITLE](/rest/about-the-rest-api/breaking-changes).

## Exceptions to standard versioning

In rare cases, {% data variables.product.github %} may make changes outside the normal API versioning cadence. These are exceptional interventions that do not alter the standard versioning guarantees for most integrators.

### Security, availability, and reliability issues

Critical security vulnerabilities, data exposure risks, or severe reliability issues may require changes outside the normal release schedule. {% data variables.product.github %} may release an unscheduled API version, backport fixes to supported versions, or in rare cases, introduce a breaking change to an existing version to protect users and platform integrity.

{% data variables.product.github %} will communicate such changes through release notes, changelogs, and direct communication explaining what changed and why. Where feasible, advance notice will be provided. Immediate action may be taken without advance notice when required.

### Low-usage services

For certain services with very low usage, {% data variables.product.github %} may deprecate functionality outside the standard versioning process. In these cases, {% data variables.product.github %} will communicate the intent and reach out to affected integrators directly.

## Supported API versions

The following REST API versions are currently supported.

| API version | End of support date |
| --- | --- |
{%- for apiVersion in allVersions[currentVersion].apiVersions %}
{%- assign versionData = tables.rest-api-versions.versions[apiVersion] %}
| `{{ apiVersion }}` | {{ versionData.end_of_support | default: "Not yet scheduled" }} |
{%- endfor %}

You can also make an API request to get all of the supported API versions. For more information, see [AUTOTITLE](/rest/meta/meta#get-all-api-versions).


---

<!-- source: https://docs.github.com/en/rest/about-the-rest-api/breaking-changes -->

---
title: Breaking changes
shortTitle: Breaking changes
intro: Learn about breaking changes that were introduced in each REST API version.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/overview/breaking-changes
category:
  - Learn about the REST API
---

## About breaking changes in the REST API

{% data reusables.rest-api.about-api-versions %}

For more information about API versions, see [AUTOTITLE](/rest/overview/api-versions).

## Upgrading to a new API version

Before upgrading to a new REST API version, you should read the section on this page that corresponds to the new API version to understand what breaking changes are included and to learn more about how to upgrade to that API version.

When you update your integration to specify the new API version in the `X-GitHub-Api-Version` header, you'll also need to make any changes required for your integration to work with the new API version.

Once your integration is updated, test your integration to verify that it works with the new API version.

{% data reusables.rest-api.breaking-changes-changelog %}


---

<!-- source: https://docs.github.com/en/rest/about-the-rest-api/comparing-githubs-rest-api-and-graphql-api -->

---
title: Comparing GitHub's REST API and GraphQL API
shortTitle: Comparing GitHub's APIs
intro: 'Learn about {% data variables.product.github %}''s APIs to extend and customize your {% data variables.product.github %} experience.'
redirect_from:
  - /v3/versions
  - /articles/getting-started-with-the-api
  - /github/extending-github/getting-started-with-the-api
  - /developers/overview/about-githubs-apis
  - /rest/overview/about-githubs-apis
  - /rest/overview/comparing-githubs-rest-api-and-graphql-api
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---

## About {% data variables.product.company_short %}'s APIs

{% data variables.product.company_short %} provides two APIs: a REST API and a GraphQL API. You can interact with both APIs using {% data variables.product.prodname_cli %}, curl, the official Octokit libraries, and third party libraries. Occasionally, a feature may be supported on one API but not the other.

You should use the API that best aligns with your needs and that you are most comfortable using. You don't need to exclusively use one API over the other. Node IDs let you move between the REST API and GraphQL API. For more information, see [AUTOTITLE](/graphql/guides/using-global-node-ids).

This article discusses the benefits of each API. For more information about the GraphQL API, see [AUTOTITLE](/graphql/overview/about-the-graphql-api). For more information about the REST API, see [AUTOTITLE](/rest/about-the-rest-api/about-the-rest-api).

## Choosing the GraphQL API

The GraphQL API returns exactly the data that you request. GraphQL also returns the data in a pre-known structure based on your request. In contrast, the REST API returns more data than you requested and returns it in a pre-determined structure. You can also accomplish the equivalent of multiple REST API request in a single GraphQL request. The ability to make fewer requests and fetch less data makes GraphQL appealing to developers of mobile applications.

For example, to get the {% data variables.product.github %} login of ten of your followers, and the login of ten followers of each of your followers, you can send a single request like:

```graphql
{
  viewer {
    followers(first: 10) {
      nodes {
        login
        followers(first: 10) {
          nodes {
            login
          }
        }
      }
    }
  }
}
```

The response will be a JSON object that follows the structure of your request.

In contrast, to get this same information from the REST API, you would need to first make a request to `GET /user/followers`. The API would return the login of each follower, along with other data about the followers that you don't need. Then, for each follower, you would need to make a request to `GET /users/{username}/followers`. In total, you would need to make 11 requests to get the same information that you could get from a single GraphQL request, and you would receive excess data.

## Choosing the REST API

Because REST APIs have been around for longer than GraphQL APIs, some developers are more comfortable with the REST API. Since REST APIs use standard HTTP verbs and concepts, many developers are already familiar with the basic concepts to use the REST API.

For example, to create an issue in the `octocat/Spoon-Knife` repository, you would need to send a request to `POST /repos/octocat/Spoon-Knife/issues` with a JSON request body:

```json
{
  "title": "Bug with feature X",
  "body": "If you do A, then B happens"
}
```

In contrast, to make an issue using the GraphQL API, you would need to get the node ID of the `octocat/Spoon-Knife` repository and then send a request like:

```graphql
mutation {
  createIssue(
    input: {
      repositoryId: "MDEwOlJlcG9zaXRvcnkxMzAwMTky"
      title: "Bug with feature X"
      body: "If you do A, then B happens"}
  ) {
    issue {
      number
      url
    }
  }
}
```


---

<!-- source: https://docs.github.com/en/rest/about-the-rest-api -->

---
title: About the REST API
intro: 'Learn more about the {% data variables.product.prodname_dotcom %} REST API and what you can do with it.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /about-the-rest-api
  - /comparing-githubs-rest-api-and-graphql-api
  - /api-versions
  - /breaking-changes
  - /about-the-openapi-description-for-the-rest-api
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/artifacts -->

---
title: REST API endpoints for GitHub Actions artifacts
allowTitleToDifferFromFilename: true
shortTitle: Artifacts
intro: >-
  Use the REST API to interact with artifacts in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About artifacts in {% data variables.product.prodname_actions %}

You can use the REST API to download, delete, and retrieve information about workflow artifacts in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-artifacts %} For more information, see [AUTOTITLE](/actions/using-workflows/storing-workflow-data-as-artifacts).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/cache -->

---
title: REST API endpoints for GitHub Actions cache
allowTitleToDifferFromFilename: true
shortTitle: Cache
intro: >-
  Use the REST API to interact with the cache for repositories in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About the cache in {% data variables.product.prodname_actions %}

You can use the REST API to query and manage the cache for repositories in {% data variables.product.prodname_actions %}. You can also install a {% data variables.product.prodname_cli %} extension to manage your caches from the command line. For more information, see [AUTOTITLE](/actions/using-workflows/caching-dependencies-to-speed-up-workflows#managing-caches).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/concurrency-groups -->

---
title: REST API endpoints for Actions concurrency groups
shortTitle: Actions concurrency groups
intro: >-
  Use the REST API to view and manage concurrency groups for GitHub Actions
  workflows.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Automate CI/CD workflows
---

## About concurrency groups in {% data variables.product.prodname_actions %}

You can use the REST API to read the state of {% data variables.product.prodname_actions %} concurrency groups, which ensure that only a single job or workflow using the same group will run at a time while additional runs are pending or canceled depending on configuration. For more information, see [AUTOTITLE](/actions/using-jobs/using-concurrency).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/hosted-runners -->

---
title: GitHub-hosted runners
shortTitle: GitHub-hosted runners
intro: Use the REST API to interact with {% data variables.product.prodname_dotcom %}-hosted runners in {% data variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Automate CI/CD workflows
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions -->

---
title: REST API endpoints for GitHub Actions
shortTitle: Actions
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data variables.product.prodname_actions
  %} for an organization or repository.
redirect_from:
  - /v3/actions
  - /rest/reference/actions
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /artifacts
  - /cache
  - /concurrency-groups
  - /hosted-runners
  - /oidc
  - /permissions
  - /secrets
  - /self-hosted-runner-groups
  - /self-hosted-runners
  - /variables
  - /workflow-jobs
  - /workflow-runs
  - /workflows
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/oidc -->

---
title: REST API endpoints for GitHub Actions OIDC
allowTitleToDifferFromFilename: true
shortTitle: OIDC
intro: 'Use the REST API to interact with JWTs for OIDC subject claims in {% data variables.product.prodname_actions %}.'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About {% data variables.product.prodname_actions %} OIDC

You can use the REST API to query and manage a customization template for an OpenID Connect (OIDC) subject claim. For more information, see [AUTOTITLE](/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/permissions -->

---
title: REST API endpoints for GitHub Actions permissions
allowTitleToDifferFromFilename: true
shortTitle: Permissions
intro: >-
  Use the REST API to interact with permissions for {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About permissions for {% data variables.product.prodname_actions %}

You can use the REST API to set permissions for the {% ifversion ghes or ghec %}enterprises, {% endif %}organizations and repositories that are allowed to run {% data variables.product.prodname_actions %}, and the actions{% ifversion actions-workflow-policy %} and reusable workflows{% endif %} that are allowed to run. For more information, see [AUTOTITLE](/actions/learn-github-actions/usage-limits-billing-and-administration#disabling-or-limiting-github-actions-for-your-repository-or-organization).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/secrets -->

---
title: REST API endpoints for GitHub Actions Secrets
allowTitleToDifferFromFilename: true
shortTitle: Secrets
intro: >-
  Use the REST API to interact with secrets in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About secrets in {% data variables.product.prodname_actions %}

You can use the REST API to create, update, delete, and retrieve information about secrets that can be used in workflows in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-secrets %} For more information, see [AUTOTITLE](/actions/security-for-github-actions/security-guides/about-secrets).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/self-hosted-runner-groups -->

---
title: REST API endpoints for self-hosted runner groups
shortTitle: Self-hosted runner groups
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with self-hosted runner groups for {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About self-hosted runner groups in {% data variables.product.prodname_actions %}

You can use the REST API to manage groups of self-hosted runners in {% data variables.product.prodname_actions %}. For more information, see [AUTOTITLE](/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups).

{% data reusables.actions.actions-authentication %} {% data variables.product.prodname_github_apps %} must have the `administration` permission for repositories or the `organization_self_hosted_runners` permission for organizations. Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises to use these endpoints.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/self-hosted-runners -->

---
title: REST API endpoints for self-hosted runners
shortTitle: Self-hosted runners
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with self-hosted runners in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About self-hosted runners in {% data variables.product.prodname_actions %}

You can use the REST API to register, view, and delete self-hosted runners in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-self-hosted-runners %} For more information, see [AUTOTITLE](/actions/how-tos/managing-self-hosted-runners).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/variables -->

---
title: REST API endpoints for GitHub Actions variables
allowTitleToDifferFromFilename: true
shortTitle: Variables
intro: 'Use the REST API to interact with variables in {% data variables.product.prodname_actions %}.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About variables in {% data variables.product.prodname_actions %}

You can use the REST API to create, update, delete, and retrieve information about variables that can be used in workflows in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-variables %} For more information, see [AUTOTITLE](/actions/learn-github-actions/variables) in the {% data variables.product.prodname_actions %} documentation.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/workflow-jobs -->

---
title: REST API endpoints for workflow jobs
shortTitle: Workflow jobs
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with workflow jobs in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About workflow jobs in {% data variables.product.prodname_actions %}

You can use the REST API to view logs and workflow jobs in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-workflow-jobs %} For more information, see [AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/workflow-runs -->

---
title: REST API endpoints for workflow runs
shortTitle: Workflow runs
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with workflow runs in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About workflow runs in {% data variables.product.prodname_actions %}

You can use the REST API to view, re-run, cancel, and view logs for workflow runs in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-workflow-runs %} For more information, see [AUTOTITLE](/actions/managing-workflow-runs).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/actions/workflows -->

---
title: REST API endpoints for workflows
shortTitle: Workflows
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with workflows in {% data
  variables.product.prodname_actions %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About workflows in {% data variables.product.prodname_actions %}

You can use the REST API to view workflows for a repository in {% data variables.product.prodname_actions %}. {% data reusables.actions.about-workflows %} For more information, see [AUTOTITLE](/actions/using-workflows/about-workflows) in the {% data variables.product.prodname_actions %} documentation.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/activity/events -->

---
title: REST API endpoints for events
shortTitle: Events
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data variables.product.github %}
  events.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About {% data variables.product.github %} events

{% data variables.product.github %} events power the various activity streams on the site.

You can use the REST API to return different types of events triggered by activity on {% data variables.product.github %}. For more information about the specific events that you can receive, see [AUTOTITLE](/webhooks-and-events/events/github-event-types). Endpoints for repository issues are also available. For more information, see [AUTOTITLE](/rest/issues/events).

Events are optimized for polling with the "ETag" header. If no new events have been triggered, you will see a "304 Not Modified" response, and your current rate limit will be untouched. There is also an "X-Poll-Interval" header that specifies how often (in seconds) you are allowed to poll. In times of high server load, the time may increase. Please obey the header.

``` shell
$ curl -I {% data variables.product.rest_url %}/users/tater/events
> HTTP/2 200
> X-Poll-Interval: 60
> ETag: "a18c3bded88eb5dbb5c849a489412bf3"

# The quotes around the ETag value are important
$ curl -I {% data variables.product.rest_url %}/users/tater/events \
$    -H 'If-None-Match: "a18c3bded88eb5dbb5c849a489412bf3"'
> HTTP/2 304
> X-Poll-Interval: 60
```

The timeline will include up to 300 events. Only events created within the past 30 days will be included. Events older than 30 days will not be included (even if the total number of events in the timeline is less than 300).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/activity/feeds -->

---
title: REST API endpoints for feeds
shortTitle: Feeds
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data variables.product.prodname_dotcom %}
  feeds.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/activity -->

---
title: REST API endpoints for activity
shortTitle: Activity
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to list events and feeds and manage notifications, starring, and watching.'
redirect_from:
  - /v3/activity
  - /rest/reference/activity
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /events
  - /feeds
  - /notifications
  - /starring
  - /watching
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/activity/notifications -->

---
title: REST API endpoints for notifications
shortTitle: Notifications
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to manage {% data variables.product.github %}
  notifications.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About {% data variables.product.github %} notifications

{% data reusables.user-settings.notifications-api-classic-pat-only %}

You can use the REST API to manage {% data variables.product.github %} notifications. For more information about notifications, see [AUTOTITLE](/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications).

All calls to these endpoints require the `notifications` or `repo` scopes. You will need the `repo` scope to access issues and commits from their respective endpoints.

Notifications are returned as "threads". A thread contains information about the current discussion of an issue, pull request, or commit.

Notifications are optimized for polling with the `Last-Modified` header. If there are no new notifications, you will see a `304 Not Modified` response, leaving your current rate limit untouched. There is an `X-Poll-Interval` header that specifies how often (in seconds) you are allowed to poll. In times of high server load, the time may increase. Please obey the header.

``` shell
# Add authentication to your requests
$ curl -I {% data variables.product.rest_url %}/notifications
HTTP/2 200
Last-Modified: Thu, 25 Oct 2012 15:16:27 GMT
X-Poll-Interval: 60

# Pass the Last-Modified header exactly
$ curl -I {% data variables.product.rest_url %}/notifications
$    -H "If-Modified-Since: Thu, 25 Oct 2012 15:16:27 GMT"
> HTTP/2 304
> X-Poll-Interval: 60
```

### About notification reasons

These GET endpoints return a `reason` key. These `reason`s correspond to events that trigger a notification.

There are a few potential `reason`s for receiving a notification.

Reason Name | Description
------------|------------
`approval_requested` | You were requested to review and approve a deployment. For more information, see [AUTOTITLE](/actions/managing-workflow-runs/reviewing-deployments).
`assign` | You were assigned to the issue.
`author` | You created the thread.
`ci_activity` | A {% data variables.product.prodname_actions %} workflow run that you triggered was completed.
`comment` | You commented on the thread.
`invitation` | You accepted an invitation to contribute to the repository.
`manual` | You subscribed to the thread (via an issue or pull request).
`member_feature_requested` | Organization members have requested to enable a feature such as Copilot.
`mention` | You were specifically **@mentioned** in the content.
`review_requested` | You, or a team you're a member of, were requested to review a pull request.{% ifversion fpt or ghec %}
`security_advisory_credit` | You were credited for contributing to a security advisory.
`security_alert` | {% data variables.product.prodname_dotcom %} discovered a [security vulnerability](/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) in your repository.{% endif %}
`state_change` | You changed the thread state (for example, closing an issue or merging a pull request).
`subscribed` | You're watching the repository.
`team_mention` | You were on a team that was mentioned.

Note that the `reason` is modified on a per-thread basis, and can change, if the `reason` on a later notification is different.

For example, if you are the author of an issue, subsequent notifications on that issue will have a `reason` of `author`. If you're then **@mentioned** on the same issue, the notifications you fetch thereafter will have a `reason` of `mention`. The `reason` remains as `mention`, regardless of whether you're ever mentioned again.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/activity/starring -->

---
title: REST API endpoints for starring
shortTitle: Starring
intro: Use the REST API to bookmark a repository.
allowTitleToDifferFromFilename: true
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About starring

You can use the REST API to star (bookmark) a repository. Stars are shown next to repositories to show an approximate level of interest. Stars have no effect on notifications or the activity feed. For more information, see [AUTOTITLE](/get-started/exploring-projects-on-github/saving-repositories-with-stars).

### Starring versus watching

In August 2012, we [changed the way watching
works](https://github.com/blog/1204-notifications-stars) on {% data variables.product.prodname_dotcom %}. Some API
client applications may still be using the original "watcher" endpoints for accessing
this data. You should now use the "star" endpoints instead (described
below). For more information, see [AUTOTITLE](/rest/activity/watching) and the [changelog post](https://developer.github.com/changes/2012-09-05-watcher-api/).

In responses from the REST API, `watchers`, `watchers_count`, and `stargazers_count` correspond to the number of users that have starred a repository, whereas `subscribers_count` corresponds to the number of watchers.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/activity/watching -->

---
title: REST API endpoints for watching
shortTitle: Watching
intro: Use the REST API to subscribe to notifications for activity in a repository.
allowTitleToDifferFromFilename: true
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About watching

You can use the REST API to subscribe to notifications for activity in a repository. To bookmark a repository instead, see [AUTOTITLE](/rest/activity/starring).

### Watching versus starring

In August 2012, we [changed the way watching
works](https://github.com/blog/1204-notifications-stars) on {% data variables.product.prodname_dotcom %}. Some API
client applications may still be using the original "watcher" endpoints for accessing
this data. You should now use the "star" endpoints instead. For more information, [AUTOTITLE](/rest/activity/starring) and the [changelog post](https://developer.github.com/changes/2012-09-05-watcher-api/).

In responses from the REST API, `subscribers_count` corresponds to the number of watchers, whereas `watchers`, `watchers_count`, and `stargazers_count` correspond to the number of users that have starred a repository.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/agent-tasks/agent-tasks -->

---
title: REST API endpoints for agent tasks
shortTitle: Agent tasks
intro: Use the REST API to start and manage {% data variables.copilot.copilot_cloud_agent %} tasks
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/agent-tasks -->

---
title: REST API endpoints for agent tasks
shortTitle: Agent tasks
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /agent-tasks
versions:
  fpt: '*'
  ghec: '*'
---



---

<!-- source: https://docs.github.com/en/rest/agents -->

---
title: REST endpoints for agents
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /secrets
  - /variables
versions:
  fpt: '*'
  ghec: '*'
---



---

<!-- source: https://docs.github.com/en/rest/agents/secrets -->

---
title: REST API endpoints for agent secrets
shortTitle: Secrets
intro: Use the REST API to manage secrets for agents.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/agents/variables -->

---
title: REST API endpoints for variables
shortTitle: Variables
intro: Use the REST API to manage variables.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/announcement-banners/enterprises -->

---
title: REST API endpoints for enterprise announcement banners
shortTitle: Enterprise
intro: >-
  The Enterprise Announcement Banners API allows you to get, set, and remove the
  announcement banner for your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Administer enterprises and billing
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/announcement-banners -->

---
title: REST API endpoints for announcement banners
shortTitle: Announcement banners
allowTitleToDifferFromFilename: true
intro: 'The Announcement Banners API enables you to view, create, and remove an announcement banner for your enterprise or organization.'
versions:
  ghec: '*'
  ghes: '*'
children:
  - /enterprises
  - /organizations
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/announcement-banners/organizations -->

---
title: REST API endpoints for organization announcement banners
shortTitle: Organization
intro: 'The Organization Announcement Banners API allows you to get, set, and remove the announcement banner for your organization.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage organizations and teams
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/apps/apps -->

---
title: 'REST API endpoints for {% data variables.product.prodname_github_apps %}'
shortTitle: '{% data variables.product.prodname_github_apps %}'
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data
  variables.product.prodname_github_apps %}
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Build apps and integrations
---

## About {% data variables.product.prodname_github_apps %}

{% data reusables.apps.general-apps-restrictions %}

This page lists endpoints that you can access while authenticated as a {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app).

See [AUTOTITLE](/rest/apps/installations) for a list of endpoints that require authentication as a {% data variables.product.prodname_github_app %} installation.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/apps -->

---
title: REST API endpoints for apps
shortTitle: Apps
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to retrieve information about {% data variables.product.prodname_github_apps %} and {% data variables.product.prodname_github_app %} installations.'
redirect_from:
  - /v3/apps
  - /rest/reference/apps
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /apps
  - /installations
  - /marketplace
  - /oauth-applications
  - /webhooks
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/apps/installations -->

---
title: 'REST API endpoints for {% data variables.product.prodname_github_app %} installations'
allowTitleToDifferFromFilename: true
shortTitle: Installations
intro: >-
  Use the REST API to get information about {% data
  variables.product.prodname_github_app %} installations and perform actions
  within those installations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Build apps and integrations
---

## About {% data variables.product.prodname_github_app %} installations

A {% data variables.product.prodname_github_app %} installation refers to the installation of the app on an {% ifversion enterprise-installed-apps %}enterprise, {% endif %}organization or user account. For information on how to authenticate as an installation and limit access to specific repositories, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation).

To list all {% data variables.product.prodname_github_app %} installations for an organization, see [AUTOTITLE](/rest/orgs/orgs#list-app-installations-for-an-organization).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/apps/marketplace -->

---
title: 'REST API endpoints for {% data variables.product.prodname_marketplace %}'
allowTitleToDifferFromFilename: true
shortTitle: Marketplace
intro: >-
  Use the REST API to interact with {% data
  variables.product.prodname_marketplace %}
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Build apps and integrations
---

## About {% data variables.product.prodname_marketplace %}

For more information about {% data variables.product.prodname_marketplace %}, see [AUTOTITLE](/apps/publishing-apps-to-github-marketplace).

These endpoints allow you to see which customers are using a pricing plan, see a customer's purchases, and see if an account has an active subscription.

### Testing with stubbed endpoints

You can [test your {% data variables.product.prodname_github_app %}](/apps/publishing-apps-to-github-marketplace/using-the-github-marketplace-api-in-your-app/testing-your-app) with **stubbed data**. Stubbed data is hard-coded, fake data that will not change based on actual subscriptions.

To test with stubbed data, use a stubbed endpoint in place of its production counterpart. This allows you to test whether the API logic succeeds before listing {% data variables.product.prodname_github_apps %} on {% data variables.product.prodname_marketplace %}.

Make sure to replace stubbed endpoints with production endpoints before deploying your {% data variables.product.prodname_github_app %}.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/apps/oauth-applications -->

---
title: REST API endpoints for OAuth authorizations
shortTitle: OAuth authorizations
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data
  variables.product.prodname_oauth_apps %} and OAuth authorizations of {% data
  variables.product.prodname_github_apps %}
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Build apps and integrations
---

## About {% data variables.product.prodname_oauth_apps %} and OAuth authorizations of {% data variables.product.prodname_github_apps %}

You can use these endpoints to manage the OAuth tokens that {% data variables.product.prodname_oauth_apps %} or {% data variables.product.prodname_github_apps %} use to access people's accounts on {% data variables.product.github %}.

Tokens for {% data variables.product.prodname_oauth_apps %} have the prefix `gho_`, while OAuth tokens for {% data variables.product.prodname_github_apps %}, used for authenticating on behalf of the user, have the prefix `ghu_`. You can use the following endpoints for both types of OAuth tokens.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/apps/webhooks -->

---
title: 'REST API endpoints for {% data variables.product.prodname_github_app %} webhooks'
allowTitleToDifferFromFilename: true
shortTitle: Webhooks
intro: >-
  Use the REST API to interact with webhooks for {% data
  variables.product.prodname_oauth_apps %}
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Build apps and integrations
---

## About webhooks for {% data variables.product.prodname_github_apps %}

A {% data variables.product.prodname_github_app %}'s webhook allows your server to receive HTTP `POST` payloads whenever certain events happen for a {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/webhooks) and [AUTOTITLE](/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api -->

---
title: Authenticating to the REST API
intro: You can authenticate to the REST API to access more endpoints and have a higher rate limit.
redirect_from:
  - /v3/auth
  - /rest/overview/other-authentication-methods
  - /rest/overview/authenticating-to-the-rest-api
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Authenticating
category:
  - Authenticate API requests
---

## About authentication

Many REST API endpoints require authentication or return additional information if you are authenticated. Additionally, you can make more requests per hour when you are authenticated.

To authenticate your request, you will need to provide an authentication token with the required scopes or permissions. There a few different ways to get a token: You can create a {% data variables.product.pat_generic %}, generate a token with a {% data variables.product.prodname_github_app %}, or use the built-in `GITHUB_TOKEN` in a {% data variables.product.prodname_actions %} workflow.

After creating a token, you can authenticate your request by sending the token in the `Authorization` header of your request. For example, in the following request, replace `YOUR-TOKEN` with a reference to your token:

```shell
curl --request GET \
--url "{% data variables.product.rest_url %}/octocat" \
--header "Authorization: Bearer YOUR-TOKEN" \
--header "X-GitHub-Api-Version: {{ allVersions[currentVersion].latestApiVersion }}"
```

> [!NOTE]
> {% data reusables.getting-started.bearer-vs-token %}

### Failed login limit

If you try to use a REST API endpoint without a token or with a token that has insufficient permissions, you will receive a `404 Not Found` or `403 Forbidden` response. Authenticating with invalid credentials will initially return a `401 Unauthorized` response.

After detecting several requests with invalid credentials within a short period, the API will temporarily reject all authentication attempts for that user (including ones with valid credentials) with a `403 Forbidden` response. For more information, see [AUTOTITLE](/rest/overview/rate-limits-for-the-rest-api).

## Authenticating with a {% data variables.product.pat_generic %}

If you want to use the {% data variables.product.company_short %} REST API for personal use, you can create a {% data variables.product.pat_generic %}. If possible, {% data variables.product.company_short %} recommends that you use a {% data variables.product.pat_v2 %} instead of a {% data variables.product.pat_v1 %}. For more information about creating a {% data variables.product.pat_generic %}, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

If you are using a {% data variables.product.pat_v2 %}, your {% data variables.product.pat_v2 %} requires specific permissions in order to access each REST API endpoint. The REST API reference document for each endpoint states whether the endpoint works with {% data variables.product.pat_v2 %}s and states what permissions are required in order for the token to use the endpoint. Some endpoints may require multiple permissions, and some endpoints may require one of multiple permissions. For an overview of which REST API endpoints a {% data variables.product.pat_v2 %} can access with each permission, see [AUTOTITLE](/rest/overview/permissions-required-for-fine-grained-personal-access-tokens).

If you are using a {% data variables.product.pat_v1 %}, it requires specific scopes in order to access each REST API endpoint. For general guidance about what scopes to choose, see [AUTOTITLE](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).

{% data variables.product.pat_generic_caps_plural %} act as your identity (limited by the scopes or permissions you selected) when you make requests to the REST API. As such, it is important to keep your {% data variables.product.pat_generic_plural %} secure. For more information about keeping your {% data variables.product.pat_generic_plural %} secure, see [AUTOTITLE](/rest/authentication/keeping-your-api-credentials-secure?apiVersion=2022-11-28).

### {% data variables.product.pat_generic_caps_plural %} and SAML SSO

{% ifversion fpt or ghec %}If you use a {% data variables.product.pat_v1 %} to access an organization that enforces SAML single sign-on (SSO) for authentication, you will need to authorize your token after creation. {% data variables.product.pat_v2_caps %}s are authorized during token creation, before access to the organization is granted. For more information, see [AUTOTITLE](/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

If you do not authorize your {% data variables.product.pat_v1 %} for SAML SSO before you try to use it to access a single organization that enforces SAML SSO, you may receive a `404 Not Found` or a `403 Forbidden` error. If you receive a `403 Forbidden` error, the `X-GitHub-SSO` header will include a URL that you can follow to authorize your token. The URL expires after one hour.

If you do not authorize your {% data variables.product.pat_v1 %} for SAML SSO before you try to use it to access multiple organizations, the API will not return results from the organizations that require SAML SSO and the `X-GitHub-SSO` header will indicate the ID of the organizations that require SAML SSO authorization of your {% data variables.product.pat_v1 %}. For example: `X-GitHub-SSO: partial-results; organizations=21955855,20582480`.

{% endif %}

## Authenticating with a token generated by an app

If you want to use the API for an organization or on behalf of another user, {% data variables.product.company_short %} recommends that you use a {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app).

The REST API reference documentation for each endpoint states whether the endpoint works with {% data variables.product.prodname_github_apps %} and states what permissions are required in order for the app to use the endpoint. Some endpoints may require multiple permissions, and some endpoints may require one of multiple permissions. For an overview of which REST API endpoints a {% data variables.product.prodname_github_app %} can access with each permission, see [AUTOTITLE](/rest/overview/permissions-required-for-github-apps).

You can also create an OAuth token with an {% data variables.product.prodname_oauth_app %} to access the REST API. However, {% data variables.product.company_short %} recommends that you use a {% data variables.product.prodname_github_app %} instead. {% data variables.product.prodname_github_apps %} allow more control over the access and permission that the app has.

{% ifversion fpt or ghec %}Access tokens created by apps are automatically authorized for SAML SSO.{% endif %}

### Using basic authentication

Some REST API endpoints for {% data variables.product.prodname_github_apps %} and {% data variables.product.prodname_oauth_apps %} require you to use basic authentication to access the endpoint. You will use the app's client ID as the username and the app's client secret as the password.

For example:

```shell
curl --request POST \
--url "{% data variables.product.rest_url %}/applications/YOUR_CLIENT_ID/token" \
--user "YOUR_CLIENT_ID:YOUR_CLIENT_SECRET" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: {{ allVersions[currentVersion].latestApiVersion }}" \
--data '{
  "access_token": "ACCESS_TOKEN_TO_CHECK"
}'
```

The client ID and client secret are associated with the app, not with the owner of the app or a user who authorized the app. They are used to perform operations on behalf of the app, such as creating access tokens.

If you are the owner of a {% data variables.product.prodname_github_app %} or {% data variables.product.prodname_oauth_app %}, or if you are an app manager for a {% data variables.product.prodname_github_app %}, you can find the client ID and generate a client secret on the settings page for your app. To navigate to your app's settings page:

1. In the upper-right corner of any page on {% data variables.product.prodname_dotcom %}, click your profile picture.
1. Navigate to your account settings.
   * For an app owned by a personal account, click **Settings**.
   * For an app owned by an organization:
     1. Click **Your organizations**.
     1. To the right of the organization, click **Settings**.
{% data reusables.user-settings.developer_settings %}
1. In the left sidebar, click **{% data variables.product.prodname_github_apps %}** or **{% data variables.product.prodname_oauth_apps %}**.
1. For {% data variables.product.prodname_github_apps %}, to the right of the {% data variables.product.prodname_github_app %} you want to access, click **Edit**. For {% data variables.product.prodname_oauth_apps %}, click the app that you want to access.
1. Next to **Client ID**, you will see the client ID for your app.
1. Next to **Client secrets**, click **Generate a new client secret** to generate a client secret for your app.

## Authenticating in a {% data variables.product.prodname_actions %} workflow

If you want to use the API in a {% data variables.product.prodname_actions %} workflow, {% data variables.product.company_short %} recommends that you authenticate with the built-in `GITHUB_TOKEN` instead of creating a token. You can grant permissions to the `GITHUB_TOKEN` with the `permissions` key. For more information, see [AUTOTITLE](/actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token).

If this is not possible, you can store your token as a secret and use the name of your secret in your {% data variables.product.prodname_actions %} workflow. For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).

### Authenticating in a {% data variables.product.prodname_actions %} workflow using {% data variables.product.prodname_cli %}

To make an authenticated request to the API in a {% data variables.product.prodname_actions %} workflow using {% data variables.product.prodname_cli %}, you can store the value of `GITHUB_TOKEN` as an environment variable, and use the `run` keyword to execute the {% data variables.product.prodname_cli %} `api` subcommand. For more information about the `run` keyword, see [AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun).

In the following example workflow, replace `PATH` with the path of the endpoint. For more information about the path, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api?tool=cli#path).{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %}

```yaml
jobs:
  use_api:
    runs-on: ubuntu-latest
    permissions: {}
    steps:
      - env:
          GH_TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
        run: |
          gh api /PATH
```

### Authenticating in a {% data variables.product.prodname_actions %} workflow using `curl`

To make an authenticated request to the API in a {% data variables.product.prodname_actions %} workflow using `curl`, you can store the value of `GITHUB_TOKEN` as an environment variable, and use the `run` keyword to execute a `curl` request to the API. For more information about the `run` keyword, see [AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun).

In the following example workflow, replace `PATH` with the path of the endpoint. For more information about the path, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api?tool=cli#path).{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %}

```yaml copy
jobs:
  use_api:
    runs-on: ubuntu-latest
    permissions: {}
    steps:
      - env:
          GH_TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
        run: |
          curl --request GET \
          --url "{% data variables.product.rest_url %}/PATH" \
          --header "Authorization: Bearer $GH_TOKEN"
```

### Authenticating in a {% data variables.product.prodname_actions %} workflow using JavaScript

For an example of how to authenticate in a {% data variables.product.prodname_actions %} workflow using JavaScript, see [AUTOTITLE](/rest/guides/scripting-with-the-rest-api-and-javascript#authenticating-in-github-actions).

## Authenticating with username and password

{% ifversion ghes %}

{% data variables.product.company_short %} recommends that you use a token to authenticate to the REST API instead of your password. You have more control over what a token can do, and you can revoke a token at anytime. However, you can also authenticate to the REST API using your username and password for basic authentication. To do so, you will pass your username and password with the `--user` option:

```shell
curl --request GET \
--url "{% data variables.product.rest_url %}/user" \
--user USERNAME:PASSWORD \
--header "X-GitHub-Api-Version: {{ allVersions[currentVersion].latestApiVersion }}"
```

{% else %}

Authentication with username and password is not supported. If you try to authenticate with user name and password, you will receive a 4xx error.

{% endif %}

## Further reading

* [AUTOTITLE](/rest/overview/keeping-your-api-credentials-secure)
* [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api#authentication)


---

<!-- source: https://docs.github.com/en/rest/authentication/endpoints-available-for-fine-grained-personal-access-tokens -->

---
title: Endpoints available for fine-grained personal access tokens
intro: 'Your {% data variables.product.pat_v2 %} can make requests to the following REST endpoints.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Endpoints for fine-grained PATs
autogenerated: github-apps
redirect_from:
  - /rest/overview/endpoints-available-for-fine-grained-personal-access-tokens
category:
  - Authenticate API requests
---

<!-- The content of this page is rendered as a NextJS page component. -->


---

<!-- source: https://docs.github.com/en/rest/authentication/endpoints-available-for-github-app-installation-access-tokens -->

---
title: Endpoints available for GitHub App installation access tokens
shortTitle: Endpoints for GitHub App installation tokens
intro: Your GitHub App can make requests to the following REST endpoints with an installation access token.
permissions: 'You can use an installation access token to access these endpoints using your {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation).'
redirect_from:
  - /v3/apps/available-endpoints
  - /rest/reference/endpoints-available-for-github-apps
  - /rest/overview/endpoints-available-for-github-apps
  - /rest/overview/endpoints-available-for-github-app-installation-access-tokens
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
autogenerated: github-apps
category:
  - Authenticate API requests
---



<!-- The content of this page is rendered as a NextJS page component. -->


---

<!-- source: https://docs.github.com/en/rest/authentication/endpoints-available-for-github-app-user-access-tokens -->

---
title: Endpoints available for GitHub App user access tokens
shortTitle: Endpoints for GitHub App user tokens
intro: Your GitHub App can make requests to the following REST endpoints with a user access token.
permissions: 'You can use a user access token to access these endpoints using your {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user).'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
autogenerated: github-apps
redirect_from:
  - /rest/overview/endpoints-available-for-github-app-user-access-tokens
category:
  - Authenticate API requests
---



<!-- The content of this page is rendered as a NextJS page component. -->


---

<!-- source: https://docs.github.com/en/rest/authentication -->

---
title: Authenticating to the REST API
shortTitle: Authentication
intro: 'Learn how to authenticate your REST API requests.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /authenticating-to-the-rest-api
  - /keeping-your-api-credentials-secure
  - /endpoints-available-for-github-app-installation-access-tokens
  - /endpoints-available-for-github-app-user-access-tokens
  - /endpoints-available-for-fine-grained-personal-access-tokens
  - /permissions-required-for-github-apps
  - /permissions-required-for-fine-grained-personal-access-tokens
---


---

<!-- source: https://docs.github.com/en/rest/authentication/keeping-your-api-credentials-secure -->

---
title: Keeping your API credentials secure
shortTitle: Keeping API credentials secure
intro: Follow these best practices to keep your API credentials and tokens secure.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/overview/keeping-your-api-credentials-secure
category:
  - Authenticate API requests
---

## Choose an appropriate authentication method

You should choose an authentication method that is appropriate for the task you want to accomplish.

* To use the API for personal use, you can create a {% data variables.product.pat_generic %}.
* To use the API on behalf of an organization or another user, you should create a {% data variables.product.prodname_github_app %}.
* To use the API in a {% data variables.product.prodname_actions %} workflow, you should authenticate with the built-in `GITHUB_TOKEN`.

For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#authenticating-with-the-api).

## Limit the permissions of your credentials

When creating a {% data variables.product.pat_generic %}, only select the minimum permissions or scopes needed, and set an expiration date for the minimum amount of time you'll need to use the token. {% data variables.product.company_short %} recommends that you use {% data variables.product.pat_v2 %}s instead of {% data variables.product.pat_v1_plural %}. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#types-of-personal-access-tokens).

{% data reusables.user-settings.token_access_capabilities %}

When creating a {% data variables.product.prodname_github_app %}, select the minimum permissions that your {% data variables.product.prodname_github_app %} will need. For more information, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/best-practices-for-creating-a-github-app).

When authenticating with `GITHUB_TOKEN` in a {% data variables.product.prodname_actions %} workflow, only give the minimum amount of permissions needed. For more information, see [AUTOTITLE](/actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token).

## Store your authentication credentials securely

Treat authentication credentials the same way you would treat your passwords or other sensitive credentials.

* Don't share authentication credentials using an unencrypted messaging or email system.
* Don't pass your {% data variables.product.pat_generic %} as plain text in the command line. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#keeping-your-personal-access-tokens-secure).
* Don't push unencrypted authentication credentials like tokens or keys to any repository, even if the repository is private. Instead consider using a {% data variables.product.prodname_actions %} secret{% ifversion fpt or ghec %} or Codespaces secret{% endif %}. For more information, see [AUTOTITLE](/actions/security-guides/encrypted-secrets){% ifversion fpt or ghec %} and [AUTOTITLE](/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces){% endif %}.
* You can use secret scanning to discover tokens, private keys, and other secrets that were pushed to a repository, or to block future pushes that contain secrets. For more information, see [AUTOTITLE](/code-security/secret-scanning/introduction/about-secret-scanning).

## Limit who can access your authentication credentials

Don't share your {% data variables.product.pat_generic %} with others. Instead of sharing a {% data variables.product.pat_generic %}, consider creating a {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/about-creating-github-apps).

If you need to share credentials with a team, store the credentials in a secure shared system. For example, you could store and share passwords securely using [1Password](https://1password.com/), or you could store keys in [Azure KeyVault](https://azure.microsoft.com/en-gb/products/key-vault) and manage access with your IAM (Identity and access management).

If you're creating a {% data variables.product.prodname_actions %} workflow that needs to access the API, you can store your credentials in an encrypted secret, and access the encrypted secret from the workflow. For more information, see [AUTOTITLE](/actions/security-guides/encrypted-secrets) and [AUTOTITLE](/apps/creating-github-apps/guides/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow).

## Use authentication credentials securely in your code

Never hardcode authentication credentials like tokens, keys, or app-related secrets into your code. Instead, consider using a secret manager such as [Azure Key Vault](https://azure.microsoft.com/products/key-vault) or [HashiCorp Vault](https://www.hashicorp.com/products/vault). For more information about securing {% data variables.product.prodname_github_app %} credentials, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/best-practices-for-creating-a-github-app).

{% ifversion fpt or ghec %}

If you find another user's {% data variables.product.pat_generic %} exposed on {% data variables.product.github %} or elsewhere, you can submit a revocation request through the REST API. See [AUTOTITLE](/rest/credentials/revoke#revoke-a-list-of-credentials).

{% ifversion ghec %}
> [!NOTE]
> The credential revocation REST API is not currently available for enterprises that use {% data variables.enterprise.data_residency %}.

{% endif %}
{% endif %}

When using a {% data variables.product.pat_generic %} in a script, consider storing your token as a {% data variables.product.prodname_actions %} secret and running your script through {% data variables.product.prodname_actions %}.{% ifversion fpt or ghec %} You can also store your token as a Codespaces secret and run your script in Codespaces.{% endif %} For more information, see [AUTOTITLE](/actions/security-guides/encrypted-secrets){% ifversion fpt or ghec %} and [AUTOTITLE](/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces){% endif %}.

If none of these options are possible, you can store authentication credentials in a `.env` file. Make sure to encrypt your `.env` file, and never push it to any repository.

## Prepare a remediation plan

You should create a plan to handle any security breaches in a timely manner. In the event that your token or other authentication credential is leaked, you will need to:

* Generate a new credential.
* Replace the old credential with the new one everywhere that you are storing or accessing the credential.
* Delete the old compromised credential.

For information about rotating compromised credentials for a {% data variables.product.prodname_github_app %}, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/best-practices-for-creating-a-github-app).

For information about creating and deleting {% data variables.product.pat_generic %}s, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).


---

<!-- source: https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens -->

---
title: Permissions required for fine-grained personal access tokens
intro: 'For each permission granted to a {% data variables.product.pat_v2 %}, these are the REST API endpoints that the app can use.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Permissions for fine-grained PATs
autogenerated: github-apps
redirect_from:
  - /rest/overview/permissions-required-for-fine-grained-personal-access-tokens
category:
  - Authenticate API requests
---

## About permissions required for {% data variables.product.pat_v2 %}

When you create a {% data variables.product.pat_v2 %}, you grant it a set of permissions. Permissions define what resources the {% data variables.product.prodname_github_app %} can access via the API. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

{% data reusables.rest-api.permission-header %}

{% data reusables.rest-api.public-access %}

{% data reusables.rest-api.additional-permissions %}

<!-- The content of this page is rendered as a NextJS page component. -->


---

<!-- source: https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps -->

---
title: Permissions required for GitHub Apps
intro: 'For each permission granted to a {% data variables.product.prodname_github_app %}, these are the REST API endpoints that the app can use.'
redirect_from:
  - /v3/apps/permissions
  - /rest/reference/permissions-required-for-github-apps
  - /rest/overview/permissions-required-for-github-apps
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Permissions for GitHub Apps
autogenerated: github-apps
category:
  - Authenticate API requests
---

## About {% data variables.product.prodname_github_app %} permissions

{% data variables.product.prodname_github_apps %} are created with a set of permissions. Permissions define what resources the {% data variables.product.prodname_github_app %} can access via the API. For more information, see [AUTOTITLE](/apps/creating-github-apps/creating-github-apps/setting-permissions-for-github-apps).

{% data reusables.rest-api.permission-header %}

{% data reusables.rest-api.public-access %}

{% data reusables.rest-api.additional-permissions %}

<!-- The content of this page is rendered as a NextJS page component. -->


---

<!-- source: https://docs.github.com/en/rest/billing/billing -->

---
title: REST API endpoints for billing
shortTitle: Billing
allowTitleToDifferFromFilename: true
intro: Use the REST API to get billing information.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/billing
  - /rest/enterprise-admin/billing
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About billing

You can get billing information for an enterprise. For more information, see [AUTOTITLE](/rest/enterprise-admin/billing).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/billing/budgets -->

---
title: Budgets
intro: Use the REST API to get budget information.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
redirect_from:
  - /rest/billing/enhanced-billing
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/billing/cost-centers -->

---
title: Cost centers
intro: Use the REST API to get cost center information.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---
## Required roles

The following roles can access cost center API endpoints:

* **Enterprise owners**
* **Billing managers**
* **Organization owners**

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/billing -->

---
title: REST API endpoints for billing
shortTitle: Billing
allowTitleToDifferFromFilename: true
intro: Use the REST API to get billing information.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /billing
  - /budgets
  - /cost-centers
  - /usage
  - /usage-reports
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/billing/usage-reports -->

---
title: Usage reports
shortTitle: Usage reports
intro: Use the REST API to create and retrieve usage report exports for an enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/billing/usage -->

---
title: Billing usage
intro: Use the REST API to get billing usage information.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

The endpoints on this page return usage that is billed to the account associated with the endpoint. For help deciding which level of usage to report on, see [AUTOTITLE](/billing/tutorials/automate-usage-reporting#step-1-decide-what-level-to-report-on).

* User endpoints return {% data variables.product.prodname_copilot_short %} usage that is billed directly to an individual user’s personal account. These endpoints are only applicable if the user has purchased their own {% data variables.product.prodname_copilot_short %} plan.
* If a user’s {% data variables.product.prodname_copilot_short %} license is managed and billed through an organization or enterprise, their usage is not included in user-level endpoints. In that case, you must use the organization- or enterprise-level endpoints instead.

{% ifversion fpt %}To view enterprise-level endpoints, select the dropdown menu at the top of the page and switch from Free, Pro, & Team to {% data variables.product.prodname_ghe_cloud %}.

{% else %}To view user- and organization-level endpoints, select the dropdown menu at the top of the page and switch from {% data variables.product.prodname_ghe_cloud %} to Free, Pro, & Team.{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/branches/branch-protection -->

---
title: REST API endpoints for protected branches
shortTitle: Protected branches
intro: Use the REST API to manage protected branches.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/branches/branches -->

---
title: REST API endpoints for branches
shortTitle: Branches
allowTitleToDifferFromFilename: true
intro: Use the REST API to modify branches and their protection settings.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/branches -->

---
title: REST API endpoints for branches and their settings
shortTitle: Branches
intro: Use the REST API to modify branches and their protection settings.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /branches
  - /branch-protection
redirect_from:
  - /rest/reference/branches
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/campaigns/campaigns -->

---
title: REST API endpoints for security campaigns
shortTitle: Security campaigns
intro: Use the REST API to create and manage security campaigns for your organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

> [!NOTE]
> These endpoints only interact with published campaigns. Draft campaigns cannot currently be viewed or managed through the API.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/campaigns -->

---
title: REST API endpoints for security campaigns
shortTitle: Campaigns
intro: Use the REST API to create and manage security campaigns for your organization.
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /campaigns
versions:
  fpt: '*'
  ghec: '*'
---



---

<!-- source: https://docs.github.com/en/rest/checks -->

---
title: REST API endpoints for checks
shortTitle: Checks
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to build {% data variables.product.prodname_github_apps %} that run powerful checks against the code changes in a repository.'
redirect_from:
  - /v3/checks
  - /rest/reference/checks
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /runs
  - /suites
autogenerated: rest
---

You can create apps that perform continuous integration, code linting, or code scanning services and provide detailed feedback on commits. For more information, see [AUTOTITLE](/rest/guides/using-the-rest-api-to-interact-with-checks) and [AUTOTITLE](/apps/creating-github-apps/writing-code-for-a-github-app/building-ci-checks-with-a-github-app).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/checks/runs -->

---
title: REST API endpoints for check runs
shortTitle: Check runs
intro: Use the REST API to manage check runs.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Automate CI/CD workflows
---

> [!NOTE]
> {% data reusables.apps.checks-availability %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/checks/suites -->

---
title: REST API endpoints for check suites
shortTitle: Check suites
intro: Use the REST API to manage check suites.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Automate CI/CD workflows
---

> [!NOTE]
> {% data reusables.apps.checks-availability %}

> [!NOTE]
> A GitHub App usually only receives one [`check_suite`](/webhooks-and-events/webhooks/webhook-events-and-payloads#check_suite) event per commit SHA, even if you push the commit SHA to more than one branch. To find out when a commit SHA is pushed to a branch, you can subscribe to branch [`create`](/webhooks-and-events/webhooks/webhook-events-and-payloads#create) events.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/classroom/classroom -->

---
title: REST API endpoints for {% data variables.product.prodname_classroom %}
shortTitle: Classroom
intro: 'Use the REST API to interact with {% data variables.product.prodname_classroom %}.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/classroom -->

---
title: REST API endpoints for {% data variables.product.prodname_classroom %}
shortTitle: Classroom
intro: 'Use the REST API to interact with {% data variables.product.prodname_classroom %}.'
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /classroom
versions:
  fpt: '*'
  ghec: '*'
---


---

<!-- source: https://docs.github.com/en/rest/code-quality/code-quality -->

---
title: REST API endpoints for code quality
shortTitle: Code quality
intro: Use the REST API to manage a code quality configuration.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/code-quality -->

---
title: code-quality
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /code-quality
versions:
  fpt: '*'
---



---

<!-- source: https://docs.github.com/en/rest/code-scanning/alert-dismissal-requests -->

---
title: >-
  REST API endpoints for {% data variables.product.prodname_code_scanning %}
  alert dismissal requests
shortTitle: Alert dismissal requests
intro: >-
  Use the REST API to interact with {% data
  variables.product.prodname_code_scanning %} alert dismissal requests from a
  repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/code-scanning/code-scanning -->

---
title: REST API endpoints for code scanning
shortTitle: Code scanning
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to retrieve and update {% data
  variables.product.prodname_code_scanning %} alerts from a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/code-scanning
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

## About code scanning

You can retrieve and update {% data variables.product.prodname_code_scanning %} alerts from a repository. You can use the endpoints to create automated reports for the {% data variables.product.prodname_code_scanning %} alerts in an organization or upload analysis results generated using offline {% data variables.product.prodname_code_scanning %} tools. For more information, see [AUTOTITLE](/code-security/code-scanning).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/code-scanning -->

---
title: REST API endpoints for code scanning
shortTitle: Code scanning
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to retrieve and update {% data
  variables.product.prodname_code_scanning %} alerts from a repository.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /alert-dismissal-requests
  - /code-scanning
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/code-security/configurations -->

---
title: Configurations
intro: >-
  Use the REST API to create and manage security configurations for your
  organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/code-security -->

---
title: REST API endpoints for code security settings
shortTitle: Code security settings
intro: Use the REST API to create and manage code security configurations for your organization.
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /configurations
versions:
  fpt: '*'
  ghec: '*'
  ghes: '>=3.15'
---


---

<!-- source: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct -->

---
title: REST API endpoints for codes of conduct
shortTitle: Codes of conduct
allowTitleToDifferFromFilename: true
intro: Use the REST API to get information about codes of conduct.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/codes-of-conduct
autogenerated: rest
category:
  - Manage organizations and teams
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codes-of-conduct -->

---
title: REST API endpoints for codes of conduct
shortTitle: Codes of conduct
allowTitleToDifferFromFilename: true
intro: Use the REST API to get information about codes of conduct.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /codes-of-conduct
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces/codespaces -->

---
title: REST API endpoints for Codespaces
shortTitle: Codespaces
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to manage {% data
  variables.product.prodname_github_codespaces %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Use Codespaces
---

## About {% data variables.product.prodname_github_codespaces %}

You can manage {% data variables.product.prodname_codespaces %} using the REST API. These endpoints are available for authenticated users, {% data variables.product.prodname_oauth_apps %}, and {% data variables.product.prodname_github_apps %}. For more information, see [AUTOTITLE](/codespaces).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces -->

---
title: REST API endpoints for Codespaces
shortTitle: Codespaces
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to manage {% data variables.product.prodname_github_codespaces %}.'
versions:
  fpt: '*'
  ghec: '*'
children:
  - /codespaces
  - /organizations
  - /organization-secrets
  - /machines
  - /repository-secrets
  - /secrets
redirect_from:
  - /rest/reference/codespaces
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces/machines -->

---
title: REST API endpoints for Codespaces machines
allowTitleToDifferFromFilename: true
shortTitle: Machines
intro: Use the REST API to manage availability of machine types for a codespace.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Use Codespaces
---

## About {% data variables.product.prodname_codespaces %} machines

You can determine which machine types are available to create a codespace, either on a given repository or as an authenticated user. For more information, see [AUTOTITLE](/codespaces/customizing-your-codespace/changing-the-machine-type-for-your-codespace#about-machine-types).

You can also use this information when changing the machine of an existing codespace by updating its `machine` property. The machine update will take place the next time the codespace is restarted. For more information, see [AUTOTITLE](/codespaces/customizing-your-codespace/changing-the-machine-type-for-your-codespace).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces/organization-secrets -->

---
title: REST API endpoints for Codespaces organization secrets
allowTitleToDifferFromFilename: true
shortTitle: Organization secrets
intro: >-
  Use the REST API to manage your organization-level {% data
  variables.product.prodname_codespaces %} secrets.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Use Codespaces
---

> [!NOTE]
> These endpoints are currently in {% data variables.release-phases.public_preview %} and subject to change.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces/organizations -->

---
title: REST API endpoints for Codespaces organizations
allowTitleToDifferFromFilename: true
shortTitle: Organizations
intro: Use the REST API to manage your organization members codespaces.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Use Codespaces
---

## About {% data variables.product.prodname_codespaces %} organizations

You can manage {% data variables.product.prodname_codespaces %} that are billed to your
organization. For more information,
see [AUTOTITLE](/codespaces).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces/repository-secrets -->

---
title: REST API endpoints for Codespaces repository secrets
allowTitleToDifferFromFilename: true
shortTitle: Repository secrets
intro: >-
  Use the REST API to manage secrets for repositories that the user has access
  to in a codespace.
permissions: >-
  Users with write access to a repository can manage {% data
  variables.product.prodname_codespaces %} repository secrets.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Use Codespaces
---

## About {% data variables.product.prodname_codespaces %} repository secrets

You can create, list, and delete secrets (such as access tokens for cloud services) for repositories that the user has access to. These secrets are made available to the codespace at runtime. For more information, see [AUTOTITLE](/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/codespaces/secrets -->

---
title: REST API endpoints for Codespaces user secrets
allowTitleToDifferFromFilename: true
shortTitle: User secrets
intro: Use the REST API manage secrets that the user has access to in a codespace.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Use Codespaces
---

## About {% data variables.product.prodname_codespaces %} user secrets

You can create, list, and delete secrets (such as access tokens for cloud services) as well as assign secrets to repositories that the user has access to. These secrets are made available to the codespace at runtime. For more information, see [AUTOTITLE](/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/collaborators/collaborators -->

---
title: REST API endpoints for collaborators
shortTitle: Collaborators
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage collaborators for a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/collaborators -->

---
title: REST API endpoints for collaborators
shortTitle: Collaborators
intro: 'Use the REST API to add, invite, and remove collaborators from a repository.'
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /collaborators
  - /invitations
redirect_from:
  - /rest/reference/collaborators
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/collaborators/invitations -->

---
title: REST API endpoints for repository invitations
allowTitleToDifferFromFilename: true
shortTitle: Invitations
intro: >-
  Use the REST API to view and manage invitations to collaborate on a
  repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About repository invitations

You can view and manage invitations to collaborate on a repository. The invited users (or external services on behalf of invited users) can choose to accept or decline the invitations.

To add a user as a collaborator, use the Collaborators endpoints instead. For more information, see [AUTOTITLE](/rest/collaborators/collaborators#add-a-repository-collaborator).

Note that the `repo:invite` [OAuth scope](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) grants targeted
access to invitations **without** also granting access to repository code, while the
`repo` scope grants permission to code as well as invitations.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/commits/comments -->

---
title: REST API endpoints for commit comments
shortTitle: Commit comments
intro: Use the REST API to interact with commit comments.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---

## About commit comments

You can create, edit, and view commit comments using the REST API. A commit comment is a comment made on a specific commit. For more information, see [AUTOTITLE](/rest/guides/working-with-comments#commit-comments).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/commits/commits -->

---
title: REST API endpoints for commits
shortTitle: Commits
allowTitleToDifferFromFilename: true
intro: Use the REST API to interact with commits.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/commits -->

---
title: REST API endpoints for commits
shortTitle: Commits
intro: Use the REST API to interact with commits.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /commits
  - /comments
  - /statuses
redirect_from:
  - /rest/reference/commits
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/commits/statuses -->

---
title: REST API endpoints for commit statuses
shortTitle: Commit statuses
intro: Use the REST API to interact with commit statuses.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---

## About commit statuses

You can use the REST API to allow external services to mark commits with an `error`, `failure`, `pending`, or `success` state, which is then reflected in pull requests involving those commits. Statuses can also include an optional `description` and `target_url`, and we highly recommend providing them as they make statuses much more useful in the GitHub UI.

As an example, one common use is for continuous integration services to mark commits as passing or failing builds using status. The `target_url` would be the full URL to the build output, and the `description` would be the high level summary of what happened with the build.

Statuses can include a `context` to indicate what service is providing that status. For example, you may have your continuous integration service push statuses with a context of `ci`, and a security audit tool push statuses with a context of `security`. You can then use the REST API to [Get the combined status for a specific reference](/rest/commits/statuses#get-the-combined-status-for-a-specific-reference) to retrieve the whole status for a commit.

Note that the `repo:status` [OAuth scope](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) grants targeted access to statuses **without** also granting access to repository code, while the `repo` scope grants permission to code as well as statuses.

If you are developing a {% data variables.product.prodname_github_app %}  and want to provide more detailed information about an external service, you may want to use the REST API to manage checks. For more information, see [AUTOTITLE](/rest/checks).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-cloud-agent-management -->

---
title: REST API endpoints for Copilot cloud agent repository management
shortTitle: Cloud agent repository management
intro: 'Use the REST API to manage repository-level settings for {% data variables.copilot.copilot_cloud_agent %}.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-coding-agent-management -->

---
title: REST API endpoints for Copilot cloud agent management
shortTitle: Copilot cloud agent management
intro: >-
  Use the REST API to manage settings for {% data
  variables.copilot.copilot_cloud_agent %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-content-exclusion-management -->

---
title: REST API endpoints for Copilot content exclusion management
shortTitle: Copilot content exclusion management
intro: 'Use the REST API to manage {% data variables.product.prodname_copilot_short %} content exclusion rules.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-custom-agents -->

---
title: REST API endpoints for Copilot custom agents
shortTitle: Copilot custom agents
intro: 'Use the REST API to manage {% data variables.copilot.copilot_custom_agents %} for your enterprise.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-metrics -->

---
title: REST API endpoints for Copilot metrics
shortTitle: Copilot metrics
intro: Use the REST API to view {% data variables.product.prodname_copilot_short %} metrics.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/copilot/copilot-usage
category:
  - Use Copilot and AI services
---

{% data reusables.copilot.copilot-metrics-closing-down %}

You can use these endpoints to get a breakdown of aggregated metrics for various {% data variables.product.prodname_copilot %} features. The API includes:

* Data for the last 100 days
* Numbers of active users and engaged users
* Breakdowns by language and IDE
* The option to view metrics for an enterprise, organization, or team

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-usage-metrics -->

---
title: REST API endpoints for Copilot usage metrics
shortTitle: Copilot usage metrics
intro: >-
  Use the REST API to view {% data variables.product.prodname_copilot_short %}
  usage metrics.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

To enable these endpoints, the "{% data variables.product.prodname_copilot_short %} usage metrics" policy must be set to **Enabled everywhere** for the enterprise. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies#defining-policies-for-your-enterprise).

For more information on the metrics returned by these endpoints, see [AUTOTITLE](/copilot/reference/copilot-usage-metrics).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot/copilot-user-management -->

---
title: REST API endpoints for Copilot user management
shortTitle: Copilot user management
intro: 'Use the REST API to manage the {% data variables.copilot.copilot_for_business %}{% ifversion ghec %} or {% data variables.copilot.copilot_enterprise %}{% endif %} subscription for your organization.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/copilot/copilot-for-business
  - /rest/copilot/copilot-business
category:
  - Use Copilot and AI services
---

> [!NOTE] These endpoints are in {% data variables.release-phases.public_preview %} and subject to change.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot -->

---
title: REST API endpoints for Copilot
shortTitle: Copilot
intro: >-
  Use the REST API to monitor and manage {% data
  variables.product.prodname_copilot %}.
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /copilot-cloud-agent-management
  - /copilot-coding-agent-management
  - /copilot-content-exclusion-management
  - /copilot-custom-agents
  - /copilot-metrics
  - /copilot-usage-metrics
  - /copilot-user-management
versions:
  fpt: '*'
  ghec: '*'
---



---

<!-- source: https://docs.github.com/en/rest/copilot-spaces/collaborators -->

---
title: Copilot Spaces collaborators
shortTitle: Collaborators
intro: Use the REST API to manage collaborators for Copilot Spaces.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot-spaces/copilot-spaces -->

---
title: REST API endpoints for Copilot Spaces
shortTitle: Copilot Spaces
intro: Use the REST API to manage Copilot Spaces and related resources.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/copilot-spaces -->

---
title: REST API endpoints for Copilot Spaces
shortTitle: Copilot Spaces
intro: >-
  Use the REST API to manage Copilot Spaces and related resources.
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /collaborators
  - /copilot-spaces
  - /resources
versions:
  fpt: '*'
  ghec: '*'
---



---

<!-- source: https://docs.github.com/en/rest/copilot-spaces/resources -->

---
title: REST API endpoints for Copilot Spaces resources
shortTitle: Resources
intro: Use the REST API to interact with Copilot Spaces resources.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/credentials -->

---
title: Credentials
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /revoke
versions:
  fpt: '*'
  ghec: '*'
  ghes: '>=3.18'
---



---

<!-- source: https://docs.github.com/en/rest/credentials/revoke -->

---
title: Revocation
shortTitle: Revocation
intro: >-
  Use the REST API to revoke credentials that you have found exposed on {% data
  variables.product.github %} or elsewhere.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.18'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Authenticate API requests
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependabot/alert-dismissal-requests -->

---
title: REST API endpoints for {% data variables.product.prodname_dependabot %} alert dismissal requests
shortTitle: Alert dismissal requests
intro: 'Use the REST API to manage {% data variables.product.prodname_dependabot %} alert dismissal requests for a repository.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependabot/alerts -->

---
title: 'REST API endpoints for {% data variables.product.prodname_dependabot_alerts %}'
allowTitleToDifferFromFilename: true
shortTitle: Alerts
intro: 'Use the REST API to interact with {% data variables.product.prodname_dependabot %} alerts for a repository.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

> [!NOTE]
> The ability to use the REST API to manage Dependabot alerts is currently in {% data variables.release-phases.public_preview %} and subject to change.

## About {% data variables.product.prodname_dependabot_alerts %}

You can view {% data variables.product.prodname_dependabot %} alerts for a repository and update individual alerts with the REST API. For more information, see [AUTOTITLE](/code-security/dependabot/dependabot-alerts/about-dependabot-alerts).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependabot -->

---
title: REST API endpoints for {% data variables.product.prodname_dependabot %}
shortTitle: Dependabot
intro: >-
  Use the REST API to interact with {% data
  variables.product.prodname_dependabot_alerts %} and secrets for an
  organization or repository.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /alert-dismissal-requests
  - /alerts
  - /repository-access
  - /secrets
redirect_from:
  - /rest/reference/dependabot
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependabot/repository-access -->

---
title: >-
  REST API endpoints for {% data variables.product.prodname_dependabot %}
  repository access
shortTitle: Repository access
intro: >-
  Use the REST API to manage which repositories {% data
  variables.product.prodname_dependabot %} can access within an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.18'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

## About {% data variables.product.prodname_dependabot %} repository access

You can list repositories that {% data variables.product.prodname_dependabot %} already has access to and set a default repository access level for {% data variables.product.prodname_dependabot %}.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependabot/secrets -->

---
title: REST API endpoints for Dependabot secrets
shortTitle: Secrets
intro: >-
  Use the REST API to manage {% data variables.product.prodname_dependabot %}
  secrets for an organization or repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

## About {% data variables.product.prodname_dependabot %} secrets

You can create, update, delete, and retrieve information about encrypted secrets using the REST API. {% data reusables.actions.about-secrets %} For more information, see [AUTOTITLE](/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot#storing-credentials-for-dependabot-to-use).

{% data reusables.actions.actions-authentication %} {% data variables.product.prodname_github_apps %} must have the `dependabot_secrets` permission to use these endpoints. Authenticated users must have collaborator access to a repository to create, update, or read secrets.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependency-graph/dependency-review -->

---
title: REST API endpoints for dependency review
shortTitle: Dependency review
intro: Use the REST API to interact with dependency changes.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

## About dependency review

You can use the REST API to view dependency changes, and the security impact of these changes, before you add them to your environment. You can view the diff of dependencies between two commits of a repository, including vulnerability data for any version updates with known vulnerabilities. For more information about dependency review, see [AUTOTITLE](/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependency-graph/dependency-submission -->

---
title: REST API endpoints for dependency submission
shortTitle: Dependency submission
allowTitleToDifferFromFilename: true
intro: Use the REST API to submit dependencies.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

## About dependency submissions

You can use the REST API to submit dependencies for a project. This enables you to add dependencies, such as those resolved when software is compiled or built, to {% data variables.product.prodname_dotcom %}'s dependency graph feature, providing a more complete picture of all of your project's dependencies.

The dependency graph shows any dependencies you submit using the API in addition to any dependencies that are identified from manifest or lock files in the repository (for example, a `package-lock.json` file in a JavaScript project). For more information about viewing the dependency graph, see [AUTOTITLE](/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository#viewing-the-dependency-graph).

Submitted dependencies will receive {% data variables.product.prodname_dependabot_alerts %} and {% data variables.product.prodname_dependabot_security_updates %} for any known vulnerabilities. You will only get {% data variables.product.prodname_dependabot_alerts %} for dependencies that are from one of the supported ecosystems for the {% data variables.product.prodname_advisory_database %}. For more information about these ecosystems, see [AUTOTITLE](/code-security/security-advisories/global-security-advisories/about-the-github-advisory-database#github-reviewed-advisories). For transitive dependencies submitted via the {% data variables.dependency-submission-api.name %}, {% data variables.product.prodname_dependabot %} will automatically open pull requests to update the parent dependency, if an update is available.

{% data reusables.dependency-submission.about-dependency-submission %}

You can submit dependencies in the form of a snapshot. A snapshot is a set of dependencies associated with a commit SHA and other metadata, that reflects the current state of your repository for a commit. You can choose to use pre-made actions or create your own actions to submit your dependencies in the required format each time your project is built. For more information, see [AUTOTITLE](/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api).

You can submit multiple sets of dependencies to be included in your dependency graph. The REST API uses the `job.correlator` property and the `detector.name` category of the snapshot to ensure the latest submissions for each workflow get shown. The `correlator` property itself is the primary field you will use to keep independent submissions distinct. An example `correlator` could be a simple combination of two variables available in actions runs: `<GITHUB_WORKFLOW> <GITHUB_JOB>`.

{% data reusables.dependency-graph.deduplication %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependency-graph -->

---
title: REST API endpoints for the dependency graph
shortTitle: Dependency graph
allowTitleToDifferFromFilename: true
intro: Use the REST API to view dependency changes and their security impact on your repository.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /dependency-review
  - /dependency-submission
  - /sboms
redirect_from:
  - /rest/reference/dependency-graph
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/dependency-graph/sboms -->

---
title: REST API endpoints for software bill of materials (SBOM)
shortTitle: Software bill of materials (SBOM)
intro: Use the REST API to export the software bill of materials (SBOM) for a repository.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---
{% data reusables.dependency-graph.sbom-export %}

This article gives details about the REST API endpoint.

{% ifversion ghes %}
> [!NOTE]
> {% data variables.product.prodname_ghe_server %} does not retrieve license information for dependencies, and does not calculate information about dependents, the repositories and packages that depend on a repository. These fields will not be populated in the response.
{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deploy-keys/deploy-keys -->

---
title: REST API endpoints for deploy keys
shortTitle: Deploy keys
intro: Use the REST API to create and manage deploy keys.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/reference/deploy_keys
autogenerated: rest
category:
  - Manage repositories and code
---

## About deploy keys

{% data reusables.repositories.deploy-keys %}

Deploy keys can either be set up using the following API endpoints, or by using the {% data variables.product.company_short %} web interface. To learn how to set deploy keys up in the web interface, see [AUTOTITLE](/authentication/connecting-to-github-with-ssh/managing-deploy-keys).

{% ifversion deploy-keys-enterprise-org-policy %}

You may be unable to create deploy keys if your organization or enterprise owner has set a policy to restrict their use. Furthermore, if this policy is enabled at the organization or enterprise level, existing deploy keys may be disabled. For more information, see [AUTOTITLE](/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-deploy-keys) and [AUTOTITLE](/organizations/managing-organization-settings/restricting-deploy-keys-in-your-organization).
{% endif %}

There are a few cases when a deploy key will be deleted by other activity:

* If the deploy key is created with a {% data variables.product.pat_generic %}, deleting the {% data variables.product.pat_generic %} will also delete the deploy key. Regenerating the {% data variables.product.pat_generic %} will not delete the deploy key.
* If the deploy key is created with an {% data variables.product.prodname_oauth_app %} token, revoking the token will also delete the deploy key.

Conversely, these activities will not delete a deploy key:

* If the deploy key is created with a {% data variables.product.prodname_github_app %} user access token, revoking the token will not delete the deploy key.
* If the deploy key is created with a {% data variables.product.prodname_github_app %} installation access token, uninstalling or deleting the app will not delete the deploy key.
* If the deploy key is created with a {% data variables.product.pat_generic %}, regenerating the {% data variables.product.pat_generic %} will not delete the deploy key.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deploy-keys -->

---
title: REST API endpoints for deploy keys
shortTitle: Deploy keys
intro: Use the REST API to create and manage deploy keys.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
children:
  - /deploy-keys
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deployments/branch-policies -->

---
title: REST API endpoints for deployment branch policies
allowTitleToDifferFromFilename: true
shortTitle: Deployment branch policies
intro: Use the REST API to manage custom deployment branch policies.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About deployment branch policies

You can use the REST API to specify custom name patterns that branches must match in order to deploy to an environment. The `deployment_branch_policy.custom_branch_policies` property for the environment must be set to `true` to use these endpoints. To update the `deployment_branch_policy` for an environment, see [AUTOTITLE](/rest/deployments/environments#create-or-update-an-environment).

For more information about restricting environment deployments to certain branches, see [AUTOTITLE](/actions/deployment/targeting-different-environments/using-environments-for-deployment#deployment-branches).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deployments/deployments -->

---
title: REST API endpoints for deployments
shortTitle: Deployments
allowTitleToDifferFromFilename: true
intro: Use the REST API to create and delete deployments and deployment environments.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About deployments

Deployments are requests to deploy a specific ref (branch, SHA, tag). GitHub dispatches a [`deployment` event](/webhooks-and-events/webhooks/webhook-events-and-payloads#deployment) that external services can listen for and act on when new deployments are created. Deployments enable developers and organizations to build loosely coupled tooling around deployments, without having to worry about the implementation details of delivering different types of applications (e.g., web, native).

Deployment statuses allow external services to mark deployments with an `error`, `failure`, `pending`, `in_progress`, `queued`, or `success` state that systems listening to [`deployment_status` events](/webhooks-and-events/webhooks/webhook-events-and-payloads#deployment_status) can consume.

Deployment statuses can also include an optional `description` and `log_url`, which are highly recommended because they make deployment statuses more useful. The `log_url` is the full URL to the deployment output, and
the `description` is a high-level summary of what happened with the deployment.

GitHub dispatches `deployment` and `deployment_status` events when new deployments and deployment statuses are created. These events allow third-party integrations to receive and respond to deployment requests, and update the status of a deployment as progress is made.

Below is a simple sequence diagram for how these interactions would work.

```text
+---------+             +--------+            +-----------+        +-------------+
| Tooling |             | GitHub |            | 3rd Party |        | Your Server |
+---------+             +--------+            +-----------+        +-------------+
     |                      |                       |                     |
     |  Create Deployment   |                       |                     |
     |--------------------->|                       |                     |
     |                      |                       |                     |
     |  Deployment Created  |                       |                     |
     |<---------------------|                       |                     |
     |                      |                       |                     |
     |                      |   Deployment Event    |                     |
     |                      |---------------------->|                     |
     |                      |                       |     SSH+Deploys     |
     |                      |                       |-------------------->|
     |                      |                       |                     |
     |                      |   Deployment Status   |                     |
     |                      |<----------------------|                     |
     |                      |                       |                     |
     |                      |                       |   Deploy Completed  |
     |                      |                       |<--------------------|
     |                      |                       |                     |
     |                      |   Deployment Status   |                     |
     |                      |<----------------------|                     |
     |                      |                       |                     |
```

Keep in mind that GitHub is never actually accessing your servers. It's up to your third-party integration to interact with deployment events. Multiple systems can listen for deployment events, and it's up to each of those systems to decide whether they're responsible for pushing the code out to your servers, building native code, etc.

Note that the `repo_deployment` [OAuth scope](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) grants targeted access to deployments and deployment statuses **without** granting access to repository code, while the `public_repo` and `repo` scopes grant permission to code as well.

### Inactive deployments

When you set the state of a deployment to `success`, then all prior non-transient, non-production environment deployments in the same repository with the same environment name will become `inactive`. To avoid this, you can set `auto_inactive` to `false` when creating the deployment status.

You can communicate that a transient environment no longer exists by setting its `state` to `inactive`. Setting the `state` to `inactive` shows the deployment as `destroyed` in {% data variables.product.prodname_dotcom %} and removes access to it.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deployments/environments -->

---
title: REST API endpoints for deployment environments
allowTitleToDifferFromFilename: true
shortTitle: Environments
intro: 'Use the REST API to create, configure, and delete deployment environments.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Automate CI/CD workflows
---

## About deployment environments

For more information about environments, see [AUTOTITLE](/actions/deployment/targeting-different-environments/using-environments-for-deployment). To manage environment secrets, see [AUTOTITLE](/rest/actions/secrets).

{% data reusables.gated-features.environments %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deployments -->

---
title: REST API endpoints for deployments
shortTitle: Deployments
intro: >-
  Use the REST API to create and delete deploy keys, deployments, and deployment
  environments.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /branch-policies
  - /deployments
  - /environments
  - /protection-rules
  - /statuses
redirect_from:
  - /rest/reference/deployments
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deployments/protection-rules -->

---
title: REST API endpoints for protection rules
shortTitle: Protection rules
intro: 'Use the REST API to create, configure, and delete deployment protection rules.'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Automate CI/CD workflows
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/deployments/statuses -->

---
title: REST API endpoints for deployment statuses
shortTitle: Deployment statuses
intro: Use the REST API to manage deployment statuses.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Automate CI/CD workflows
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/emojis/emojis -->

---
title: REST API endpoints for emojis
shortTitle: Emojis
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to list and view all the available emojis to use on {% data
  variables.product.github %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/emojis
autogenerated: rest
category:
  - Learn about the REST API
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/emojis -->

---
title: REST API endpoints for emojis
shortTitle: Emojis
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to list and view all the available emojis to use on {% data variables.product.github %}.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /emojis
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/admin-stats -->

---
title: REST API endpoints for admin stats
shortTitle: Admin stats
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve a variety of metrics about your installation.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

{% ifversion ghes %}## About admin stats

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators. Normal users will receive a `404` response.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}{% elsif ghec %}{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/announcement -->

---
title: REST API endpoints for global announcements
shortTitle: Announcement
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage the global announcement banner in your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About announcements

You can use the REST API to manage the global announcement banner in your enterprise. For more information, see [AUTOTITLE](/admin/user-management/managing-users-in-your-enterprise/customizing-user-messages-for-your-enterprise#creating-a-global-announcement-banner).

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/audit-log -->

---
title: REST API endpoints for enterprise audit logs
shortTitle: Audit log
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve audit logs for an enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/bypass-requests -->

---
title: REST API endpoints for bypass requests
shortTitle: Bypass requests
intro: Use the REST API to manage enterprise push rule bypass requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/code-security-and-analysis -->

---
title: REST API endpoints for enterprise security features for code
shortTitle: Security features for code
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage use of security features for your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/credential-authorizations -->

---
title: REST API endpoints for enterprise credential authorizations
shortTitle: Credential authorizations
intro:  Use the REST API to manage enterprise credential authorizations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/custom-properties-for-orgs -->

---
title: REST API for organization custom properties in an enterprise
shortTitle: Custom properties for organizations
intro: >-
  Use the REST API to manage custom properties for organizations belonging to an
  enterprise
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.21'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/custom-properties -->

---
title: Custom properties
shortTitle: Custom properties
intro: Use the REST API to manage custom properties for your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.18'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/enterprise-roles -->

---
title: REST API endpoints for enterprise roles
shortTitle: Enterprise roles
intro: 'Use the REST API to manage the enterprise roles available in this enterprise'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/enterprises -->

---
title:  REST API endpoints for enterprise access verification
shortTitle: Enterprise access verification
intro: 'Use the REST API to manage enterprise access verification configuration in your {% data variables.product.github %} enterprise.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/global-webhooks -->

---
title: REST API endpoints for global webhooks
shortTitle: Global webhooks
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage global webhooks for your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About global webhooks

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators Normal users will receive a `404` response. To learn how to configure global webhooks, see [About global webhooks](/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/managing-global-webhooks).

Global webhooks are automatically installed on your enterprise. You can use global webhooks to automatically monitor, respond to, or enforce rules for users, organizations, teams, and repositories on your enterprise.

Global webhooks can subscribe to the [organization](/webhooks-and-events/webhooks/webhook-events-and-payloads#organization), [user](/webhooks-and-events/webhooks/webhook-events-and-payloads#user), [repository](/webhooks-and-events/webhooks/webhook-events-and-payloads#repository), [team](/webhooks-and-events/webhooks/webhook-events-and-payloads#team), [member](/webhooks-and-events/webhooks/webhook-events-and-payloads#member), [membership](/webhooks-and-events/webhooks/webhook-events-and-payloads#membership), [fork](/webhooks-and-events/webhooks/webhook-events-and-payloads#fork), and [ping](/webhooks-and-events/webhooks/about-webhooks#ping-event) event types.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin -->

---
title: REST API endpoints for GitHub Enterprise administration
intro: Use the REST API to administer your enterprise.
allowTitleToDifferFromFilename: true
redirect_from:
  - /v3/enterprise-admin
  - /v3/enterprise
  - /rest/reference/enterprise-admin
  - /rest/enterprise-admin/management-console
versions:
  ghes: '*'
  ghec: '*'
shortTitle: Enterprise administration
children:
  - /admin-stats
  - /announcement
  - /audit-log
  - /bypass-requests
  - /code-security-and-analysis
  - /credential-authorizations
  - /custom-properties
  - /custom-properties-for-orgs
  - /enterprise-roles
  - /enterprises
  - /global-webhooks
  - /ldap
  - /licensing
  - /manage-ghes
  - /network-configurations
  - /org-pre-receive-hooks
  - /organization-installations
  - /orgs
  - /pre-receive-environments
  - /pre-receive-hooks
  - /repo-pre-receive-hooks
  - /rules
  - /scim
  - /users
autogenerated: rest
---

{% ifversion ghec %}

> [!NOTE]
> This information applies to {% data variables.product.prodname_ghe_cloud %}. To see the {% data variables.product.prodname_ghe_server %} version, use the **{% data ui.pages.article_version %}** drop-down menu.

{% endif %}

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

## Endpoint URLs

These endpoints{% ifversion ghes %}, except the Manage GitHub Enterprise Server API,{% endif %} are prefixed with the following URL:

```shell
{% data variables.product.rest_url %}
```

{% ifversion ghec %}
When endpoints include `{enterprise}`, replace `{enterprise}` with the handle for your enterprise account, which is included in the URL for your enterprise settings. For example, if your enterprise account is located at `https://github.com/enterprises/octo-enterprise`, replace `{enterprise}` with `octo-enterprise`.
{% endif %}

{% ifversion ghes %}

Endpoints for the  Manage GitHub Enterprise Server API are only prefixed with a hostname and administration port:

```shell
http(s)://HOSTNAME:ADMINISTRATION-PORT/
```

{% endif %}
{% ifversion ghes %}

## Authentication

Your {% data variables.product.prodname_ghe_server %} installation's API endpoints accept the same authentication methods as the {% data variables.product.github %} API. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

OAuth tokens must have the `site_admin` [OAuth scope](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes) when used with these endpoints.

These endpoints are only accessible to authenticated {% data variables.product.prodname_ghe_server %} site administrators, except for endpoints of the [AUTOTITLE](/rest/enterprise-admin/manage-ghes) API, which allow authentication as a Management Console user. See [AUTOTITLE](/admin/configuration/administering-your-instance-from-the-management-console).

{% data reusables.enterprise_management_console.api-deprecation %}

{% endif %}

{% ifversion ghes %}

## Version information

The current version of your enterprise is returned in the REST API response header:
`X-GitHub-Enterprise-Version: {{currentVersion}}.0`
You can also read the current version by calling `GET /meta`. For more information, see [AUTOTITLE](/rest/meta).

{% endif %}

## Endpoints

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/ldap -->

---
title: REST API endpoints for LDAP
shortTitle: LDAP
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to update account relationships between a {% data variables.product.prodname_ghe_server %} user or team and its linked LDAP entry or
  queue a new synchronization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About LDAP

You can use these endpoints to update the Distinguished Name (DN) that a user or team maps to. Note that in most cases, you must have [LDAP Sync enabled](/admin/identity-and-access-management/using-ldap-for-enterprise-iam/using-ldap) for your {% data variables.product.prodname_ghe_server %} appliance. The [Update LDAP mapping for a user](#update-ldap-mapping-for-a-user) endpoint can be used when LDAP is enabled, even if LDAP Sync is disabled.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/licensing -->

---
title: Licensing
intro: Use the REST API to get licensing information.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
autogenerated: rest
redirect_from:
  - /rest/enterprise-admin/license
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/manage-ghes -->

---
title: REST API endpoints for managing GitHub Enterprise Server
allowTitleToDifferFromFilename: true
shortTitle: Manage GHES
intro: >-
  Use the REST API to manage your {% data variables.product.prodname_ghe_server %}
  instance.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About the Manage {% data variables.product.prodname_ghe_server %} API

You can manage {% data variables.location.product_location %} using the Manage {% data variables.product.prodname_ghe_server %} API. For example, you can retrieve information about the version of the {% data variables.product.prodname_ghe_server %} software running on the instance, or on instances with multiple nodes, view the status of replication.

> [!TIP] You can use this API to replace the functionality of the **Management Console API**, which was removed in {% data variables.product.prodname_ghe_server %} version 3.15.

Specify the port number when making API calls to endpoints for the Manage {% data variables.product.prodname_ghe_server %} API. If your instance uses TLS, the port number is 8443. Otherwise, the port number is 8080. If you cannot provide a port number, you'll need to configure your client to automatically follow redirects. For more information, see [AUTOTITLE](/admin/configuration/configuring-network-settings/configuring-tls).

You can also use the {% data variables.product.prodname_ghe_server %} extension of the {% data variables.product.prodname_cli %} to invoke endpoints in the Manage {% data variables.product.prodname_ghe_server %} API. For more information, see the [`github/gh-es`](https://github.com/github/gh-es/blob/main/README.md) repository.

### Authentication

To authenticate requests to endpoints for the Manage {% data variables.product.prodname_ghe_server %} API, specify the password for the instance's root site administrator account as an authentication token. Use standard HTTP authentication to send the password. The `api_key` user identifies the root site administrator. The following example demonstrates authentication for this API. Replace ROOT-SITE-ADMINISTRATOR-PASSWORD with the password, and ADMINISTRATION-PORT with either 8443 or 8080.

```shell
curl -L -u "api_key:ROOT-SITE-ADMINISTRATOR-PASSWORD" 'http(s)://HOSTNAME:ADMINISTRATION-PORT/manage'
```

### Authentication as a {% data variables.enterprise.management_console %} user

{% data variables.enterprise.management_console %} user accounts can also authenticate to access these endpoints. For more information, see [AUTOTITLE](/admin/configuration/administering-your-instance-from-the-management-console/managing-access-to-the-management-console#management-console-user).

To authenticate with the password for a {% data variables.enterprise.management_console %} user account, use standard HTTP authentication. In the following example, replace YOUR_USER_NAME and YOUR_PASSWORD with the account's user name and password.

```shell
curl -L -u "YOUR_USER_NAME:YOUR_PASSWORD" 'http(s)://HOSTNAME:ADMINISTRATION-PORT/manage'
```

### Query parameters

By default, the response includes information from about all configured nodes for the instance. On an instance with multiple nodes, the details originate from `/data/user/common/cluster.conf`. You can use the following query parameters to filter the response for information about specific nodes.

| Query parameter | Description |
| :- | :- |
| `uuid` | Unique identifier for the node. |
| `cluster_role` | For nodes in a cluster, the roles that apply to the node. For more information, see [AUTOTITLE](/admin/enterprise-management/configuring-clustering/about-cluster-nodes). |

You can specify multiple values for the query parameter by delimiting the values with a comma. For example, the following request uses curl to return any nodes with the `web-server` or `storage-server` role.

```shell
curl -L -u "api_key:ROOT-SITE-ADMINISTRATOR-PASSWORD" 'http(s)://HOSTNAME:ADMINISTRATION-PORT/manage/v1/config/nodes?cluster_role=WebServer,StorageServer'
```

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/network-configurations -->

---
title: REST API endpoints for enterprise network configurations
shortTitle: Network configurations
intro: Use the REST API to interact with enterprise network configurations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/org-pre-receive-hooks -->

---
title: REST API endpoints for organization pre-receive hooks
shortTitle: Organization pre-receive hooks
intro: >-
  Use the REST API to view and modify enforcement of the pre-receive hooks that
  are available to an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About organization pre-receive hooks

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

### Object attributes

| Name                             | Type      | Description                                               |
|----------------------------------|-----------|-----------------------------------------------------------|
| `name`                           | `string`  | The name of the hook.                                     |
| `enforcement`                    | `string`  | The state of enforcement for the hook on this repository. |
| `allow_downstream_configuration` | `boolean` | Whether repositories can override enforcement.            |
| `configuration_url`              | `string`  | URL for the endpoint where enforcement is set.            |

Possible values for `enforcement` are `enabled`, `disabled` and`testing`. `disabled` indicates the pre-receive hook will not run. `enabled` indicates it will run and reject any pushes that result in a non-zero status. `testing` means the script will run but will not cause any pushes to be rejected.

`configuration_url` may be a link to this endpoint or this hook's global configuration. Only site admins are able to access the global configuration.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/organization-installations -->

---
title: REST API for managing organization GitHub App installations
shortTitle: GitHub App installations
intro: >-
  Use the REST API to manage which {% data
  variables.product.prodname_github_apps %} are installed in your enterprise's
  organizations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/orgs -->

---
title: REST API endpoints for enterprise organizations
shortTitle: Organizations
intro: Use the REST API to create organizations on your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About organization administration

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators. Normal users will receive a `404` response.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/pre-receive-environments -->

---
title: REST API endpoints for pre-receive environments
shortTitle: Pre-receive environments
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create, list, update and delete environments for
  pre-receive hooks.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About pre-receive environments

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators. Normal users will receive a `404` response.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

### Object attributes

#### Pre-receive Environment

| Name                  | Type      | Description                                                                |
|-----------------------|-----------|----------------------------------------------------------------------------|
| `name`                | `string`  | The name of the environment as displayed in the UI.                        |
| `image_url`           | `string`  | URL to the tarball that will be downloaded and extracted.                  |
| `default_environment` | `boolean` | Whether this is the default environment that ships with {% data variables.product.github %}. |
| `download`            | `object`  | This environment's download status.                                        |
| `hooks_count`         | `integer` | The number of pre-receive hooks that use this environment.                 |

#### Pre-receive Environment Download

| Name            | Type     | Description                                             |
|-----------------|----------|---------------------------------------------------------|
| `state`         | `string` | The state of the most recent download.                  |
| `downloaded_at` | `string` | The time when the most recent download started.         |
| `message`       | `string` | On failure, this will have any error messages produced. |

Possible values for `state` are `not_started`, `in_progress`, `success`, `failed`.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/pre-receive-hooks -->

---
title: REST API endpoints for pre-receive hooks
shortTitle: Pre-receive hooks
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to create, list, update and delete pre-receive hooks.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About pre-receive hooks

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators. Normal users will receive a `404` response.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

### Object attributes

#### Pre-receive Hook

| Name                             | Type      | Description                                                     |
|----------------------------------|-----------|-----------------------------------------------------------------|
| `name`                           | `string`  | The name of the hook.                                           |
| `script`                         | `string`  | The script that the hook runs.                                  |
| `script_repository`              | `object`  | The GitHub repository where the script is kept.                 |
| `environment`                    | `object`  | The pre-receive environment where the script is executed.       |
| `enforcement`                    | `string`  | The state of enforcement for this hook.                         |
| `allow_downstream_configuration` | `boolean` | Whether enforcement can be overridden at the org or repo level. |

Possible values for _enforcement_ are `enabled`, `disabled` and`testing`. `disabled` indicates the pre-receive hook will not run. `enabled` indicates it will run and reject
any pushes that result in a non-zero status. `testing` means the script will run but will not cause any pushes to be rejected.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/repo-pre-receive-hooks -->

---
title: REST API endpoints for repository pre-receive hooks
shortTitle: Repository pre-receive hooks
intro: >-
  Use the REST API to view and modify enforcement of the pre-receive hooks that
  are available to a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About repository pre-receive hooks

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

| Name                | Type     | Description                                               |
|---------------------|----------|-----------------------------------------------------------|
| `name`              | `string` | The name of the hook.                                     |
| `enforcement`       | `string` | The state of enforcement for the hook on this repository. |
| `configuration_url` | `string` | URL for the endpoint where enforcement is set.            |

Possible values for _enforcement_ are `enabled`, `disabled` and`testing`. `disabled` indicates the pre-receive hook will not run. `enabled` indicates it will run and reject any pushes that result in a non-zero status. `testing` means the script will run but will not cause any pushes to be rejected.

`configuration_url` may be a link to this repository, its organization owner or global configuration. Authorization to access the endpoint at `configuration_url` is determined at the owner or site admin level.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/rules -->

---
title: REST API endpoints for rules
shortTitle: Rules
intro: >-
  Use the REST API to manage rulesets for an enterprise. Rulesets control how
  people can interact with repositories and code.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/scim -->

---
title: REST API endpoints for SCIM
shortTitle: SCIM
allowTitleToDifferFromFilename: true
intro: Use the REST API to automate user creation and team memberships with SCIM.
versions:
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

{% ifversion emu-public-scim-schema %}

> [!NOTE]
> * {% data reusables.scim.ghec-open-scim-operation-differentiation %}
> * {% data reusables.scim.ghec-open-scim-test-in-isolation %}

{% endif %}

## About SCIM

{% ifversion ghec %}

{% data reusables.enterprise_user_management.about-scim-provisioning %} If you don't use a partner IdP with an existing integration, you can integrate using the following API endpoints. For more information, see [AUTOTITLE](/admin/identity-and-access-management/provisioning-user-accounts-for-enterprise-managed-users/provisioning-users-with-scim-using-the-rest-api).

### Base URL

To manage your enterprise's users and groups using SCIM, use the following base URL to communicate with the endpoints in this category.

```http
{% data variables.product.rest_url %}/scim/v2/enterprises/{enterprise}/
```

### Authentication

To authenticate API requests, the person who configures SCIM on the IdP must use a {% data variables.product.pat_v1 %} with `scim:enterprise` scope, which the IdP must provide in the request's `Authorization` header. For more information about {% data variables.product.pat_v1_plural %}, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

{% data variables.product.company_short %} recommends authenticating as the setup user for the enterprise. Other user accounts are created through SCIM, so authenticating as a different user could result in unintended consequences, such as getting locked out of your enterprise. Write requests to these APIs are possible through our published IdP applications, or through direct API access to our SCIM endpoints. If another enterprise owner needs to read information from the API, use a {% data variables.product.pat_v1 %} with the `admin:enterprise` scope to make `GET` requests on your current SCIM implementation. For more information, see [AUTOTITLE](/admin/identity-and-access-management/provisioning-user-accounts-for-enterprise-managed-users/configuring-scim-provisioning-for-enterprise-managed-users#creating-a-personal-access-token).

### Mapping of SAML and SCIM data

After a {% data variables.enterprise.prodname_managed_user %} successfully authenticates to access your enterprise using SAML SSO, {% data variables.product.github %} links the user to a SCIM provisioned identity. To link the identities successfully, the SAML identity provider and the SCIM integration must use matching unique identifiers.

{% data variables.product.company_short %} requires the following SAML claim and SCIM attribute to successfully match the user with the identity provisioned by SCIM. Identity providers may differ in the field used to uniquely identify a user.

#### Microsoft Entra ID for SAML

To use Entra ID (previously known as Azure AD) for SAML, the following SAML claims and SCIM attribute must match.

| SAML claim | Matching SCIM attribute |
| :- | :- |
| `http://schemas.microsoft.com/identity/claims/objectidentifier` | `externalId` |

#### Other IdPs for SAML

To use other IdPs for SAML, the following SAML claims and SCIM attribute must match.

| SAML claim | Matching SCIM attribute |
| :- | :- |
| `NameID` | `userName` |

### Supported SCIM user attributes

`Users` endpoints in this category support the following attributes within a request's parameters.

| Name | Type | Description |
| :- | :- | :- |
| `displayName` | String | Human-readable name for a user. |
| `name.formatted` | String | The user's full name, including all middle names, titles, and suffixes, formatted for display.|
| `name.givenName` | String | The first name of the user. |
| `name.familyName` | String | The last name of the user. |
| `userName` | String | The username for the user, generated by the SCIM provider. Undergoes [normalization](/admin/identity-and-access-management/managing-iam-for-your-enterprise/username-considerations-for-external-authentication#about-username-normalization) before being used. Must be unique per user. |
| `emails` | Array | List of the user's emails. |
| `roles` | Array | List of the user's roles. |
| `externalId` | String | This identifier is generated by a SCIM provider. Must be unique per user. |
| `id` | String | Identifier generated by the GitHub's SCIM endpoint. |
| `active` | Boolean | Indicates whether the identity is active (`true`) or should be suspended (`false`). |

### Supported SCIM group attributes

`Groups` endpoints in this category support the following attributes within a request's parameters.

| Name | Type | Description |
| :- | :- | :- |
| `displayName` | String | Human-readable name for a group. |
| `members` | String | List of members who are assigned to the group in SCIM provider |
| `externalId` | String | This identifier is generated by a SCIM provider. Must be unique per user. |

{% endif %}

{% ifversion ghes %}

{% data reusables.scim.ghes-beta-note %}

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

{% data variables.product.github %} provides endpoints for use by SCIM-enabled Identity Providers (IdPs). An integration on the IdP can use the REST API to automatically provision, manage, or deprovision user accounts on a {% data variables.product.prodname_ghe_server %} instance that uses SAML single sign-on (SSO) for authentication. See [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes).

These endpoints are based on SCIM 2.0. For more information, refer to your IdP's documentation or see the [specification on the IETF website](https://datatracker.ietf.org/doc/html/rfc7644).

### Root URLs

An IdP can use the following root URL to communicate with the endpoints in this category for a {% data variables.product.prodname_ghe_server %} instance.

```http
{% data variables.product.rest_url %}/scim/v2/
```

Do **not** include the `enterprises/{enterprise}/` portion of the URLs provided in the endpoint documentation below. This part of the path is not applicable to {% data variables.product.prodname_ghe_server %}. In the future, this documentation will display the correct URLs for {% data variables.product.prodname_ghe_server %}.

Endpoints in this category are case-sensitive. For example, the first letter in the `Users` endpoint must be capitalized.

```shell
GET /scim/v2/Users/{scim_user_id}
```

### Authentication

The SCIM integration on the IdP performs actions on behalf of an enterprise owner for the {% data variables.product.prodname_ghe_server %} instance. For more information, see [AUTOTITLE](/admin/user-management/managing-users-in-your-enterprise/roles-in-an-enterprise#enterprise-owners).

To authenticate API requests, the person who configures SCIM on the IdP must use a {% data variables.product.pat_v1 %} with the {% ifversion scim-enterprise-scope %}`scim:enterprise`{% else %}`admin:enterprise`{% endif %} scope, which the IdP must provide in the request's `Authorization` header. For more information about {% data variables.product.pat_v1_plural %}, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

> [!NOTE]
> Enterprise owners must generate and use a {% data variables.product.pat_v1 %} for authentication of requests to endpoints in this category. {% data variables.product.pat_v2_caps %} and GitHub app callers are not supported at this time.

### Mapping of SAML and SCIM data

After a {% data variables.product.prodname_ghe_server %} user successfully authenticates using SAML SSO, {% data variables.product.github %} links the user to a SCIM provisioned identity. To link the identities successfully, the SAML identity provider and the SCIM integration must use matching unique identifiers.

When a mismatch between a user's SAML and SCIM data occurs, {% data variables.product.company_short %} will return an error stating which attributes from SAML and SCIM did not match. For more information on this error, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/troubleshooting-identity-and-access-management-for-your-enterprise#saml-and-scim-data-mismatch-errors).

{% data variables.product.company_short %} requires the following SAML claim and SCIM attribute to successfully match the user with the identity provisioned by SCIM. Identity providers may differ in the field used to uniquely identify a user.

#### Microsoft Entra ID for SAML

To use Entra ID (previously known as Azure AD) for SAML, the following SAML claims and SCIM attribute must match.

| SAML claim | Matching SCIM attribute |
| :- | :- |
| `http://schemas.microsoft.com/identity/claims/objectidentifier` | `externalId` |

#### Other IdPs for SAML

To use other IdPs for SAML, {% data variables.product.company_short %} will use the "Username" attribute configured in your SAML "User attributes" to match against the SCIM attribute listed below. If left blank, the "Username" attribute in your SAML "User attributes" will default to the SAML `NameID`. For more information about SAML configurations, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise#configuring-saml-sso).

| SAML claim | Matching SCIM attribute |
| :- | :- |
| "Username" attribute configured in your SAML "User attributes", or `NameID` if left blank | `userName` |

### Supported SCIM user attributes

`User` endpoints in this category support the following attributes within a request's parameters.

| Name | Type | Description |
| :- | :- | :- |
| `displayName` | String | Human-readable name for a user. |
| `name.formatted` | String | The user's full name, including all middle names, titles, and suffixes, formatted for display.
| `name.givenName` | String | The first name of the user. |
| `name.familyName` | String | The last name of the user. |
| `userName` | String | The username for the user, generated by the IdP. Undergoes [normalization](/admin/identity-and-access-management/managing-iam-for-your-enterprise/username-considerations-for-external-authentication#about-username-normalization) before being used.
| `emails` | Array | List of the user's emails. |
| `roles` | Array | List of the user's roles. |
| `externalId` | String | This identifier is generated by an IdP provider. You can find the `externalId` for a user either on the IdP, or by using the [List SCIM provisioned identities](#list-scim-provisioned-identities-for-an-enterprise) endpoint and filtering on other known attributes, such as a user's username or email address on the {% data variables.product.prodname_ghe_server %} instance. |
| `id` | String | Identifier generated by the instance's SCIM endpoint. |
| `active` | Boolean | Indicates whether the identity is active (`true`) or should be suspended (`false`). |

{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-admin/users -->

---
title: REST API endpoints for enterprise users
shortTitle: Users
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to suspend, unsuspend, promote, and
  demote users on your enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
autogenerated: rest
category:
  - Administer enterprises and billing
---

## About user administration

These endpoints are only available to [authenticated](/rest/overview/authenticating-to-the-rest-api) site administrators. Normal users will receive a `403` response.

{% data reusables.user-settings.enterprise-admin-api-classic-pat-only %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-teams/enterprise-team-members -->

---
title: REST API endpoints for enterprise team memberships
shortTitle: Enterprise team members
intro: >-
  Use the REST API to create and manage membership of enterprise teams in your
  {% data variables.product.github %} enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

## About enterprise team members

{% data reusables.enterprise.enterprise-team-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-teams/enterprise-team-organizations -->

---
title: REST API endpoints for enterprise team organizations
shortTitle: Enterprise team organizations
intro: >-
  Use the REST API to create and manage organization assignments for enterprise
  teams in your {% data variables.product.github %} enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

## About enterprise team organizations

{% data reusables.enterprise.enterprise-team-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-teams/enterprise-teams -->

---
title: REST API endpoints for enterprise teams
shortTitle: Enterprise teams
intro: >-
  Use the REST API to create and manage enterprise teams in your {% data
  variables.product.github %} enterprise.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Administer enterprises and billing
---

## About enterprise teams

{% data reusables.enterprise.enterprise-team-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/enterprise-teams -->

---
title: Enterprise teams
autogenerated: rest
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create and manage enterprise teams in your {% data
  variables.product.github %} enterprise.
children:
  - /enterprise-team-members
  - /enterprise-team-organizations
  - /enterprise-teams
versions:
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
---



---

<!-- source: https://docs.github.com/en/rest/gists/comments -->

---
title: REST API endpoints for gist comments
allowTitleToDifferFromFilename: true
shortTitle: Comments
intro: Use the REST API to view and modify comments on a gist.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About gist comments

You can use the REST API to view and modify comments on a gist. For more information about gists, see [AUTOTITLE](/get-started/writing-on-github/editing-and-sharing-content-with-gists).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/gists/gists -->

---
title: REST API endpoints for gists
shortTitle: Gists
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to list, create, update and delete the public gists on
  GitHub.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About gists

You can use the REST API to view and modify gists. For more information about gists, see [AUTOTITLE](/get-started/writing-on-github/editing-and-sharing-content-with-gists).

{% ifversion ghec %}

> [!NOTE] Gists are not available with {% data variables.product.prodname_emus %}.

{% endif %}

### Authentication

You can read public gists {% ifversion ghes %}and create them for anonymous users without a token.{% else %} anonymously, but you must be signed into {% data variables.product.github %} to create gists.{% endif %} To read or write gists on a user's behalf, you need the gist OAuth scope and a token. For more information, see [AUTOTITLE](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps).

<!-- When an OAuth client does not have the gists scope, the API will return a 404 "Not Found" response regardless of the validity of the credentials. The API will return a 401 "Bad credentials" response if the gists scope was given to the application but the credentials are invalid. -->

### Truncation

The API provides up to one megabyte of content for each file in the gist. Each file returned for a gist through the API has a key called `truncated`. If `truncated` is `true`, the file is too large and only a portion of the contents were returned in `content`.

If you need the full contents of the file, you can make a `GET` request to the URL specified by `raw_url`. Be aware that for files larger than ten megabytes, you'll need to clone the gist via the URL provided by `git_pull_url`.

In addition to a specific file's contents being truncated, the entire files list may be truncated if the total number exceeds 300 files. If the top level `truncated` key is `true`, only the first 300 files have been returned in the files list. If you need to fetch all of the gist's files, you'll need to clone the gist via the URL provided by `git_pull_url`.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/gists -->

---
title: REST API endpoints for gists and gist comments
shortTitle: Gists
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to list, create, update and delete the public gists on {% data variables.product.github %}.'
redirect_from:
  - /v3/gists
  - /rest/reference/gists
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /gists
  - /comments
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/git/blobs -->

---
title: REST API endpoints for Git blobs
shortTitle: Blobs
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with a Git blob (binary large object), the object
  type used to store the contents of each file in a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About Git blobs

A Git blob (binary large object) is the object type used to store the contents of each file in a repository. The file's SHA-1 hash is computed and stored in the blob object. These endpoints allow you to read and write [blob objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
to your Git database on {% data variables.product.github %}. Blobs leverage custom media types. For more information about the use of media types in the API, see [AUTOTITLE](/rest/overview/media-types).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/git/commits -->

---
title: REST API endpoints for Git commits
shortTitle: Commits
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with commit objects in your Git database on {%
  data variables.product.github %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About Git commits

A Git commit is a snapshot of the hierarchy ([Git tree](/rest/git/trees)) and the contents of the files ([Git blob](/rest/git/blobs)) in a Git repository. These endpoints allow you to read and write [commit objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#_git_commit_objects) to your Git database on {% data variables.product.github %}.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/git -->

---
title: REST API endpoints for Git database
shortTitle: Git database
intro: 'Use the REST API to interact with raw Git objects in your Git database on {% data variables.product.github %} and to list and update Git references (branch heads and tags).'
allowTitleToDifferFromFilename: true
redirect_from:
  - /v3/git
  - /rest/reference/git
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /blobs
  - /commits
  - /refs
  - /tags
  - /trees
autogenerated: rest
---

## About Git database

The REST API gives you access to read and write raw Git objects to your Git database on {% data variables.product.github %} and to list and update your references (branch heads and tags). For more information about using the REST API to interact with your Git database, see [AUTOTITLE](/rest/guides/using-the-rest-api-to-interact-with-your-git-database).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/git/refs -->

---
title: REST API endpoints for Git references
shortTitle: References
intro: >-
  Use the REST API to interact with references in your Git database on {% data
  variables.product.github %}
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---

## About Git references

A Git reference (`git ref`) is a file that contains a Git commit SHA-1 hash. When referring to a Git commit, you can use the Git reference, which is an easy-to-remember name, rather than the hash. The Git reference can be rewritten to point to a new commit. A branch is a Git reference that stores the new Git commit hash. These endpoints allow you to read and write [references](https://git-scm.com/book/en/v2/Git-Internals-Git-References) to your Git database on {% data variables.product.github %}.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/git/tags -->

---
title: REST API endpoints for Git tags
shortTitle: Tags
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with tag objects in your Git database on {% data
  variables.product.github %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About Git tags

A Git tag is similar to a [Git reference](/rest/git/refs), but the Git commit that it points to never changes. Git tags are helpful when you want to point to specific releases. These endpoints allow you to read and write [tag objects](https://git-scm.com/book/en/v2/Git-Internals-Git-References#_tags) to your Git database on {% data variables.product.github %}. The API only supports [annotated tag objects](https://git-scm.com/book/en/v2/Git-Internals-Git-References#_tags), not lightweight tags.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/git/trees -->

---
title: REST API endpoints for Git trees
shortTitle: Trees
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with tree objects in your Git database on {% data
  variables.product.github %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About Git trees

A Git tree object creates the hierarchy between files in a Git repository. You can use the Git tree object to create the relationship between directories and the files they contain. These endpoints allow you to read and write [tree objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#_tree_objects) to your Git database on {% data variables.product.github %}.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/gitignore/gitignore -->

---
title: REST API endpoints for gitignore
shortTitle: Gitignore
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to get `.gitignore` templates that can be used to ignore
  files and directories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/gitignore
autogenerated: rest
category:
  - Manage repositories and code
---

## About gitignore

When you create a new repository on {% data variables.product.github %} via the API, you can specify a [.gitignore template](/get-started/git-basics/ignoring-files) to apply to the repository upon creation. You can use the REST API to get .gitignore templates from the {% data variables.product.github %} [.gitignore repository](https://github.com/github/gitignore).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/gitignore -->

---
title: REST API endpoints for gitignore
shortTitle: Gitignore
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to get `.gitignore` templates that can be used to ignore
  files and directories.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /gitignore
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/guides/building-a-ci-server -->

---
title: Building a CI server
intro: Build your own CI system using the Status API.
redirect_from:
  - /guides/building-a-ci-server
  - /v3/guides/building-a-ci-server
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Build apps and integrations
---



You can use the REST API to tie together commits with
a testing service, so that every push you make can be tested and represented
in a {% data variables.product.github %} pull request. For more information about the relevant endpoints, see [AUTOTITLE](/rest/commits/statuses).

This guide will use that API to demonstrate a setup that you can use.
In our scenario, we will:

* Run our CI suite when a Pull Request is opened (we'll set the CI status to pending).
* When the CI is finished, we'll set the Pull Request's status accordingly.

Our CI system and host server will be figments of our imagination. They could be
Travis, Jenkins, or something else entirely. The crux of this guide will be setting up
and configuring the server managing the communication.

If you haven't already, [download `ngrok`](https://ngrok.com/), and learn how
to [use it](/webhooks-and-events/webhooks/configuring-your-server-to-receive-payloads#using-ngrok). We find it to be a very useful tool for exposing local
applications to the internet.

{% ifversion cli-webhook-forwarding %}

> [!NOTE]
> Alternatively, you can use webhook forwarding to set up your local environment to receive webhooks. For more information, see [AUTOTITLE](/webhooks-and-events/webhooks/receiving-webhooks-with-the-github-cli).

{% endif %}

Note: you can download the complete source code for this project
[from the platform-samples repo](https://github.com/github/platform-samples/tree/master/api/ruby/building-a-ci-server).

## Writing your server

We'll write a quick Sinatra app to prove that our local connections are working.
Let's start with this:

``` ruby
require 'sinatra'
require 'json'

post '/event_handler' do
  payload = JSON.parse(params[:payload])
  "Well, it worked!"
end
```

(If you're unfamiliar with how Sinatra works, we recommend [reading the Sinatra guide](http://www.sinatrarb.com/).)

Start this server up. By default, Sinatra starts on port `4567`, so you'll want
to configure `ngrok` to start listening for that, too.

In order for this server to work, we'll need to set a repository up with a webhook. The webhook should be configured to fire whenever a pull request is created, or merged.

Go ahead and create a repository you're comfortable playing around in. Might we suggest [@octocat's Spoon/Knife repository](https://github.com/octocat/Spoon-Knife)?

After that, you'll create a new webhook in your repository, feeding it the URL that `ngrok` gave you, and choosing `application/x-www-form-urlencoded` as the content type.

Click **Update webhook**. You should see a body response of `Well, it worked!`.
Great! Click on **Let me select individual events**, and select the following:

* Status
* Pull Request

These are the events {% data variables.product.github %} will send to our server whenever the relevant action
occurs. Let's update our server to _just_ handle the Pull Request scenario right now:

``` ruby
post '/event_handler' do
  @payload = JSON.parse(params[:payload])

  case request.env['HTTP_X_GITHUB_EVENT']
  when "pull_request"
    if @payload["action"] == "opened"
      process_pull_request(@payload["pull_request"])
    end
  end
end

helpers do
  def process_pull_request(pull_request)
    puts "It's #{pull_request['title']}"
  end
end
```

What's going on? Every event that {% data variables.product.github %} sends out attached a `X-GitHub-Event`
HTTP header. We'll only care about the PR events for now. From there, we'll
take the payload of information, and return the title field. In an ideal scenario,
our server would be concerned with every time a pull request is updated, not just
when it's opened. That would make sure that every new push passes the CI tests.
But for this demo, we'll just worry about when it's opened.

To test out this proof-of-concept, make some changes in a branch in your test
repository, and open a pull request. Your server should respond accordingly!

## Working with statuses

With our server in place, we're ready to start our first requirement, which is
setting (and updating) CI statuses. Note that at any time you update your server,
you can click **Redeliver** to send the same payload. There's no need to make a
new pull request every time you make a change!

Since we're interacting with the {% data variables.product.github %} API, we'll use [Octokit.rb](https://github.com/octokit/octokit.rb)
to manage our interactions. We'll configure that client with
[a {% data variables.product.pat_generic %}](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token):

``` ruby
# !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
# Instead, set and test environment variables, like below
ACCESS_TOKEN = ENV['MY_PERSONAL_TOKEN']

before do
  @client ||= Octokit::Client.new(:access_token => ACCESS_TOKEN)
end
```

After that, we'll just need to update the pull request on {% data variables.product.github %} to make clear
that we're processing on the CI:

``` ruby
def process_pull_request(pull_request)
  puts "Processing pull request..."
  @client.create_status(pull_request['base']['repo']['full_name'], pull_request['head']['sha'], 'pending')
end
```

We're doing three very basic things here:

* We're looking up the full name of the repository
* We're looking up the last SHA of the pull request
* We're setting the status to "pending"

That's it! From here, you can run whatever process you need to in order to execute
your test suite. Maybe you're going to pass off your code to Jenkins, or call
on another web service via its API, like [Travis](https://api.travis-ci.com/docs/). After that, you'd
be sure to update the status once more. In our example, we'll just set it to `"success"`:

``` ruby
def process_pull_request(pull_request)
  @client.create_status(pull_request['base']['repo']['full_name'], pull_request['head']['sha'], 'pending')
  sleep 2 # do busy work...
  @client.create_status(pull_request['base']['repo']['full_name'], pull_request['head']['sha'], 'success')
  puts "Pull request processed!"
end
```

## Conclusion

At GitHub, we've used a version of [Janky](https://github.com/github/janky) to manage our CI for years.
The basic flow is essentially the exact same as the server we've built above.
At GitHub, we:

* Fire to Jenkins when a pull request is created or updated (via Janky)
* Wait for a response on the state of the CI
* If the code is green, we merge the pull request

All of this communication is funneled back to our chat rooms. You don't need to
build your own CI setup to use this example.
You can always rely on [GitHub integrations](https://github.com/integrations).


---

<!-- source: https://docs.github.com/en/rest/guides/delivering-deployments -->

---
title: Delivering deployments
intro: 'Using the Deployments REST API, you can build custom tooling that interacts with your server and a third-party app.'
redirect_from:
  - /guides/delivering-deployments
  - /guides/automating-deployments-to-integrators
  - /v3/guides/delivering-deployments
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Build apps and integrations
---



You can use the REST API to deploy your projects hosted on {% data variables.product.github %} on a server that you own. For more information about the endpoints to manage deployments and statuses, see [AUTOTITLE](/rest/deployments). You can also use the REST API to coordinate your deployments the moment your code lands on the default branch. For more information, see [AUTOTITLE](/rest/guides/building-a-ci-server).

This guide will use the REST API to demonstrate a setup that you can use.
In our scenario, we will:

* Merge a pull request.
* When the CI is finished, we'll set the pull request's status accordingly.
* When the pull request is merged, we'll run our deployment to our server.

Our CI system and host server will be figments of our imagination. They could be
Heroku, Amazon, or something else entirely. The crux of this guide will be setting up
and configuring the server managing the communication.

If you haven't already, be sure to [download `ngrok`](https://ngrok.com/), and learn how
to [use it](/webhooks-and-events/webhooks/configuring-your-server-to-receive-payloads#using-ngrok). We find it to be a very useful tool for exposing local
applications to the internet.

{% ifversion cli-webhook-forwarding %}

> [!NOTE]
> Alternatively, you can use webhook forwarding to set up your local environment to receive webhooks. For more information, see [AUTOTITLE](/webhooks-and-events/webhooks/receiving-webhooks-with-the-github-cli).

{% endif %}

Note: you can download the complete source code for this project
[from the platform-samples repo](https://github.com/github/platform-samples/tree/master/api/ruby/delivering-deployments).

## Writing your server

We'll write a quick Sinatra app to prove that our local connections are working.
Let's start with this:

``` ruby
require 'sinatra'
require 'json'

post '/event_handler' do
  payload = JSON.parse(params[:payload])
  "Well, it worked!"
end
```

(If you're unfamiliar with how Sinatra works, we recommend [reading the Sinatra guide](http://www.sinatrarb.com/).)

Start this server up. By default, Sinatra starts on port `4567`, so you'll want
to configure `ngrok` to start listening for that, too.

In order for this server to work, we'll need to set a repository up with a webhook. The webhook should be configured to fire whenever a pull request is created, or merged.

Go ahead and create a repository you're comfortable playing around in. Might we
suggest [@octocat's Spoon/Knife repository](https://github.com/octocat/Spoon-Knife)?

After that, you'll create a new webhook in your repository, feeding it the URL that `ngrok` gave you, and choosing `application/x-www-form-urlencoded` as the content type.

Click **Update webhook**. You should see a body response of `Well, it worked!`.
Great! Click on **Let me select individual events.**, and select the following:

* Deployment
* Deployment status
* Pull Request

These are the events {% data variables.product.github %} will send to our server whenever the relevant action
occurs. We'll configure our server to _just_ handle when pull requests are merged
right now:

``` ruby
post '/event_handler' do
  @payload = JSON.parse(params[:payload])

  case request.env['HTTP_X_GITHUB_EVENT']
  when "pull_request"
    if @payload["action"] == "closed" && @payload["pull_request"]["merged"]
      puts "A pull request was merged! A deployment should start now..."
    end
  end
end
```

What's going on? Every event that {% data variables.product.github %} sends out attached a `X-GitHub-Event`
HTTP header. We'll only care about the PR events for now. When a pull request is
merged (its state is `closed`, and `merged` is `true`), we'll kick off a deployment.

To test out this proof-of-concept, make some changes in a branch in your test
repository, open a pull request, and merge it. Your server should respond accordingly!

## Working with deployments

With our server in place, the code being reviewed, and our pull request
merged, we want our project to be deployed.

We'll start by modifying our event listener to process pull requests when they're
merged, and start paying attention to deployments:

``` ruby
when "pull_request"
  if @payload["action"] == "closed" && @payload["pull_request"]["merged"]
    start_deployment(@payload["pull_request"])
  end
when "deployment"
  process_deployment(@payload)
when "deployment_status"
  update_deployment_status
end
```

Based on the information from the pull request, we'll start by filling out the
`start_deployment` method:

``` ruby
def start_deployment(pull_request)
  user = pull_request['user']['login']
  payload = JSON.generate(:environment => 'production', :deploy_user => user)
  @client.create_deployment(pull_request['head']['repo']['full_name'], pull_request['head']['sha'], {:payload => payload, :description => "Deploying my sweet branch"})
end
```

Deployments can have some metadata attached to them, in the form of a `payload`
and a `description`. Although these values are optional, it's helpful to use
for logging and representing information.

When a new deployment is created, a completely separate event is triggered. That's
why we have a new `switch` case in the event handler for `deployment`. You can
use this information to be notified when a deployment has been triggered.

Deployments can take a rather long time, so we'll want to listen for various events,
such as when the deployment was created, and what state it's in.

Let's simulate a deployment that does some work, and notice the effect it has on
the output. First, let's complete our `process_deployment` method:

``` ruby
def process_deployment
  payload = JSON.parse(@payload['payload'])
  # you can send this information to your chat room, monitor, pager, etc.
  puts "Processing '#{@payload['description']}' for #{payload['deploy_user']} to #{payload['environment']}"
  sleep 2 # simulate work
  @client.create_deployment_status("repos/#{@payload['repository']['full_name']}/deployments/#{@payload['id']}", 'pending')
  sleep 2 # simulate work
  @client.create_deployment_status("repos/#{@payload['repository']['full_name']}/deployments/#{@payload['id']}", 'success')
end
```

Finally, we'll simulate storing the status information as console output:

``` ruby
def update_deployment_status
  puts "Deployment status for #{@payload['id']} is #{@payload['state']}"
end
```

Let's break down what's going on. A new deployment is created by `start_deployment`,
which triggers the `deployment` event. From there, we call `process_deployment`
to simulate work that's going on. During that processing, we also make a call to
`create_deployment_status`, which lets a receiver know what's going on, as we
switch the status to `pending`.

After the deployment is finished, we set the status to `success`.

## Conclusion

At GitHub, we've used a version of `Heaven` to manage
our deployments for years. A common flow is essentially the same as the
server we've built above:

* Wait for a response on the state of the CI checks (success or failure)
* If the required checks succeed, merge the pull request
* `Heaven` takes the merged code, and deploys it to staging and production servers
* In the meantime, `Heaven` also notifies everyone about the build, via [Hubot](https://github.com/github/hubot) sitting in our chat rooms

That's it! You don't need to build your own deployment setup to use this example.
You can always rely on [GitHub integrations](https://github.com/integrations).


---

<!-- source: https://docs.github.com/en/rest/guides/discovering-resources-for-a-user -->

---
title: Discovering resources for a user
intro: Learn how to find the repositories and organizations that your app can access for a user in a reliable way for your authenticated requests to the REST API.
redirect_from:
  - /guides/discovering-resources-for-a-user
  - /v3/guides/discovering-resources-for-a-user
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Discover resources for a user
category:
  - Build apps and integrations
---



When making authenticated requests to the {% data variables.product.github %} API, applications often need to fetch the current user's repositories and organizations. In this guide, we'll explain how to reliably discover those resources.

To interact with the {% data variables.product.github %} API, we'll be using [Octokit.rb](https://github.com/octokit/octokit.rb). You can find the complete source code for this project in the [platform-samples](https://github.com/github/platform-samples/tree/master/api/ruby/discovering-resources-for-a-user) repository.

## Getting started

If you haven't already, you should read the [Basics of Authentication](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app) guide before working through the examples below. The examples below assume that you have [registered an {% data variables.product.prodname_oauth_app %}](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app#registering-your-app) and that your [application has an OAuth token for a user](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app#making-authenticated-requests).

## Discover the repositories that your app can access for a user

In addition to having their own personal repositories, a user may be a collaborator on repositories owned by other users and organizations. Collectively, these are the repositories where the user has privileged access: either it's a private repository where the user has read or write access, or it's {% ifversion fpt %}a public{% elsif ghec or ghes %}a public or internal{% endif %} repository where the user has write access.

[OAuth scopes](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) and [organization application policies](https://developer.github.com/changes/2015-01-19-an-integrators-guide-to-organization-application-policies/) determine which of those repositories your app can access for a user. Use the workflow below to discover those repositories.

As always, first we'll require [GitHub's Octokit.rb](https://github.com/octokit/octokit.rb) Ruby library. Then we'll configure Octokit.rb to automatically handle pagination for us. For more information about pagination, see [AUTOTITLE](/rest/guides/using-pagination-in-the-rest-api).

``` ruby
require 'octokit'

Octokit.auto_paginate = true
```

Next, we'll pass in our application's [OAuth token for a given user](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app#making-authenticated-requests):

``` ruby
# !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
# Instead, set and test environment variables, like below.
client = Octokit::Client.new :access_token => ENV["OAUTH_ACCESS_TOKEN"]
```

Then, we're ready to fetch the [repositories that our application can access for the user](/rest/repos/repos#list-repositories-for-the-authenticated-user):

``` ruby
client.repositories.each do |repository|
  full_name = repository[:full_name]
  has_push_access = repository[:permissions][:push]

  access_type = if has_push_access
                  "write"
                else
                  "read-only"
                end

  puts "User has #{access_type} access to #{full_name}."
end
```

## Discover the organizations that your app can access for a user

Applications can perform all sorts of organization-related tasks for a user. To perform these tasks, the app needs an [OAuth authorization](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) with sufficient permission. For example, the `read:org` scope allows you to [list teams](/rest/teams/teams#list-teams), and the `user` scope lets you [publicize the user’s organization membership](/rest/orgs/members#set-public-organization-membership-for-the-authenticated-user). Once a user has granted one or more of these scopes to your app, you're ready to fetch the user’s organizations.

Just as we did when discovering repositories above, we'll start by requiring [GitHub's Octokit.rb](https://github.com/octokit/octokit.rb) Ruby library and configuring it to take care of pagination for us. For more information about pagination, see [AUTOTITLE](/rest/guides/using-pagination-in-the-rest-api).

``` ruby
require 'octokit'

Octokit.auto_paginate = true
```

Next, we'll pass in our application's [OAuth token for a given user](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app#making-authenticated-requests) to initialize our API client:

``` ruby
# !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
# Instead, set and test environment variables, like below.
client = Octokit::Client.new :access_token => ENV["OAUTH_ACCESS_TOKEN"]
```

Then, we can [list the organizations that our application can access for the user](/rest/orgs/orgs#list-organizations-for-the-authenticated-user):

``` ruby
client.organizations.each do |organization|
  puts "User belongs to the #{organization[:login]} organization."
end
```

### Return all of the user's organization memberships

If you've read the docs from cover to cover, you may have noticed an [API method for listing a user's public organization memberships](/rest/orgs/orgs#list-organizations-for-a-user). Most applications should avoid this API method. This method only returns the user's public organization memberships, not their private organization memberships.

As an application, you typically want all of the user's organizations that your app is authorized to access. The workflow above will give you exactly that.


---

<!-- source: https://docs.github.com/en/rest/guides/encrypting-secrets-for-the-rest-api -->

---
title: Encrypting secrets for the REST API
intro: In order to create or update a secret with the REST API, you must encrypt the value of the secret.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Encrypt secrets
category:
  - Build apps and integrations
---

## About encrypting secrets

Several REST API endpoints let you create secrets on {% data variables.product.company_short %}. To use these endpoints, you must encrypt the secret value using libsodium. For more information, see the [libsodium documentation](https://libsodium.gitbook.io/doc/bindings_for_other_languages).

In order to encrypt a secret, you need a Base64 encoded public key. You can get a public key from the REST API. To determine which endpoint to use to get the public key, look at the documentation for the `encrypted_value` parameter in the endpoint that you will use to create a secret .

## Example encrypting a secret using Node.js

If you are using Node.js, you can encrypt your secret using the libsodium-wrappers library. For more information, see [libsodium-wrappers](https://www.npmjs.com/package/libsodium-wrappers).

In the following example, replace `YOUR_SECRET` with the plain text value that you want to encrypt. Replace `YOUR_BASE64_KEY` with your Base64 encoded public key. The documentation for the endpoint that you will use to create a secret will tell you which endpoint you can use to get the public key. `ORIGINAL` is not a placeholder; it is a parameter for the libsodium-wrappers library.

```javascript copy
const sodium = require('libsodium-wrappers')

const secret = 'YOUR_SECRET'
const key = 'YOUR_BASE64_KEY'

//Check if libsodium is ready and then proceed.
sodium.ready.then(() => {
  // Convert the secret and key to a Uint8Array.
  let binkey = sodium.from_base64(key, sodium.base64_variants.ORIGINAL)
  let binsec = sodium.from_string(secret)

  // Encrypt the secret using libsodium
  let encBytes = sodium.crypto_box_seal(binsec, binkey)

  // Convert the encrypted Uint8Array to Base64
  let output = sodium.to_base64(encBytes, sodium.base64_variants.ORIGINAL)

  // Print the output
  console.log(output)
});
```

## Example encrypting a secret using Python

If you are using Python 3, you can encrypt your secret using the PyNaCl library. For more information, see [PyNaCl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox).

In the following example, replace `YOUR_SECRET` with the plain text value that you want to encrypt. Replace `YOUR_BASE64_KEY` with your Base64 encoded public key. The documentation for the endpoint that you will use to create a secret will tell you which endpoint you can use to get the public key.

```python copy
from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")

encrypt("YOUR_BASE64_KEY", "YOUR_SECRET")
```

## Example encrypting a secret using C#

If you are using C#, you can encrypt your secret using the Sodium.Core package. For more information, see [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/).

In the following example, replace `YOUR_SECRET` with the plain text value that you want to encrypt. Replace `YOUR_BASE64_KEY` with your Base64 encoded public key. The documentation for the endpoint that you will use to create a secret will tell you which endpoint you can use to get the public key.

```csharp copy
var secretValue = System.Text.Encoding.UTF8.GetBytes("YOUR_SECRET");
var publicKey = Convert.FromBase64String("YOUR_BASE64_KEY");

var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
```

## Example encrypting a secret using Ruby

If you are using Ruby, you can encrypt your secret using the RbNaCl gem. For more information, see [RbNaCl](https://github.com/RubyCrypto/rbnacl).

In the following example, replace `YOUR_SECRET` with the plain text value that you want to encrypt. Replace `YOUR_BASE64_KEY` with your Base64 encoded public key. The documentation for the endpoint that you will use to create a secret will tell you which endpoint you can use to get the public key.

```ruby copy
require "rbnacl"
require "base64"

key = Base64.decode64("YOUR_BASE64_KEY")
public_key = RbNaCl::PublicKey.new(key)

box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
encrypted_secret = box.encrypt("YOUR_SECRET")

# Print the base64 encoded secret
puts Base64.strict_encode64(encrypted_secret)
```


---

<!-- source: https://docs.github.com/en/rest/guides -->

---
title: Guides
intro: 'Learn about getting started with the REST API, authentication, and how to use the REST API for a variety of tasks.'
redirect_from:
  - /guides
  - /v3/guides
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /scripting-with-the-rest-api-and-javascript
  - /scripting-with-the-rest-api-and-ruby
  - /discovering-resources-for-a-user
  - /delivering-deployments
  - /rendering-data-as-graphs
  - /working-with-comments
  - /building-a-ci-server
  - /using-the-rest-api-to-interact-with-your-git-database
  - /using-the-rest-api-to-interact-with-checks
  - /encrypting-secrets-for-the-rest-api
---
This section of the documentation is intended to get you up-and-running with
real-world {% data variables.product.github %} API applications. We'll go over everything you need to know, from authentication to results manipulation to integrating results with other apps.
Every tutorial will include a project, and each project will be saved and documented in our public
[platform-samples](https://github.com/github/platform-samples) repository.


---

<!-- source: https://docs.github.com/en/rest/guides/rendering-data-as-graphs -->

---
title: Rendering data as graphs
intro: Learn how to visualize the programming languages from your repository using the D3.js library and Ruby Octokit.
redirect_from:
  - /guides/rendering-data-as-graphs
  - /v3/guides/rendering-data-as-graphs
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Build apps and integrations
---



In this guide, we're going to use the API to fetch information about repositories
that we own, and the programming languages that make them up. Then, we'll
visualize that information in a couple of different ways using the [D3.js](https://d3js.org/) library. To
interact with the {% data variables.product.github %} API, we'll be using the excellent Ruby library, [Octokit](https://github.com/octokit/octokit.rb).

If you haven't already, you should read the [Basics of Authentication](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app)
guide before starting this example. You can find the complete source code for this project in the [platform-samples](https://github.com/github/platform-samples/tree/master/api/ruby/rendering-data-as-graphs) repository.

Let's jump right in!

## Setting up an {% data variables.product.prodname_oauth_app %}

First, [register a new application](https://github.com/settings/applications/new) on {% data variables.product.github %}. Set the main and callback
URLs to `http://localhost:4567/`. As [before](/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app), we're going to handle authentication for the API by
implementing a Rack middleware using [sinatra-auth-github](https://rubygems.org/gems/sinatra_auth_github):

``` ruby
require 'sinatra/auth/github'

module Example
  class MyGraphApp < Sinatra::Base
    # !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
    # Instead, set and test environment variables, like below
    # if ENV['GITHUB_CLIENT_ID'] && ENV['GITHUB_CLIENT_SECRET']
    #  CLIENT_ID        = ENV['GITHUB_CLIENT_ID']
    #  CLIENT_SECRET    = ENV['GITHUB_CLIENT_SECRET']
    # end

    CLIENT_ID = ENV['GH_GRAPH_CLIENT_ID']
    CLIENT_SECRET = ENV['GH_GRAPH_SECRET_ID']

    enable :sessions

    set :github_options, {
      :scopes    => "repo",
      :secret    => CLIENT_SECRET,
      :client_id => CLIENT_ID,
      :callback_url => "/"
    }

    register Sinatra::Auth::Github

    get '/' do
      if !authenticated?
        authenticate!
      else
        access_token = github_user["token"]
      end
    end
  end
end
```

Set up a similar _config.ru_ file as in the previous example:

``` ruby
ENV['RACK_ENV'] ||= 'development'
require "rubygems"
require "bundler/setup"

require File.expand_path(File.join(File.dirname(__FILE__), 'server'))

run Example::MyGraphApp
```

## Fetching repository information

This time, in order to talk to the {% data variables.product.github %} API, we're going to use the [Octokit
Ruby library](https://github.com/octokit/octokit.rb). This is much easier than directly making a bunch of
REST calls. Plus, Octokit was developed by a GitHubber, and is actively maintained,
so you know it'll work.

Authentication with the API via Octokit is easy. Just pass your login
and token to the `Octokit::Client` constructor:

``` ruby
if !authenticated?
  authenticate!
else
  octokit_client = Octokit::Client.new(:login => github_user.login, :oauth_token => github_user.token)
end
```

Let's do something interesting with the data about our repositories. We're going
to see the different programming languages they use, and count which ones are used
most often. To do that, we'll first need a list of our repositories from the API.
With Octokit, that looks like this:

``` ruby
repos = client.repositories
```

Next, we'll iterate over each repository, and count the language that {% data variables.product.github %}
associates with it:

``` ruby
language_obj = {}
repos.each do |repo|
  # sometimes language can be nil
  if repo.language
    if !language_obj[repo.language]
      language_obj[repo.language] = 1
    else
      language_obj[repo.language] += 1
    end
  end
end

languages.to_s
```

When you restart your server, your web page should display something
that looks like this:

``` ruby
{"JavaScript"=>13, "PHP"=>1, "Perl"=>1, "CoffeeScript"=>2, "Python"=>1, "Java"=>3, "Ruby"=>3, "Go"=>1, "C++"=>1}
```

So far, so good, but not very human-friendly. A visualization
would be great in helping us understand how these language counts are distributed. Let's feed
our counts into D3 to get a neat bar graph representing the popularity of the languages we use.

## Visualizing language counts

D3.js, or just D3, is a comprehensive library for creating many kinds of charts, graphs, and interactive visualizations.
Using D3 in detail is beyond the scope of this guide, but for a good introductory article,
check out [D3 for Mortals](http://recursion.org/d3-for-mere-mortals/).

D3 is a JavaScript library, and likes working with data as arrays. So, let's convert our Ruby hash into
a JSON array for use by JavaScript in the browser.

``` ruby
languages = []
language_obj.each do |lang, count|
  languages.push :language => lang, :count => count
end

erb :lang_freq, :locals => { :languages => languages.to_json}
```

We're simply iterating over each key-value pair in our object and pushing them into
a new array. The reason we didn't do this earlier is because we didn't want to iterate
over our `language_obj` object while we were creating it.

Now, _lang_freq.erb_ is going to need some JavaScript to support rendering a bar graph.
For now, you can just use the code provided here, and refer to the resources linked above
if you want to learn more about how D3 works:

``` html
<!DOCTYPE html>
<meta charset="utf-8">
<html>
  <head>
    <script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.0.1/d3.v3.min.js"></script>
    <style>
    svg {
      padding: 20px;
    }
    rect {
      fill: #2d578b
    }
    text {
      fill: white;
    }
    text.yAxis {
      font-size: 12px;
      font-family: Helvetica, sans-serif;
      fill: black;
    }
    </style>
  </head>
  <body>
    <p>Check this sweet data out:</p>
    <div id="lang_freq"></div>

  </body>
  <script>
    var data = <%= languages %>;

    var barWidth = 40;
    var width = (barWidth + 10) * data.length;
    var height = 300;

    var x = d3.scale.linear().domain([0, data.length]).range([0, width]);
    var y = d3.scale.linear().domain([0, d3.max(data, function(datum) { return datum.count; })]).
      rangeRound([0, height]);

    // add the canvas to the DOM
    var languageBars = d3.select("#lang_freq").
      append("svg:svg").
      attr("width", width).
      attr("height", height);

    languageBars.selectAll("rect").
      data(data).
      enter().
      append("svg:rect").
      attr("x", function(datum, index) { return x(index); }).
      attr("y", function(datum) { return height - y(datum.count); }).
      attr("height", function(datum) { return y(datum.count); }).
      attr("width", barWidth);

    languageBars.selectAll("text").
      data(data).
      enter().
      append("svg:text").
      attr("x", function(datum, index) { return x(index) + barWidth; }).
      attr("y", function(datum) { return height - y(datum.count); }).
      attr("dx", -barWidth/2).
      attr("dy", "1.2em").
      attr("text-anchor", "middle").
      text(function(datum) { return datum.count;});

    languageBars.selectAll("text.yAxis").
      data(data).
      enter().append("svg:text").
      attr("x", function(datum, index) { return x(index) + barWidth; }).
      attr("y", height).
      attr("dx", -barWidth/2).
      attr("text-anchor", "middle").
      text(function(datum) { return datum.language;}).
      attr("transform", "translate(0, 18)").
      attr("class", "yAxis");
  </script>
</html>
```

Phew! Again, don't worry about what most of this code is doing. The relevant part
here is a line way at the top--`var data = <%= languages %>;`--which indicates
that we're passing our previously created `languages` array into ERB for manipulation.

As the "D3 for Mortals" guide suggests, this isn't necessarily the best use of
D3. But it does serve to illustrate how you can use the library, along with Octokit,
to make some really amazing things.

## Combining different API calls

Now it's time for a confession: the `language` attribute within repositories
only identifies the "primary" language defined. That means that if you have
a repository that combines several languages, the one with the most bytes of code
is considered to be the primary language.

Let's combine a few API calls to get a _true_ representation of which language
has the greatest number of bytes written across all our code. A [treemap](https://www.d3-graph-gallery.com/treemap.html)
should be a great way to visualize the sizes of our coding languages used, rather
than simply the count. We'll need to construct an array of objects that looks
something like this:

``` json
[ { "name": "language1", "size": 100},
  { "name": "language2", "size": 23}
  ...
]
```

Since we already have a list of repositories above, let's inspect each one, and
call the [GET /repos/{owner}/{repo}/languages endpoint](/rest/repos/repos#list-repository-languages):

``` ruby
repos.each do |repo|
  repo_name = repo.name
  repo_langs = octokit_client.languages("#{github_user.login}/#{repo_name}")
end
```

From there, we'll cumulatively add each language found to a list of languages:

``` ruby
repo_langs.each do |lang, count|
  if !language_obj[lang]
    language_obj[lang] = count
  else
    language_obj[lang] += count
  end
end
```

After that, we'll format the contents into a structure that D3 understands:

``` ruby
language_obj.each do |lang, count|
  language_byte_count.push :name => "#{lang} (#{count})", :count => count
end

# some mandatory formatting for D3
language_bytes = [ :name => "language_bytes", :elements => language_byte_count]
```

(For more information on D3 tree map magic, check out [this simple tutorial](/rest/repos/repos#list-repository-languages).)

To wrap up, we pass this JSON information over to the same ERB template:

``` ruby
erb :lang_freq, :locals => { :languages => languages.to_json, :language_byte_count => language_bytes.to_json}
```

Like before, here's a bunch of JavaScript that you can drop
directly into your template:

``` html
<div id="byte_freq"></div>
<script>
  var language_bytes = <%= language_byte_count %>
  var childrenFunction = function(d){return d.elements};
  var sizeFunction = function(d){return d.count;};
  var colorFunction = function(d){return Math.floor(Math.random()*20)};
  var nameFunction = function(d){return d.name;};

  var color = d3.scale.linear()
              .domain([0,10,15,20])
              .range(["grey","green","yellow","red"]);

  drawTreemap(5000, 2000, '#byte_freq', language_bytes, childrenFunction, nameFunction, sizeFunction, colorFunction, color);

  function drawTreemap(height,width,elementSelector,language_bytes,childrenFunction,nameFunction,sizeFunction,colorFunction,colorScale){

      var treemap = d3.layout.treemap()
          .children(childrenFunction)
          .size([width,height])
          .value(sizeFunction);

      var div = d3.select(elementSelector)
          .append("div")
          .style("position","relative")
          .style("width",width + "px")
          .style("height",height + "px");

      div.data(language_bytes).selectAll("div")
          .data(function(d){return treemap.nodes(d);})
          .enter()
          .append("div")
          .attr("class","cell")
          .style("background",function(d){ return colorScale(colorFunction(d));})
          .call(cell)
          .text(nameFunction);
  }

  function cell(){
      this
          .style("left",function(d){return d.x + "px";})
          .style("top",function(d){return d.y + "px";})
          .style("width",function(d){return d.dx - 1 + "px";})
          .style("height",function(d){return d.dy - 1 + "px";});
  }
</script>
```

Et voila! Beautiful rectangles containing your repo languages, with relative
proportions that are easy to see at a glance. You might need to
tweak the height and width of your treemap, passed as the first two
arguments to `drawTreemap` above, to get all the information to show up properly.


---

<!-- source: https://docs.github.com/en/rest/guides/scripting-with-the-rest-api-and-javascript -->

---
title: Scripting with the REST API and JavaScript
shortTitle: Script with JavaScript
intro: Write a script using the Octokit.js SDK to interact with the REST API.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Build apps and integrations
contentType: tutorials
---

## About Octokit.js

If you want to write a script using JavaScript to interact with {% data variables.product.company_short %}'s REST API, {% data variables.product.company_short %} recommends that you use the Octokit.js SDK. Octokit.js is maintained by {% data variables.product.company_short %}. The SDK implements best practices and makes it easier for you to interact with the REST API via JavaScript. Octokit.js works with all modern browsers, Node.js, and Deno. For more information about Octokit.js, see [the Octokit.js README](https://github.com/octokit/octokit.js/#readme).

## Prerequisites

This guide assumes that you are familiar with JavaScript and the {% data variables.product.company_short %} REST API. For more information about the REST API, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api).

You must install and import `octokit` in order to use the Octokit.js library. This guide uses import statements in accordance with ES6. For more information about different installation and import methods, see [the Octokit.js README's Usage section](https://github.com/octokit/octokit.js/#usage).

## Instantiating and authenticating

> [!WARNING]
> Treat your authentication credentials like a password.
>
> To keep your credentials secure, you can store your credentials as a secret and run your script through {% data variables.product.prodname_actions %}. For more information, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).
{% ifversion ghec or fpt %}
>
> You can also store your credentials as a {% data variables.product.prodname_codespaces %} secret and run your script in {% data variables.product.prodname_codespaces %}. For more information, see [AUTOTITLE](/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces).
{% endif %}
>
> If {% ifversion ghec or fpt %}these options are not possible{% else %}this is not possible{% endif %}, consider using another CLI service to store your credentials securely.

### Authenticating with a {% data variables.product.pat_generic %}

If you want to use the {% data variables.product.company_short %} REST API for personal use, you can create a {% data variables.product.pat_generic %}. For more information about creating a {% data variables.product.pat_generic %}, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

First, import `Octokit` from `octokit`. Then, pass your {% data variables.product.pat_generic %} when you create an instance of `Octokit`. In the following example, replace `YOUR-TOKEN` with a reference to your {% data variables.product.pat_generic %}.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %}

```javascript copy
import { Octokit } from "octokit";

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",{% endif %}
  auth: 'YOUR-TOKEN',
});
```

### Authenticating with a {% data variables.product.prodname_github_app %}

If you want to use the API on behalf of an organization or another user, {% data variables.product.company_short %} recommends that you use a {% data variables.product.prodname_github_app %}. If an endpoint is available to {% data variables.product.prodname_github_apps %}, the REST reference documentation for that endpoint will indicate what type of {% data variables.product.prodname_github_app %} token is required. For more information, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app) and [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app).

Instead of importing `Octokit` from `octokit`, import `App`. In the following example, replace `APP_ID` with a reference to your app's ID. Replace `PRIVATE_KEY` with a reference to your app's private key. Replace `INSTALLATION_ID` with the ID of the installation of your app that you want to authenticate on behalf of. You can find your app's ID and generate a private key on the settings page for your app. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps). You can get an installation ID with the `GET /users/{username}/installation`, `GET /repos/{owner}/{repo}/installation`, or `GET /orgs/{org}/installation` endpoints. For more information, see [AUTOTITLE](/rest/apps/apps).{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %}

```javascript copy
import { App } from "octokit";

const app = new App({
  appId: APP_ID,
  privateKey: PRIVATE_KEY,{% ifversion ghes %}
  Octokit: Octokit.defaults({
    baseUrl: "{% data variables.product.rest_url %}",
  }),{% endif %}
});

const octokit = await app.getInstallationOctokit(INSTALLATION_ID);
```

### Authenticating in {% data variables.product.prodname_actions %}

If you want to use the API in a {% data variables.product.prodname_actions %} workflow, {% data variables.product.company_short %} recommends that you authenticate with the built-in `GITHUB_TOKEN` instead of creating a token. You can grant permissions to the `GITHUB_TOKEN` with the `permissions` key. For more information about `GITHUB_TOKEN`, see [AUTOTITLE](/actions/concepts/security/github_token).

If your workflow needs to access resources outside of the workflow's repository, then you will not be able to use `GITHUB_TOKEN`. In that case, store your credentials as a secret and replace `GITHUB_TOKEN` in the examples below with the name of your secret. For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).

If you use the `run` keyword to execute your JavaScript script in your {% data variables.product.prodname_actions %} workflows, you can store the value of `GITHUB_TOKEN` as an environment variable. Your script can access the environment variable as `process.env.VARIABLE_NAME`.

For example, this workflow step stores `GITHUB_TOKEN` in an environment variable called `TOKEN`:

```yaml
- name: Run script
  env:
    TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
  run: |
    node .github/actions-scripts/use-the-api.mjs
```

The script that the workflow runs uses `process.env.TOKEN` to authenticate:

```javascript copy
import { Octokit } from "octokit";

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",{% endif %}
  auth: process.env.TOKEN,
});
```

### Instantiating without authentication

You can use the REST API without authentication, although you will have a lower rate limit and will not be able to use some endpoints. To create an instance of `Octokit` without authenticating, do not pass the `auth` argument.{% ifversion ghes %} Set the base URL to `{% data variables.product.rest_url %}`. Replace `[hostname]` with the name of {% data variables.location.product_location %}.{% endif %}

```javascript copy
import { Octokit } from "octokit";

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",
{% endif %}});
```

## Making requests

Octokit supports multiple ways of making requests. You can use the `request` method to make requests if you know the HTTP verb and path for the endpoint. You can use the `rest` method if you want to take advantage of autocompletion in your IDE and typing. For paginated endpoints, you can use the `paginate` method to request multiple pages of data.

### Using the `request` method to make requests

To use the `request` method to make requests, pass the HTTP method and path as the first argument. Pass any body, query, or path parameters in an object as the second argument. For example, to make a `GET` request to `/repos/{owner}/{repo}/issues` and pass the `owner`, `repo`, and `per_page` parameters:

```javascript copy
await octokit.request("GET /repos/{owner}/{repo}/issues", {
  owner: "github",
  repo: "docs",
  per_page: 2
});
```

The `request` method automatically passes the `Accept: application/vnd.github+json` header. To pass additional headers or a different `Accept` header, add a `headers` property to the object that is passed as a second argument. The value of the `headers` property is an object with the header names as keys and header values as values. For example, to send a `content-type` header with a value of `text/plain` and a `x-github-api-version` header with a value of `{{ allVersions[currentVersion].latestApiVersion }}`:

```javascript copy
await octokit.request("POST /markdown/raw", {
  text: "Hello **world**",
  headers: {
    "content-type": "text/plain",
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});
```

### Using `rest` endpoint methods to make requests

Every REST API endpoint has an associated `rest` endpoint method in Octokit. These methods generally autocomplete in your IDE for convenience. You can pass any parameters as an object to the method.

```javascript copy
await octokit.rest.issues.listForRepo({
  owner: "github",
  repo: "docs",
  per_page: 2
});
```

Additionally, if you are using a typed language such as TypeScript, you can import types to use with these methods. For more information, see [the TypeScript section in the plugin-rest-endpoint-methods.js README](https://github.com/octokit/plugin-rest-endpoint-methods.js/#typescript).

### Making paginated requests

If the endpoint is paginated and you want to fetch more than one page of results, you can use the `paginate` method. `paginate` will fetch the next page of results until it reaches the last page and then return all of the results as a single array. A few endpoints return paginated results as array in an object, as opposed to returning the paginated results as an array. `paginate` always returns an array of items even if the raw result was an object.

For example, the following example gets all of the issues from the `github/docs` repository. Although it requests 100 issues at a time, the function won't return until the last page of data is reached.

```javascript copy
const issueData = await octokit.paginate("GET /repos/{owner}/{repo}/issues", {
  owner: "github",
  repo: "docs",
  per_page: 100,
  headers: {
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});
```

The `paginate` method accepts an optional map function, which you can use to collect only the data that you want from the response. This reduces memory usage by your script. The map function can take a second argument, `done`, which you can call to end the pagination before the last page is reached. This lets you fetch a subset of pages. For example, the following example continues to fetch results until an issue that includes "test" in the title is returned. For the pages of data that were returned, only the issue title and author are stored.

```javascript copy
const issueData = await octokit.paginate("GET /repos/{owner}/{repo}/issues", {
  owner: "github",
  repo: "docs",
  per_page: 100,
  headers: {
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
},
    (response, done) => response.data.map((issue) => {
    if (issue.title.includes("test")) {
      done()
    }
    return ({title: issue.title, author: issue.user.login})
  })
);
```

Instead of fetching all of the results at once, you can use `octokit.paginate.iterator()` to iterate through a single page at a time. For example, the following example fetches one page of results at a time and processes each object from the page before fetching the next page. Once an issue that includes "test" in the title is reached, the script stops the iteration and returns the issue title and issue author of each object that was processed. The iterator is the most memory efficient method for fetching paginated data.

```javascript copy
const iterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/issues", {
  owner: "github",
  repo: "docs",
  per_page: 100,
  headers: {
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});

let issueData = []
let breakLoop = false
for await (const {data} of iterator) {
  if (breakLoop) break
  for (const issue of data) {
    if (issue.title.includes("test")) {
      breakLoop = true
      break
    } else {
      issueData = [...issueData, {title: issue.title, author: issue.user.login}];
    }
  }
}
```

You can use the `paginate` method with the `rest` endpoint methods as well. Pass the `rest` endpoint method as the first argument. Pass any parameters as the second argument.

```javascript copy
const iterator = octokit.paginate.iterator(octokit.rest.issues.listForRepo, {
  owner: "github",
  repo: "docs",
  per_page: 100,
  headers: {
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});
```

For more information about pagination, see [AUTOTITLE](/rest/guides/using-pagination-in-the-rest-api).

## Catching errors

### Catching all errors

Sometimes, the {% data variables.product.company_short %} REST API will return an error. For example, you will get an error if your access token is expired or if you omitted a required parameter. Octokit.js automatically retries the request when it gets an error other than `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, and `422 Unprocessable Entity`. If an API error occurs even after retries, Octokit.js throws an error that includes the HTTP status code of the response (`response.status`) and the response headers (`response.headers`). You should handle these errors in your code. For example, you can use a try/catch block to catch errors:

```javascript copy
let filesChanged = []

try {
  const iterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", {
    owner: "github",
    repo: "docs",
    pull_number: 22809,
    per_page: 100,
    headers: {
      "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
    },
  });

  for await (const {data} of iterator) {
    filesChanged = [...filesChanged, ...data.map(fileData => fileData.filename)];
  }
} catch (error) {
  if (error.response) {
    console.error(`Error! Status: ${error.response.status}. Message: ${error.response.data.message}`)
  }
  console.error(error)
}
```

### Handling intended error codes

Sometimes, {% data variables.product.company_short %} uses a 4xx status code to indicate a non-error response. If the endpoint you are using does this, you can add additional handling for specific errors. For example, the `GET /user/starred/{owner}/{repo}` endpoint will return a `404` if the repository is not starred. The following example uses the `404` response to indicate that the repository was not starred; all other errors codes are treated as errors.

```javascript copy
try {
  await octokit.request("GET /user/starred/{owner}/{repo}", {
    owner: "github",
    repo: "docs",
    headers: {
      "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
    },
  });

  console.log(`The repository is starred by me`);

} catch (error) {
  if (error.status === 404) {
    console.log(`The repository is not starred by me`);
  } else {
    console.error(`An error occurred while checking if the repository is starred: ${error?.response?.data?.message}`);
  }
}
```

### Handling rate limit errors

If you receive a rate limit error, you may want to retry your request after waiting. When you are rate limited, {% data variables.product.company_short %} responds with a `403 Forbidden` error and the `x-ratelimit-remaining` response header value will be `"0"`. The response headers will include a `x-ratelimit-reset` header, which tells you the time at which the current rate limit window resets, in UTC epoch seconds. You can retry your request after the time specified by `x-ratelimit-reset`.

```javascript copy
async function requestRetry(route, parameters) {
  try {
    const response = await octokit.request(route, parameters);
    return response
  } catch (error) {
    if (error.response && error.status === 403 && error.response.headers['x-ratelimit-remaining'] === '0') {
      const resetTimeEpochSeconds = error.response.headers['x-ratelimit-reset'];
      const currentTimeEpochSeconds = Math.floor(Date.now() / 1000);
      const secondsToWait = resetTimeEpochSeconds - currentTimeEpochSeconds;
      console.log(`You have exceeded your rate limit. Retrying in ${secondsToWait} seconds.`);
      setTimeout(requestRetry, secondsToWait * 1000, route, parameters);
    } else {
      console.error(error);
    }
  }
}

const response = await requestRetry("GET /repos/{owner}/{repo}/issues", {
    owner: "github",
    repo: "docs",
    per_page: 2
  })
```

## Using the response

The `request` method returns a promise that resolves to an object if the request was successful. The object properties are `data` (the response body returned by the endpoint), `status` (the HTTP response code), `url` (the URL of the request), and `headers` (an object containing the response headers). Unless otherwise specified, the response body is in JSON format. Some endpoints do not return a response body; in those cases, the `data` property is omitted.

```javascript copy
const response = await octokit.request("GET /repos/{owner}/{repo}/issues/{issue_number}", {
  owner: "github",
  repo: "docs",
  issue_number: 11901,
  headers: {
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});

console.log(`The status of the response is: ${response.status}`)
console.log(`The request URL was: ${response.url}`)
console.log(`The x-ratelimit-remaining response header is: ${response.headers["x-ratelimit-remaining"]}`)
console.log(`The issue title is: ${response.data.title}`)
```

Similarly, the `paginate` method returns a promise. If the request was successful, the promise resolves to an array of data returned by the endpoint. Unlike the `request` method, the `paginate` method does not return the status code, URL, or headers.

```javascript copy
const data = await octokit.paginate("GET /repos/{owner}/{repo}/issues", {
  owner: "github",
  repo: "docs",
  per_page: 100,
  headers: {
    "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});

console.log(`${data.length} issues were returned`)
console.log(`The title of the first issue is: ${data[0].title}`)
```

## Example script

Here is a full example script that uses Octokit.js. The script imports `Octokit` and creates a new instance of `Octokit`. If you wanted to authenticate with a {% data variables.product.prodname_github_app %} instead of a {% data variables.product.pat_generic %}, you would import and instantiate `App` instead of `Octokit`. For more information, see [Authenticating with a {% data variables.product.prodname_github_app %}](#authenticating-with-a-github-app).

The `getChangedFiles` function gets all of the files changed for a pull request. The `commentIfDataFilesChanged` function calls the `getChangedFiles` function. If any of the files that the pull request changed include `/data/` in the file path, then the function will comment on the pull request.

```javascript copy
import { Octokit } from "octokit";

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",{% endif %}
  auth: 'YOUR-TOKEN',
});

async function getChangedFiles({owner, repo, pullNumber}) {
  let filesChanged = []

  try {
    const iterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", {
      owner: owner,
      repo: repo,
      pull_number: pullNumber,
      per_page: 100,
      headers: {
        "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
      },
    });

    for await (const {data} of iterator) {
      filesChanged = [...filesChanged, ...data.map(fileData => fileData.filename)];
    }
  } catch (error) {
    if (error.response) {
      console.error(`Error! Status: ${error.response.status}. Message: ${error.response.data.message}`)
    }
    console.error(error)
  }

  return filesChanged
}

async function commentIfDataFilesChanged({owner, repo, pullNumber}) {
  const changedFiles = await getChangedFiles({owner, repo, pullNumber});

  const filePathRegex = new RegExp(/\/data\//, "i");
  if (!changedFiles.some(fileName => filePathRegex.test(fileName))) {
    return;
  }

  try {
    const {data: comment} = await octokit.request("POST /repos/{owner}/{repo}/issues/{issue_number}/comments", {
      owner: owner,
      repo: repo,
      issue_number: pullNumber,
      body: `It looks like you changed a data file. These files are auto-generated. \n\nYou must revert any changes to data files before your pull request will be reviewed.`,
      headers: {
        "x-github-api-version": "{{ allVersions[currentVersion].latestApiVersion }}",
      },
    });

    return comment.html_url;
  } catch (error) {
    if (error.response) {
      console.error(`Error! Status: ${error.response.status}. Message: ${error.response.data.message}`)
    }
    console.error(error)
  }
}

await commentIfDataFilesChanged({owner: "github", repo: "docs", pullNumber: 191});
```

## Next steps

* To learn more about Octokit.js see [the Octokit.js documentation](https://github.com/octokit/octokit.js/#readme).
* For some real life examples, look at how {% data variables.product.company_short %} Docs uses Octokit.js by [searching the {% data variables.product.company_short %} Docs repository](https://github.com/search?q=repo%3Agithub%2Fdocs%20path%3A.github%20octokit&type=code).


---

<!-- source: https://docs.github.com/en/rest/guides/scripting-with-the-rest-api-and-ruby -->

---
title: Scripting with the REST API and Ruby
shortTitle: Script with Ruby
intro: Learn how to write a script using the Octokit.rb SDK to interact with the REST API.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Build apps and integrations
contentType: tutorials
---

## About Octokit.rb

If you want to write a script using Ruby to interact with the {% data variables.product.company_short %} REST API, {% data variables.product.company_short %} recommends that you use the Octokit.rb SDK. Octokit.rb is maintained by {% data variables.product.company_short %}. The SDK implements best practices and makes it easier for you to interact with the REST API via Ruby. Octokit.rb works with all modern browsers, Node.rb, and Deno. For more information about Octokit.rb, see [the Octokit.rb README](https://github.com/octokit/octokit.rb/#readme).

## Prerequisites

This guide assumes that you are familiar with Ruby and the {% data variables.product.company_short %} REST API. For more information about the REST API, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api).

You must install and import the `octokit` gem in order to use the Octokit.rb library. This guide uses import statements in accordance with Ruby's conventions. For more information about different installation methods, see [the Octokit.rb README's Installation section](https://github.com/octokit/octokit.rb/#installation).

## Instantiating and authenticating

> [!WARNING]
> Treat your authentication credentials like a password.
>
> To keep your credentials secure, you can store your credentials as a secret and run your script through {% data variables.product.prodname_actions %}. For more information, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).
{% ifversion ghec or fpt %}
>
> You can also store your credentials as a {% data variables.product.prodname_codespaces %} secret and run your script in {% data variables.product.prodname_codespaces %}. For more information, see [AUTOTITLE](/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces).
{% endif %}
>
> If {% ifversion ghec or fpt %}these options are not possible{% else %}this is not possible{% endif %}, consider using another CLI service to store your credentials securely.

### Authenticating with a {% data variables.product.pat_generic %}

If you want to use the {% data variables.product.company_short %} REST API for personal use, you can create a {% data variables.product.pat_generic %}. For more information about creating a {% data variables.product.pat_generic %}, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

First, require the `octokit` library. Then, create an instance of `Octokit` by passing your {% data variables.product.pat_generic %} as the `access_token` option. In the following example, replace `YOUR-TOKEN` with your {% data variables.product.pat_generic %}.

```ruby copy
require 'octokit'

octokit = Octokit::Client.new(access_token: 'YOUR-TOKEN')
```

### Authenticating with a {% data variables.product.prodname_github_app %}

If you want to use the API on behalf of an organization or another user, {% data variables.product.company_short %} recommends that you use a {% data variables.product.prodname_github_app %}. If an endpoint is available to {% data variables.product.prodname_github_apps %}, the REST reference documentation for that endpoint will indicate what type of {% data variables.product.prodname_github_app %} token is required. For more information, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app) and [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app).

Instead of requiring `octokit`, create an instance of `Octokit::Client` by passing your {% data variables.product.prodname_github_app %}'s information as options. In the following example, replace `APP_ID` with your app's ID, `PRIVATE_KEY` with your app's private key, and `INSTALLATION_ID` with the ID of the installation of your app that you want to authenticate on behalf of. You can find your app's ID and generate a private key on the settings page for your app. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps). You can get an installation ID with the `GET /users/{username}/installation`, `GET /repos/{owner}/{repo}/installation`, or `GET /orgs/{org}/installation` endpoints. For more information, see [AUTOTITLE](/rest/apps/apps).{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %}

```ruby copy
require 'octokit'

app = Octokit::Client.new(
  client_id: APP_ID,
  client_secret: PRIVATE_KEY,
  installation_id: INSTALLATION_ID
)

octokit = Octokit::Client.new(bearer_token: app.create_app_installation.access_token)
```

### Authenticating in {% data variables.product.prodname_actions %}

If you want to use the API in a {% data variables.product.prodname_actions %} workflow, {% data variables.product.company_short %} recommends that you authenticate with the built-in `GITHUB_TOKEN` instead of creating a token. You can grant permissions to the `GITHUB_TOKEN` with the `permissions` key. For more information about `GITHUB_TOKEN`, see [AUTOTITLE](/actions/concepts/security/github_token).

If your workflow needs to access resources outside of the workflow's repository, then you will not be able to use `GITHUB_TOKEN`. In that case, store your credentials as a secret and replace `GITHUB_TOKEN` in the examples below with the name of your secret. For more information about secrets, see [AUTOTITLE](/actions/security-guides/using-secrets-in-github-actions).

If you use the `run` keyword to execute your Ruby script in your {% data variables.product.prodname_actions %} workflows, you can store the value of `GITHUB_TOKEN` as an environment variable. Your script can access the environment variable as `ENV['VARIABLE_NAME']`.

For example, this workflow step stores `GITHUB_TOKEN` in an environment variable called `TOKEN`:

```yaml
- name: Run script
  env:
    TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
  run: |
    ruby .github/actions-scripts/use-the-api.rb
```

The script that the workflow runs uses `ENV['TOKEN']` to authenticate:

```ruby copy
require 'octokit'

octokit = Octokit::Client.new(access_token: ENV['TOKEN'])
```

### Instantiating without authentication

You can use the REST API without authentication, although you will have a lower rate limit and will not be able to use some endpoints. To create an instance of `Octokit` without authenticating, do not pass the `access_token` option.

```ruby copy
require 'octokit'

octokit = Octokit::Client.new
```

## Making requests

Octokit supports multiple ways of making requests. You can use the `request` method to make requests if you know the HTTP verb and path for the endpoint. You can use the `rest` method if you want to take advantage of autocompletion in your IDE and typing. For paginated endpoints, you can use the `paginate` method to request multiple pages of data.

### Using the `request` method to make requests

To use the `request` method to make requests, pass the HTTP method and path as the first argument. Pass any body, query, or path parameters in a hash as the second argument. For example, to make a `GET` request to `/repos/{owner}/{repo}/issues` and pass the `owner`, `repo`, and `per_page` parameters:

```ruby copy
octokit.request("GET /repos/{owner}/{repo}/issues", owner: "github", repo: "docs", per_page: 2)
```

The `request` method automatically passes the `Accept: application/vnd.github+json` header. To pass additional headers or a different `Accept` header, add a `headers` option to the hash that is passed as a second argument. The value of the `headers` option is a hash with the header names as keys and header values as values. For example, to send a `content-type` header with a value of `text/plain`:

```ruby copy
octokit.request("POST /markdown/raw", text: "Hello **world**", headers: { "content-type" => "text/plain" })
```

### Using `rest` endpoint methods to make requests

Every REST API endpoint has an associated `rest` endpoint method in Octokit. These methods generally autocomplete in your IDE for convenience. You can pass any parameters as a hash to the method.

```ruby copy
octokit.rest.issues.list_for_repo(owner: "github", repo: "docs", per_page: 2)
```

### Making paginated requests

If the endpoint is paginated and you want to fetch more than one page of results, you can use the `paginate` method. `paginate` will fetch the next page of results until it reaches the last page and then return all of the results as an array. A few endpoints return paginated results as an array in an object, as opposed to returning the paginated results as an array. `paginate` always returns an array of items even if the raw result was an object.

For example, the following example gets all of the issues from the `github/docs` repository. Although it requests 100 issues at a time, the function won't return until the last page of data is reached.

```ruby copy
issue_data = octokit.paginate("GET /repos/{owner}/{repo}/issues", owner: "github", repo: "docs", per_page: 100)
```

The `paginate` method accepts an optional block, which you can use to process each page of results. This allows you to collect only the data that you want from the response. For example, the following example continues to fetch results until an issue that includes "test" in the title is returned. For the pages of data that were returned, only the issue title and author are stored.

```ruby copy
issue_data = octokit.paginate("GET /repos/{owner}/{repo}/issues", owner: "github", repo: "docs", per_page: 100) do |response, done|
  response.data.map do |issue|
    if issue.title.include?("test")
      done.call
    end
    { title: issue.title, author: issue.user.login }
  end
end
```

Instead of fetching all of the results at once, you can use `octokit.paginate.iterator()` to iterate through a single page at a time. For example, the following example fetches one page of results at a time and processes each object from the page before fetching the next page. Once an issue that includes "test" in the title is reached, the script stops the iteration and returns the issue title and issue author of each object that was processed. The iterator is the most memory-efficient method for fetching paginated data.

```ruby copy
iterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/issues", owner: "github", repo: "docs", per_page: 100)
issue_data = []
break_loop = false
iterator.each do |data|
  break if break_loop
  data.each do |issue|
    if issue.title.include?("test")
      break_loop = true
      break
    else
      issue_data << { title: issue.title, author: issue.user.login }
    end
  end
end
```

You can use the `paginate` method with the `rest` endpoint methods as well. Pass the `rest` endpoint method as the first argument and any parameters as the second argument.

```ruby copy
iterator = octokit.paginate.iterator(octokit.rest.issues.list_for_repo, owner: "github", repo: "docs", per_page: 100)
```

For more information about pagination, see [AUTOTITLE](/rest/guides/using-pagination-in-the-rest-api).

## Catching errors

### Catching all errors

Sometimes, the {% data variables.product.company_short %} REST API will return an error. For example, you will get an error if your access token is expired or if you omitted a required parameter. Octokit.rb automatically retries the request when it gets an error other than `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, and `422 Unprocessable Entity`. If an API error occurs even after retries, Octokit.rb throws an error that includes the HTTP status code of the response (`response.status`) and the response headers (`response.headers`). You should handle these errors in your code. For example, you can use a try/catch block to catch errors:

```ruby copy
begin
files_changed = []

iterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", owner: "github", repo: "docs", pull_number: 22809, per_page: 100)
iterator.each do | data |
    files_changed.concat(data.map {
      | file_data | file_data.filename
    })
  end
rescue Octokit::Error => error
if error.response
puts "Error! Status: #{error.response.status}. Message: #{error.response.data.message}"
end
puts error
end
```

### Handling intended error codes

Sometimes, {% data variables.product.company_short %} uses a 4xx status code to indicate a non-error response. If the endpoint you are using does this, you can add additional handling for specific errors. For example, the `GET /user/starred/{owner}/{repo}` endpoint will return a `404` if the repository is not starred. The following example uses the `404` response to indicate that the repository was not starred; all other error codes are treated as errors.

```ruby copy
begin
octokit.request("GET /user/starred/{owner}/{repo}", owner: "github", repo: "docs")
puts "The repository is starred by me"
rescue Octokit::NotFound => error
puts "The repository is not starred by me"
rescue Octokit::Error => error
puts "An error occurred while checking if the repository is starred: #{error&.response&.data&.message}"
end
```

### Handling rate limit errors

If you receive a rate limit error, you may want to retry your request after waiting. When you are rate limited, {% data variables.product.company_short %} responds with a `403 Forbidden` error, and the `x-ratelimit-remaining` response header value will be `"0"`. The response headers will include a `x-ratelimit-reset` header, which tells you the time at which the current rate limit window resets, in UTC epoch seconds. You can retry your request after the time specified by `x-ratelimit-reset`.

```ruby copy
def request_retry(route, parameters)
 begin
 response = octokit.request(route, parameters)
 return response
 rescue Octokit::RateLimitExceeded => error
 reset_time_epoch_seconds = error.response.headers['x-ratelimit-reset'].to_i
 current_time_epoch_seconds = Time.now.to_i
 seconds_to_wait = reset_time_epoch_seconds - current_time_epoch_seconds
 puts "You have exceeded your rate limit. Retrying in #{seconds_to_wait} seconds."
 sleep(seconds_to_wait)
 retry
 rescue Octokit::Error => error
 puts error
 end
 end

 response = request_retry("GET /repos/{owner}/{repo}/issues", owner: "github", repo: "docs", per_page: 2)
```

## Using the response

The `request` method returns a response object if the request was successful. The response object contains `data` (the response body returned by the endpoint), `status` (the HTTP response code), `url` (the URL of the request), and `headers` (a hash containing the response headers). Unless otherwise specified, the response body is in JSON format. Some endpoints do not return a response body; in those cases, the `data` property is omitted.

```ruby copy
response = octokit.request("GET /repos/{owner}/{repo}/issues/{issue_number}", owner: "github", repo: "docs", issue_number: 11901)
 puts "The status of the response is: #{response.status}"
 puts "The request URL was: #{response.url}"
 puts "The x-ratelimit-remaining response header is: #{response.headers['x-ratelimit-remaining']}"
 puts "The issue title is: #{response.data['title']}"
```

Similarly, the `paginate` method returns a response object. If the `request` was successful, the `response` object contains data, status, url, and headers.

```ruby copy
response = octokit.paginate("GET /repos/{owner}/{repo}/issues", owner: "github", repo: "docs", per_page: 100)
puts "#{response.data.length} issues were returned"
puts "The title of the first issue is: #{response.data[0]['title']}"
```

## Example script

Here is a full example script that uses Octokit.rb. The script imports ``Octokit`` and creates a new instance of `Octokit`. If you want to authenticate with a {% data variables.product.prodname_github_app %} instead of a {% data variables.product.pat_generic %}, you would import and instantiate `App` instead of `Octokit`. For more information, see [Authenticating with a {% data variables.product.prodname_github_app %}](#authenticating-with-a-github-app) in this guide.

The `get_changed_files` function gets all of the files changed for a pull request. The `comment_if_data_files_changed` function calls the `get_changed_files` function. If any of the files that the pull request changed include `/data/` in the file path, then the function will comment on the pull request.

```ruby copy
require "octokit"

 octokit = Octokit::Client.new(access_token: "YOUR-TOKEN")

 def get_changed_files(octokit, owner, repo, pull_number)
 files_changed = []

 begin
 iterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", owner: owner, repo: repo, pull_number: pull_number, per_page: 100)
 iterator.each do | data |
     files_changed.concat(data.map {
       | file_data | file_data.filename
     })
   end
 rescue Octokit::Error => error
 if error.response
 puts "Error! Status: #{error.response.status}. Message: #{error.response.data.message}"
 end
 puts error
 end

 files_changed
 end

 def comment_if_data_files_changed(octokit, owner, repo, pull_number)
 changed_files = get_changed_files(octokit, owner, repo, pull_number)

 if changed_files.any ? {
   | file_name | /\/data\//i.match ? (file_name)
 }
 begin
 comment = octokit.create_pull_request_review_comment(owner, repo, pull_number, "It looks like you changed a data file. These files are auto-generated. \n\nYou must revert any changes to data files before your pull request will be reviewed.")
 comment.html_url
 rescue Octokit::Error => error
 if error.response
 puts "Error! Status: #{error.response.status}. Message: #{error.response.data.message}"
 end
 puts error
 end
 end
 end

# Example usage
owner = "github"
repo = "docs"
pull_number = 22809
comment_url = comment_if_data_files_changed(octokit, owner, repo, pull_number)

puts "A comment was added to the pull request: #{comment_url}"
```

> [!NOTE]
> This is just a basic example. In practice, you may want to use error handling and conditional checks to handle various scenarios.

## Next steps

To learn more about working with the {% data variables.product.company_short %} REST API and Octokit.rb, explore the following resources:

* To learn more about Octokit.rb see [the Octokit.rb documentation](https://github.com/octokit/octokit.rb/#readme).
* To find detailed information about {% data variables.product.company_short %}'s available REST API endpoints, including their request and response structures, see the [AUTOTITLE](/rest).


---

<!-- source: https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-checks -->

---
title: Using the REST API to interact with checks
intro: 'You can use the REST API to build {% data variables.product.prodname_github_apps %} that run powerful checks against code changes in a repository. You can create apps that perform continuous integration, code linting, or code scanning services and provide detailed feedback on commits.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Get started - Checks
redirect_from:
  - /rest/guides/getting-started-with-the-checks-api
category:
  - Build apps and integrations
---

## Overview

Rather than binary pass/fail build statuses, {% data variables.product.prodname_github_apps %} can report rich statuses, annotate lines of code with detailed information, and re-run tests. REST API to manage checks is available exclusively to your GitHub Apps.

For an example of how to use the REST API with a {% data variables.product.prodname_github_app %}, see [AUTOTITLE](/apps/creating-github-apps/guides/creating-ci-tests-with-the-checks-api).

You can use statuses with [protected branches](/rest/repos#branches) to prevent people from merging pull requests prematurely. For more information, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging).

## About check suites

When someone pushes code to a repository, GitHub creates a check suite for the last commit. A check suite is a collection of the [check runs](/rest/checks#check-runs) created by a single GitHub App for a specific commit. Check suites summarize the status and conclusion of the check runs that a suite includes.

The `status` can be `queued`, `in_progress`, `requested`, `waiting`, `pending`, or `completed`. Only {% data variables.product.prodname_actions %} can set a status of `requested`, `waiting`, or `pending`.

If the status is `completed`, the conclusion can be any of the following:
* `action_required`
* `cancelled`
* `timed_out`
* `failure`
* `neutral`
* `skipped`
* `stale`
* `startup_failure`
* `success`

The check suite reports the highest priority check run `conclusion` in the check suite's `conclusion`. For example, if three check runs have conclusions of `timed_out`, `success`, and `neutral` the check suite conclusion will be `timed_out`.

By default, GitHub creates a check suite automatically when code is pushed to the repository. This default flow sends the `check_suite` event (with `requested` action) to all GitHub Apps that have the `checks:write` permission. When your GitHub App receives the `check_suite` event, it can create new check runs for the latest commit. GitHub automatically adds new check runs to the correct [check suite](/rest/checks#check-suites) based on the check run's repository and SHA.

If you don't want to use the default automatic flow, you can control when you create check suites. To change the default settings for the creation of check suites, use the [Update repository preferences for check suites](/rest/checks/suites#update-repository-preferences-for-check-suites) endpoint. All changes to the automatic flow settings are recorded in the audit log for the repository. If you have disabled the automatic flow, you can create a check suite using the [Create a check suite](/rest/checks/suites#create-a-check-suite) endpoint. You should continue to use the [Create a check run](/rest/checks/runs#create-a-check-run) endpoint to provide feedback on a commit.

{% data reusables.apps.checks-availability %}

To use the endpoints to manage check suites, the {% data variables.product.prodname_github_app %} must have the `checks:write` permission and can also subscribe to the [check_suite](/webhooks-and-events/webhooks/webhook-events-and-payloads#check_suite) webhook.

{% data reusables.shortdesc.authenticating_github_app %}

## About check runs

A check run is an individual test that is part of a check suite. Each run includes a status and conclusion.

The `status` can be `queued`, `in_progress`, `requested`, `waiting`, `pending`, or `completed`. Only {% data variables.product.prodname_actions %} can set a status of `requested`, `waiting`, or `pending`.

If the status is `completed`, the conclusion can be any of the following:
* `action_required`
* `cancelled`
* `timed_out`
* `failure`
* `neutral`
* `skipped`
* `success`

If a check run is in an incomplete state for more than 14 days, then the check run's `conclusion` becomes `stale` and appears on {% data variables.product.prodname_dotcom %} as stale with {% octicon "issue-reopened" aria-label="The issue-reopened icon" %}. Only {% data variables.product.prodname_dotcom %} can mark check runs as `stale`. For more information about possible conclusions of a check run, see the [`conclusion` parameter](/rest/checks#create-a-check-run--parameters).

As soon as you receive the [`check_suite`](/webhooks-and-events/webhooks/webhook-events-and-payloads#check_suite) webhook, you can create the check run, even if the check is not complete. You can update the `status` of the check run as it completes with the values `queued`, `in_progress`, or `completed`, and you can update the `output` as more details become available. A check run can contain timestamps, a link to more details on your external site, detailed annotations for specific lines of code, and information about the analysis performed.

Annotations add information from your check run to specific lines of code. Each annotation includes an `annotation_level` property, which can be `notice`, `warning`, or `failure`. The annotation also includes `path`, `start_line`, and `end_line` to specify what location the annotation refers to. The annotation includes a `message` to describe the result. For more information, see [AUTOTITLE](/rest/checks/runs).

A check can also be manually re-run in the GitHub UI. See [AUTOTITLE](/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks#checks) for more details. When this occurs, the {% data variables.product.prodname_github_app %} that created the check run will receive the [`check_run`](/webhooks-and-events/webhooks/webhook-events-and-payloads#check_run) webhook requesting a new check run. If you create a check run without creating a check suite, {% data variables.product.github %} creates the check suite for you automatically.

{% data reusables.apps.checks-availability %}

To use the endpoints to manage check runs, the {% data variables.product.prodname_github_app %} must have the `checks:write` permission and can also subscribe to the [check_run](/webhooks-and-events/webhooks/webhook-events-and-payloads#check_run) webhook.

## Check runs and requested actions

When you set up a check run with requested actions (not to be confused with {% data variables.product.prodname_actions %}), you can display a button in the pull request view on {% data variables.product.prodname_dotcom %} that allows people to request your {% data variables.product.prodname_github_app %} to perform additional tasks.

For example, a code linting app could use requested actions to display a button in a pull request to automatically fix detected syntax errors.

To create a button that can request additional actions from your app, use the [`actions` object](/rest/checks/runs#create-a-check-run--parameters) when you [Create a check run](/rest/checks#create-a-check-run). For example, the `actions` object below displays a button in the **Checks** tab of a pull request with the label "Fix this." The button appears after the check run completes.

```json
"actions": [{
  "label": "Fix this",
  "description": "Let us fix that for you",
  "identifier": "fix_errors"
}]
```

When a user clicks the button, {% data variables.product.prodname_dotcom %} sends the [`check_run.requested_action` webhook](/webhooks-and-events/webhooks/webhook-events-and-payloads#check_run) to your app. When your app receives a `check_run.requested_action` webhook event, it can look for the `requested_action.identifier` key in the webhook payload to determine which button was clicked and perform the requested task.

For a detailed example of how to set up requested actions with the REST API, see [AUTOTITLE](/apps/creating-github-apps/guides/creating-ci-tests-with-the-checks-api#part-2-creating-the-octo-rubocop-ci-test).

## Retention of checks data

{% data reusables.pull_requests.retention-checks-data %}


---

<!-- source: https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database -->

---
title: Using the REST API to interact with your Git database
intro: 'Use the REST API to read and write raw Git objects to your Git database on {% data variables.product.github %} and to list and update your references (branch heads and tags).'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Get started - Git database
redirect_from:
  - /rest/guides/getting-started-with-the-git-database-api
category:
  - Build apps and integrations
---

## Overview

This basically allows you to reimplement a lot of Git functionality with the REST API - by creating raw objects directly into the database and updating branch references you could technically do just about anything that Git can do without having Git installed.

The REST API will return a `409 Conflict` if the Git repository is empty
or unavailable. An unavailable repository typically means {% data variables.product.github %} is in the process of creating the repository. For an empty repository, you can use the [`PUT /repos/{owner}/{repo}/contents/{path}`](/rest/repos/contents#create-or-update-file-contents) REST API endpoint to create content and initialize the repository so you can use the API to manage the Git database. Contact {% data variables.contact.contact_support %} if this response status persists.

For more information on the Git object database, please read the
[Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain) chapter of
the Pro Git book.

As an example, if you wanted to commit a change to a file in your
repository, you would:

* Get the current commit object
* Retrieve the tree it points to
* Retrieve the content of the blob object that tree has for that particular file path
* Change the content somehow and post a new blob object with that new content, getting a blob SHA back
* Post a new tree object with that file path pointer replaced with your new blob SHA getting a tree SHA back
* Create a new commit object with the current commit SHA as the parent and the new tree SHA, getting a commit SHA back
* Update the reference of your branch to point to the new commit SHA

It might seem complex, but it's actually pretty simple when you understand
the model and it opens up a ton of things you could potentially do with the API.

## Checking mergeability of pull requests

> [!WARNING]
> Please do not depend on using Git directly or [`GET /repos/{owner}/{repo}/git/refs/{ref}`](/rest/git/refs#get-a-reference) for updates to `merge` Git refs, because this content becomes outdated without warning.

A consuming API needs to explicitly request a pull request to create a _test_ merge commit. A _test_ merge commit is created when you view the pull request in the UI and the "Merge" button is displayed, or when you [get](/rest/pulls/pulls#get-a-pull-request), [create](/rest/pulls/pulls#create-a-pull-request), or [edit](/rest/pulls#update-a-pull-request) a pull request using the REST API. Without this request, the `merge` Git refs will fall out of date until the next time someone views the pull request.

If you are currently using polling methods that produce outdated `merge` Git refs, then GitHub recommends using the following steps to get the latest changes from the default branch:

1. Receive the pull request webhook.
1. Call [`GET /repos/{owner}/{repo}/pulls/{pull_number}`](/rest/pulls/pulls#get-a-pull-request) to start a background job for creating the merge commit candidate.
1. Poll your repository using [`GET /repos/{owner}/{repo}/pulls/{pull_number}`](/rest/pulls/pulls#get-a-pull-request) to see if the `mergeable` attribute is `true` or `false`. You can use Git directly or [`GET /repos/{owner}/{repo}/git/refs/{ref}`](/rest/git/refs#get-a-reference) for updates to `merge` Git refs only after performing the previous steps.


---

<!-- source: https://docs.github.com/en/rest/guides/working-with-comments -->

---
title: Working with comments
intro: 'Using the REST API, you can access and manage comments in your pull requests, issues, or commits.'
redirect_from:
  - /guides/working-with-comments
  - /v3/guides/working-with-comments
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Build apps and integrations
---



For any Pull Request, {% data variables.product.github %} provides three kinds of comment views:
[comments on the Pull Request](https://github.com/octocat/Spoon-Knife/pull/1176#issuecomment-24114792) as a whole, [comments on a specific line](https://github.com/octocat/Spoon-Knife/pull/1176#discussion_r6252889) within the Pull Request,
and [comments on a specific commit](https://github.com/octocat/Spoon-Knife/commit/cbc28e7c8caee26febc8c013b0adfb97a4edd96e#commitcomment-4049848) within the Pull Request.

Each of these types of comments goes through a different portion of the {% data variables.product.github %} API.
In this guide, we'll explore how you can access and manipulate each one. For every
example, we'll be using [this sample Pull Request made](https://github.com/octocat/Spoon-Knife/pull/1176) on the "octocat"
repository. As always, samples can be found in [our platform-samples repository](https://github.com/github/platform-samples/tree/master/api/ruby/working-with-comments).

## Pull Request Comments

To access comments on a Pull Request, you'll use [the endpoints to manage issues](/rest/issues/comments).
This may seem counterintuitive at first. But once you understand that a Pull
Request is just an Issue with code, it makes sense to use these endpoints to
create comments on a Pull Request.

We'll demonstrate fetching Pull Request comments by creating a Ruby script using
[Octokit.rb](https://github.com/octokit/octokit.rb). You'll also want to create a [{% data variables.product.pat_generic %}](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

The following code should help you get started accessing comments from a Pull Request
using Octokit.rb:

``` ruby
require 'octokit'

# !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
# Instead, set and test environment variables, like below
client = Octokit::Client.new :access_token => ENV['MY_PERSONAL_TOKEN']

client.issue_comments("octocat/Spoon-Knife", 1176).each do |comment|
  username = comment[:user][:login]
  post_date = comment[:created_at]
  content = comment[:body]

  puts "#{username} made a comment on #{post_date}. It says:\n'#{content}'\n"
end
```

Here, we're specifically calling out to the API to get the comments (`issue_comments`),
providing both the repository's name (`octocat/Spoon-Knife`), and the Pull Request ID
we're interested in (`1176`). After that, it's simply a matter of iterating through
the comments to fetch information about each one.

## Pull Request Comments on a Line

Within the diff view, you can start a discussion on a particular aspect of a singular
change made within the Pull Request. These comments occur on the individual lines
within a changed file. The endpoint URL for this discussion comes from [the endpoint to manage pull request reviews](/rest/pulls/comments).

The following code fetches all the Pull Request comments made on files, given a single Pull Request number:

``` ruby
require 'octokit'

# !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
# Instead, set and test environment variables, like below
client = Octokit::Client.new :access_token => ENV['MY_PERSONAL_TOKEN']

client.pull_request_comments("octocat/Spoon-Knife", 1176).each do |comment|
  username = comment[:user][:login]
  post_date = comment[:created_at]
  content = comment[:body]
  path = comment[:path]
  position = comment[:position]

  puts "#{username} made a comment on #{post_date} for the file called #{path}, on line #{position}. It says:\n'#{content}'\n"
end
```

You'll notice that it's incredibly similar to the example above. The difference
between this view and the Pull Request comment is the focus of the conversation.
A comment made on a Pull Request should be reserved for discussion or ideas on
the overall direction of the code. A comment made as part of a Pull Request review should
deal specifically with the way a particular change was implemented within a file.

## Commit Comments

The last type of comments occur specifically on individual commits. For this reason,
they make use of [the endpoint to manage commit comments](/rest/commits#get-a-commit-comment).

To retrieve the comments on a commit, you'll want to use the SHA1 of the commit.
In other words, you won't use any identifier related to the Pull Request. Here's an example:

``` ruby
require 'octokit'

# !!! DO NOT EVER USE HARD-CODED VALUES IN A REAL APP !!!
# Instead, set and test environment variables, like below
client = Octokit::Client.new :access_token => ENV['MY_PERSONAL_TOKEN']

client.commit_comments("octocat/Spoon-Knife", "cbc28e7c8caee26febc8c013b0adfb97a4edd96e").each do |comment|
  username = comment[:user][:login]
  post_date = comment[:created_at]
  content = comment[:body]

  puts "#{username} made a comment on #{post_date}. It says:\n'#{content}'\n"
end
```

Note that this API call will retrieve single line comments, as well as comments made
on the entire commit.


---

<!-- source: https://docs.github.com/en/rest/index -->

---
title: GitHub REST API documentation
shortTitle: REST API
intro: >-
  Create integrations, retrieve data, and automate your workflows with the {%
  data variables.product.prodname_dotcom %} REST API.
introLinks:
  overview: /rest/about-the-rest-api/about-the-rest-api
  quickstart: /rest/quickstart
layout: discovery-landing
includedCategories:
  - Learn about the REST API
  - Authenticate API requests
  - Build apps and integrations
  - Manage repositories and code
  - Manage issues, pull requests, and projects
  - Automate CI/CD workflows
  - Secure code and manage vulnerabilities
  - Manage organizations and teams
  - Administer enterprises and billing
  - Manage users and activity
  - Use Codespaces
  - Use Copilot and AI services
carousels:
  recommended:
    - /rest/quickstart
    - /rest/using-the-rest-api/getting-started-with-the-rest-api
    - /rest/authentication/authenticating-to-the-rest-api
    - /rest/using-the-rest-api/best-practices-for-using-the-rest-api
    - /rest/using-the-rest-api/rate-limits-for-the-rest-api
    - /rest/authentication/keeping-your-api-credentials-secure
    - /rest/guides/scripting-with-the-rest-api-and-javascript
    - /rest/using-the-rest-api/troubleshooting-the-rest-api
    - /rest/using-the-rest-api/using-pagination-in-the-rest-api
redirect_from:
  - /v3
  - /rest/reference
  - /rest/overview
  - /developers/overview
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /quickstart
  - /about-the-rest-api
  - /using-the-rest-api
  - /authentication
  - /guides
  - /actions
  - /activity
  - /agent-tasks
  - /agents
  - /announcement-banners
  - /apps
  - /billing
  - /branches
  - /campaigns
  - /checks
  - /classroom
  - /code-quality
  - /code-scanning
  - /code-security
  - /codes-of-conduct
  - /codespaces
  - /collaborators
  - /commits
  - /copilot
  - /copilot-spaces
  - /credentials
  - /dependabot
  - /dependency-graph
  - /deploy-keys
  - /deployments
  - /emojis
  - /enterprise-admin
  - /enterprise-teams
  - /gists
  - /git
  - /gitignore
  - /interactions
  - /issues
  - /licenses
  - /markdown
  - /meta
  - /metrics
  - /migrations
  - /models
  - /oauth-authorizations
  - /orgs
  - /packages
  - /pages
  - /private-registries
  - /projects
  - /projects-classic
  - /pulls
  - /rate-limit
  - /reactions
  - /releases
  - /repos
  - /scim
  - /search
  - /secret-scanning
  - /security-advisories
  - /teams
  - /users
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/interactions -->

---
title: REST API endpoints for interactions
shortTitle: Interactions
allowTitleToDifferFromFilename: true
intro: Use the REST API to set the interaction limit for the users in your organizations and repositories.
permissions: People with owner or admin access can set the interaction limit for the users in their organizations and repositories.
redirect_from:
  - /v3/interactions
  - /rest/reference/interactions
versions:
  fpt: '*'
  ghec: '*'
children:
  - /orgs
  - /repos
  - /user
autogenerated: rest
---

## About interactions

Users interact with repositories by commenting, opening issues, and creating pull requests. You can use the REST API to allow people with owner or admin access to temporarily restrict interaction with public repositories to a certain type of user.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/interactions/orgs -->

---
title: REST API endpoints for organization interactions
shortTitle: Organization
intro: >-
  Use the REST API to temporarily restrict which type of user can comment, open
  issues, or create pull requests in the organization's public repositories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage organizations and teams
---

## About organization interactions

Organization owners can temporarily restrict which type of user can comment, open issues, or create pull requests in the organization's public repositories. {% data reusables.interactions.interactions-detail %} Here's more about the types of {% data variables.product.github %} users:

* {% data reusables.interactions.existing-user-limit-definition %} in the organization.
* {% data reusables.interactions.contributor-user-limit-definition %} in the organization.
* {% data reusables.interactions.collaborator-user-limit-definition %} in the organization.

Setting the interaction limit at the organization level will overwrite any interaction limits that are set for individual repositories owned by the organization. To set different interaction limits for individual repositories owned by the organization, use the [Repository](/rest/interactions/repos) interactions endpoints instead.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/interactions/repos -->

---
title: REST API endpoints for repository interactions
shortTitle: Repository
intro: >-
  Use the REST API to temporarily restrict which type of user can comment, open
  issues, or create pull requests in a public repository.
permissions: >-
  People with owner or admin access to temporarily restrict which type of user
  can comment, open issues, or create pull requests in a public repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---

## About repository interactions

People with owner or admin access can use the REST API to temporarily restrict which type of user can comment, open issues, or create pull requests in a public repository. {% data reusables.interactions.interactions-detail %} Here's more about the types of {% data variables.product.github %} users:

* {% data reusables.interactions.existing-user-limit-definition %} in the repository.
* {% data reusables.interactions.contributor-user-limit-definition %} in the repository.
* {% data reusables.interactions.collaborator-user-limit-definition %} in the repository.

If an interaction limit is enabled for the user or organization that owns the repository, the limit cannot be changed for the individual repository. Instead, use the [User](/rest/interactions/user) or [Organization](/rest/interactions/orgs) interactions endpoints to change the interaction limit.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/interactions/user -->

---
title: REST API endpoints for user interactions
shortTitle: User
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to temporarily restrict which type of user can comment, open
  issues, or create pull requests in your public repositories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About user interactions

You can use the REST API to temporarily restrict which type of user can comment, open issues, or create pull requests on your public repositories. {% data reusables.interactions.interactions-detail %} Here's more about the types of {% data variables.product.github %} users:

* {% data reusables.interactions.existing-user-limit-definition %} from interacting with your repositories.
* {% data reusables.interactions.contributor-user-limit-definition %} from interacting with your repositories.
* {% data reusables.interactions.collaborator-user-limit-definition %} from interacting with your repositories.

Setting the interaction limit at the user level will overwrite any interaction limits that are set for individual repositories owned by the user. To set different interaction limits for individual repositories owned by the user, use the [Repository](/rest/interactions/repos) interactions endpoints instead.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/assignees -->

---
title: REST API endpoints for issue assignees
allowTitleToDifferFromFilename: true
shortTitle: Assignees
intro: Use the REST API to manage assignees on issues and pull requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About issue and pull request assignees

You can use the REST API to view, add, and remove assignees on issues and pull requests. {% data reusables.pull_requests.issues-pr-shared-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/comments -->

---
title: REST API endpoints for issue comments
allowTitleToDifferFromFilename: true
shortTitle: Comments
intro: Use the REST API to manage comments on issues and pull requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About issue and pull request comments

You can use the REST API to create and manage comments on issues and pull requests. {% data reusables.pull_requests.issues-pr-shared-api %} To manage pull request review comments, see [AUTOTITLE](/rest/pulls/comments).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/events -->

---
title: REST API endpoints for issue events
allowTitleToDifferFromFilename: true
shortTitle: Events
intro: >-
  Use the REST API to retrieve events triggered by activity in issues and pull
  requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About events

You can use the REST API to view different types of events triggered by activity in issues and pull requests. For more information about the specific events that you can receive, see [AUTOTITLE](/webhooks-and-events/events/issue-event-types). To view {% data variables.product.github %} activity outside of issues and pull requests, you can use the [Events](/webhooks-and-events/events/github-event-types) endpoints.

{% data reusables.pull_requests.issues-pr-shared-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues -->

---
title: REST API endpoints for issues
shortTitle: Issues
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to view and manage issues, including issue assignees,
  comments, labels, and milestones.
redirect_from:
  - /v3/issues
  - /rest/reference/issues
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /assignees
  - /comments
  - /events
  - /issue-dependencies
  - /issue-field-values
  - /issues
  - /labels
  - /milestones
  - /sub-issues
  - /timeline
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/issue-dependencies -->

---
title: REST API endpoints for issue dependencies
shortTitle: Issue dependencies
intro: Use the REST API to view, add, and remove issue dependencies.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/issue-field-values -->

---
title: REST API endpoints for issue field values
shortTitle: Issue field values
intro: Use the REST API to view and manage issue field values for issues.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/issues -->

---
title: REST API endpoints for issues
shortTitle: Issues
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage issues and pull requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/labels -->

---
title: REST API endpoints for labels
shortTitle: Labels
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to manage labels for repositories, issues and pull requests.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About labels

You can use the REST API to manage labels for a repository and add or remove labels to issues and pull requests. {% data reusables.pull_requests.issues-pr-shared-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/milestones -->

---
title: REST API endpoints for milestones
shortTitle: Milestones
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage milestones.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/sub-issues -->

---
title: REST API endpoints for sub-issues
shortTitle: Sub-issues
intro: Use the REST API to view, add, remove, and reprioritize sub-issues.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/issues/timeline -->

---
title: REST API endpoints for timeline events
allowTitleToDifferFromFilename: true
shortTitle: Timeline
intro: >-
  Use the REST API to receive events triggered by timeline activity in issues
  and pull requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About timeline events

You can use the REST API to view different types of events triggered by timeline activity in issues and pull requests. For more information about the specific events that you can receive, see [AUTOTITLE](/webhooks-and-events/events/issue-event-types). To view {% data variables.product.github %} activity outside of issues and pull requests, see [AUTOTITLE](/webhooks-and-events/events/github-event-types).

You can use timeline events to display information about issues and pull requests or determine who should be notified of issue comments.

{% data reusables.pull_requests.issues-pr-shared-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/licenses -->

---
title: REST API endpoints for licenses
shortTitle: Licenses
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to retrieve popular open source licenses and information
  about a particular project's license file.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /licenses
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/licenses/licenses -->

---
title: REST API endpoints for licenses
shortTitle: Licenses
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to retrieve popular open source licenses and information
  about a particular project's license file.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/licenses
autogenerated: rest
category:
  - Manage repositories and code
---

## About licenses

{% data variables.product.company_short %} uses [the open source Ruby Gem Licensee](https://github.com/benbalter/licensee) to attempt to identify the license for a project. Licensee matches the contents of a project's `LICENSE` file (if it exists) against a short list of known licenses. As a result, the API does not take into account the licenses of project dependencies or other means of documenting a project's license such as references to the license name in the documentation.

If a license is matched, the license key and name returned conforms to the [SPDX specification](https://spdx.org/).

**Note:** These endpoints will also return a repository's license information:

* [Get a repository](/rest/repos/repos#get-a-repository)
* [List repositories for a user](/rest/repos/repos#list-repositories-for-a-user)
* [List organization repositories](/rest/repos/repos#list-organization-repositories)
* [List forks](/rest/repos/forks#list-forks)
* [List repositories watched by a user](/rest/activity/watching#list-repositories-watched-by-a-user)
* [List team repositories](/rest/teams/teams#list-team-repositories)

> [!WARNING]
> GitHub is a lot of things, but it’s not a law firm. As such, {% data variables.product.company_short %} does not provide legal advice. Using the API or sending us an email about it does not constitute legal advice nor does it create an attorney-client relationship. If you have any questions about what you can and can't do with a particular license, you should consult with your own legal counsel before moving forward. In fact, you should always consult with your own lawyer before making any decisions that might have legal ramifications or that may impact your legal rights.
>
> {% data variables.product.company_short %} created these endpoints to help users get information about open source licenses and the projects that use them. We hope it helps, but please keep in mind that we’re not lawyers (at least most of us aren't) and that we make mistakes like everyone else. For that reason, {% data variables.product.company_short %} provides the API on an "as-is" basis and makes no warranties regarding any information or licenses provided on or through it, and disclaims liability for damages resulting from using the API.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/markdown -->

---
title: REST API endpoints for Markdown
shortTitle: Markdown
allowTitleToDifferFromFilename: true
intro: Use the REST API to render a Markdown document as an HTML page or as raw text.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /markdown
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/markdown/markdown -->

---
title: REST API endpoints for Markdown
shortTitle: Markdown
allowTitleToDifferFromFilename: true
intro: Use the REST API to render a markdown document as an HTML page or as raw text.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/markdown
autogenerated: rest
category:
  - Learn about the REST API
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/meta -->

---
title: REST API endpoints for meta data
shortTitle: Meta
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to get meta information about {% data
  variables.product.github %}, including the IP addresses of {% data
  variables.product.github %} services.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /meta
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/meta/meta -->

---
title: REST API endpoints for meta data
shortTitle: Meta
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to get meta information about {% data
  variables.product.github %}, including the IP addresses of {% data
  variables.product.github %} services.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/meta
autogenerated: rest
category:
  - Learn about the REST API
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/metrics/community -->

---
title: REST API endpoints for community metrics
shortTitle: Community
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve information about your community profile.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/metrics -->

---
title: REST API endpoints for metrics
shortTitle: Metrics
intro: 'Use the REST API to retrieve the community profile, statistics, and traffic for your repository.'
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/reference/repository-metrics
  - /rest/reference/metrics
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /community
  - /statistics
  - /traffic
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/metrics/statistics -->

---
title: REST API endpoints for repository statistics
shortTitle: Statistics
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to fetch the data that {% data variables.product.github
  %} uses for visualizing different types of repository activity.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About repository statistics

You can use the REST API to fetch the data that {% data variables.product.github %} uses for visualizing different types of repository activity.

### Best practices for caching

Computing repository statistics is an expensive operation, so we try to return cached
data whenever possible. If the data hasn't been cached when you query a repository's
statistics, you'll receive a `202` response; a background job is also fired to
start compiling these statistics. You should allow the job a short time to complete, and
then submit the request again. If the job has completed, that request will receive a
`200` response with the statistics in the response body.

Repository statistics are cached by the SHA of the repository's default branch; pushing to the default branch resets the statistics cache.

### Statistics exclude some types of commits

The statistics exposed by the API match the statistics shown by [different repository graphs](/repositories/viewing-activity-and-data-for-your-repository/about-repository-graphs).

To summarize this:
* All statistics exclude merge commits.
* Contributor statistics also exclude empty commits.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/metrics/traffic -->

---
title: REST API endpoints for repository traffic
shortTitle: Traffic
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve information provided in your repository graph.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About repository traffic

You can use these endpoints to retrieve information provided in your repository graph, for repositories that you have write access to. For more information, see [AUTOTITLE](/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository).

{% ifversion ghec %}

> [!NOTE]
> Repository traffic stats are not available through the REST API or UI on {% data variables.enterprise.data_residency_site %}.

{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/migrations -->

---
title: REST API endpoints for migrations
shortTitle: Migrations
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to migrate the repositories and users of your organization from {% data variables.product.prodname_dotcom_the_website %} to {% data variables.product.prodname_ghe_server %}.'
redirect_from:
  - /v3/migrations
  - /v3/migration
  - /v3/migration/migrations
  - /rest/reference/migrations
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /orgs
  - /source-imports
  - /users
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/migrations/orgs -->

---
title: REST API endpoints for organization migrations
allowTitleToDifferFromFilename: true
shortTitle: Organizations
intro: >-
  Use the REST API to export one or more repositories so you can move them to {%
  ifversion ghes %}another{% endif %} {% data
  variables.product.prodname_ghe_server %}{% ifversion ghes %} instance{% endif
  %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

## About organization migrations

These endpoints are only available to authenticated organization owners. For more information, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#permission-levels-for-an-organization) and [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

{% data variables.migrations.organization_migrations_intro %}

{% ifversion ghec %}{% data variables.migrations.enterprise_cloud_with_data_residency %}{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/migrations/source-imports -->

---
title: REST API endpoints for source imports
shortTitle: Source endpoints
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to start an import from a Git source repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About source imports

> [!WARNING]
> Due to very low levels of usage and available alternatives, the Source Imports API has been {% data variables.release-phases.retired %}. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

{% data variables.migrations.source_imports_intro %} A typical source import would start the import and then (optionally) update the authors and/or update the preference for using Git LFS if large files exist in the import. You can also create a webhook that listens for the [`RepositoryImportEvent`](/webhooks-and-events/webhooks/webhook-events-and-payloads#repository_import) to find out the status of the import.

{% data reusables.user-settings.imports-api-classic-pat-only %}

The following diagram provides a more detailed example:

```text
+---------+                     +--------+                              +---------------------+
| Tooling |                     | GitHub |                              | Original Repository |
+---------+                     +--------+                              +---------------------+
     |                              |                                              |
     |  Start import                |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |                              |  Download source data                        |
     |                              |--------------------------------------------->|
     |                              |                        Begin streaming data  |
     |                              |<---------------------------------------------|
     |                              |                                              |
     |  Get import progress         |                                              |
     |----------------------------->|                                              |
     |       "status": "importing"  |                                              |
     |<-----------------------------|                                              |
     |                              |                                              |
     |  Get commit authors          |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |  Map a commit author         |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |                              |                                              |
     |                              |                       Finish streaming data  |
     |                              |<---------------------------------------------|
     |                              |                                              |
     |                              |  Rewrite commits with mapped authors         |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Map a commit author         |                                              |
     |----------------------------->|                                              |
     |                              |  Rewrite commits with mapped authors         |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Get large files             |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |  opt_in to Git LFS           |                                              |
     |----------------------------->|                                              |
     |                              |  Rewrite commits for large files             |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Get import progress         |                                              |
     |----------------------------->|                                              |
     |        "status": "complete"  |                                              |
     |<-----------------------------|                                              |
     |                              |                                              |
     |                              |                                              |
```

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/migrations/users -->

---
title: REST API endpoints for user migrations
allowTitleToDifferFromFilename: true
shortTitle: Users
intro: >-
  Use the REST API to review, backup, or migrate your user data stored on {%
  data variables.product.github %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About user migrations

These endpoints are only available to authenticated account owners. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

{% data variables.migrations.user_migrations_intro %} For a list of migration data that you can download, see [Download a user migration archive](#download-a-user-migration-archive).

To download an archive, you'll need to start a user migration first. Once the status of the migration is `exported`, you can download the migration.

Once you've created a migration archive, it will be available to download for seven days. But, you can delete the user migration archive sooner if you'd like. You can unlock your repository when the migration is `exported` to begin using your repository again or delete the repository if you no longer need the source data.

{% ifversion ghec %}{% data variables.migrations.enterprise_cloud_with_data_residency %}{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/models/catalog -->

---
title: REST API endpoints for models catalog
shortTitle: Catalog
intro: Use the REST API to get a list of models available for use, including details like ID, supported input/output modalities, and rate limits.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

## About {% data variables.product.prodname_github_models %} catalog

You can use the REST API to explore available models in the {% data variables.product.prodname_github_models %} catalog.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/models/embeddings -->

---
title: REST API endpoints for model embeddings
shortTitle: Embeddings
intro: Use the REST API to work with embedding requests for models.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/models -->

---
title: Models
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /catalog
  - /embeddings
  - /inference
versions:
  fpt: '*'
---



---

<!-- source: https://docs.github.com/en/rest/models/inference -->

---
title: REST API endpoints for models inference
shortTitle: Inference
intro: Use the REST API to submit a chat completion request to a specified model, with or without organizational attribution.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Use Copilot and AI services
---

## About {% data variables.product.prodname_github_models %} inference

You can use the REST API to run inference requests using the {% data variables.product.prodname_github_models %} platform. The API requires the `models: read` scope when using a {% data variables.product.pat_v2 %} or when authenticating using a {% data variables.product.prodname_github_app %}.

The API supports:

* Accessing top models from OpenAI, DeepSeek, Microsoft, Llama, and more.
* Running chat-based inference requests with full control over sampling and response parameters.
* Streaming or non-streaming completions.
* Organizational attribution and usage tracking.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/oauth-authorizations -->

---
title: REST API endpoints for OAuth app authorizations
shortTitle: OAuth app authorizations
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage the access {% data variables.product.prodname_oauth_apps %} have to your account.
versions:
  ghes: '*'
children:
  - /oauth-authorizations
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/oauth-authorizations/oauth-authorizations -->

---
title: REST API endpoints for OAuth app authorizations
shortTitle: OAuth app authorizations
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to manage the access {% data
  variables.product.prodname_oauth_apps %} have to your account.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: '*'
redirect_from:
  - /rest/reference/oauth-authorizations
autogenerated: rest
category:
  - Build apps and integrations
---

## About OAuth authorizations

You can use the REST API to manage the access {% data variables.product.prodname_oauth_apps %} have to your account. You can only access these endpoints via basic authentication using your username and password, not tokens.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/api-insights -->

---
title: REST API endpoints for API Insights
shortTitle: API Insights
intro: Use the REST API to view statistics for API usage in an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/artifact-metadata -->

---
title: REST API endpoints for artifact metadata
shortTitle: Artifact metadata
intro: "Use these endpoints to retrieve and manage metadata for artifacts in your organization. Artifact metadata provides information about build artifacts, their provenance, and related details."
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

You can use these endpoints to upload storage and deployment records for software that your organization builds with {% data variables.product.prodname_actions %}. The records are displayed on the organization's {% data variables.product.virtual_registry %}. See [AUTOTITLE](/code-security/concepts/supply-chain-security/linked-artifacts).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/attestations -->

---
title: REST API endpoints for artifact attestations
shortTitle: Artifact attestations
intro: Use the REST API to interact with artifact attestations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/blocking -->

---
title: REST API endpoints for blocking users
shortTitle: Blocking users
intro: Use the REST API to block and unblock users in an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage organizations and teams
---

## About blocking users

The token used to authenticate the call must have the `admin:org` scope in order to make any blocking calls for an organization. Otherwise, the response returns `HTTP 404`.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/bypass-requests -->

---
title: REST API endpoints for organization push rule bypass requests
shortTitle: Bypass requests
intro: Use the REST API to manage organization push rule bypass requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.17'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/custom-properties-for-orgs -->

---
title: REST API endpoints for an organization's custom property values
shortTitle: Custom properties for organizations
intro: Use the REST API to manage custom property values for an organization
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.21'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/custom-properties -->

---
title: REST API endpoints for custom properties
shortTitle: Custom properties
intro: Use the REST API to create and manage custom properties for an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/orgs/properties
category:
  - Manage organizations and teams
---

## About custom properties

You can use the REST API to create and manage custom properties for an organization. You can use custom properties to add metadata to repositories in your organization. For more information, see [AUTOTITLE](/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/custom-roles -->

---
title: REST API endpoints for custom repository roles
shortTitle: Custom roles
intro: Use the REST API to interact with custom repository roles.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/orgs/custom_roles
autogenerated: rest
category:
  - Manage organizations and teams
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs -->

---
title: REST API endpoints for organizations
shortTitle: Organizations
intro: >-
  Use the REST API to control and manage all your {% data
  variables.product.github %} organizations.
allowTitleToDifferFromFilename: true
redirect_from:
  - /v3/orgs
  - /rest/reference/orgs
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /api-insights
  - /artifact-metadata
  - /attestations
  - /blocking
  - /bypass-requests
  - /custom-properties
  - /custom-properties-for-orgs
  - /custom-roles
  - /issue-fields
  - /issue-types
  - /members
  - /network-configurations
  - /organization-roles
  - /orgs
  - /outside-collaborators
  - /personal-access-tokens
  - /rule-suites
  - /rules
  - /security-managers
  - /webhooks
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/issue-fields -->

---
title: REST API endpoints for issue fields
shortTitle: Issue fields
intro: Use the REST API to create and manage issue fields for an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/issue-types -->

---
title: REST API endpoints for issue types
shortTitle: Issue types
intro: Use the REST API to interact with issue types in an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/members -->

---
title: REST API endpoints for organization members
allowTitleToDifferFromFilename: true
shortTitle: Members
intro: Use the REST API to manage memberships in your organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

{% ifversion ghec %}

> [!NOTE] If you use {% data variables.product.prodname_emus %}, you add members to organizations directly, rather than sending invitations. The operations for managing organization invitations will not work in your enterprise. However, the operations for viewing or managing membership directly will work as expected.

{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/network-configurations -->

---
title: REST API endpoints for network configurations
shortTitle: Network configurations
intro: REST API endpoints for network configurations
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
redirect_from:
  - /rest/settings/network-configurations
  - /rest/settings
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/organization-roles -->

---
title: REST API endpoints for organization roles
shortTitle: Organization roles
intro: Use the REST API to interact with organization roles.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/orgs -->

---
title: REST API endpoints for organizations
shortTitle: Organizations
intro: Use the REST API to interact with organizations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage organizations and teams
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/outside-collaborators -->

---
title: REST API endpoints for outside collaborators
shortTitle: Outside collaborators
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage outside collaborators.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

{% data reusables.enterprise-managed.repo-collaborators-note %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/personal-access-tokens -->

---
title: REST API endpoints for personal access tokens
shortTitle: Personal access tokens
intro: 'Use the REST API to manage {% data variables.product.pat_v2 %}s.'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/rule-suites -->

---
title: REST API endpoints for rule suites
shortTitle: Rule suites
intro: Use the REST API to manage rule suites for organizations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/rules -->

---
title: REST API endpoints for rules
shortTitle: Rules
intro: >-
  Use the REST API to manage rulesets for organizations. Organization rulesets
  control how people can interact with selected branches and tags in
  repositories in an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/security-managers -->

---
title: REST API endpoints for security managers
shortTitle: Security managers
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage security managers in an organization.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

## About security managers

{% data reusables.organizations.about-security-managers %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/orgs/webhooks -->

---
title: REST API endpoints for organization webhooks
allowTitleToDifferFromFilename: true
shortTitle: Webhooks
intro: Use the REST API to interact with webhooks in an organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

## About organization webhooks

Organization webhooks allow your server to receive HTTP `POST` payloads whenever certain events happen in an organization. For more information, see [AUTOTITLE](/webhooks).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/packages -->

---
title: REST API endpoints for packages
shortTitle: Packages
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to interact with {% data variables.product.prodname_registry %}.'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /packages
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/packages/packages -->

---
title: REST API endpoints for packages
shortTitle: Packages
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to interact with {% data variables.product.prodname_registry %}.'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/packages
autogenerated: rest
category:
  - Manage repositories and code
---

## About {% data variables.product.prodname_registry %}

{% data variables.product.prodname_registry %} supports a range of package managers for publishing packages. For more information, see [AUTOTITLE](/packages/learn-github-packages/introduction-to-github-packages#supported-clients-and-formats).

After you publish a package, you can use the REST API to manage the package in your {% data variables.product.prodname_dotcom %} repositories and organizations. For more information, see [AUTOTITLE](/packages/learn-github-packages/deleting-and-restoring-a-package).

To use the REST API to manage {% data variables.product.prodname_registry %}, you must authenticate using a {% data variables.product.pat_v1 %}.
* To access package metadata, your token must include the `read:packages` scope.
* To delete packages and package versions, your token must include the `read:packages` and `delete:packages` scopes.
* To restore packages and package versions, your token must include the `read:packages` and `write:packages` scopes.

If your package is in a registry that supports granular permissions, then your token does not need the `repo` scope to access or manage this package. If your package is in a registry that only supports repository-scoped permissions, then your token must also include the `repo` scope since your package inherits permissions from a {% data variables.product.prodname_dotcom %} repository. For a list of registries that only support repository-scoped permissions, see [AUTOTITLE](/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages).

{% ifversion ghec %}
To access resources in an organization with SSO enabled, you must enable SSO for your {% data variables.product.pat_v1 %}. For more information, see [AUTOTITLE](/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).
{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pages -->

---
title: REST API endpoints for {% data variables.product.prodname_pages %}
shortTitle: Pages
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data variables.product.prodname_pages %}
  sites and builds.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /pages
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pages/pages -->

---
title: 'REST API endpoints for {% data variables.product.prodname_pages %}'
shortTitle: Pages
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with {% data variables.product.prodname_pages %}
  sites and builds.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/pages
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/private-registries -->

---
title: Private registries
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /organization-configurations
versions:
  fpt: '*'
  ghec: '*'
  ghes: '>=3.16'
---



---

<!-- source: https://docs.github.com/en/rest/private-registries/organization-configurations -->

---
title: Organization configurations
shortTitle: Organization configurations
intro: Use the REST API to manage private registry configurations for organizations.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage organizations and teams
---


<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects/drafts -->

---
title: REST API endpoints for draft Project items
shortTitle: Draft Project items
intro: Use the REST API to manage draft items in Projects.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects/fields -->

---
title: REST API endpoints for Project fields
shortTitle: Project fields
intro: Use the REST API to manage Project fields
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects -->

---
title: Projects
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /drafts
  - /fields
  - /items
  - /projects
  - /views
versions:
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
---



---

<!-- source: https://docs.github.com/en/rest/projects/items -->

---
title: REST API endpoints for Project items
shortTitle: Project items
intro: Use the REST API to manage Project items
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects/projects -->

---
title: REST API endpoints for Projects
shortTitle: Projects
intro: Use the REST API to manage Projects
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects/views -->

---
title: REST API endpoints for Project views
shortTitle: Project views
intro: Use the REST API to manage Project views
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.20'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects-classic/cards -->

---
title: >-
  REST API endpoints for {% data variables.product.prodname_project_v1_caps %}
  cards
shortTitle: Cards
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create and manage cards on a {% data
  variables.projects.projects_v1_board %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: <=3.16
autogenerated: rest
redirect_from:
  - /rest/projects/cards
  - /v3/projects/cards
  - /rest/reference/projects/cards
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects-classic/collaborators -->

---
title: >-
  REST API endpoints for {% data variables.product.prodname_project_v1_caps %}
  collaborators
shortTitle: Collaborators
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to manage collaborators on a {% data
  variables.projects.projects_v1_board %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: <=3.16
autogenerated: rest
redirect_from:
  - /rest/projects/collaborators
  - /v3/projects/collaborators
  - /rest/reference/projects/collaborators
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects-classic/columns -->

---
title: >-
  REST API endpoints for {% data variables.product.prodname_project_v1_caps %}
  columns
shortTitle: Columns
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create and manage columns on a {% data
  variables.projects.projects_v1_board %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: <=3.16
autogenerated: rest
redirect_from:
  - /rest/projects/columns
  - /v3/projects/columns
  - /rest/reference/projects/columns
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/projects-classic -->

---
title: 'REST API endpoints for {% data variables.product.prodname_projects_v1_caps %}'
shortTitle: '{% data variables.product.prodname_projects_v1_caps %}'
intro: 'Use the REST API to create, list, update, delete and customize {% data variables.projects.projects_v1_boards %}.'
redirect_from:
  - /v3/projects
  - /rest/reference/projects
autogenerated: rest
allowTitleToDifferFromFilename: true
children:
  - /cards
  - /collaborators
  - /columns
  - /projects
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
---



---

<!-- source: https://docs.github.com/en/rest/projects-classic/projects -->

---
title: REST API endpoints for {% data variables.product.prodname_projects_v1_caps %}
shortTitle: Boards
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create and manage {% data
  variables.projects.projects_v1_boards %} in a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: <=3.16
autogenerated: rest
redirect_from:
  - /v3/projects/projects
  - /rest/reference/projects/projects
category:
  - Manage issues, pull requests, and projects
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pulls/comments -->

---
title: REST API endpoints for pull request review comments
shortTitle: Review comments
intro: Use the REST API to interact with pull request review comments.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About pull request review comments

Pull request review comments are comments made on a portion of the unified diff during a pull request review. These are different from commit comments and issue comments in a pull request. For more information, see [AUTOTITLE](/rest/commits/comments) and [AUTOTITLE](/rest/issues/comments).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pulls -->

---
title: REST API endpoints for pull requests
shortTitle: Pull requests
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage pull requests and pull request reviews.
redirect_from:
  - /v3/pulls
  - /rest/reference/pulls
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /pulls
  - /comments
  - /review-requests
  - /reviews
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pulls/pulls -->

---
title: REST API endpoints for pull requests
shortTitle: Pull requests
allowTitleToDifferFromFilename: true
intro: Use the REST API to interact with pull requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About pull requests

You can list, view, edit, create, and merge pull requests using the REST API. For information about how to interact with comments on a pull request, see [AUTOTITLE](/rest/issues/comments).

Pull requests are a type of issue. Any actions that are available in both pull requests and issues, like managing assignees, labels, and milestones, are handled by the REST API to manage issues. To perform these actions on pull requests, you must use the issues API endpoints (for example, `/repos/{owner}/{repo}/issues/{issue_number}`), not the pull requests endpoints. For more information, see [AUTOTITLE](/rest/issues).

### Link Relations

Pull requests have these possible link relations:

* `self`: The API location of this pull request
* `html`: The HTML location of this pull request
* `issue`: The API location of this pull request's [issue](/rest/issues)
* `comments`: The API location of this pull request's [issue comments](/rest/issues/comments)
* `review_comments`: The API location of this pull request's [review comments](/rest/pulls/comments)
* `review_comment`: The [URL template](/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia) to construct the API location for a [review comment](/rest/pulls/comments) in this pull request's repository
* `commits`: The API location of this pull request's [commits](#list-commits-on-a-pull-request)
* `statuses`: The API location of this pull request's [commit statuses](/rest/commits#commit-statuses), which are the statuses of its `head` branch

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pulls/review-requests -->

---
title: REST API endpoints for review requests
shortTitle: Review requests
allowTitleToDifferFromFilename: true
intro: Use the REST API to interact with review requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About review requests

Pull request authors and repository owners and collaborators can request a pull request review from anyone with write access to the repository. Each requested reviewer will receive a notification asking them to review the pull request.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/pulls/reviews -->

---
title: REST API endpoints for pull request reviews
shortTitle: Reviews
allowTitleToDifferFromFilename: true
intro: Use the REST API to interact with pull request reviews.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About pull request reviews

Pull Request Reviews are groups of pull request review comments on a pull request, grouped together with a state and optional body comment.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/quickstart -->

---
title: Quickstart for GitHub REST API
intro: 'Learn how to get started with the {% data variables.product.prodname_dotcom %} REST API.'
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Quickstart
redirect_from:
  - /guides/getting-started
  - /v3/guides/getting-started
category:
  - Learn about the REST API
---

## Introduction

This article describes how to quickly get started with the {% data variables.product.prodname_dotcom %} REST API using {% data variables.product.prodname_cli %}, `curl`, or JavaScript. For a more detailed guide, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api).

{% cli %}

## Using {% data variables.product.prodname_cli %} in the command line

{% data variables.product.prodname_cli %} is the easiest way to use the {% data variables.product.prodname_dotcom %} REST API from the command line.

{% data reusables.rest-api.github-cli-install-and-auth %}

1. Make a request using the {% data variables.product.prodname_cli %} `api` subcommand, followed by the path. Use the `--method` or `-X` flag to specify the method. For more information, see the [{% data variables.product.prodname_cli %} `api` documentation](https://cli.github.com/manual/gh_api).

   This example makes a request to the "Get Octocat" endpoint, which uses the method `GET` and the path `/octocat`. For the full reference documentation for this endpoint, see [AUTOTITLE](/rest/meta/meta#get-octocat).

   ```shell copy
   gh api /octocat --method GET
   ```

## Using {% data variables.product.prodname_cli %} in {% data variables.product.prodname_actions %}

You can also use {% data variables.product.prodname_cli %} in your {% data variables.product.prodname_actions %} workflows. For more information, see [AUTOTITLE](/actions/using-workflows/using-github-cli-in-workflows).

### Authenticating with an access token

Instead of using the `gh auth login` command, pass an access token as an environment variable called `GH_TOKEN`. {% data variables.product.prodname_dotcom %} recommends that you use the built-in `GITHUB_TOKEN` instead of creating a token. If this is not possible, store your token as a secret and replace `GITHUB_TOKEN` in the example below with the name of your secret. For more information about `GITHUB_TOKEN`, see [AUTOTITLE](/actions/security-guides/automatic-token-authentication). For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).

The following example workflow uses the [List repository issues](/rest/issues/issues#list-repository-issues) endpoint, and requests a list of issues in {% ifversion ghes %}a repository you specify{% else %}the `octocat/Spoon-Knife` repository{% endif %}.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-OWNER` with the name of the account that owns the repository. Replace `REPO-NAME` with the name of the repository.{% endif %}

```yaml copy
on:
  workflow_dispatch:
jobs:
  use_api:
    runs-on: ubuntu-latest
    permissions:
      issues: read
    steps:
      - env:
          GH_TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
        run: |
          gh api {% data variables.product.rest_url %}{% data variables.rest.example_request_url %}
```

### Authenticating with a {% data variables.product.prodname_github_app %}

If you are authenticating with a {% data variables.product.prodname_github_app %}, you can create an installation access token within your workflow:

1. Store your {% data variables.product.prodname_github_app %}'s ID as a configuration variable. In the following example, replace `APP_ID` with the name of the configuration variable. You can find your app ID on the settings page for your app or through the API. For more information, see [AUTOTITLE](/rest/apps/apps#get-an-app). For more information about configuration variables, see [AUTOTITLE](/actions/learn-github-actions/variables#defining-configuration-variables-for-multiple-workflows).
1. Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`.) In the following example, replace `APP_PEM` with the name of the secret. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps). For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).
1. Add a step to generate a token, and use that token instead of `GITHUB_TOKEN`. Note that this token will expire after 60 minutes. {% ifversion fpt or ghec %}For example:{% else %}In the following example, replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-OWNER` with the name of the account that owns the repository. Replace `REPO-NAME` with the name of the repository.{% endif %}

   ```yaml copy
   on:
     workflow_dispatch:
   jobs:
     track_pr:
       runs-on: ubuntu-latest
       steps:
         - name: Generate token
           id: generate-token
           uses: actions/create-github-app-token@v2
           with:
             app-id: {% raw %}${{ vars.APP_ID }}{% endraw %}
             private-key: {% raw %}${{ secrets.APP_PEM }}{% endraw %}
         - name: Use API
           env:
             GH_TOKEN: {% raw %}${{ steps.generate-token.outputs.token }}{% endraw %}
           run: |
             gh api {% data variables.product.rest_url %}{% data variables.rest.example_request_url %}
   ```

{% endcli %}

{% javascript %}

## Using Octokit.js

You can use Octokit.js to interact with the {% data variables.product.prodname_dotcom %} REST API in your JavaScript scripts. For more information, see [Scripting with the REST API and JavaScript](/rest/guides/scripting-with-the-rest-api-and-javascript).

1. Create an access token. For example, create a {% data variables.product.pat_generic %} or a {% data variables.product.prodname_github_app %} user access token. You will use this token to authenticate your request, so you should give it any scopes or permissions that are required to access that endpoint. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api) or [Identifying and authorizing users for GitHub Apps](/developers/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps).

   > [!WARNING]
   > Treat your access token like a password.
   >
   > To keep your token secure, you can store your token as a secret and run your script through {% data variables.product.prodname_actions %}. For more information, see the [Using Octokit.js in {% data variables.product.prodname_actions %}](#using-octokitjs-in-github-actions) section.
   {%- ifversion fpt or ghec %}
   >
   You can also store your token as a {% data variables.product.prodname_codespaces %} secret and run your script in {% data variables.product.prodname_codespaces %}. For more information, see [Managing encrypted secrets for your codespaces](/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces).
   {% endif %}
   >
   > If these options are not possible, consider using another CLI service to store your token securely.

1. Install `octokit`. For example, `npm install octokit`. For other ways to install or load `octokit`, see [the Octokit.js README](https://github.com/octokit/octokit.js/#readme).
1. Import `octokit` in your script. For example, `import { Octokit } from "octokit";`. For other ways to import `octokit`, see [the Octokit.js README](https://github.com/octokit/octokit.js/#readme).
1. Create an instance of `Octokit` with your token.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %} Replace `YOUR-TOKEN` with your token.

   ```javascript copy
   const octokit = new Octokit({ {% ifversion ghes %}
     baseUrl: "{% data variables.product.rest_url %}",{% endif %}
     auth: 'YOUR-TOKEN'
   });
   ```

1. Use `octokit.request` to execute your request. Send the HTTP method and path as the first argument. Specify any path, query, and body parameters in an object as the second argument. For more information about parameters, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api#using-parameters).

   For example, in the following request the HTTP method is `GET`, the path is `/repos/{owner}/{repo}/issues`, and the parameters are {% ifversion ghes %}`owner: "REPO-OWNER"` and `repo: "REPO-NAME"`{% else %}`owner: "octocat"` and `repo: "Spoon-Knife"`{% endif %}.{% ifversion ghes %} Replace `REPO-OWNER` with the name of the account that owns the repository, and `REPO-NAME` with the name of the repository.{% endif %}

   ```javascript copy
   await octokit.request("GET /repos/{owner}/{repo}/issues", {
     owner: "{% ifversion ghes %}REPO-OWNER{% else %}octocat{% endif %}",
     repo: "{% ifversion ghes %}REPO-NAME{% else %}Spoon-Knife{% endif %}",
   });
   ```

## Using Octokit.js in {% data variables.product.prodname_actions %}

You can also execute your JavaScript scripts in your {% data variables.product.prodname_actions %} workflows. For more information, see [AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun).

### Authenticating with an access token

{% data variables.product.prodname_dotcom %} recommends that you use the built-in `GITHUB_TOKEN` instead of creating a token. If this is not possible, store your token as a secret and replace `GITHUB_TOKEN` in the example below with the name of your secret. For more information about `GITHUB_TOKEN`, see [AUTOTITLE](/actions/security-guides/automatic-token-authentication). For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).

The following example workflow:

1. Checks out the repository content
1. Sets up Node.js
1. Installs `octokit`
1. Stores the value of `GITHUB_TOKEN` as an environment variable called `TOKEN` and runs `.github/actions-scripts/use-the-api.mjs`, which can access that environment variable as `process.env.TOKEN`

```yaml
on:
  workflow_dispatch:
jobs:
  use_api_via_script:
    runs-on: ubuntu-latest
    permissions:
      issues: read
    steps:
      - name: Check out repo content
        uses: {% data reusables.actions.action-checkout %}

      - name: Setup Node
        uses: {% data reusables.actions.action-setup-node %}
        with:
          node-version: '16.17.0'
          cache: npm

      - name: Install dependencies
        run: npm install octokit

      - name: Run script
        run: |
          node .github/actions-scripts/use-the-api.mjs
        env:
          TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
```

The following is an example JavaScript script with the file path `.github/actions-scripts/use-the-api.mjs`.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-OWNER` with the name of the account that owns the repository. Replace `REPO-NAME` with the name of the repository.{% endif %}

```javascript
import { Octokit } from "octokit"

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",{% endif %}
  auth: process.env.TOKEN
});

try {
  const result = await octokit.request("GET /repos/{owner}/{repo}/issues", {
      owner: "{% ifversion ghes %}REPO-OWNER{% else %}octocat{% endif %}",
      repo: "{% ifversion ghes %}REPO-NAME{% else %}Spoon-Knife{% endif %}",
    });

  const titleAndAuthor = result.data.map(issue => {title: issue.title, authorID: issue.user.id})

  console.log(titleAndAuthor)

} catch (error) {
  console.log(`Error! Status: ${error.status}. Message: ${error.response.data.message}`)
}
```

### Authenticating with a {% data variables.product.prodname_github_app %}

If you are authenticating with a {% data variables.product.prodname_github_app %}, you can create an installation access token within your workflow:

1. Store your {% data variables.product.prodname_github_app %}'s ID as a configuration variable. In the following example, replace `APP_ID` with the name of the configuration variable. You can find your app ID on the settings page for your app or through the App API. For more information, see [AUTOTITLE](/rest/apps/apps#get-an-app). For more information about configuration variables, see [AUTOTITLE](/actions/learn-github-actions/variables#defining-configuration-variables-for-multiple-workflows).
1. Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`.) In the following example, replace `APP_PEM` with the name of the secret. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps). For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).
1. Add a step to generate a token, and use that token instead of `GITHUB_TOKEN`. Note that this token will expire after 60 minutes. For example:

   ```yaml
   on:
     workflow_dispatch:
   jobs:
     use_api_via_script:
       runs-on: ubuntu-latest
       steps:
         - name: Check out repo content
           uses: {% data reusables.actions.action-checkout %}

         - name: Setup Node
           uses: {% data reusables.actions.action-setup-node %}
           with:
             node-version: '16.17.0'
             cache: npm

         - name: Install dependencies
           run: npm install octokit

         - name: Generate token
           id: generate-token
           uses: actions/create-github-app-token@v2
           with:
             app-id: {% raw %}${{ vars.APP_ID }}{% endraw %}
             private-key: {% raw %}${{ secrets.APP_PEM }}{% endraw %}

         - name: Run script
           run: |
             node .github/actions-scripts/use-the-api.mjs
           env:
             TOKEN: {% raw %}${{ steps.generate-token.outputs.token }}{% endraw %}

   ```

{% endjavascript %}

{% curl %}

## Using `curl` in the command line

> [!NOTE]
> If you want to make API requests from the command line, {% data variables.product.prodname_dotcom %} recommends that you use {% data variables.product.prodname_cli %}, which simplifies authentication and requests. For more information about getting started with the REST API using {% data variables.product.prodname_cli %}, see the {% data variables.product.prodname_cli %} version of this article.

1. Install `curl` if it isn't already installed on your machine. To check if `curl` is installed, execute `curl --version` in the command line. If the output provides information about the version of `curl`, that means `curl` is installed. If you get a message similar to `command not found: curl`, you need to download and install `curl`. For more information, see [the curl project download page](https://curl.se/download.html).

1. Create an access token. For example, create a {% data variables.product.pat_generic %} or a {% data variables.product.prodname_github_app %} user access token. You will use this token to authenticate your request, so you should give it any scopes or permissions that are required to access the endpoint. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

   > [!WARNING]
   > Treat your access token like a password.
   {%- ifversion fpt or ghec %}
   >
   > To keep your token secure, you can store your token as a {% data variables.product.prodname_codespaces %} secret and use the command line through {% data variables.product.prodname_codespaces %}. For more information, see [Managing encrypted secrets for your codespaces](/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces).
   {% endif %}
   >
   > You can also use {% data variables.product.prodname_cli %} instead of `curl`. {% data variables.product.prodname_cli %} will take care of authentication for you. For more information, see the {% data variables.product.prodname_cli %} version of this page.
   >
   > If these options are not possible, consider using another CLI service to store your token securely.

1. Use the `curl` command to make your request. Pass your token in an `Authorization` header.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-OWNER` with the name of the account that owns the repository. Replace `REPO-NAME` with the name of the repository.{% endif %} Replace `YOUR-TOKEN` with your token.

   ```shell copy
   curl --request GET \
   --url "{% data variables.product.rest_url %}{% data variables.rest.example_request_url %}" \
   --header "Accept: application/vnd.github+json" \
   --header "Authorization: Bearer YOUR-TOKEN"
   ```

   > [!NOTE]
   > {% data reusables.getting-started.bearer-vs-token %}

## Using `curl` commands in {% data variables.product.prodname_actions %}

You can also use `curl` commands in your {% data variables.product.prodname_actions %} workflows.

### Authenticating with an access token

{% data variables.product.prodname_dotcom %} recommends that you use the built-in `GITHUB_TOKEN` instead of creating a token. If this is not possible, store your token as a secret and replace `GITHUB_TOKEN` in the example below with the name of your secret. For more information about `GITHUB_TOKEN`, see [AUTOTITLE](/actions/security-guides/automatic-token-authentication). For more information about secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).

{% ifversion ghes %}In the following example, replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-OWNER` with the name of the account that owns the repository. Replace `REPO-NAME` with the name of the repository.{% endif %}

```yaml copy
on:
  workflow_dispatch:
jobs:
  use_api:
    runs-on: ubuntu-latest
    permissions:
      issues: read
    steps:
      - env:
          GH_TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
        run: |
          curl --request GET \
          --url "{% data variables.product.rest_url %}{% data variables.rest.example_request_url %}" \
          --header "Accept: application/vnd.github+json" \
          --header "Authorization: Bearer $GH_TOKEN"
```

### Authenticating with a {% data variables.product.prodname_github_app %}

If you are authenticating with a {% data variables.product.prodname_github_app %}, you can create an installation access token within your workflow:

1. Store your {% data variables.product.prodname_github_app %}'s ID as a configuration variable. In the following example, replace `APP_ID` with the name of the configuration variable. You can find your app ID on the settings page for your app or through the App API. For more information, see [AUTOTITLE](/rest/apps/apps#get-an-app). For more information about configuration variables, see [AUTOTITLE](/actions/learn-github-actions/variables#defining-configuration-variables-for-multiple-workflows).
1. Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`.) In the following example, replace `APP_PEM` with the name of the secret. For more information, see [AUTOTITLE](/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps). For more information about storing secrets, see [AUTOTITLE](/actions/security-guides/encrypted-secrets).
1. Add a step to generate a token, and use that token instead of `GITHUB_TOKEN`. Note that this token will expire after 60 minutes. {% ifversion fpt or ghec %}For example:{% else %}In the following example, replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-OWNER` with the name of the account that owns the repository. Replace `REPO-NAME` with the name of the repository.{% endif %}

   ```yaml copy
   on:
     workflow_dispatch:
   jobs:
     use_api:
       runs-on: ubuntu-latest
       steps:
         - name: Generate token
           id: generate-token
           uses: actions/create-github-app-token@v2
           with:
             app-id: {% raw %}${{ vars.APP_ID }}{% endraw %}
             private-key: {% raw %}${{ secrets.APP_PEM }}{% endraw %}

         - name: Use API
           env:
             GH_TOKEN: {% raw %}${{ steps.generate-token.outputs.token }}{% endraw %}
           run: |
             curl --request GET \
             --url "{% data variables.product.rest_url %}{% data variables.rest.example_request_url %}" \
             --header "Accept: application/vnd.github+json" \
             --header "Authorization: Bearer $GH_TOKEN"

   ```

{% endcurl %}

## Next steps

For a more detailed guide, see [Getting started with the REST API](/rest/guides/getting-started-with-the-rest-api).


---

<!-- source: https://docs.github.com/en/rest/rate-limit -->

---
title: REST API endpoints for rate limits
shortTitle: Rate limit
allowTitleToDifferFromFilename: true
intro: Use the REST API to check your current rate limit status.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /rate-limit
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/rate-limit/rate-limit -->

---
title: REST API endpoints for rate limits
shortTitle: Rate limit
allowTitleToDifferFromFilename: true
intro: Use the REST API to check your current rate limit status.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/rate-limit
autogenerated: rest
category:
  - Learn about the REST API
---

## About rate limits

You can check your current rate limit status at any time. For more information about rate limit rules, see [AUTOTITLE](/rest/overview/rate-limits-for-the-rest-api).

The REST API for searching items has a custom rate limit that is separate from the rate limit governing the other REST API endpoints. For more information, see [AUTOTITLE](/rest/search/search). The GraphQL API also has a custom rate limit that is separate from and calculated differently than rate limits in the REST API. For more information, see [AUTOTITLE](/graphql/overview/resource-limitations#rate-limit). For these reasons, the API response categorizes your rate limit. Under `resources`, you'll see objects relating to different categories:

* The `core` object provides your rate limit status for all non-search-related resources in the REST API.

* The `search` object provides your rate limit status for the REST API for searching (excluding code searches). For more information, see [AUTOTITLE](/rest/search/search).

* The `code_search` object provides your rate limit status for the REST API for searching code. For more information, see [AUTOTITLE](/rest/search/search#search-code).

* The `graphql` object provides your rate limit status for the GraphQL API.

* The `integration_manifest` object provides your rate limit status for the `POST /app-manifests/{code}/conversions` operation. For more information, see [AUTOTITLE](/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app-from-a-manifest#3-you-exchange-the-temporary-code-to-retrieve-the-app-configuration).

* The `dependency_snapshots` object provides your rate limit status for submitting snapshots to the dependency graph. For more information, see [AUTOTITLE](/rest/dependency-graph).

* The `code_scanning_upload` object provides your rate limit status for uploading SARIF results to code scanning. For more information, see [AUTOTITLE](/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github).

* The `actions_runner_registration` object provides your rate limit status for registering self-hosted runners in {% data variables.product.prodname_actions %}. For more information, see [AUTOTITLE](/rest/actions/self-hosted-runners).

For more information on the headers and values in the rate limit response, see [AUTOTITLE](/rest/overview/rate-limits-for-the-rest-api).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/reactions -->

---
title: REST API endpoints for reactions
shortTitle: Reactions
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with reactions on {% data
  variables.product.prodname_dotcom %}.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /reactions
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/reactions/reactions -->

---
title: REST API endpoints for reactions
shortTitle: Reactions
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to interact with reactions on {% data
  variables.product.prodname_dotcom %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/reactions
autogenerated: rest
category:
  - Manage issues, pull requests, and projects
---

## About reactions

You can create and manage reactions to comments, issues, pull requests, and discussions on {% data variables.product.prodname_dotcom %}. When creating a reaction, the allowed values for the `content` parameter are as follows (with the corresponding emoji for reference):

{% data reusables.repositories.reaction_list %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/README -->

# REST
 The `/content/rest` directory is where the GitHub REST API docs live!
 
 * The `/content/rest/about-the-rest-api`, `/content/rest/guides` and `/content/rest/using-the-rest-api` directories contain regular articles. These are human-editable.
* The remaining directories contain an article for each group of endpoints in the GitHub REST API. Most of the content in this directory is rendered using `include` tags.

  The content rendered by `include` tags is sourced from the `/src/rest/data` directory, which is automatically generated from the API source code internally in GitHub, and should not be edited by a human. For more information, see the [`/src/rest/README.md`](/src/rest/README.md).

  **We cannot accept changes to content that is rendered by `include` tags. However, you can open an issue describing the changes you would like to see.**


---

<!-- source: https://docs.github.com/en/rest/releases/assets -->

---
title: REST API endpoints for release assets
shortTitle: Release assets
intro: Use the REST API to manage release assets.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/releases -->

---
title: REST API endpoints for releases and release assets
shortTitle: Releases
intro: 'Use the REST API to create, modify, and delete releases and release assets.'
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /releases
  - /assets
redirect_from:
  - /rest/reference/releases
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/releases/releases -->

---
title: REST API endpoints for releases
shortTitle: Releases
allowTitleToDifferFromFilename: true
intro: 'Use the REST API to create, modify, and delete releases.'
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

> [!NOTE]
> These endpoints replace the endpoints to manage downloads. You can retrieve the download count and browser download URL from these endpoints.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/attestations -->

---
title: REST API endpoints for repository attestations
shortTitle: Attestations
intro: Use the REST API to manage repository attestations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage repositories and code
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/autolinks -->

---
title: REST API endpoints for repository autolinks
allowTitleToDifferFromFilename: true
shortTitle: Autolinks
intro: Use the REST API to add autolinks to external resources.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

## About repository autolinks

To help streamline your workflow, you can use the REST API to add autolinks to external resources like JIRA issues and Zendesk tickets. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-autolinks-to-reference-external-resources).

{% data variables.product.prodname_github_apps %} require repository administration permissions with read or write access to use these endpoints.

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/bypass-requests -->

---
title: REST API endpoints for repository push rule bypass requests
shortTitle: Bypass requests
intro: Use the REST API to manage repository push rule bypass requests.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.17'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage repositories and code
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/contents -->

---
title: REST API endpoints for repository contents
allowTitleToDifferFromFilename: true
shortTitle: Contents
intro: >-
  Use the REST API to create, modify, and delete Base64 encoded content in a
  repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/custom-properties -->

---
title: REST API endpoints for custom properties
shortTitle: Custom properties
intro: Use the REST API to list the custom properties assigned to a repository by the organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/repos/properties
category:
  - Manage repositories and code
---

## About custom properties

You can use the REST API to view the custom properties that were assigned to a repository by the organization that owns the repository. For more information, see [AUTOTITLE](/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization). For more information about the REST API endpoints to manage custom properties, see [AUTOTITLE](/rest/orgs/properties).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/forks -->

---
title: REST API endpoints for forks
shortTitle: Forks
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage repository forks.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos -->

---
title: REST API endpoints for repositories
shortTitle: Repositories
intro: >-
  Use the REST API to create, manage and control the workflow of public and
  private {% data variables.product.github %} repositories.
allowTitleToDifferFromFilename: true
redirect_from:
  - /v3/repos
  - /rest/reference/repos
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /attestations
  - /autolinks
  - /bypass-requests
  - /contents
  - /custom-properties
  - /forks
  - /lfs
  - /repos
  - /rule-suites
  - /rules
  - /tags
  - /webhooks
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/lfs -->

---
title: REST API endpoints for Git LFS
shortTitle: Git LFS
intro: >-
  Use the REST API to enable or disable {% data
  variables.large_files.product_name_long %} (LFS) for a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---

## About {% data variables.large_files.product_name_short %}

You can use {% data variables.large_files.product_name_short %} to store large files in a Git repository. The REST API allows you to enable or disable the feature for an individual repository. For more information about {% data variables.large_files.product_name_short %}, see [AUTOTITLE](/repositories/working-with-files/managing-large-files/about-git-large-file-storage).

People with admin access to a repository can use these endpoints.

{% ifversion ghec %}

Usage of {% data variables.large_files.product_name_short %} is subject to billing. For more information, see [AUTOTITLE](/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/about-billing-for-git-large-file-storage).

If you want to use these endpoints for a repository that belongs to an organization, you must have admin access to the repository (which can be inherited as an organization owner), and your role must also provide you with access to the organization's billing.

* If repository is owned by an organization on {% data variables.product.prodname_team %}, you must be an organization owner or billing manager. For more information, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners).
* If repository is owned by an organization that is on {% data variables.product.prodname_ghe_cloud %} and is not owned by an enterprise account, you must be an organization owner or billing manager. For more information, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners).
* If repository is owned by an organization that is owned by an enterprise account, you must be an enterprise owner or billing manager. For more information, see [AUTOTITLE](/admin/user-management/managing-users-in-your-enterprise/roles-in-an-enterprise#enterprise-owners).

{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/repos -->

---
title: REST API endpoints for repositories
shortTitle: Repositories
intro: >-
  Use the REST API to manage repositories on {% data
  variables.product.company_short %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/rule-suites -->

---
title: REST API endpoints for rule suites
shortTitle: Rule suites
intro: Use the REST API to manage rule suites for repositories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage repositories and code
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/rules -->

---
title: REST API endpoints for rules
shortTitle: Rules
intro: >-
  Use the REST API to manage rulesets for repositories. Rulesets control how
  people can interact with selected branches and tags in a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
redirect_from:
  - /early-access/repositories/using-the-rest-api-to-manage-repository-rulesets
category:
  - Manage repositories and code
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/tags -->

---
title: REST API endpoints for repository tags
allowTitleToDifferFromFilename: true
shortTitle: Tags
intro: Use the REST API to manage tags for a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghes: <=3.20
autogenerated: rest
category:
  - Manage repositories and code
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/repos/webhooks -->

---
title: REST API endpoints for repository webhooks
shortTitle: Webhooks
intro: Use the REST API to create and manage webhooks for your repositories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
redirect_from:
  - /rest/webhooks/repo-deliveries
  - /rest/webhooks/repo-config
  - /rest/webhooks/repos
  - /rest/webhooks
category:
  - Manage repositories and code
---

## About repository webhooks

Repository webhooks allow your server to receive HTTP `POST` payloads whenever certain events happen in a repository. For more information, see [AUTOTITLE](/webhooks).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/scim -->

---
title: REST API endpoints for SCIM
shortTitle: SCIM
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to control and manage your GitHub organization members' access
  with SCIM.
versions:
  ghec: '*'
children:
  - /scim
autogenerated: rest
---

{% data reusables.scim.organization-rest-api-ghec-deployment-option %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/scim/scim -->

---
title: REST API endpoints for SCIM
shortTitle: SCIM
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to control and manage your GitHub organization members' access
  with SCIM.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
redirect_from:
  - /rest/reference/scim
autogenerated: rest
category:
  - Administer enterprises and billing
---

{% data reusables.scim.organization-rest-api-ghec-deployment-option %}

## About SCIM

### SCIM Provisioning for Organizations

These endpoints are used by SCIM-enabled Identity Providers (IdPs) to automate provisioning of {% data variables.product.github %} organization membership and are based on version 2.0 of the [SCIM standard](http://www.simplecloud.info/). IdPs should use the base URL `{% data variables.product.rest_url %}/scim/v2/organizations/{org}/` for {% data variables.product.github %} SCIM endpoints.

> [!NOTE]
> * These endpoints are only available for individual organizations that use {% data variables.product.prodname_ghe_cloud %} with SAML SSO enabled. For more information about SCIM, see [AUTOTITLE](/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/about-scim-for-organizations). For more information about authorizing a token for a SAML SSO organization, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).
> * These endpoints cannot be used with an enterprise account or with an {% data variables.enterprise.prodname_emu_org %}.

### Authentication

You must authenticate as an owner of a {% data variables.product.github %} organization to use these endpoints. The REST API expects an OAuth 2.0 Bearer token (for example, a {% data variables.product.prodname_github_app %} user access token) to be included in the `Authorization` header. If you use a {% data variables.product.pat_v1 %} for authentication, it must have the `admin:org` scope and you must also [authorize it for use with your SAML SSO organization](/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

### Matching SAML and SCIM attributes

To successfully link a {% data variables.product.github %} user account to a SCIM identity in an organization, specific attributes from your Identity Provider's SAML response and SCIM API provisioning call must match for a user.

#### Microsoft Entra ID for SAML

When using Entra ID (previously known as Azure AD) for SAML, the following SAML attribute and SCIM attribute must match.

| SAML attribute | Matching SCIM attribute |
| :- | :- |
| `http://schemas.microsoft.com/identity/claims/objectidentifier` | `externalId` |

#### Other IdPs for SAML

When using other IdPs for SAML, the following SAML claims and SCIM attribute must match.

| SAML attribute | Matching SCIM attribute |
| :- | :- |
| `NameID` | `userName` |

There are two different ways a {% data variables.product.github %} user account can get linked to a SCIM identity in an organization when these SAML/SCIM attributes match:

1. For users who are not yet members of the organization:
   * The IdP sends a SCIM provisioning call to {% data variables.product.github %} for a user who is not a member of an organization. This generates an organization invitation and an unlinked SCIM identity in the organization.
   * User authenticates via SAML in the organization.
   * {% data variables.product.github %} automatically links the SAML and SCIM identity to the new user account in the organization.

1. For existing organization members:
   * The IdP sends a SCIM provisioning call to {% data variables.product.github %} for a user who is already a member of the organization.
   * If the organization member does not have a linked SAML identity in the organization, this generates an organization invitation and an unlinked SCIM identity in the organization. User authenticates via SAML in the organization to link their SAML and SCIM identity.
   * If the organization member has a linked SAML identity in the organization, {% data variables.product.github %} automatically links the SCIM identity to the existing user account in the organization. No organization invite is created.

Ensuring that a user gets properly linked to their SCIM identity in the organization can help prevent unexpected issues with SCIM deprovisioning when the user's access to the app is removed on the IdP side. For more information on auditing the linked SCIM identities in an organization, see [AUTOTITLE](/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/troubleshooting-identity-and-access-management-for-your-organization#auditing-organization-members-on-github)

### Supported SCIM User attributes

Name | Type | Description
-----|------|--------------
`userName`|`string` | The username for the user.
`name.givenName`|`string` | The first name of the user.
`name.familyName`|`string` | The last name of the user.
`emails` | `array` | List of user emails.
`externalId` | `string` | This identifier is generated by the SAML provider, and is used as a unique ID by the SAML provider to match against a GitHub user. You can find the `externalID` for a user either at the SAML provider, or using the [List SCIM provisioned identities](#list-scim-provisioned-identities) endpoint and filtering on other known attributes, such as a user's GitHub username or email address.
`id` | `string` | Identifier generated by the GitHub SCIM endpoint.
`active` | `boolean` | Used to indicate whether the identity is active (true) or should be deprovisioned (false).

> [!NOTE]
> These endpoints are case sensitive. For example, the first letter in the `Users` endpoint must be capitalized:
>
> ```shell
> GET /scim/v2/organizations/{org}/Users/{scim_user_id}
> ```

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/search -->

---
title: REST API endpoints for search
shortTitle: Search
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to search for specific items on {% data
  variables.product.github %}.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /search
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/search/search -->

---
title: REST API endpoints for search
shortTitle: Search
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to search for specific items on {% data
  variables.product.github %}.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/search
autogenerated: rest
category:
  - Manage repositories and code
---

## About search

You can use the REST API to search for the specific item you want to find. For example, you can find a user or a specific file in a repository. Think of it the way you think of performing a search on Google. It's designed to help you find the one result you're looking for (or maybe the few results you're looking for). Just like searching on Google, you sometimes want to see a few pages of search results so that you can find the item that best meets your needs. To satisfy that need, the {% data variables.product.github %} REST API provides **up to 1,000 results for each search**.

You can narrow your search using queries. To learn more about the search query syntax, see [AUTOTITLE](/rest/search/search#constructing-a-search-query).

### Ranking search results

Unless another sort option is provided as a query parameter, results are sorted by best match in descending order. Multiple factors are combined to boost the most relevant item to the top of the result list.

### Rate limit

{% data reusables.enterprise.rate_limit %}

The REST API has a custom rate limit for searching. For authenticated requests, you can make up to
30 requests per minute{% ifversion fpt or ghec %} for all search endpoints except for the [Search code](/rest/search/search#search-code) endpoint. The [Search code](/rest/search/search#search-code) endpoint requires you to authenticate and limits you to 9 requests per minute{% endif %}. For unauthenticated requests, the rate limit allows you to make up to 10 requests per minute.

For information about how to determine your current rate limit status, see [Rate Limit](/rest/rate-limit/rate-limit).

### Constructing a search query

Each endpoint for searching uses [query parameters](https://en.wikipedia.org/wiki/Query_string) to perform searches on {% data variables.product.github %}. See the individual endpoints for examples that include the endpoint and query parameters.

A query can contain any combination of search qualifiers supported on {% data variables.product.github %}. The format of the search query is:

```text
SEARCH_KEYWORD_1 SEARCH_KEYWORD_N QUALIFIER_1 QUALIFIER_N
```

For example, if you wanted to search for all _repositories_ owned by `defunkt` that
contained the word `GitHub` and `Octocat` in the README file, you would use the
following query with the _search repositories_ endpoint:

```text
GitHub Octocat in:readme user:defunkt
```

**Note:** Be sure to use your language's preferred HTML-encoder to construct your query strings. For example:

```javascript
// JavaScript
const queryString = 'q=' + encodeURIComponent('GitHub Octocat in:readme user:defunkt');
```

See [AUTOTITLE](/search-github/searching-on-github)
for a complete list of available qualifiers, their format, and an example of
how to use them. For information about how to use operators to match specific
quantities, dates, or to exclude results, see [AUTOTITLE](/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax).

### Limitations on query length

You cannot use queries that:
* Are longer than 256 characters (not including operators or qualifiers).
* Have more than five `AND`, `OR`, or `NOT` operators.

These search queries will return a "Validation failed" error message.

### Search scope limits

To keep the REST API fast for everyone, we limit the number of repositories a query will search through. The REST API will find up to 4,000 repositories that match your filters and return results from those repositories.

### Timeouts and incomplete results

To keep the REST API fast for everyone, we limit how long any individual query
can run. For queries that [exceed the time limit](https://developer.github.com/changes/2014-04-07-understanding-search-results-and-potential-timeouts/),
the API returns the matches that were already found prior to the timeout, and
the response has the `incomplete_results` property set to `true`.

Reaching a timeout does not necessarily mean that search results are incomplete.
More results might have been found, but also might not.

### Access errors or missing search results

You need to successfully authenticate and have access to the repositories in your search queries, otherwise, you'll see a `422 Unprocessable Entry` error with a "Validation Failed" message. For example, your search will fail if your query includes `repo:`, `user:`, or `org:` qualifiers that request resources that you don't have access to when you sign in on {% data variables.product.prodname_dotcom %}.

When your search query requests multiple resources, the response will only contain the resources that you have access to and will **not** provide an error message listing the resources that were not returned.

For example, if your search query searches for the `octocat/test` and `codertocat/test` repositories, but you only have access to `octocat/test`, your response will show search results for `octocat/test` and nothing for `codertocat/test`. This behavior mimics how search works on {% data variables.product.prodname_dotcom %}.

### Text match metadata

On {% data variables.product.prodname_dotcom %}, you can use the context provided by code snippets and highlights in search results. The endpoints for searching return additional metadata that allows you to highlight the matching search terms when displaying search results.

Requests can opt to receive those text fragments in the response, and every fragment is accompanied by numeric offsets identifying the exact location of each matching search term.

To get this metadata in your search results, specify the `text-match` media type in your `Accept` header.

```shell
application/vnd.github.text-match+json
```

When you provide the `text-match` media type, you will receive an extra key in the JSON payload called `text_matches` that provides information about the position of your search terms within the text and the `property` that includes the search term. Inside the `text_matches` array, each object includes
the following attributes:

Name | Description
-----|-----------|
`object_url` | The URL for the resource that contains a string property matching one of the search terms.
`object_type` | The name for the type of resource that exists at the given `object_url`.
`property` | The name of a property of the resource that exists at `object_url`. That property is a string that matches one of the search terms. (In the JSON returned from `object_url`, the full content for the `fragment` will be found in the property with this name.)
`fragment` | A subset of the value of `property`. This is the text fragment that matches one or more of the search terms.
`matches` | An array of one or more search terms that are present in `fragment`. The indices (i.e., "offsets") are relative to the fragment. (They are not relative to the _full_ content of `property`.)

#### Example

Using a `curl` command, and the [example issue search](#search-issues-and-pull-requests) above, our API
request would look like this:

``` shell
curl -H 'Accept: application/vnd.github.text-match+json' \
'{% data variables.product.rest_url %}/search/issues?q=windows+label:bug \
+language:python+state:open&sort=created&order=asc'
```

The response will include a `text_matches` array for each search result. In the JSON below, we have two objects in the `text_matches` array.

The first text match occurred in the `body` property of the issue. We see a fragment of text from the issue body. The search term (`windows`) appears twice within that fragment, and we have the indices for each occurrence.

The second text match occurred in the `body` property of one of the issue's comments. We have the URL for the issue comment. And of course, we see a fragment of text from the comment body. The search term (`windows`) appears once within that fragment.

```json
{
  "text_matches": [
    {
      "object_url": "https://api.github.com/repositories/215335/issues/132",
      "object_type": "Issue",
      "property": "body",
      "fragment": "comprehensive windows font I know of).\n\nIf we can find a commonly
      distributed windows font that supports them then no problem (we can use html
      font tags) but otherwise the '(21)' style is probably better.\n",
      "matches": [
        {
          "text": "windows",
          "indices": [
            14,
            21
          ]
        },
        {
          "text": "windows",
          "indices": [
            78,
            85
          ]
        }
      ]
    },
    {
      "object_url": "https://api.github.com/repositories/215335/issues/comments/25688",
      "object_type": "IssueComment",
      "property": "body",
      "fragment": " right after that are a bit broken IMHO :). I suppose we could
      have some hack that maxes out at whatever the font does...\n\nI'll check
      what the state of play is on Windows.\n",
      "matches": [
        {
          "text": "Windows",
          "indices": [
            163,
            170
          ]
        }
      ]
    }
  ]
}
```

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/secret-scanning/alert-dismissal-requests -->

---
title: Alert dismissal requests
shortTitle: Alert dismissal requests
intro: Use the REST API to manage alert dismissal requests for secret scanning.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.18'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/secret-scanning/delegated-bypass -->

---
title: REST API endpoints for push protection bypass requests
shortTitle: Push protection bypass
intro: >-
  Use the REST API to manage push protection bypass requests for secret
  scanning.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '>=3.17'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/secret-scanning -->

---
title: REST API endpoints for secret scanning
shortTitle: Secret scanning
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve and update secret alerts from a repository.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
children:
  - /alert-dismissal-requests
  - /delegated-bypass
  - /push-protection
  - /secret-scanning
autogenerated: rest
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/secret-scanning/push-protection -->

---
title: REST API endpoints for secret scanning push protection
shortTitle: Push protection
intro: Use the REST API to manage secret scanning push protection.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '>=3.19'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/secret-scanning/secret-scanning -->

---
title: REST API endpoints for secret scanning
shortTitle: Secret scanning
allowTitleToDifferFromFilename: true
intro: Use the REST API to retrieve and update secret alerts from a repository.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /rest/reference/secret-scanning
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

{% data reusables.secret-scanning.api-beta %}

## About secret scanning

You can use the API to:

* Enable or disable {% data variables.product.prodname_secret_scanning %} and push protection for a repository. For more information, see [AUTOTITLE](/rest/repos/repos#update-a-repository) and expand the "Properties of the `security_and_analysis` object" section.
* Retrieve and update {% data variables.secret-scanning.alerts %} from a repository. For further details, see the sections below.

For more information about {% data variables.product.prodname_secret_scanning %}, see [AUTOTITLE](/code-security/secret-scanning/introduction/about-secret-scanning).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/security-advisories/global-advisories -->

---
title: REST API endpoints for global security advisories
shortTitle: Global security advisories
intro: Use the REST API to view global security advisories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Secure code and manage vulnerabilities
---

{% ifversion ghes %}

> [!NOTE]
> To use these endpoints, an administrator must enable {% data variables.product.prodname_github_connect %} for {% data variables.location.product_location %}. For more information, see [AUTOTITLE](/code-security/security-advisories/global-security-advisories/browsing-security-advisories-in-the-github-advisory-database#accessing-the-local-advisory-database-on-your-github-enterprise-server-instance).

{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/security-advisories -->

---
title: REST API endpoints for security advisories
shortTitle: Security advisories
intro: Use the REST API to view and manage security advisories.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '>=3.11'
children:
  - /global-advisories
  - /repository-advisories
autogenerated: rest
allowTitleToDifferFromFilename: true
---


<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/security-advisories/repository-advisories -->

---
title: REST API endpoints for repository security advisories
shortTitle: Repository security advisories
allowTitleToDifferFromFilename: true
intro: Use the REST API to view and manage repository security advisories.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
category:
  - Secure code and manage vulnerabilities
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/teams/external-groups -->

---
title: REST API endpoints for external groups
shortTitle: External groups
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to view the external identity provider groups that are
  available to your organization and manage the connection between external
  groups and teams in your organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

## About external groups

{% data reusables.scim.ghes-beta-note %}

To use these endpoints, the authenticated user must be a team maintainer or an owner of the organization associated with the team.

{% ifversion ghec %}

> [!NOTE]
> * These endpoints are only available for organizations that are part of an enterprise using {% data variables.product.prodname_emus %}. For more information, see [AUTOTITLE](/admin/identity-and-access-management/using-enterprise-managed-users-for-iam/about-enterprise-managed-users).
> * If your organization uses team synchronization, you can use the API to manage team synchronization. For more information, see [AUTOTITLE](/rest/teams/team-sync).

{% endif %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/teams -->

---
title: REST API endpoints for teams
shortTitle: Teams
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create and manage teams in your {% data
  variables.product.github %} organization.
redirect_from:
  - /v3/teams
  - /rest/reference/teams
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /external-groups
  - /members
  - /team-sync
  - /teams
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/teams/members -->

---
title: REST API endpoints for team members
intro: >-
  Use the REST API to create and manage membership of teams in your {% data
  variables.product.github %} organization.
allowTitleToDifferFromFilename: true
shortTitle: Members
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

## About team members

{% data reusables.organizations.team-api %}

> [!NOTE]
> When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API to make changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see [AUTOTITLE](/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/managing-team-synchronization-for-your-organization).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/teams/team-sync -->

---
title: REST API endpoints for team synchronization
shortTitle: Team synchronization
intro: >-
  Use the REST API to manage connections between {% data
  variables.product.github %} teams and external identity provider (IdP)
  groups.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  ghec: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage organizations and teams
---

## About team synchronization

To use these endpoints, the authenticated user must be a team maintainer or an owner of the organization associated with the team. The token you use to authenticate will also need to be authorized for use with your IdP (SSO) provider. For more information, see [AUTOTITLE](/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

You can manage {% data variables.product.github %} team members through your IdP with team synchronization. Team synchronization must be enabled to use these endpoints. For more information, see [AUTOTITLE](/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/managing-team-synchronization-for-your-organization).

> [!NOTE]
> These endpoints cannot be used with {% data variables.product.prodname_emus %}. To learn more about managing an {% data variables.enterprise.prodname_emu_org %}, see [AUTOTITLE](/enterprise-cloud@latest/rest/teams/external-groups).

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/teams/teams -->

---
title: REST API endpoints for teams
shortTitle: Teams
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to create and manage teams in your {% data
  variables.product.github %} organization.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage organizations and teams
---

## About teams

{% data reusables.organizations.team-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/attestations -->

---
title: REST API endpoints for artifact attestations
shortTitle: Attestations
intro: Use the REST API to manage artifact attestations.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
autogenerated: rest
allowTitleToDifferFromFilename: true
category:
  - Manage users and activity
---

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/blocking -->

---
title: REST API endpoints for blocking users
shortTitle: Blocking users
intro: Use the REST API to manage blocked users.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage users and activity
---

## About blocking users

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/emails -->

---
title: REST API endpoints for emails
shortTitle: Emails
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage email addresses of authenticated users.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About email administration

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/followers -->

---
title: REST API endpoints for followers
shortTitle: Followers
allowTitleToDifferFromFilename: true
intro: Use the REST API to get information about followers of authenticated users.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About follower administration

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/gpg-keys -->

---
title: REST API endpoints for GPG keys
shortTitle: GPG keys
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage GPG keys of authenticated users.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About user GPG key administration

The data returned in the `public_key` response field is not a GPG formatted key. When a user uploads a GPG key, it is parsed and the cryptographic public key is extracted and stored. This cryptographic key is what the endpoints in this category will return. This key is not suitable for direct use in programs such as GPG.

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users -->

---
title: REST API endpoints for users
shortTitle: Users
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to get public and private information about authenticated
  users.
redirect_from:
  - /v3/users
  - /rest/reference/users
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /attestations
  - /blocking
  - /emails
  - /followers
  - /gpg-keys
  - /keys
  - /social-accounts
  - /ssh-signing-keys
  - /users
autogenerated: rest
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/keys -->

---
title: REST API endpoints for Git SSH keys
shortTitle: Git SSH keys
intro: Use the REST API to manage Git SSH keys of authenticated users.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage users and activity
---

## About Git SSH key administration

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/social-accounts -->

---
title: REST API endpoints for social accounts
shortTitle: Social accounts
allowTitleToDifferFromFilename: true
intro: Use the REST API to manage social accounts of authenticated users.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---

## About social account administration

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/ssh-signing-keys -->

---
title: REST API endpoints for SSH signing keys
shortTitle: SSH signing keys
intro: Use the REST API to manage SSH signing keys of authenticated users.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
allowTitleToDifferFromFilename: true
autogenerated: rest
category:
  - Manage users and activity
---

## About SSH signing key administration

{% data reusables.user-settings.user-api %}

<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/users/users -->

---
title: REST API endpoints for users
shortTitle: Users
allowTitleToDifferFromFilename: true
intro: >-
  Use the REST API to get public and private information about authenticated
  users.
versions: # DO NOT MANUALLY EDIT. CHANGES WILL BE OVERWRITTEN BY A 🤖
  fpt: '*'
  ghec: '*'
  ghes: '*'
autogenerated: rest
category:
  - Manage users and activity
---



<!-- Content after this section is automatically generated -->


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api -->

---
title: Best practices for using the REST API
intro: 'Follow these best practices when using {% data variables.product.company_short %}''s API.'
redirect_from:
  - /guides/best-practices-for-integrators
  - /v3/guides/best-practices-for-integrators
  - /rest/guides/best-practices-for-integrators
  - /rest/guides/best-practices-for-using-the-rest-api
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Best practices
category:
  - Learn about the REST API
---

{% ifversion ghes %}

> [!NOTE]
> Rate limits are only enabled for your instance if your site administrator has enabled them. Even if rate limits are disabled for your instance, you may still want to follow the best practices that are intended to help you avoid exceeding the rate limit. This can help reduce load on your servers.

{% endif %}

## Avoid polling

You should subscribe to webhook events instead of polling the API for data. This will help your integration stay within the API rate limit. For more information, see [AUTOTITLE](/webhooks).

## Make authenticated requests

Authenticated requests have a higher primary rate limit than unauthenticated requests. To avoid exceeding the rate limit, you should make authenticated requests. For more information, see [AUTOTITLE](/rest/overview/rate-limits-for-the-rest-api).

## Avoid concurrent requests

To avoid exceeding secondary rate limits, you should make requests serially instead of concurrently. To achieve this, you can implement a queue system for requests.

## Pause between mutative requests

If you are making a large number of `POST`, `PATCH`, `PUT`, or `DELETE` requests, wait at least one second between each request. This will help you avoid secondary rate limits.

## Handle rate limit errors appropriately

If you receive a rate limit error, you should stop making requests temporarily according to these guidelines:

* If the `retry-after` response header is present, you should not retry your request until after that many seconds has elapsed.
* If the `x-ratelimit-remaining` header is `0`, you should not make another request until after the time specified by the `x-ratelimit-reset` header. The `x-ratelimit-reset` header is in UTC epoch seconds.
* Otherwise, wait for at least one minute before retrying. If your request continues to fail due to a secondary rate limit, wait for an exponentially increasing amount of time between retries, and throw an error after a specific number of retries.

Continuing to make requests while you are rate limited may result in the banning of your integration.

{% data reusables.organizations.api-insights-learn-about %}

## Follow redirects

The {% data variables.product.github %} REST API uses HTTP redirection where appropriate. You should assume that any
request may result in a redirection. Receiving an HTTP redirection is not an error, and you should follow the redirect.

A `301` status code indicates permanent redirection. You should repeat your request to the URL specified by the `location` header. Additionally, you should update your code to use this URL for future requests.

A `302` or `307` status code indicates temporary redirection. You should repeat your request to the URL specified by the `location` header. However, you should not update your code to use this URL for future requests.

Other redirection status codes may be used in accordance with HTTP specifications.

## Do not manually parse URLs

Many API endpoints return URL values for fields in the response body. You should not try to parse these URLs or to predict the structure of future URLs. This can cause your integration to break if {% data variables.product.company_short %} changes the structure of the URL in the future. Instead, you should look for a field that contains the information that you need. For example, the endpoint to create an issue returns an `html_url` field with a value like `https://github.com/octocat/Hello-World/issues/1347` and a `number` field with a value like `1347`. If you need to know the number of the issue, use the `number` field instead of parsing the `html_url` field.

Similarly, you should not try to manually construct pagination queries. Instead, you should use the link headers to determine what pages of results you can request. For more information, see [AUTOTITLE](/rest/guides/using-pagination-in-the-rest-api).

## Use conditional requests if appropriate

Most endpoints return an `etag` header, and many endpoints return a `last-modified` header. You can use the values of these headers to make conditional `GET` requests. If the response has not changed, you will receive a `304 Not Modified` response. Making a conditional request does not count against your primary rate limit if a `304` response is returned and the request was made while correctly authorized with an `Authorization` header.

For example, if a previous request returned an `etag` header value of `644b5b0155e6404a9cc4bd9d8b1ae730`, you can use the `if-none-match` header in a future request:

```shell
curl -H "Authorization: Bearer YOUR-TOKEN" {% data variables.product.rest_url %}/meta --include --header 'if-none-match: "644b5b0155e6404a9cc4bd9d8b1ae730"'
```

For example, if a previous request returned a `last-modified` header value of `Wed, 25 Oct 2023 19:17:59 GMT`, you can use the `if-modified-since` header in a future request:

```shell
curl -H "Authorization: Bearer YOUR-TOKEN" {% data variables.product.rest_url %}/repos/github/docs --include --header 'if-modified-since: Wed, 25 Oct 2023 19:17:59 GMT'
```

Conditional requests for unsafe methods, such as `POST`, `PUT`, `PATCH`, and `DELETE` are not supported unless otherwise noted in the documentation for a specific endpoint.

## Do not ignore errors

You should not ignore repeated `4xx` and `5xx` error codes. Instead, you should ensure that you are correctly interacting with the API. For example, if an endpoint requests a string and you are passing it a numeric value, you will receive a validation error. Similarly, attempting to access an unauthorized or nonexistent endpoint will result in a `4xx` error.

Intentionally ignoring repeated validation errors may result in the suspension of your app for abuse.

## Further reading

* [AUTOTITLE](/webhooks/using-webhooks/best-practices-for-using-webhooks)
* [AUTOTITLE](/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app)


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api -->

---
title: Getting started with the REST API
shortTitle: Getting started
intro: 'Learn how to use the {% data variables.product.github %} REST API.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/guides/getting-started-with-the-rest-api
  - /rest/initialize-the-repo
  - /rest/overview/resources-in-the-rest-api
  - /rest/using-the-rest-api/resources-in-the-rest-api
  - /v3/media
  - /rest/overview/media-types
  - /rest/using-the-rest-api/media-types
category:
  - Learn about the REST API
---

## Introduction

This article describes how to use the {% data variables.product.github %} REST API with {% data variables.product.prodname_cli %}, `curl`, or JavaScript. For a quickstart guide, see [AUTOTITLE](/rest/quickstart).

{% curl %}

{% ifversion ghec %}

Examples in this article send requests to `{% data variables.product.rest_url %}`. If you access {% data variables.product.github %} at a different domain, such as `{% data variables.enterprise.data_residency_example_domain %}`, the endpoint for API requests will reflect that domain. For example: `https://api.octocorp.ghe.com/`.

{% endif %}

{% endcurl %}

## About requests to the REST API

This section describes the elements that make up an API request:

* [HTTP method](#http-method)
* [Path](#path)
* [Headers](#headers)
* [Media types](#media-types)
* [Authentication](#authentication)
* [Parameters](#parameters)

Every request to the REST API includes an HTTP method and a path. Depending on the REST API endpoint, you might also need to specify request headers, authentication information, query parameters, or body parameters.

The REST API reference documentation describes the HTTP method, path, and parameters for every endpoint. It also displays example requests and responses for each endpoint. For more information, see the [REST reference documentation](/rest).

### HTTP method

The HTTP method of an endpoint defines the type of action it performs on a given resource. Some common HTTP methods are `GET`, `POST`, `DELETE`, and `PATCH`. The REST API reference documentation provides the HTTP method for every endpoint.

For example, the HTTP method for the ["List repository issues" endpoint](/rest/issues/issues#list-repository-issues) is `GET`."

Where possible, the {% data variables.product.github %} REST API strives to use an appropriate HTTP method for each action.

* `GET`: Used for retrieving resources.
* `POST`: Used for creating resources.
* `PATCH`: Used for updating properties of resources.
* `PUT`: Used for replacing resources or collections of resources.
* `DELETE`: Used for deleting resources.

### Path

Each endpoint has a path. The REST API reference documentation gives the path for every endpoint. For example, the path for the ["List repository issues" endpoint](/rest/issues/issues#list-repository-issues) is `/repos/{owner}/{repo}/issues`.

The curly brackets `{}` in a path denote path parameters that you need to specify. Path parameters modify the endpoint path and are required in your request. For example, the path parameters for the ["List repository issues" endpoint](/rest/issues/issues#list-repository-issues) are `{owner}` and `{repo}`. To use this path in your API request, replace `{repo}` with the name of the repository where you would like to request a list of issues, and replace `{owner}` with the name of the account that owns the repository.

### Headers

Headers provide extra information about the request and the desired response. Following are some examples of headers that you can use in your requests to the {% data variables.product.prodname_dotcom %} REST API. For an example of a request that uses headers, see [Making a request](#making-a-request).

#### `Accept`

Most {% data variables.product.prodname_dotcom %} REST API endpoints specify that you should pass an `Accept` header with a value of `application/vnd.github+json`. The value of the `Accept` header is a media type. For more information about media types, see [Media types](#media-types).

#### `X-GitHub-Api-Version`

You should use this header to specify a version of the REST API to use for your request. For more information, see [AUTOTITLE](/rest/overview/api-versions).

{% ifversion fpt or ghec %}

#### `User-Agent`

All API requests must include a valid `User-Agent` header. The `User-Agent` header identifies the user or application that is making the request.

{% cli %}

By default, {% data variables.product.prodname_cli %} sends a valid `User-Agent` header. However, {% data variables.product.prodname_dotcom %} recommends using your {% data variables.product.github %} username, or the name of your application, for the `User-Agent` header value. This allows {% data variables.product.prodname_dotcom %} to contact you if there are problems.

{% endcli %}

{% curl %}

By default, `curl` sends a valid `User-Agent` header. However {% data variables.product.prodname_dotcom %} recommends using your {% data variables.product.github %} username, or the name of your application, for the `User-Agent` header value. This allows {% data variables.product.prodname_dotcom %} to contact you if there are problems.

{% endcurl %}

{% javascript %}

If you use the Octokit.js SDK, the SDK will send a valid `User-Agent` header for you. However, {% data variables.product.prodname_dotcom %} recommends using your {% data variables.product.github %} username, or the name of your application, for the `User-Agent` header value. This allows {% data variables.product.prodname_dotcom %} to contact you if there are problems.

{% endjavascript %}

The following is an example `User-Agent` for an app named `Awesome-Octocat-App`:

```shell
User-Agent: Awesome-Octocat-App
```

Requests with no `User-Agent` header will be rejected. If you provide an invalid `User-Agent` header, you will receive a `403 Forbidden` response.

{% endif %}

<!-- Anchor to maintain links to this heading -->
<a name="media-types"></a>

### Media types

You can specify one or more media types by adding them to the `Accept` header of your request. For more information about the `Accept` header, see [`Accept`](#accept).

Media types specify the format of the data you want to consume from the API. Media types are specific to resources, allowing them to change independently and support formats that other resources don't. The documentation for each {% data variables.product.prodname_dotcom %} REST API endpoint will describe the media types that it supports. For more information, see the [AUTOTITLE](/rest).

The most common media types supported by the {% data variables.product.prodname_dotcom %} REST API are `application/vnd.github+json` and `application/json`.

There are custom media types that you can use with some endpoints. For example, the REST API to manage [commits](/rest/commits/commits#get-a-commit) and [pull requests](/rest/pulls/pulls) support the media types `diff`, `patch`, and `sha`. The media types `full`, `raw`, `text`, or `html` are used by some other endpoints.

All custom media types for {% data variables.product.github %} look like this: `application/vnd.github.PARAM+json`, where `PARAM` is the name of the media type. For example, to specify the `raw` media type, you would use `application/vnd.github.raw+json`.

For an example of a request that uses media types, see [Making a request](#making-a-request).

### Authentication

Many endpoints require authentication or return additional information if you are authenticated. Additionally, you can make more requests per hour when you are authenticated.

{% curl %}

To authenticate your request, you will need to provide an authentication token with the required scopes or permissions. There a few different ways to get a token: You can create a {% data variables.product.pat_generic %}, generate a token with a {% data variables.product.prodname_github_app %}, or use the built-in `GITHUB_TOKEN` in a {% data variables.product.prodname_actions %} workflow. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

For an example of a request that uses an authentication token, see [Making a request](#making-a-request).

> [!NOTE]
> If you don't want to create a token, you can use {% data variables.product.prodname_cli %}. {% data variables.product.prodname_cli %} will take care of authentication for you, and help keep your account secure. For more information, see the [{% data variables.product.prodname_cli %} version of this page](/rest/guides/getting-started-with-the-rest-api?tool=cli).

> [!WARNING]
> Treat your access token the same way you would treat your passwords or other sensitive credentials. For more information, see [AUTOTITLE](/rest/overview/keeping-your-api-credentials-secure).

{% endcurl %}

{% cli %}

Although some REST API endpoints are accessible without authentication, {% data variables.product.prodname_cli %} requires you to authenticate before you can use the `api` subcommand to make an API request. Use the `auth login` subcommand to authenticate to {% data variables.product.github %}. For more information, see [Making a request](#making-a-request).

{% endcli %}

{% javascript %}

To authenticate your request, you will need to provide an authentication token with the required scopes or permissions. There a few different ways to get a token: You can create a {% data variables.product.pat_generic %}, generate a token with a {% data variables.product.prodname_github_app %}, or use the built-in `GITHUB_TOKEN` in a {% data variables.product.prodname_actions %} workflow. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

For an example of a request that uses an authentication token, see [Making a request](#making-a-request).

> [!WARNING]
> Treat your access token the same way you would treat your passwords or other sensitive credentials. For more information, see [AUTOTITLE](/rest/overview/keeping-your-api-credentials-secure).

{% endjavascript %}

### Parameters

Many API methods require or allow you to send additional information in parameters in your request. There are a few different types of parameters: Path parameters, body parameters, and query parameters.

#### Path parameters

Path parameters modify the endpoint path. These parameters are required in your request. For more information, see [Path](#path).

#### Body parameters

Body parameters allow you to pass additional data to the API. These parameters can be optional or required, depending on the endpoint. For example, a body parameter may allow you to specify an issue title when creating a new issue, or specify certain settings when enabling or disabling a feature. The documentation for each {% data variables.product.prodname_dotcom %} REST API endpoint will describe the body parameters that it supports. For more information, see the [AUTOTITLE](/rest).

For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) requires that you specify a title for the new issue in your request. It also allows you to optionally specify other information, such as text to put in the issue body, users to assign to the new issue, or labels to apply to the new issue. For an example of a request that uses body parameters, see [Making a request](#making-a-request).

You must authenticate your request to pass body parameters. For more information, see [Authentication](#authentication).

#### Query parameters

Query parameters allow you to control what data is returned for a request. These parameters are usually optional. The documentation for each {% data variables.product.prodname_dotcom %} REST API endpoint will describe any query parameters that it supports. For more information, see the [AUTOTITLE](/rest).

For example, the ["List public events" endpoint](/rest/activity/events#list-public-events) returns thirty issues by default. You can use the `per_page` query parameter to return two issues instead of 30. You can use the `page` query parameter to fetch only the first page of results. For an example of a request that uses query parameters, see [Making a request](#making-a-request).

## Making a request

{% cli %}

This section demonstrates how to make an authenticated request to the {% data variables.product.prodname_dotcom %} REST API using {% data variables.product.prodname_cli %}.

### 1. Setup

Install {% data variables.product.prodname_cli %} on macOS, Windows, or Linux. For more information, see [Installation](https://github.com/cli/cli#installation) in the {% data variables.product.prodname_cli %} repository.

### 2. Authenticate

1. To authenticate to {% data variables.product.github %}, run the following command from your terminal.

   ```shell
   gh auth login
   ```

   You can use the `--scopes` option to specify what scopes you want. If you want to authenticate with a token that you created, you can use the `--with-token` option. For more information, see the [{% data variables.product.prodname_cli %} `auth login` documentation](https://cli.github.com/manual/gh_auth_login).

1. Select where you want to authenticate to:

   * If you access {% data variables.product.github %} at {% data variables.product.prodname_dotcom_the_website %}, select **{% data variables.product.prodname_dotcom_the_website %}**.
   * If you access {% data variables.product.github %} at a different domain, select **Other**, then enter your hostname (for example: `octocorp.ghe.com`).

1. Follow the rest of the on-screen prompts.

   {% data variables.product.prodname_cli %} automatically stores your Git credentials for you when you choose HTTPS as your preferred protocol for Git operations and answer "yes" to the prompt asking if you would like to authenticate to Git with your {% data variables.product.prodname_dotcom %} credentials. This can be useful as it allows you to use Git commands like `git push` and `git pull` without needing to set up a separate credential manager or use SSH.

### 3. Choose an endpoint for your request

1. Choose an endpoint to make a request to. You can explore {% data variables.product.github %}'s [REST API documentation](/rest) to discover endpoints that you can use to interact with {% data variables.product.github %}.
1. Identify the HTTP method and path of the endpoint. You will send these with your request. For more information, see [HTTP method](#http-method) and [Path](#path).

   For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) uses the HTTP method `POST` and the path `/repos/{owner}/{repo}/issues`.

1. Identify any required path parameters. Required path parameters appear in curly brackets `{}` in the path of the endpoint. Replace each parameter placeholder with the desired value. For more information, see [Path](#path).

   For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) uses the path `/repos/{owner}/{repo}/issues`, and the path parameters are `{owner}` and `{repo}`. To use this path in your API request, replace `{repo}` with the name of the repository where you would like to create a new issue, and replace `{owner}` with the name of the account that owns the repository.

### 4. Make a request with {% data variables.product.prodname_cli %}

Use the {% data variables.product.prodname_cli %} `api` subcommand to make your API request. For more information, see the [{% data variables.product.prodname_cli %} `api` documentation](https://cli.github.com/manual/gh_api).

In your request, specify the following options and values:

{%- ifversion not fpt %}
* **--hostname:** If you are authenticated to multiple accounts across {% data variables.product.github %} platforms, specify where you are making the request. For example: `--hostname {% data variables.enterprise.data_residency_example_domain %}`.
{%- endif %}
* **--method** followed by the HTTP method and the path of the endpoint. For more information, see [HTTP method](#http-method) and [Path](#path).
* **--header:**
  * **`Accept`:** Pass the media type in an `Accept` header. To pass multiple media types in an `Accept` header, separate the media types with a comma: `Accept: application/vnd.github+json,application/vnd.github.diff`. For more information, see [`Accept`](#accept) and [Media types](#media-types).
  * **`X-GitHub-Api-Version`:** Pass the API version in a `X-GitHub-Api-Version` header. For more information, see [`X-GitHub-Api-Version`](#x-github-api-version).
* **`-f`** or **`-F`** followed by any body parameters or query parameters in `key=value` format. Use the `-F` option to pass a parameter that is a number, Boolean, or null. Use the `-f` option to pass string parameters.

  Some endpoints use query parameters that are arrays. To send an array in the query string, use the query parameter once per array item, and append `[]` after the query parameter name. For example, to provide an array of two repository IDs, use `-f repository_ids[]=REPOSITORY_A_ID -f repository_ids[]=REPOSITORY_B_ID`.

  If you do not need to specify any body parameters or query parameters in your request, omit this option. For more information, see [Body parameters](#body-parameters) and [Query parameters](#query-parameters). For examples, see [Example request using body parameters](#example-request-using-body-parameters) and [Example request using query parameters](#example-request-using-query-parameters).
{%- ifversion not fpt %}
* **--hostname:** If you are authenticated to multiple accounts across {% data variables.product.github %} platforms, specify where you are making the request. For example: `--hostname {% data variables.enterprise.data_residency_example_domain %}`.
{%- endif %}

#### Example request

The following example request uses the ["Get Octocat" endpoint](/rest/meta/meta#get-octocat) to return the octocat as ASCII art.

```shell copy
gh api --method GET /octocat \
--header 'Accept: application/vnd.github+json' \
--header "X-GitHub-Api-Version: {{ defaultRestApiVersion }}"
```

#### Example request using query parameters

The ["List public events" endpoint](/rest/activity/events#list-public-events) returns thirty issues by default. The following example uses the `per_page` query parameter to return two issues instead of 30, and the `page` query parameter to fetch only the first page of results.

```shell copy
gh api --method GET /events -F per_page=2 -F page=1
--header 'Accept: application/vnd.github+json' \
```

#### Example request using body parameters

The following example uses the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) to create a new issue in {% ifversion ghes %}a specified{% else %}the octocat/Spoon-Knife{% endif %} repository.{% ifversion ghes %} Replace `REPO-NAME` with the name of the repository where you want to create a new issue, and replace `REPO-OWNER` with the name of the account that owns the repository.{% endif %} In the response, find the `html_url` of your issue, and navigate to your issue in the browser.

```shell copy
gh api --method POST /repos/{% ifversion ghes %}REPO-OWNER/REPO-NAME{% else %}octocat/Spoon-Knife{% endif %}/issues \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: {{ defaultRestApiVersion }}" \
-f title='Created with the REST API' \
-f body='This is a test issue created by the REST API' \
```

{% endcli %}

{% curl %}

This section demonstrates how to make an authenticated request to the {% data variables.product.prodname_dotcom %} REST API using `curl`.

### 1. Setup

You must have `curl` installed on your machine. To check if `curl` is already installed, run `curl --version` on the command line.

* If the output provides information about the version of `curl`, that means `curl` is installed.
* If you get a message similar to `command not found: curl`, that means `curl` is not installed. Download and install `curl`. For more information, see [the curl download page](https://curl.se/download.html).

### 2. Choose an endpoint for your request

1. Choose an endpoint to make a request to. You can explore {% data variables.product.github %}'s [REST API documentation](/rest) to discover endpoints that you can use to interact with {% data variables.product.github %}.
1. Identify the HTTP method and path of the endpoint. You will send these with your request. For more information, see [HTTP method](#http-method) and [Path](#path).

   For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) uses the HTTP method `POST` and the path `/repos/{owner}/{repo}/issues`.

1. Identify any required path parameters. Required path parameters appear in curly brackets `{}` in the path of the endpoint. Replace each parameter placeholder with the desired value. For more information, see [Path](#path).

   For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) uses the path `/repos/{owner}/{repo}/issues`, and the path parameters are `{owner}` and `{repo}`. To use this path in your API request, replace `{repo}` with the name of the repository where you would like to create a new issue, and replace `{owner}` with the name of the account that owns the repository.

### 3. Create authentication credentials

Create an access token to authenticate your request. You can save your token and use it for multiple requests. Give the token any scopes or permissions that are required to access the endpoint. You will send this token in an `Authorization` header with your request. For more information, see [Authentication](#authentication).

### 4. Make a `curl` request

Use the `curl` command to make your request. For more information, see [the curl documentation](https://curl.se/docs/manpage.html).

Specify the following options and values in your request:

* **`--request` or `-X`** followed by the HTTP method as the value. For more information, see [HTTP method](#http-method).
* **`--url`** followed by the full path as the value. The full path is a URL that includes the base URL for the GitHub REST API (`{% data variables.product.rest_url %}`{% ifversion ghec %} or `https://{% data variables.enterprise.data_residency_api %}`, depending on where you access {% data variables.product.github %}{% endif %}) and the path of the endpoint, like this: `{% data variables.product.rest_url %}/PATH`.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %} Replace `PATH` with the path of the endpoint. For more information, see [Path](#path).

  To use query parameters, add a `?` to the end of the path, then append your query parameter name and value in the form `parameter_name=value`. Separate multiple query parameters with `&`. If you need to send an array in the query string, use the query parameter once per array item, and append `[]` after the query parameter name. For example, to provide an array of two repository IDs, use `?repository_ids[]=REPOSITORY_A_ID&repository_ids[]=REPOSITORY_B_ID`. For more information, see [Query parameters](#query-parameters). For an example, see [Example request using query parameters](#example-request-using-query-parameters-1).
* **`--header` or `-H`:**
  * **`Accept`:** Pass the media type in an `Accept` header. To pass multiple media types in an `Accept` header, separate the media types with a comma, for example: `Accept: application/vnd.github+json,application/vnd.github.diff`. For more information, see [`Accept`](#accept) and [Media types](#media-types).
  * **`X-GitHub-Api-Version`:** Pass the API version in a `X-GitHub-Api-Version` header. For more information, see [`X-GitHub-Api-Version`](#x-github-api-version).
  * **`Authorization`:** Pass your authentication token in an `Authorization` header. Note that in most cases you can use `Authorization: Bearer` or `Authorization: token` to pass a token. However, if you are passing a JSON web token (JWT), you must use `Authorization: Bearer`. For more information, see [Authentication](#authentication). For an example of a request that uses an `Authorization` header, see [Example request using body parameters](#example-request-using-body-parameters-1).
* **`--data` or `-d`** followed by any body parameters within a JSON object. If you do not need to specify any body parameters in your request, omit this option. For more information, see [Body parameters](#body-parameters). For an example, see [Example request using body parameters](#example-request-using-body-parameters-1).

#### Example request

The following example request uses the ["Get Octocat" endpoint](/rest/meta/meta#get-octocat) to return the octocat as ASCII art.

```shell copy
curl --request GET \
--url "https://api.github.com/octocat" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: {{ defaultRestApiVersion }}"
```

#### Example request using query parameters

The ["List public events" endpoint](/rest/activity/events#list-public-events) returns thirty issues by default. The following example uses the `per_page` query parameter to return two issues instead of 30, and the `page` query parameter to fetch only the first page of results.

```shell copy
curl --request GET \
--url "{% data variables.product.rest_url %}/events?per_page=2&page=1" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: {{ defaultRestApiVersion }}" \
  https://api.github.com/events
```

#### Example request using body parameters

The following example uses the [Create an issue](/rest/issues/issues#create-an-issue) endpoint to create a new issue in {% ifversion ghes %}a specified{% else %}the octocat/Spoon-Knife{% endif %} repository.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}. Replace `REPO-NAME` with the name of the repository where you want to create a new issue, and replace `REPO-OWNER` with the name of the account that owns the repository.{% endif %} Replace `YOUR-TOKEN` with the authentication token you created in a previous step.

> [!NOTE]
> If you are using a {% data variables.product.pat_v2 %}, you must replace `{% ifversion ghes %}REPO-OWNER` and `REPO-NAME{% else %}octocat/Spoon-Knife{% endif %}` with a repository that you own or that is owned by an organization that you are a member of. Your token must have access to that repository and have read and write permissions for repository issues. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

```shell copy
curl \
--request POST \
--url "{% data variables.product.rest_url %}/repos/{% ifversion ghes %}REPO-OWNER/REPO-NAME{% else %}octocat/Spoon-Knife{% endif %}/issues" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: {{ defaultRestApiVersion }}" \
--header "Authorization: Bearer YOUR-TOKEN" \
--data '{
  "title": "Created with the REST API",
  "body": "This is a test issue created by the REST API"
}'
```

{% endcurl %}

{% javascript %}

This section demonstrates how to make a request to the {% data variables.product.prodname_dotcom %} REST API using JavaScript and [Octokit.js](https://github.com/octokit/octokit.js). For a more detailed guide, see [AUTOTITLE](/rest/guides/scripting-with-the-rest-api-and-javascript).

### 1. Setup

You must install `octokit` to use the Octokit.js library shown in the following examples.

* Install `octokit`. For example, `npm install octokit`. For other ways to install or load `octokit`, see [the Octokit.js README](https://github.com/octokit/octokit.js/#readme).

### 2. Choose an endpoint for your request

1. Choose an endpoint to make a request to. You can explore {% data variables.product.github %}'s [REST API documentation](/rest) to discover endpoints that you can use to interact with {% data variables.product.github %}.
1. Identify the HTTP method and path of the endpoint. You will send these with your request. For more information, see [HTTP method](#http-method) and [Path](#path).

   For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) uses the HTTP method `POST` and the path `/repos/{owner}/{repo}/issues`.

1. Identify any required path parameters. Required path parameters appear in curly brackets `{}` in the path of the endpoint. Replace each parameter placeholder with the desired value. For more information, see [Path](#path).

   For example, the ["Create an issue" endpoint](/rest/issues/issues#create-an-issue) uses the path `/repos/{owner}/{repo}/issues`, and the path parameters are `{owner}` and `{repo}`. To use this path in your API request, replace `{repo}` with the name of the repository where you would like to create a new issue, and replace `{owner}` with the name of the account that owns the repository.

### 3. Create an access token

Create an access token to authenticate your request. You can save your token and use it for multiple requests. Give the token any scopes or permissions that are required to access the endpoint. You will send this token in an `Authorization` header with your request. For more information, see [Authentication](#authentication).

### 4. Make a request with Octokit.js

1. Import `octokit` in your script. For example, `import { Octokit } from "octokit";`. For other ways to import `octokit`, see [the Octokit.js README](https://github.com/octokit/octokit.js/#readme).
1. Create an instance of `Octokit` with your token.{% ifversion ghes %} Set the base URL to `{% data variables.product.rest_url %}`. Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %} Replace `YOUR-TOKEN` with your token.

   ```javascript copy
   const octokit = new Octokit({ {% ifversion ghes %}
     baseUrl: "{% data variables.product.rest_url %}",{% endif %}
     auth: 'YOUR-TOKEN'
   });
   ```

1. Use `octokit.request` to execute your request.

   * Send the HTTP method and path as the first argument to the `request` method. For more information, see [HTTP method](#http-method) and [Path](#path).
   * Specify all path, query, and body parameters in an object as the second argument to the `request` method. For more information, see [Parameters](#parameters).

   In the following example request, the HTTP method is `POST`, the path is `/repos/{owner}/{repo}/issues`, the path parameters are `owner: "{% ifversion ghes %}REPO-OWNER{% else %}octocat{% endif %}"` and `repo: "{% ifversion ghes %}REPO-NAME{% else %}Spoon-Knife{% endif %}"`, and the body parameters are `title: "Created with the REST API"` and `body: "This is a test issue created by the REST API"`.{% ifversion ghes %} Replace `REPO-OWNER` with the name of the account that owns the repository, and `REPO-NAME` with the name of the repository.{% endif %}

   > [!NOTE]
   > If you are using a {% data variables.product.pat_v2 %}, you must replace `{% ifversion ghes %}REPO-OWNER` and `REPO-NAME{% else %}octocat/Spoon-Knife{% endif %}` with a repository that you own or that is owned by an organization that you are a member of. Your token must have access to that repository and have read and write permissions for repository issues. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

   ```javascript copy
   await octokit.request("POST /repos/{owner}/{repo}/issues", {
     owner: "{% ifversion ghes %}REPO-OWNER{% else %}octocat{% endif %}",
     repo: "{% ifversion ghes %}REPO-NAME{% else %}Spoon-Knife{% endif %}",
     title: "Created with the REST API",
     body: "This is a test issue created by the REST API",
   });
   ```

   The `request` method automatically passes the `Accept: application/vnd.github+json` header. To pass additional headers or a different `Accept` header, add a `headers` property to the object that is passed as a second argument. The value of the `headers` property is an object with the header names as keys and header values as values.

   For example, the following code will send a `content-type` header with a value of `text/plain` and a `X-GitHub-Api-Version` header with a value of `{{ allVersions[currentVersion].latestApiVersion }}`.

   ```javascript copy
   await octokit.request("GET /octocat", {
     headers: {
       "content-type": "text/plain",
       "X-GitHub-Api-Version": "{{ allVersions[currentVersion].latestApiVersion }}",
     },
   });
   ```

{% endjavascript %}

## Using the response

After you make a request, the API will return the response status code, response headers, and potentially a response body.

### About the response code and headers

Every request will return an HTTP status code that indicates the success of the response. For more information about response codes, see [the MDN HTTP response status code documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

Additionally, the response will include headers that give more details about the response. Headers that start with `X-` or `x-` are custom to {% data variables.product.company_short %}. For example, the `x-ratelimit-remaining` and `x-ratelimit-reset` headers tell you how many requests you can make in a time period.

{% cli %}

To view the status code and headers, use the `--include` or `--i` option when you send your request.

For example, this request gets a list of issues in {% ifversion ghes %}a specified{% else %}the octocat/Spoon-Knife{% endif %} repository:

```shell
gh api \
--header 'Accept: application/vnd.github+json' \
--method GET /repos/{% ifversion ghes %}REPO-OWNER/REPO-NAME{% else %}octocat/Spoon-Knife{% endif %}/issues \
-F per_page=2 --include
```

And it returns a response code and headers that look something like this:

```shell
HTTP/2.0 200 OK
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset
Cache-Control: private, max-age=60, s-maxage=60
Content-Security-Policy: default-src 'none'
Content-Type: application/json; charset=utf-8
Date: Thu, 04 Aug 2022 19:56:41 GMT
Etag: W/"a63dfbcfdb73621e9d2e89551edcf9856731ced534bd7f1e114a5da1f5f73418"
Link: <https://api.github.com/repositories/1300192/issues?per_page=1&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=1&page=14817>; rel="last"
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Server: GitHub.com
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
Vary: Accept, Authorization, Cookie, Accept-Encoding, Accept, X-Requested-With
X-Accepted-Oauth-Scopes: repo
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-Github-Api-Version-Selected: 2022-08-09
X-Github-Media-Type: github.v3; format=json
X-Github-Request-Id: 1C73:26D4:E2E500:1EF78F4:62EC2479
X-Oauth-Client-Id: 178c6fc778ccc68e1d6a
X-Oauth-Scopes: gist, read:org, repo, workflow
X-Ratelimit-Limit: 15000
X-Ratelimit-Remaining: 14996
X-Ratelimit-Reset: 1659645499
X-Ratelimit-Resource: core
X-Ratelimit-Used: 4
X-Xss-Protection: 0
```

In this example, the response code is `200`, which indicates a successful request.

{% endcli %}

{% javascript %}

When you make a request with Octokit.js, the `request` method returns a promise. If the request was successful, the promise resolves to an object that includes the HTTP status code of the response (`status`) and the response headers (`headers`). If an error occurs, the promise resolves to an object that includes the HTTP status code of the response (`status`) and the response headers (`response.headers`).

You can use a `try/catch` block to catch an error if it occurs. For example, if the request in the following script is successful, the script will log the status code and the value of the `x-ratelimit-remaining` header. If the request was not successful, the script will log the status code, the value of the `x-ratelimit-remaining` header, and the error message.

In the following example, replace `REPO-OWNER` with the name of the account that owns the repository, and `REPO-NAME` with the name of the repository.

```javascript copy
try {
  const result = await octokit.request("GET /repos/{owner}/{repo}/issues", {
    owner: "REPO-OWNER",
    repo: "REPO-NAME",
    per_page: 2,
  });

  console.log(`Success! Status: ${result.status}. Rate limit remaining: ${result.headers["x-ratelimit-remaining"]}`)

} catch (error) {
  console.log(`Error! Status: ${error.status}. Rate limit remaining: ${error.headers["x-ratelimit-remaining"]}. Message: ${error.response.data.message}`)
}
```

{% endjavascript %}

{% curl %}

To view the status code and headers, use the `--include` or `--i` option when you send your request.

For example, this request gets a list of issues in {% ifversion ghes %}a specified{% else %}the octocat/Spoon-Knife{% endif %} repository:

```shell
curl --request GET \
--url "https://api.github.com/repos/{% ifversion ghes %}REPO-OWNER/REPO-NAME{% else %}octocat/Spoon-Knife{% endif %}/issues?per_page=2" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN" \
--include
```

And it returns a response code and headers that look something like this:

```shell
HTTP/2 200
server: GitHub.com
date: Thu, 04 Aug 2022 20:07:51 GMT
content-type: application/json; charset=utf-8
cache-control: public, max-age=60, s-maxage=60
vary: Accept, Accept-Encoding, Accept, X-Requested-With
etag: W/"7fceb7e8c958d3ec4d02524b042578dcc7b282192e6c939070f4a70390962e18"
x-github-media-type: github.v3; format=json
link: <https://api.github.com/repositories/1300192/issues?per_page=2&sort=updated&direction=asc&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=2&sort=updated&direction=asc&page=7409>; rel="last"
access-control-expose-headers: ETag, Link, Location, Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset
access-control-allow-origin: *
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 0
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
content-security-policy: default-src 'none'
x-ratelimit-limit: 15000
x-ratelimit-remaining: 14996
x-ratelimit-reset: 1659645535
x-ratelimit-resource: core
x-ratelimit-used: 4
accept-ranges: bytes
content-length: 4936
x-github-request-id: 14E0:4BC6:F1B8BA:208E317:62EC2715
```

In this example, the response code is `200`, which indicates a successful request.

{% endcurl %}

### About the response body

Many endpoints will return a response body. Unless otherwise specified, the response body is in JSON format. Blank fields are included as `null` instead of being omitted. All timestamps return in UTC time, ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.

Unlike the GraphQL API where you specify what information you want, the REST API typically returns more information than you need. If desired, you can parse the response to pull out specific pieces of information.

{% cli %}

For example, you can use `>` to redirect the response to a file. In the following example, replace `REPO-OWNER` with the name of the account that owns the repository, and `REPO-NAME` with the name of the repository.

```shell copy
gh api \
--header 'Accept: application/vnd.github+json' \
--method GET /repos/REPO-OWNER/REPO-NAME/issues \
-F per_page=2 > data.json
```

Then you can use jq to get the title and author ID of each issue:

```shell copy
jq '.[] | {title: .title, authorID: .user.id}' data.json
```

The previous two commands return something like:

```json
{
  "title": "Update index.html",
  "authorID": 10701255
}
{
  "title": "Edit index file",
  "authorID": 53709285
}
```

For more information about jq, see [the jq documentation](https://stedolan.github.io/jq/).

{% endcli %}

{% javascript %}

For example, you can get the title and author ID of each issue. In the following example, replace `REPO-OWNER` with the name of the account that owns the repository, and `REPO-NAME` with the name of the repository.

```javascript copy
try {
  const result = await octokit.request("GET /repos/{owner}/{repo}/issues", {
    owner: "REPO-OWNER",
    repo: "REPO-NAME",
    per_page: 2,
  });

  const titleAndAuthor = result.data.map(issue => {title: issue.title, authorID: issue.user.id})

  console.log(titleAndAuthor)

} catch (error) {
  console.log(`Error! Status: ${error.status}. Message: ${error.response.data.message}`)
}
```

{% endjavascript %}

{% curl %}

For example, you can use `>` to redirect the response to a file. In the following example, replace `REPO-OWNER` with the name of the account that owns the repository, and `REPO-NAME` with the name of the repository.{% ifversion ghes %} Replace `HOSTNAME` with the name of {% data variables.location.product_location %}.{% endif %}

```shell copy
curl --request GET \
--url "{% data variables.product.rest_url %}/repos/REPO-OWNER/REPO-NAME/issues?per_page=2" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN" > data.json
```

Then you can use jq to get the title and author ID of each issue:

```shell copy
jq '.[] | {title: .title, authorID: .user.id}' data.json
```

The previous two commands return something like:

```json
{
  "title": "Update index.html",
  "authorID": 10701255
}
{
  "title": "Edit index file",
  "authorID": 53709285
}
```

For more information about jq, see [the jq documentation](https://stedolan.github.io/jq/).

{% endcurl %}

#### Detailed versus summary representations

A response can include all attributes for a resource or only a subset of attributes, depending on whether you fetch an individual resource or a list of resources.

* When you fetch an _individual resource_, like a specific repository, the response will typically include all attributes for that resource. This is the "detailed" representation of the resource.
* When you fetch a _list of resources_, like a list of multiple repositories, the response will only include a subset of the attributes for each resource. This is the "summary" representation of the resource.

Note that authorization sometimes influences the amount of detail included in a representation.

The reason for this is because some attributes are computationally expensive for the API to provide, so {% data variables.product.prodname_dotcom %} excludes those attributes from the summary representation. To obtain those attributes, you can fetch the detailed representation.

The documentation provides an example response for each API method. The example response illustrates all attributes that are returned by that method.

#### Hypermedia

All resources may have one or more `*_url` properties linking to other resources. These are meant to provide explicit URLs so that proper API clients don't need to construct URLs on their own. It is highly recommended that API clients use these. Doing so will make future upgrades of the API easier for developers. All URLs are expected to be proper [RFC 6570](https://datatracker.ietf.org/doc/html/rfc6570) URI templates.

You can then expand these templates using something like the [uri_template](https://github.com/hannesg/uri_template) gem:

```ruby
>> tmpl = URITemplate.new('/notifications{?since,all,participating}')
>> tmpl.expand
=> "/notifications"

>> tmpl.expand all: 1
=> "/notifications?all=1"

>> tmpl.expand all: 1, participating: 1
=> "/notifications?all=1&participating=1"
```

## Rate limiting

The {% data variables.product.github %} REST API limits the number of requests you can make within a given time period. For more information about rate limits and how to check your current rate limit status, see [AUTOTITLE](/rest/using-the-rest-api/rate-limits-for-the-rest-api).

## Next steps

This article demonstrated how to list and create issues in a repository. For more practice, try to comment on an issue, edit the title of an issue, or close an issue. For more information, see the ["Create an issue comment" endpoint](/rest/issues/comments#create-an-issue-comment) and the ["Update an issue" endpoint](/rest/issues/issues#update-an-issue).

For more information about other endpoints that you can use, see the [REST reference documentation](/rest).


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/github-event-types -->

---
title: GitHub event types
intro: 'For the {% data variables.product.prodname_dotcom %} Events API, learn about each event type, the triggering action on {% data variables.product.prodname_dotcom %}, and each event''s unique properties.'
redirect_from:
  - /v3/activity/event_types
  - /developers/webhooks-and-events/github-event-types
  - /developers/webhooks-and-events/events/github-event-types
  - /webhooks-and-events/events/github-event-types
  - /developers/webhooks-and-events/events
  - /rest/overview/github-event-types
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---
The Events API can return different types of events triggered by activity on GitHub. Each event response contains shared properties, but has a unique `payload` object determined by its event type. The [Event object common properties](#event-object-common-properties) describes the properties shared by all events, and each event type describes the `payload` properties that are unique to the specific event.

{% ifversion fpt or ghec %}

{% endif %}

## Event object common properties

The event objects returned from the Events API endpoints have the same structure.

| Event API attribute name | Type | Description |
|--------------------------|-------------|-------------|
| `id` | `integer` | Unique identifier for the event. |
| `type` | `string` | The type of event. Events uses PascalCase for the name. |
| `actor` | `object` | The user that triggered the event. |
| `actor.id` | `integer` | The unique identifier for the actor. |
| `actor.login` | `string` | The username of the actor. |
| `actor.display_login` | `string` | The specific display format of the username. |
| `actor.gravatar_id` | `string` | The unique identifier of the Gravatar profile for the actor. |
| `actor.url` | `string` | The REST API URL used to retrieve the user object, which includes additional user information. |
| `actor.avatar_url` | `string` | The URL of the actor's profile image. |
| `repo` | `object` | The repository object where the event occurred.  |
| `repo.id` | `integer` | The unique identifier of the repository. |
| `repo.name` | `string` | The name of the repository, which includes the owner and repository name. For example, `octocat/hello-world` is the name of the `hello-world` repository owned by the `octocat` personal account. |
| `repo.url` | `string` | The REST API URL used to retrieve the repository object, which includes additional repository information. |
| `payload` | `object` | The event payload object is unique to the event type. See the event type below for the event API `payload` object. |
| `public` | `boolean` | Whether the event is visible to all users. |
| `created_at` | `string` | The date and time when the event was triggered. It is formatted according to ISO 8601. |
| `org` | `object` | The organization that was chosen by the actor to perform action that triggers the event.<br />_The property appears in the event object only if it is applicable._ |
| `org.id` | `integer` | The unique identifier for the organization. |
| `org.login` | `string` | The name of the organization. |
| `org.gravatar_id` | `string` | The unique identifier of the Gravatar profile for the organization. |
| `org.url` | `string` | The REST API URL used to retrieve the organization object, which includes additional organization information. |
| `org.avatar_url` | `string` | The URL of the organization's profile image. |

### Example WatchEvent event object

This example shows the format of the [WatchEvent](#watchevent) response when using the [Events API](/rest/activity/events).

```http
HTTP/2 200
Link: <https://api.github.com/resource?page=2>; rel="next",
      <https://api.github.com/resource?page=5>; rel="last"
```

```json
[
  {
    "id": "12345",
    "type": "WatchEvent",
    "actor": {
      "id": 1,
      "login": "octocat",
      "display_login": "octocat",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif"
    },
    "repo": {
      "id": 3,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "payload": {
      "action": "started"
    },
    "public": false,
    "created_at": "2011-09-06T17:26:27Z",
    "org": {
      "id": 1,
      "login": "github",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/github",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif"
    },
  }
]
```

## CommitCommentEvent

{% data reusables.webhooks.commit_comment_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for CommitCommentEvent

{% data reusables.webhooks.commit_comment_properties %}

## CreateEvent

{% data reusables.webhooks.create_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for CreateEvent

{% data reusables.webhooks.create_properties %}

## DeleteEvent

{% data reusables.webhooks.delete_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for DeleteEvent

{% data reusables.webhooks.delete_properties %}

{% ifversion fpt or ghec %}

## DiscussionEvent

{% data reusables.webhooks.discussion_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for DiscussionEvent

{% data reusables.webhooks.discussion_properties %}

{% endif %}

## ForkEvent

{% data reusables.webhooks.fork_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for ForkEvent

{% data reusables.webhooks.fork_properties %}

## GollumEvent

{% data reusables.webhooks.gollum_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for GollumEvent

{% data reusables.webhooks.gollum_properties %}

## IssueCommentEvent

{% data reusables.webhooks.issue_comment_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for IssueCommentEvent

{% data reusables.webhooks.issue_comment_webhook_properties %}
{% data reusables.webhooks.issue_comment_properties %}

## IssuesEvent

{% data reusables.webhooks.issues_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for IssuesEvent

{% data reusables.webhooks.issue_event_api_properties %}
{% data reusables.webhooks.issue_properties %}

## MemberEvent

{% data reusables.webhooks.member_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for MemberEvent

{% data reusables.webhooks.member_event_api_properties %}
{% data reusables.webhooks.member_properties %}

## PublicEvent

{% data reusables.webhooks.public_short_desc %}

### Event `payload` object for PublicEvent

This event returns an empty `payload` object.

## PullRequestEvent

{% data reusables.webhooks.pull_request_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for PullRequestEvent

{% data reusables.webhooks.pull_request_event_api_properties %}
{% data reusables.webhooks.pull_request_properties %}

## PullRequestReviewEvent

{% data reusables.webhooks.pull_request_review_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for PullRequestReviewEvent

{% data reusables.webhooks.pull_request_review_properties %}

## PullRequestReviewCommentEvent

{% data reusables.webhooks.pull_request_review_comment_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for PullRequestReviewCommentEvent

{% data reusables.webhooks.pull_request_review_comment_event_api_properties %}
{% data reusables.webhooks.pull_request_review_comment_properties %}

## PushEvent

{% data reusables.webhooks.push_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for PushEvent

{% data reusables.webhooks.push_properties %}

## ReleaseEvent

{% data reusables.webhooks.release_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for ReleaseEvent

{% data reusables.webhooks.release_event_api_properties %}
{% data reusables.webhooks.release_properties %}

## WatchEvent

{% data reusables.webhooks.watch_short_desc %}

{% data reusables.webhooks.events_api_payload %}

### Event `payload` object for WatchEvent

{% data reusables.webhooks.watch_properties %}


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api -->

---
title: Using the REST API
intro: 'Learn how to use the {% data variables.product.prodname_dotcom %} REST API, follow best practices, and troubleshoot problems.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /getting-started-with-the-rest-api
  - /rate-limits-for-the-rest-api
  - /using-pagination-in-the-rest-api
  - /libraries-for-the-rest-api
  - /best-practices-for-using-the-rest-api
  - /troubleshooting-the-rest-api
  - /timezones-and-the-rest-api
  - /using-cors-and-jsonp-to-make-cross-origin-requests
  - /issue-event-types
  - /github-event-types
---


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/issue-event-types -->

---
title: Issue event types
intro: 'For the REST APIs for issue events and timeline events, learn about each event type, the triggering action on {% data variables.product.prodname_dotcom %}, and each event''s unique properties.'
redirect_from:
  - /v3/issues/issue-event-types
  - /developers/webhooks-and-events/issue-event-types
  - /developers/webhooks-and-events/events/issue-event-types
  - /webhooks-and-events/events/issue-event-types
  - /rest/overview/issue-event-types
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---
Issue events are triggered by activity in issues and pull requests and are available in the REST API for [Issue events](/rest/issues/events) and [Timeline events](/rest/issues/timeline). Each event type specifies whether the event is available in the REST API for issue events or timeline events.

GitHub's REST API considers every pull request to be an issue, but not every issue is a pull request. For this reason, the Issue Events and Timeline Events endpoints may return both issues and pull requests in the response. Pull requests have a `pull_request` property in the `issue` object. Because pull requests are issues, issue and pull request numbers do not overlap in a repository. For example, if you open your first issue in a repository, the number will be 1. If you then open a pull request, the number will be 2. Each event type specifies if the event occurs in pull request, issues, or both.

## Issue event object common properties

Issue events all have the same object structure, except events that are only available in the REST API for timeline events. Some events also include additional properties that provide more context about the event resources. Refer to the specific event for details about any properties that differ from this object format.

{% data reusables.issue-events.issue-event-common-properties %}

{% ifversion projects-v1 %}

## added_to_project

The issue or pull request was added to a {% data variables.projects.projects_v1_board %}. {% data reusables.projects.disabled-projects %}

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for added_to_project

{% data reusables.pre-release-program.starfox-preview %}
{% data reusables.pre-release-program.api-preview-warning %}

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.project-card-properties %}

{% endif %}

## assigned

The issue or pull request was assigned to a user.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for assigned

{% data reusables.issue-events.issue-event-common-properties %}
`assignee` | `object` | The person assigned to this issue.
`assigner` | `object` | The person who performed the assignment for this issue. This field is available in the REST API for issue events but not the REST API for timeline events.

## automatic_base_change_failed

GitHub unsuccessfully attempted to automatically change the base branch of the pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "x" aria-label="Not supported" %} |

{% endrowheaders %}

### Properties for automatic_base_change_failed

{% data reusables.issue-events.issue-event-common-properties %}

## automatic_base_change_succeeded

GitHub successfully attempted to automatically change the base branch of the pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "x" aria-label="Not supported" %} |

{% endrowheaders %}

### Properties for automatic_base_change_succeeded

{% data reusables.issue-events.issue-event-common-properties %}

## base_ref_changed

The base reference branch of the pull request changed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "x" aria-label="Not supported" %} |

{% endrowheaders %}

### Properties for base_ref_changed

{% data reusables.issue-events.issue-event-common-properties %}

## closed

The issue or pull request was closed. When the `commit_id` is present, it identifies the commit that closed the issue using "closes / fixes" syntax. For more information about the syntax, see [AUTOTITLE](/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword).

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for closed

{% data reusables.issue-events.issue-event-common-properties %}

## commented

A comment was added to the issue or pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for commented

{% data reusables.issue-events.timeline_events_object_properties %}

Name | Type | Description
-----|------|--------------
`url` | `string` | The REST API URL to retrieve the issue comment.
`html_url` | `string` | The HTML URL of the issue comment.
`issue_url` | `string` | The HTML URL of the issue.
`id` | `integer` | The unique identifier of the event.
`node_id` | `string` | The [Global Node ID](/graphql/guides/using-global-node-ids) of the event.
`user` | `object` | The person who commented on the issue.
`created_at` | `string` | The timestamp indicating when the comment was added.
`updated_at` | `string` | The timestamp indicating when the comment was updated or created, if the comment is never updated.
`author_association` | `string` | The permissions the user has in the issue's repository. For example, the value would be `"OWNER"` if the owner of repository created a comment.
`body` | `string` | The comment body text.
`event` | `string` | The event value is `"commented"`.
`actor` | `object` | The person who generated the event.

## committed

A commit was added to the pull request's `HEAD` branch.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for committed

{% data reusables.issue-events.timeline_events_object_properties %}

Name | Type | Description
-----|------|--------------
`sha` | `string` | The SHA of the commit in the pull request.
`node_id` | `string` | The [Global Node ID](/graphql/guides/using-global-node-ids) of the event.
`url` | `string` | The REST API URL to retrieve the commit.
`html_url` | `string` | The HTML URL of the commit.
`author` | `object` | The person who authored the commit.
`committer` | `object` | The person who committed the commit on behalf of the author.
`tree` | `object` | The Git tree of the commit.
`message` | `string` | The commit message.
`parents` | `array of objects` | A list of parent commits.
`verification` | `object` | The result of verifying the commit's signature. For more information, see [AUTOTITLE](/rest/git/commits#get-a-commit).
`event` | `string` | The event value is `"committed"`.

## connected

The issue or pull request was linked to another issue or pull request. For more information, see [AUTOTITLE](/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for connected

{% data reusables.issue-events.issue-event-common-properties %}

## convert_to_draft

The pull request was converted to draft mode.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for convert_to_draft

{% data reusables.issue-events.issue-event-common-properties %}

{% ifversion projects-v1 %}

## converted_note_to_issue

The issue was created by converting a note in a {% data variables.projects.projects_v1_board %} to an issue. {% data reusables.projects.disabled-projects %}

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for converted_note_to_issue

{% data reusables.pre-release-program.starfox-preview %}
{% data reusables.pre-release-program.api-preview-warning %}

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.project-card-properties %}

{% endif %}

## converted_to_discussion

The issue was closed and converted to a discussion.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for converted_to_discussion

{% data reusables.issue-events.issue-event-common-properties %}

## cross-referenced

The issue or pull request was referenced from another issue or pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for cross-referenced

{% data reusables.issue-events.timeline_events_object_properties %}

Name | Type | Description
-----|------|--------------
`actor` | `object` | The person who generated the event.
`created_at` | `string` | The timestamp indicating when the cross-reference was added.
`updated_at` | `string` | The timestamp indicating when the cross-reference was updated or created, if the cross-reference is never updated.
`source` | `object` | The issue or pull request that added a cross-reference.
`source[type]` | `string` | This value will always be `"issue"` because pull requests are of type issue. Only cross-reference events triggered by issues or pull requests are returned in the REST API for timeline events. To determine if the issue that triggered the event is a pull request, you can check if the `source[issue][pull_request]` object exists.
`source[issue]` | `object` | The `issue` object that added the cross-reference.
`event` | `string` | The event value is `"cross-referenced"`.

## demilestoned

The issue or pull request was removed from a milestone.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for demilestoned

{% data reusables.issue-events.issue-event-common-properties %}
`milestone` | `object` | The milestone object.
`milestone[title]` | `string` | The title of the milestone.

## deployed

The pull request was deployed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for deployed

{% data reusables.issue-events.issue-event-common-properties %}

## deployment_environment_changed

The pull request deployment environment was changed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "x" aria-label="Not supported" %} |

{% endrowheaders %}

### Properties for deployment_environment_changed

{% data reusables.issue-events.issue-event-common-properties %}

## disconnected

The issue or pull request was unlinked from another issue or pull request. For more information, see [AUTOTITLE](/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for disconnected

{% data reusables.issue-events.issue-event-common-properties %}

## head_ref_deleted

The pull request's `HEAD` branch was deleted.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for head_ref_deleted

{% data reusables.issue-events.issue-event-common-properties %}

## head_ref_restored

The pull request's `HEAD` branch was restored to the last known commit.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

## head_ref_force_pushed

The pull request's HEAD branch was force pushed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for head_ref_force_pushed

{% data reusables.issue-events.issue-event-common-properties %}

## labeled

A label was added to the issue or pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for labeled

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.label-properties %}

## locked

The issue or pull request was locked.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for locked

{% data reusables.issue-events.issue-event-common-properties %}
`lock_reason` | `string` | The reason an issue or pull request conversation was locked, if one was provided.

## mentioned

The `actor` was `@mentioned` in an issue or pull request body.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for mentioned

{% data reusables.issue-events.issue-event-common-properties %}

## marked_as_duplicate

A user with write permissions marked an issue as a duplicate of another issue, or a pull request as a duplicate of another pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for marked_as_duplicate

{% data reusables.issue-events.issue-event-common-properties %}

## merged

The pull request was merged. The `commit_id` attribute is the SHA1 of the `HEAD` commit that was merged. The `commit_repository` is always the same as the main repository.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for merged

{% data reusables.issue-events.issue-event-common-properties %}

## milestoned

The issue or pull request was added to a milestone.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for milestoned

{% data reusables.issue-events.issue-event-common-properties %}
`milestone` | `object` | The milestone object.
`milestone[title]` | `string` | The title of the milestone.

{% ifversion projects-v1 %}

## moved_columns_in_project

The issue or pull request was moved between columns in a {% data variables.projects.projects_v1_board %}. {% data reusables.projects.disabled-projects %}

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for moved_columns_in_project

{% data reusables.pre-release-program.starfox-preview %}
{% data reusables.pre-release-program.api-preview-warning %}

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.project-card-properties %}
`previous_column_name` | `string` | The name of the column the issue was moved from.

{% endif %}

## pinned

The issue was pinned.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for pinned

{% data reusables.issue-events.issue-event-common-properties %}

## ready_for_review

A draft pull request was marked as ready for review.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for ready_for_review

{% data reusables.issue-events.issue-event-common-properties %}

## referenced

The issue was referenced from a commit message. The `commit_id` attribute is the commit SHA1 of where that happened and the commit_repository is where that commit was pushed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for referenced

{% data reusables.issue-events.issue-event-common-properties %}

{% ifversion projects-v1 %}

## removed_from_project

The issue or pull request was removed from a {% data variables.projects.projects_v1_board %}. {% data reusables.projects.disabled-projects %}

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for removed_from_project

{% data reusables.pre-release-program.starfox-preview %}
{% data reusables.pre-release-program.api-preview-warning %}

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.project-card-properties %}

{% endif %}

## renamed

The issue or pull request title was changed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for renamed

{% data reusables.issue-events.issue-event-common-properties %}
`rename` | `object` | The name details.
`rename[from]` | `string` | The previous name.
`rename[to]` | `string` | The new name.

## reopened

The issue or pull request was reopened.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for reopened

{% data reusables.issue-events.issue-event-common-properties %}

## review_dismissed

The pull request review was dismissed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for review_dismissed

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.review-dismissed-properties %}

## review_requested

A pull request review was requested.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for review_requested

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.review-request-properties %}

## review_request_removed

A pull request review request was removed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for review_request_removed

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.review-request-properties %}

## reviewed

The pull request was reviewed.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Pull requests| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for reviewed

{% data reusables.issue-events.timeline_events_object_properties %}

Name | Type | Description
-----|------|--------------
`id` | `integer` | The unique identifier of the event.
`node_id` | `string` | The [Global Node ID](/graphql/guides/using-global-node-ids) of the event.
`user` | `object` | The person who commented on the issue.
`body` | `string` | The review summary text.
`commit_id` | `string` | The SHA of the latest commit in the pull request at the time of the review.
`submitted_at` | `string` | The timestamp indicating when the review was submitted.
`state` | `string` | The state of the submitted review. Can be one of: `commented`, `changes_requested`, `approved` or `dismissed`.
`html_url` | `string` | The HTML URL of the review.
`pull_request_url` | `string` | The REST API URL to retrieve the pull request.
`author_association` | `string` | The permissions the user has in the issue's repository. For example, the value would be `"OWNER"` if the owner of repository created a comment.
`_links` | `object` | The `html_url` and `pull_request_url`.
`event` | `string` | The event value is `"reviewed"`.

## subscribed

Someone subscribed to receive notifications for an issue or pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for subscribed

{% data reusables.issue-events.issue-event-common-properties %}

## transferred

The issue was transferred to another repository.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for transferred

{% data reusables.issue-events.issue-event-common-properties %}

## unassigned

A user was unassigned from the issue.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for unassigned

{% data reusables.issue-events.issue-event-common-properties %}
`assignee` | `object` | The person unassigned from this issue.
`assigner` | `object` | The person who performed the unassignment for this issue. This field is available in the REST API for issue events but not the REST API for timeline events.

## unlabeled

A label was removed from the issue.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for unlabeled

{% data reusables.issue-events.issue-event-common-properties %}
{% data reusables.issue-events.label-properties %}

## unlocked

The issue was unlocked.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for unlocked

{% data reusables.issue-events.issue-event-common-properties %}
`lock_reason` | `string` | The reason an issue or pull request conversation was locked, if one was provided.

## unmarked_as_duplicate

An issue that a user had previously marked as a duplicate of another issue is no longer considered a duplicate, or a pull request that a user had previously marked as a duplicate of another pull request is no longer considered a duplicate.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for unmarked_as_duplicate

{% data reusables.issue-events.issue-event-common-properties %}

## unpinned

The issue was unpinned.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for unpinned

{% data reusables.issue-events.issue-event-common-properties %}

## unsubscribed

Someone unsubscribed from receiving notifications for an issue or pull request.

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "x" aria-label="Not supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for unsubscribed

{% data reusables.issue-events.issue-event-common-properties %}

{% ifversion fpt or ghec %}

## user_blocked

An organization owner blocked a user from the organization. This was done [through one of the blocked user's comments on the issue](/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-a-comment).

This event is available for the following issue types.

{% rowheaders %}

|  | REST API for issue events | REST API for timeline events |
|---|---|---|
|Issues| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |
|Pull requests| {% octicon "check" aria-label="Supported" %} | {% octicon "check" aria-label="Supported" %} |

{% endrowheaders %}

### Properties for user_blocked

{% data reusables.issue-events.issue-event-common-properties %}

{% endif %}


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api -->

---
title: Libraries for the REST API
shortTitle: Libraries
intro: 'You can use the official Octokit libraries and other third-party libraries to extend and simplify how you use the {% data variables.product.company_short %} API.'
redirect_from:
  - /libraries
  - /v3/libraries
  - /rest/overview/libraries
  - /rest/overview/libraries-for-the-rest-api
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---

## About libraries

You can use libraries to extend and simplify the way your application interacts with {% data variables.product.company_short %}'s API. Each library provides pre-built code for a specific programming language. After integrating a library into your project, you can use the pre-built code modules to interact with {% data variables.product.company_short %}'s API via a specific programming language.

{% data variables.product.company_short %} maintains official Octokit libraries for some languages. There are also third-party libraries that you can use with {% data variables.product.company_short %}'s API, which are not maintained by {% data variables.product.company_short %}.

## Official {% data variables.product.company_short %} libraries

{% data variables.product.company_short %} maintains these official client libraries for the {% data variables.product.company_short %} API. These repositories are open source, and community contributions are welcome.

For more information, see [AUTOTITLE](/rest/guides/scripting-with-the-rest-api-and-javascript) and [AUTOTITLE](/rest/guides/scripting-with-the-rest-api-and-ruby).

* JavaScript: [octokit.js](https://github.com/octokit/octokit.js)
* Ruby: [octokit.rb](https://github.com/octokit/octokit.rb)
* .NET: [octokit.net](https://github.com/octokit/octokit.net)
* Terraform: [terraform-provider-github](https://github.com/integrations/terraform-provider-github)

<!-- markdownlint-disable GHD034 -->

## Third-party libraries

The following are examples of third-party libraries that you can use to interact with the {% data variables.product.company_short %} API in various programming languages.

These third-party libraries are not maintained by {% data variables.product.company_short %}. Libraries provided by third parties are governed by separate terms of service, privacy policy, and support documentation.

### Clojure

* Tentacles: [clj-commons/tentacles](https://github.com/clj-commons/tentacles)

### Dart

* github.dart: [SpinlockLabs/github.dart](https://github.com/SpinlockLabs/github.dart)

### Emacs Lisp

* gh.el: [sigma/gh.el](https://github.com/sigma/gh.el)

### Go

* go-github: [google/go-github](https://github.com/google/go-github)

### Haskell

* haskell-github: [haskell-github/github](https://github.com/fpco/github)

### Java

* GitHub API for Java, an object oriented representation of the GitHub API: [hub4j/github-api](https://hub4j.github.io/github-api/)
* JCabi GitHub API, based on Java7 JSON API (JSR-353), simplifies tests with a runtime GitHub stub, and covers the entire API: [github.jcabi.com (Personal Website)](https://github.jcabi.com)

### JavaScript

* NodeJS GitHub library: [pksunkara/octonode](https://github.com/pksunkara/octonode)
* Github.js wrapper around the GitHub API: [github-tools/github](https://github.com/github-tools/github)
* Promise-Based CoffeeScript library for the Browser or NodeJS: [philschatz/github-client](https://github.com/philschatz/github-client)

### Julia

* GitHub.jl: [JuliaWeb/GitHub.jl](https://github.com/JuliaWeb/GitHub.jl)

### OCaml

* ocaml-github: [mirage/ocaml-github](https://github.com/mirage/ocaml-github)

### Perl

* Pithub: [plu/Pithub](https://github.com/plu/Pithub)
* Net::GitHub: [fayland/perl-net-github](https://github.com/fayland/perl-net-github)

### PHP

* PHP GitHub API: [KnpLabs/php-github-api](https://github.com/KnpLabs/php-github-api)
* GitHub Joomla! Package: [joomla-framework/github-api](https://github.com/joomla-framework/github-api)
* GitHub bridge for Laravel: [GrahamCampbell/Laravel-GitHub](https://github.com/GrahamCampbell/Laravel-GitHub)

### PowerShell

* PowerShellForGitHub: [microsoft/PowerShellForGitHub](https://github.com/microsoft/PowerShellForGitHub)

### Python

* gidgethub: [gidgethub/gidgethub](https://github.com/gidgethub/gidgethub)
* ghapi: [fastai/ghapi](https://github.com/fastai/ghapi)
* PyGithub: [PyGithub/PyGithub](https://github.com/PyGithub/PyGithub)
* libsaas: [duckboard/libsaas](https://github.com/ducksboard/libsaas)
* github3.py: [sigmavirus24/github3.py](https://github.com/sigmavirus24/github3.py)
* agithub: [mozilla/agithub](https://github.com/mozilla/agithub)
* github-flask: [github-flask (Official Website)](http://github-flask.readthedocs.org)
* githubkit: [yanyongyu/githubkit](https://github.com/yanyongyu/githubkit)
* octokit.py: [khornberg/octokit.py](https://github.com/khornberg/octokit.py)

### Ruby

* GitHub API Gem: [piotrmurach/github](https://github.com/piotrmurach/github)

### Rust

* Octocrab: [XAMPPRocky/octocrab](https://github.com/XAMPPRocky/octocrab)

### Scala

* Github4s: [47deg/github4s](https://github.com/47deg/github4s)

### Shell

* ok.sh: [whiteinge/ok.sh](https://github.com/whiteinge/ok.sh)


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api -->

---
title: Rate limits for the REST API
shortTitle: Rate limits
intro: 'Learn about REST API rate limits, how to avoid exceeding them, and what to do if you do exceed them.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /rest/overview/rate-limits-for-the-rest-api
category:
  - Learn about the REST API
---

{% ifversion ghes %}

Rate limits are disabled by default for {% data variables.product.prodname_ghe_server %}. Contact your site administrator to confirm the rate limits for your instance.

If you are a site administrator, you can set rate limits, including secondary rate limits, for your instance. See [AUTOTITLE](/admin/configuration/configuring-user-applications-for-your-enterprise/configuring-rate-limits).

If you are developing an app for users or organizations outside of your instance, the standard {% data variables.product.github %} rate limits apply. See [AUTOTITLE](/free-pro-team@latest/rest/overview/rate-limits-for-the-rest-api) in the {% data variables.product.prodname_free_user %} documentation.

## About secondary rate limits

{% data reusables.rest-api.secondary-rate-limit-rest-graphql %}

{% else %}

## About primary rate limits

{% data variables.product.company_short %} limits the number of REST API requests that you can make within a specific amount of time. This limit helps prevent abuse and denial-of-service attacks, and ensures that the API remains available for all users.

Some endpoints, like the search endpoints, have more restrictive limits. For more information about these endpoints, see [AUTOTITLE](/rest/rate-limit/rate-limit). The GraphQL API also has a separate primary rate limit. See [AUTOTITLE](/graphql/overview/resource-limitations).

{% data reusables.organizations.api-insights-learn-about %}

In general, you can calculate your primary rate limit for the REST API based on your method of authentication, as described below.

### Primary rate limit for unauthenticated users

{% data reusables.rest-api.primary-rate-limit-unauthenticated-users %}

### Primary rate limit for authenticated users

{% data reusables.rest-api.primary-rate-limit-authenticated-users %}

{% ifversion ghec %}
> [!NOTE]
> The [Enterprise audit logs API endpoint](/rest/enterprise-admin/audit-log#get-the-audit-log-for-an-enterprise) has a rate limit of 1,750 queries per hour, per user and IP address. If your integration receives a rate limit error (typically a 403 or 429 response), it should wait before making another request to the GitHub API.
{% endif %}

### Primary rate limit for Git LFS access

API requests are required when you upload or download Git LFS content. These count towards a separate rate limiting bucket with a limit of 300 requests per minute for unauthenticated requests and 3,000 requests per minute for authenticated requests.

Git LFS uses a batch API which processes 100 Git LFS objects per API request by default. That means unauthenticated users can download 30,000 Git LFS objects per minute and authenticated users can upload/download 300,000 Git LFS objects per minute.

### Primary rate limit for {% data variables.product.prodname_github_app %} installations

{% data reusables.rest-api.primary-rate-limit-github-app-installations %}

### Primary rate limit for {% data variables.product.prodname_oauth_apps %}

Primary rate limits for OAuth access tokens generated by a {% data variables.product.prodname_oauth_app %} are dictated by the primary rate limits for authenticated users. This rate limit is combined with any requests that another {% data variables.product.prodname_github_app %} or {% data variables.product.prodname_oauth_app %} makes on that user's behalf and any requests that the user makes with a {% data variables.product.pat_generic %}. See [Primary rate limit for authenticated users](#primary-rate-limit-for-authenticated-users).

OAuth apps can also use their client ID and client secret to fetch public data. For example:

```shell
curl -u YOUR_CLIENT_ID:YOUR_CLIENT_SECRET -I {% data variables.product.rest_url %}/meta
```

{% data reusables.rest-api.primary-rate-limit-oauth-apps %}

> [!NOTE]
> Never include your app's client secret in client-side code or in code that runs on a user device. The client secret can be used to generate OAuth access tokens for users who have authorized your app, so you should always keep the client secret secure.

### Primary rate limit for `GITHUB_TOKEN` in {% data variables.product.prodname_actions %}

You can use the built-in `GITHUB_TOKEN` to authenticate requests in {% data variables.product.prodname_actions %} workflows. See [AUTOTITLE](/actions/security-guides/automatic-token-authentication).

{% data reusables.rest-api.primary-rate-limit-github-token-in-actions %}

## About secondary rate limits

{% data reusables.rest-api.secondary-rate-limit-rest-graphql %}

## Checking the status of your rate limit

You can use the headers that are sent with each response to determine the current status of your primary rate limit.

Header name | Description
-----------|-----------|
`x-ratelimit-limit` | The maximum number of requests that you can make per hour
`x-ratelimit-remaining` | The number of requests remaining in the current rate limit window
`x-ratelimit-used` | The number of requests you have made in the current rate limit window
`x-ratelimit-reset` | The time at which the current rate limit window resets, in UTC epoch seconds
`x-ratelimit-resource` | The rate limit resource that the request counted against. For more information about the different resources, see [AUTOTITLE](/rest/rate-limit/rate-limit#get-rate-limit-status-for-the-authenticated-user).

You can also call the `GET /rate_limit` endpoint to check your rate limit. Calling this endpoint does not count against your primary rate limit, but it can count against your secondary rate limit. See [AUTOTITLE](/rest/rate-limit/rate-limit). When possible, you should use the rate limit response headers instead of calling the API to check your rate limit.

There is not a way to check the status of your secondary rate limit.

## Exceeding the rate limit

If you exceed your primary rate limit, you will receive a `403` or `429` response, and the `x-ratelimit-remaining` header will be `0`. You should not retry your request until after the time specified by the `x-ratelimit-reset` header.

If you exceed a secondary rate limit, you will receive a `403` or `429` response and an error message that indicates that you exceeded a secondary rate limit. If the `retry-after` response header is present, you should not retry your request until after that many seconds has elapsed. If the `x-ratelimit-remaining` header is `0`, you should not retry your request until after the time, in UTC epoch seconds, specified by the `x-ratelimit-reset` header. Otherwise, wait for at least one minute before retrying. If your request continues to fail due to a secondary rate limit, wait for an exponentially increasing amount of time between retries, and throw an error after a specific number of retries.

Continuing to make requests while you are rate limited may result in the banning of your integration.

## Staying under the rate limit

You should follow best practices to help you stay under the rate limits. See [AUTOTITLE](/rest/guides/best-practices-for-using-the-rest-api).

{% ifversion ghec or ghes %}

You can also stream the audit log in order to view API requests. This can help you troubleshoot integrations that are exceeding the rate limit. See [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).

{% endif %}

## Getting a higher rate limit

If you want a higher primary rate limit, consider making authenticated requests instead of unauthenticated requests. Authenticated requests have a significantly higher rate limit than unauthenticated requests.

If you are using a {% data variables.product.pat_generic %} for automation in your organization, consider whether a {% data variables.product.prodname_github_app %} will work instead.{% ifversion fpt %} The rate limit for {% data variables.product.prodname_github_apps %} using an installation access token scales with the number of repositories and number of organization users.{% endif %}{% ifversion ghec %} {% data variables.product.prodname_github_apps %} used by {% data variables.product.prodname_ghe_cloud %} accounts have a higher rate limit than {% data variables.product.pat_generic_plural %}.{% endif %} See [AUTOTITLE](/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps).

{% ifversion fpt %}

If you are using {% data variables.product.prodname_github_apps %} or {% data variables.product.prodname_oauth_apps %}, consider upgrading to {% data variables.product.prodname_ghe_cloud %}. {% data variables.product.prodname_github_apps %} or {% data variables.product.prodname_oauth_apps %} have higher rate limits for organizations that use {% data variables.product.prodname_ghe_cloud %}.

{% endif %}

{% endif %}


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/timezones-and-the-rest-api -->

---
title: Timezones and the REST API
shortTitle: Timezones
intro: 'Some REST API endpoints allow you to specify timezone information with your request.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---

Some requests that create new data, such as creating a new commit, allow you to provide timezone information when specifying or generating timestamps.

Note that these rules apply only to data passed to the API, not to data returned by the API. Timestamps returned by the API are in UTC time, ISO 8601 format.

## Determining the timezone for a request

To determine timezone information for applicable API calls, we apply these rules in order of priority:

1. [Explicitly providing an ISO 8601 timestamp with timezone information](#explicitly-providing-an-iso-8601-timestamp-with-timezone-information)
1. [Using the `Time-Zone` header](#using-the-time-zone-header)
1. [Using the last known timezone for the user](#using-the-last-known-timezone-for-the-user)
1. [Defaulting to UTC without other timezone information](#defaulting-to-utc-without-other-timezone-information)

### Explicitly providing an ISO 8601 timestamp with timezone information

For API calls that allow for a timestamp to be specified, we use that exact timestamp. These timestamps look something like `2014-02-27T15:05:06+01:00`.

An example of this is the API to manage commits. For more information, see [AUTOTITLE](/rest/git/commits#create-a-commit).

### Using the `Time-Zone` header

It is possible to supply a `Time-Zone` header, which defines a timezone according to the [list of names from the Olson database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

```shell
curl -H "Time-Zone: Europe/Amsterdam" -X POST {% data variables.product.rest_url %}/repos/github-linguist/linguist/contents/new_file.md
```

This means that we generate a timestamp for the moment your API call is made, in the timezone this header defines.

For example, the API to manage contents generates a git commit for each addition or change, and it uses the current time as the timestamp. For more information, see [AUTOTITLE](/rest/repos/contents). The `Time-Zone` header will determine the timezone used for generating that current timestamp.

### Using the last known timezone for the user

If no `Time-Zone` header is specified and you make an authenticated call to the API, we use the last known timezone for the authenticated user. The last known timezone is updated whenever you browse the {% data variables.product.github %} website.

### Defaulting to UTC without other timezone information

If the steps above don't result in any information, we use UTC as the timezone.


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api -->

---
title: Troubleshooting the REST API
shortTitle: Troubleshooting
intro: Learn how to diagnose and resolve common problems for the REST API.
redirect_from:
  - /v3/troubleshooting
  - /rest/overview/troubleshooting
  - /rest/overview/troubleshooting-the-rest-api
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---

## Rate limit errors

{% data variables.product.company_short %} enforces rate limits to ensure that the API stays available for all users. For more information, see [AUTOTITLE](/rest/overview/rate-limits-for-the-rest-api).

If you exceed your primary rate limit, you will receive a `403 Forbidden` or `429 Too Many Requests ` response, and the `x-ratelimit-remaining` header will be `0`. If you exceed a secondary rate limit, you will receive a `403 Forbidden` or `429 Too Many Requests ` response and an error message that indicates that you exceeded a secondary rate limit.

If you receive a rate limit error, you should stop making requests temporarily according to these guidelines:

* If the `retry-after` response header is present, you should not retry your request until after that many seconds has elapsed.
* If the `x-ratelimit-remaining` header is `0`, you should not make another request until after the time specified by the `x-ratelimit-reset` header. The `x-ratelimit-reset` header is in UTC epoch seconds.
* Otherwise, wait for at least one minute before retrying. If your request continues to fail due to a secondary rate limit, wait for an exponentially increasing amount of time between retries, and throw an error after a specific number of retries.

Continuing to make requests while you are rate limited may result in the banning of your integration.

{% data reusables.organizations.api-insights-learn-about %}

For more information about how to avoid exceeding the rate limits, see [AUTOTITLE](/rest/guides/best-practices-for-using-the-rest-api).

## `404 Not Found` for an existing resource

If you make a request to access a private resource and your request isn't properly authenticated, you will receive a `404 Not Found` response. {% data variables.product.company_short %} uses a `404 Not Found` response instead of a `403 Forbidden` response to avoid confirming the existence of private repositories.

If you get a `404 Not Found` response when you know that the resource that you are requesting exists, you should check your authentication. For example:

* If you are using a {% data variables.product.pat_v1 %}, you should ensure that:
  * The token has the scopes that are required to use the endpoint. For more information, see [AUTOTITLE](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes) and [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token).
  * The owner of the token has any permissions that are required to use the endpoint. For example, if an endpoint can only be used by organization owners, only users that are owners of the affected organization can use the endpoint.
  * The token has not been expired or revoked. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation).
* If you are using a {% data variables.product.pat_v2 %}, you should ensure that:
  * The token has the permissions that are required to use the endpoint. For more information about the required permissions, see the documentation for the endpoint.
  * The resource owner that was specified for the token matches the owner of the resource that the endpoint will affect. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token).
  * The token has access to any private repositories that the endpoint will affect. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token).
  * The owner of the token has any permissions that are required to use the endpoint. For example, if an endpoint can only be used by organization owners, only users that are owners of the affected organization can use the endpoint.
  * The token has not been expired or revoked. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation).
* If you are using a {% data variables.product.prodname_github_app %} installation access token, you should ensure that:
  * The {% data variables.product.prodname_github_app %} has the permissions that are required to use the endpoint. For more information about the required permissions, see the documentation for the endpoint.
  * The endpoint is only affecting resources owned by the account where the {% data variables.product.prodname_github_app %} is installed.
  * The {% data variables.product.prodname_github_app %} has access to any repositories that the endpoint will affect.
  * The token has not been expired or revoked. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation).
* If you are using a {% data variables.product.prodname_github_app %} user access token, you should ensure that:
  * The {% data variables.product.prodname_github_app %} has the permissions that are required to use the endpoint. For more information about the required permissions, see the documentation for the endpoint.
  * The user that authorized the token has any permissions that are required to use the endpoint. For example, if an endpoint can only be used by organization owners, only users that are owners of the affected organization can use the endpoint.
  * The {% data variables.product.prodname_github_app %} has access to any repositories that the endpoint will affect.
  * The user has access to any repositories that the endpoint will affect.
  * The user has approved any updated permissions for your {% data variables.product.prodname_github_app %}. For more information, see [AUTOTITLE](/apps/using-github-apps/approving-updated-permissions-for-a-github-app).
* If you are using an {% data variables.product.prodname_oauth_app %} user access token, you should ensure that:
  * The token has the scopes that are required to use the endpoint. For more information, see [AUTOTITLE](/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).
  * The user that authorized the token has any permissions that are required to use the endpoint. For example, if an endpoint can only be used by organization owners, only users that are owners of the affected organization can use the endpoint.
  * The organization has not blocked OAuth app access, if you are using an endpoint that will affect resources owned by an organization. App owners cannot see whether their app is blocked, but they can instruct users of the app to check this. For more information, see {% ifversion fpt or ghec %}[AUTOTITLE](/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions).{% else %}[AUTOTITLE](/free-pro-team@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions) in the {% data variables.product.prodname_free_team %} documentation.{% endif %}
  * The token has not been expired or revoked. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation).
* If you are using `GITHUB_TOKEN` in a {% data variables.product.prodname_actions %} workflow, you should ensure that:
  * The endpoint is only affecting resources owned by the repository where the workflow is running. If you need to access resources outside of that repository, such as resources owned by an organization or resources owned by another repository, you should use a {% data variables.product.pat_generic %} or an access token for a {% data variables.product.prodname_github_app %}.

For more information about authentication, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

You should also check for typos in your URL. For example, adding a trailing slash to the endpoint will result in a `404 Not Found`. You can refer to the reference documentation for the endpoint to confirm that you have the correct URL.

Additionally, any path parameters must be URL encoded. For example, any slashes in the parameter value must be replaced with `%2F`. If you don't properly encode any slashes in the parameter name, the endpoint URL will be misinterpreted.

## Missing results

Most endpoints that return a list of resources support pagination. For most of these endpoints, only the first 30 resources are returned by default. In order to see all of the resources, you need to paginate through the results. For more information, see [AUTOTITLE](/rest/guides/using-pagination-in-the-rest-api).

If you are using pagination correctly and still do not see all of the results that you expect, you should confirm that the authentication credentials that you used have access to all of the expected resources. For example, if you are using a {% data variables.product.prodname_github_app %} installation access token, if the installation was only granted access to a subset of repositories in an organization, any request for all repositories in that organization will return only the repositories that the app installation can access.

{% ifversion fpt or ghec %}

## Requires authentication when using basic authentication

Basic authentication with your username and password is not supported. Instead, you should use a {% data variables.product.pat_generic %} or an access token for a {% data variables.product.prodname_github_app %} or {% data variables.product.prodname_oauth_app %}. For more information, see [AUTOTITLE](/rest/overview/authenticating-to-the-rest-api).

{% endif %}

## Timeouts

If {% data variables.product.github %} takes more than 10 seconds to process an API request, {% data variables.product.github %} will terminate the request and you will receive a timeout response and a "Server Error" message.

{% data variables.product.github %} reserves the right to change the timeout window to protect the speed and reliability of the API.

You can check the status of the REST API at [githubstatus.com](https://www.githubstatus.com/) to determine whether the timeout is due to a problem with the API. You can also try to simplify your request or try your request later. For example, if you are requesting 100 items on a page, you can try requesting fewer items.

## Resource not accessible

If you are using a {% data variables.product.prodname_github_app %} or {% data variables.product.pat_v2 %} and you receive a "Resource not accessible by integration" or "Resource not accessible by {% data variables.product.pat_generic %}" error, then your token has insufficient permissions. For more information about the required permissions, see the documentation for the endpoint.

You can use the `X-Accepted-GitHub-Permissions` header to identify the permissions that are required to access the REST API endpoint.

The value of the `X-Accepted-GitHub-Permissions` header is a comma separated list of the permissions that are required to use the endpoint. Occasionally, you can choose from multiple permission sets. In these cases, multiple comma-separated lists will be separated by a semicolon.

For example:

* `X-Accepted-GitHub-Permissions: contents=read` means that your {% data variables.product.prodname_github_app %} or {% data variables.product.pat_v2 %} needs read access to the contents permission.
* `X-Accepted-GitHub-Permissions: pull_requests=write,contents=read` means that your {% data variables.product.prodname_github_app %} or {% data variables.product.pat_v2 %} needs write access to the pull request permission and read access to the contents permission.
* `X-Accepted-GitHub-Permissions: pull_requests=read,contents=read; issues=read,contents=read` means that your {% data variables.product.prodname_github_app %} or {% data variables.product.pat_v2 %} needs either read access to the pull request permission and read access to the contents permission, or read access to the issues permission and read access to the contents permission.

## Problems parsing JSON

If you send invalid JSON in the request body, you may receive a `400 Bad Request` response and a "Problems parsing JSON" error message. You can use a linter or JSON validator to help you identify errors in your JSON.

## Body should be a JSON object

If the endpoint expects a JSON object and you do not format your request body as a JSON object, you may receive a `400 Bad Request` response and a "Body should be a JSON object" error message.

## Invalid request

If you omit required parameters or you use the wrong type for a parameter, you may receive a `422 Unprocessable Entity` response and an "Invalid request" error message. For example, you will get this error if you specify a parameter value as an array but the endpoint is expecting a string. You can refer to the reference documentation for the endpoint to verify that you are using the correct parameter types and that you are including all of the required parameters.

## Validation Failed

If your request could not be processed, you may receive a `422 Unprocessable Entity` response and a "Validation Failed" error message. The response body will include an `errors` property, which includes a `code` property to help you diagnose the problem.

Code | Description
-----------|-----------|
`missing` | A resource does not exist.
`missing_field` | A parameter that was required was not specified. Review the documentation for the endpoint to see what parameters are required.
`invalid` | The formatting of a parameter is invalid. Review the endpoint documentation for more specific information.
`already_exists` | Another resource has the same value as one of your parameters. This can happen in resources that must have some unique key (such as label names).
`unprocessable` | The parameters that were provided were invalid.
`custom` | Refer to the `message` property to diagnose the error.

## Not a supported version

You should use the `X-GitHub-Api-Version` header to specify an API version. For example:

```shell
curl {% data reusables.rest-api.version-header %} https://api.github.com/zen
```

If you specify a version that does not exist, you will receive a `400 Bad Request` error and a message about the version not being supported.

For more information, see [AUTOTITLE](/rest/overview/api-versions).

## User agent required

Requests without a valid `User-Agent` header will be rejected. You should use your username or the name of your application for the `User-Agent` value.

curl sends a valid `User-Agent` header by default.

## Other errors

If you observe an error that is not addressed here, you should refer to the error message that the API gives you. Most error messages will provide a clue about what is wrong and a link to relevant documentation.

If you observe unexpected failures, you can use [githubstatus.com](https://www.githubstatus.com/) or the [{% data variables.product.company_short %} status API](https://www.githubstatus.com/api) to check for incidents affecting the API.

## Further reading

* [AUTOTITLE](/rest/guides/best-practices-for-using-the-rest-api)
* [AUTOTITLE](/webhooks/testing-and-troubleshooting-webhooks/troubleshooting-webhooks)
* [AUTOTITLE](/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app)


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/using-cors-and-jsonp-to-make-cross-origin-requests -->

---
title: Using CORS and JSONP to make cross-origin requests
shortTitle: CORS and JSONP
intro: You can make API requests across domains using cross-origin resource sharing (CORS) and JSONP callbacks.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
category:
  - Learn about the REST API
---

## About cross-origin requests

A cross-origin request is a request made to a different domain than the one originating the request. For security reasons, most web browsers block cross-origin requests. However, you can use cross-origin resource sharing (CORS) and JSONP callbacks to make cross-origin requests.

## Cross-origin resource sharing (CORS)

The REST API supports cross-origin resource sharing (CORS) for AJAX requests from any origin. For more information, see the [CORS W3C Recommendation](http://www.w3.org/TR/cors/) and the [HTML 5 Security Guide](https://code.google.com/archive/p/html5security/wikis/CrossOriginRequestSecurity.wiki)

Here's a sample request sent from a browser hitting
`http://example.com`:

```shell
$ curl -I {% data variables.product.rest_url %} -H "Origin: http://example.com"
HTTP/2 302
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: ETag, Link, x-ratelimit-limit, x-ratelimit-remaining, x-ratelimit-reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval
```

This is what the CORS preflight request looks like:

```shell
$ curl -I {% data variables.product.rest_url %} -H "Origin: http://example.com" -X OPTIONS
HTTP/2 204
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Authorization, Content-Type, If-Match, If-Modified-Since, If-None-Match, If-Unmodified-Since, X-Requested-With
Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE
Access-Control-Expose-Headers: ETag, Link, x-ratelimit-limit, x-ratelimit-remaining, x-ratelimit-reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval
Access-Control-Max-Age: 86400
```

## JSON-P callbacks

You can send a `?callback` parameter to any GET call to have the results
wrapped in a JSON function. This is typically used when browsers want to embed {% data variables.product.github %} content in web pages and avoid cross-domain problems. The response includes the same data output as the regular API, plus the relevant HTTP Header information.

```shell
$ curl {% data variables.product.rest_url %}?callback=foo

> /**/foo({
>   "meta": {
>     "status": 200,
>     "x-ratelimit-limit": "5000",
>     "x-ratelimit-remaining": "4966",
>     "x-ratelimit-reset": "1372700873",
>     "Link": [ // pagination headers and other links
>       ["{% data variables.product.rest_url %}?page=2", {"rel": "next"}]
>     ]
>   },
>   "data": {
>     // the data
>   }
> })
```

You can write a JavaScript handler to process the callback. Here's a minimal example you can try:

```html
<html>
<head>
<script type="text/javascript">
function foo(response) {
  var meta = response.meta;
  var data = response.data;
  console.log(meta);
  console.log(data);
}

var script = document.createElement('script');
script.src = '{% data variables.product.rest_url %}?callback=foo';

document.getElementsByTagName('head')[0].appendChild(script);
</script>
</head>

<body>
  <p>Open up your browser's console.</p>
</body>
</html>
```

All of the headers have the same string value as the HTTP Headers, except `Link`. `Link` headers are pre-parsed for you and come through as an array of `[url, options]` tuples.

For example, a link that looks like this:

```shell
Link: <url1>; rel="next", <url2>; rel="foo"; bar="baz"
```

will look like this in the Callback output:

```json
{
  "Link": [
    [
      "url1",
      {
        "rel": "next"
      }
    ],
    [
      "url2",
      {
        "rel": "foo",
        "bar": "baz"
      }
    ]
  ]
}
```


---

<!-- source: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api -->

---
title: Using pagination in the REST API
intro: Learn how to navigate through paginated responses from the REST API.
redirect_from:
  - /guides/traversing-with-pagination
  - /v3/guides/traversing-with-pagination
  - /rest/guides/traversing-with-pagination
  - /rest/guides/using-pagination-in-the-rest-api
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Pagination
category:
  - Learn about the REST API
---

## About pagination

When a response from the REST API would include many results, {% data variables.product.company_short %} will paginate the results and return a subset of the results. For example, `GET /repos/octocat/Spoon-Knife/issues` will only return 30 issues from the `octocat/Spoon-Knife` repository even though the repository includes over 1600 open issues. This makes the response easier to handle for servers and for people.

You can use the `link` header from the response to request additional pages of data. If an endpoint supports the `per_page` query parameter, you can control how many results are returned on a page.

This article demonstrates how to request additional pages of results for paginated responses, how to change the number of results returned on each page, and how to write a script to fetch multiple pages of results.

## Using `link` headers

When a response is paginated, the response headers will include a `link` header. If the endpoint does not support pagination, or if all results fit on a single page, the `link` header will be omitted.

The `link` header contains URLs that you can use to fetch additional pages of results. For example, the previous, next, first, and last page of results.

To see the response headers for a particular endpoint, you can use curl, GitHub CLI, or a library you're using to make requests. To see the response headers if you are using a library to make requests, follow the documentation for that library. To see the response headers if you are using curl or GitHub CLI, pass the `--include` flag with your request. For example:

  ```shell
  curl --include --request GET \
  --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
  --header "Accept: application/vnd.github+json"
  ```

If the response is paginated, the `link` header will look something like this:

```http
link: <https://api.github.com/repositories/1300192/issues?page=2>; rel="prev", <https://api.github.com/repositories/1300192/issues?page=4>; rel="next", <https://api.github.com/repositories/1300192/issues?page=515>; rel="last", <https://api.github.com/repositories/1300192/issues?page=1>; rel="first"
```

The `link` header provides the URL for the previous, next, first, and last page of results:

* The URL for the previous page is followed by `rel="prev"`.
* The URL for the next page is followed by `rel="next"`.
* The URL for the last page is followed by `rel="last"`.
* The URL for the first page is followed by `rel="first"`.

In some cases, only a subset of these links are available. For example, the link to the previous page won't be included if you are on the first page of results, and the link to the last page won't be included if it can't be calculated.

You can use the URLs from the `link` header to request another page of results. For example, to request the last page of results based on the previous example:

```shell
curl --include --request GET \
--url "https://api.github.com/repositories/1300192/issues?page=515" \
--header "Accept: application/vnd.github+json"
```

The URLs in the `link` header use query parameters to indicate which page of results to return. The query parameters in the `link` URLs may differ between endpoints, however each paginated endpoint will use the `page`, `before`/`after`, or `since` query parameters. (Some endpoints use the `since` parameter for something other than pagination.) In all cases, you can use the URLs in the `link` header to fetch additional pages of results. For more information about query parameters see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api#using-query-parameters).

## Changing the number of items per page

If an endpoint supports the `per_page` query parameter, then you can control how many results are returned on a page. For more information about query parameters see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api#using-query-parameters).

For example, this request uses the `per_page` query parameter to return two items per page:

```shell
curl --include --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues?per_page=2" \
--header "Accept: application/vnd.github+json"
```

The `per_page` parameter will automatically be included in the `link` header. For example:

```http
link: <https://api.github.com/repositories/1300192/issues?per_page=2&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=2&page=7715>; rel="last"
```

## Scripting with pagination

Instead of manually copying URLs from the `link` header, you can write a script to fetch multiple pages of results.

The following examples use JavaScript and {% data variables.product.company_short %}'s Octokit.js library. For more information about Octokit.js, see [AUTOTITLE](/rest/guides/getting-started-with-the-rest-api?tool=javascript) and [the Octokit.js README](https://github.com/octokit/octokit.js/#readme).

### Example using the Octokit.js pagination method

To fetch paginated results with Octokit.js, you can use `octokit.paginate()`. `octokit.paginate()` will fetch the next page of results until it reaches the last page and then return all of the results as a single array. A few endpoints return paginated results as array in an object, as opposed to returning the paginated results as an array. `octokit.paginate()` always returns an array of items even if the raw result was an object.

For example, this script gets all of the issues from the `octocat/Spoon-Knife` repository. Although it requests 100 issues at a time, the function won't return until the last page of data is reached.

```javascript copy
import { Octokit } from "octokit";

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",
{% endif %}});

const data = await octokit.paginate("GET /repos/{owner}/{repo}/issues", {
  owner: "octocat",
  repo: "Spoon-Knife",
  per_page: 100,
  headers: {
    "X-GitHub-Api-Version": "{{ allVersions[currentVersion].latestApiVersion }}",
  },
});

console.log(data)
```

You can pass an optional map function to `octokit.paginate()` to end pagination before the last page is reached or to reduce memory usage by keeping only a subset of the response. You can also use `octokit.paginate.iterator()` to iterate through a single page at a time instead of requesting every page. For more information, see [the Octokit.js documentation](https://github.com/octokit/octokit.js#pagination).

### Example creating a pagination method

If you are using another language or library that doesn't have a pagination method, you can build your own pagination method. This example still uses the Octokit.js library to make requests, but does not rely on `octokit.paginate()`.

The `getPaginatedData` function makes a request to an endpoint with `octokit.request()`. The data from the response is processed by `parseData`, which handles cases where no data is returned or cases where the data that is returned is an object instead of an array. The processed data is then appended to a list that contains all of the paginated data collected so far. If the response includes a `link` header and if the `link` header includes a link for the next page, then the function uses a RegEx pattern (`nextPattern`) to get the URL for the next page. The function then repeats the previous steps, now using this new URL. Once the `link` header no longer includes a link to the next page, all of the results are returned.

```javascript copy
import { Octokit } from "octokit";

const octokit = new Octokit({ {% ifversion ghes %}
  baseUrl: "{% data variables.product.rest_url %}",
{% endif %}});

async function getPaginatedData(url) {
  const nextPattern = /(?<=<)([\S]*)(?=>; rel="next")/i;
  let pagesRemaining = true;
  let data = [];

  while (pagesRemaining) {
    const response = await octokit.request(`GET ${url}`, {
      per_page: 100,
      headers: {
        "X-GitHub-Api-Version":
          "{{ allVersions[currentVersion].latestApiVersion }}",
      },
    });

    const parsedData = parseData(response.data)
    data = [...data, ...parsedData];

    const linkHeader = response.headers.link;

    pagesRemaining = linkHeader && linkHeader.includes(`rel=\"next\"`);

    if (pagesRemaining) {
      url = linkHeader.match(nextPattern)[0];
    }
  }

  return data;
}

function parseData(data) {
  // If the data is an array, return that
    if (Array.isArray(data)) {
      return data
    }

  // Some endpoints respond with 204 No Content instead of empty array
  //   when there is no data. In that case, return an empty array.
  if (!data) {
    return []
  }

  // Otherwise, the array of items that we want is in an object
  // Delete keys that don't include the array of items
  delete data.incomplete_results;
  delete data.repository_selection;
  delete data.total_count;
  // Pull out the array of items
  const namespaceKey = Object.keys(data)[0];
  data = data[namespaceKey];

  return data;
}

const data = await getPaginatedData("/repos/octocat/Spoon-Knife/issues");

console.log(data);
```
