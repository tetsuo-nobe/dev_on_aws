## CodePipelineを活用したLambda関数(Node.js)のCI/CD
- リポジトリ: CodeCommit
- ビルド: CodeBuild
  - buildspec.ymlにビルド手順を記述
- デプロイ: SAMでBlue/Greenデプロイを指定
  - SAMテンプレート: template.yaml
    - デプロイの指定
      - Canary10Percent5Minutes
        - 更新時、10%のトラフィックを新バージョンに向ける。5分後に100%を新バージョンに向ける。



