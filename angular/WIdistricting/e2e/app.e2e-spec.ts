import { WIdistrictingPage } from './app.po';

describe('widistricting App', () => {
  let page: WIdistrictingPage;

  beforeEach(() => {
    page = new WIdistrictingPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
